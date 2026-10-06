import hashlib, hmac, json, mimetypes, os, re, secrets, sys, threading, time, traceback
from http.cookies import SimpleCookie
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, unquote, urlparse

AKAR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AKAR)
import dashboard as dash
from klien import RE_SLUG, GalatData, kerangka_kosong, muat, ukuran_jpeg
from skin import SKIN

BOLEH = (
    "nama", "area", "wa", "wa_tampil", "alamat", "peta", "jam", "lead", "harga_lead", "harga_catatan", "jam_lead",
    "tip_layanan", "pesan_lead", "faq", "grup", "stylist", "kamar", "checkin", "checkout", "menu", "ongkir",
    "areaAntar", "tempatAmbil", "skin", "title", "deskripsi", "foto",
)
RE_TOKEN = re.compile(r"^[A-Za-z0-9_-]{20,64}$")
RE_FOTO_KLIEN = re.compile(r"^(hero|foto([1-9]|1[0-2]))\.jpg$")
BATAS_JSON_KLIEN = 256 * 1024
BATAS_JSON_ADMIN = 2 * 1024 * 1024
BATAS_FOTO_KLIEN = 1024 * 1024
BATAS_FOTO_ADMIN = 6 * 1024 * 1024
MAKS_BERKAS_KLIEN = 16
DOMAIN_SEMENTARA = "pratinjau-klien.com"
SLUG_TERLARANG = {"dist", "admin", "isi"}
CFG = {}
TULIS = threading.Lock()
JEJAK = {}
JEJAK_KUNCI = threading.Lock()


def folder():
    return CFG["folder"]


def jalur_meta(slug):
    return os.path.join(folder(), "_meta", slug + ".json")


def baca_meta(slug):
    try:
        with open(jalur_meta(slug), "r", encoding="utf-8") as f:
            m = json.load(f)
        return m if isinstance(m, dict) else {}
    except (OSError, ValueError):
        return {}


def tulis_meta(slug, m):
    os.makedirs(os.path.join(folder(), "_meta"), exist_ok=True)
    sementara = jalur_meta(slug) + ".tmp"
    with open(sementara, "w", encoding="utf-8", newline="\n") as f:
        json.dump(m, f, ensure_ascii=False, indent=2)
        f.write("\n")
    os.replace(sementara, jalur_meta(slug))


def cari_token(token):
    if not RE_TOKEN.match(token or ""):
        return None
    jalur = os.path.join(folder(), "_meta")
    if not os.path.isdir(jalur):
        return None
    hasil = None
    for nama in os.listdir(jalur):
        if not nama.endswith(".json"):
            continue
        slug = nama[:-5]
        if not RE_SLUG.match(slug):
            continue
        tok = baca_meta(slug).get("token", "")
        if isinstance(tok, str) and hmac.compare_digest(tok, token):
            hasil = slug
    return hasil


def terlalu_sering(kunci, maks, detik, catat=True):
    sekarang = time.time()
    with JEJAK_KUNCI:
        waktu = [t for t in JEJAK.get(kunci, []) if sekarang - t < detik]
        if len(waktu) >= maks:
            JEJAK[kunci] = waktu
            return True
        if catat:
            waktu.append(sekarang)
        JEJAK[kunci] = waktu
        if len(JEJAK) > 5000:
            for k in list(JEJAK)[:2500]:
                JEJAK.pop(k, None)
    return False


def tanda(pesan, exp):
    return hmac.new(CFG["kunci"], ("%s|%d" % (pesan, exp)).encode("utf-8"), hashlib.sha256).hexdigest()


def buat_tanda(pesan, detik):
    exp = int(time.time()) + detik
    return "%d.%s" % (exp, tanda(pesan, exp))


def cek_tanda(pesan, nilai):
    try:
        exp_s, sig = nilai.split(".", 1)
        exp = int(exp_s)
    except (AttributeError, ValueError):
        return False
    return exp > time.time() and hmac.compare_digest(sig, tanda(pesan, exp))


def periksa_bentuk(v, dalam=0):
    if dalam > 7:
        raise GalatData("Data terlalu bersarang.")
    if isinstance(v, str):
        if len(v) > 4000:
            raise GalatData("Ada teks yang terlalu panjang (maks 4000 karakter).")
    elif isinstance(v, list):
        if len(v) > 150:
            raise GalatData("Ada daftar yang terlalu panjang.")
        for x in v:
            periksa_bentuk(x, dalam + 1)
    elif isinstance(v, dict):
        if len(v) > 60:
            raise GalatData("Ada objek dengan terlalu banyak isian.")
        for k, x in v.items():
            if not isinstance(k, str) or len(k) > 60:
                raise GalatData("Nama isian tidak valid.")
            periksa_bentuk(x, dalam + 1)
    elif not (v is None or isinstance(v, (bool, int, float))):
        raise GalatData("Tipe data tidak didukung.")


def bersihkan_foto(foto):
    if not isinstance(foto, dict):
        raise GalatData("foto harus berupa objek.")
    hasil = {"hero": {"berkas": "", "alt": ""}, "galeri": []}

    def satu(it):
        if not isinstance(it, dict):
            raise GalatData("Isi foto tidak valid.")
        b, a = it.get("berkas", ""), it.get("alt", "")
        if not isinstance(b, str) or not isinstance(a, str):
            raise GalatData("Isi foto tidak valid.")
        if b and not RE_FOTO_KLIEN.match(b):
            raise GalatData("Nama berkas foto tidak valid.")
        return {"berkas": b, "alt": a}

    if isinstance(foto.get("hero"), dict):
        hasil["hero"] = satu(foto["hero"])
    gal = foto.get("galeri", [])
    if not isinstance(gal, list) or len(gal) > 12:
        raise GalatData("Galeri maksimal 12 foto.")
    hasil["galeri"] = [satu(x) for x in gal]
    return hasil


def simpan_klien(slug, kiriman):
    if not isinstance(kiriman, dict):
        raise GalatData("Data tidak valid.")
    periksa_bentuk(kiriman)
    with TULIS:
        d = dash.baca_json(slug)
        for k in BOLEH:
            if k not in kiriman:
                continue
            v = kiriman[k]
            if k == "skin":
                if v not in SKIN[d["jenis"]]:
                    raise GalatData("Tampilan tidak dikenal.")
            elif k == "foto":
                v = bersihkan_foto(v)
            d[k] = v
        dash.tulis_json(slug, d)


def cek_klien(slug):
    d = dash.baca_json(slug)
    d["paket"] = 1
    d["domain"] = DOMAIN_SEMENTARA
    d.pop("bayar", None)
    try:
        u = muat(slug, folder(), d)
    except GalatData as ex:
        return {"galat": list(ex.daftar), "peringatan": []}
    return {"galat": [], "peringatan": list(u["_peringatan"])}


def data_klien(slug):
    d = dash.baca_json(slug)
    keluar = {"jenis": d.get("jenis")}
    for k in BOLEH:
        if k in d:
            keluar[k] = d[k]
    return keluar


def meta_klien(slug):
    d = dash.baca_json(slug)
    j = d["jenis"]
    return {
        "peran": "klien", "slug": slug, "folder": "",
        "jenis": {j: dash.meta()["jenis"][j]},
        "status": baca_meta(slug).get("status", "buka"),
    }


def daftar_admin():
    hasil = dash.daftar_proyek()
    for p in hasil:
        m = baca_meta(p["slug"])
        p["status"] = m.get("status", "buka")
        p["dikirim"] = m.get("dikirim")
        p["tautan"] = "/isi/" + m["token"] if m.get("token") else None
    return hasil


def proyek_baru(jenis, slug):
    if not RE_SLUG.match(slug) or len(slug) > 40 or slug in SLUG_TERLARANG:
        raise GalatData("Nama proyek tidak valid. Pakai huruf kecil, angka, tanda hubung, maksimal 40 karakter.")
    if os.path.exists(dash.jalur_data(slug)):
        raise GalatData("Proyek '%s' sudah ada. Pakai nama lain." % slug)
    kerangka_kosong(jenis, slug, folder())
    tulis_meta(slug, {"token": secrets.token_urlsafe(24), "status": "buka", "dibuat": time.strftime("%Y-%m-%dT%H:%M:%S")})


def tulis_foto(slug, nama, isi, klien):
    os.makedirs(dash.jalur_foto(slug), exist_ok=True)
    tujuan = os.path.join(dash.jalur_foto(slug), nama)
    sementara = tujuan + ".tmp"
    if klien and not os.path.exists(tujuan) and len(os.listdir(dash.jalur_foto(slug))) >= MAKS_BERKAS_KLIEN:
        raise GalatData("Jumlah foto sudah mencapai batas.")
    with open(sementara, "wb") as f:
        f.write(isi)
    if klien:
        try:
            w, h = ukuran_jpeg(sementara)
        except ValueError:
            os.remove(sementara)
            raise GalatData("Berkas bukan foto JPG yang valid.")
        if (w, h) != (720, 540):
            os.remove(sementara)
            raise GalatData("Ukuran foto harus 720x540. Muat ulang halaman lalu coba lagi.")
    os.replace(sementara, tujuan)


class Penanganan(BaseHTTPRequestHandler):
    server_version = "Isi"
    timeout = 30

    def log_message(self, *a):
        pass

    def skema(self):
        return "https" if CFG["aman"] else "http"

    def kirim(self, kode, tubuh, tipe="application/json; charset=utf-8", tambahan=None, tanpa_csp=False):
        if not isinstance(tubuh, bytes):
            tubuh = json.dumps(tubuh, ensure_ascii=False).encode("utf-8")
        self.send_response(kode)
        self.send_header("Content-Type", tipe)
        self.send_header("Content-Length", str(len(tubuh)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Referrer-Policy", "same-origin")
        self.send_header("X-Robots-Tag", "noindex, nofollow")
        if not tanpa_csp:
            self.send_header("X-Frame-Options", "DENY")
            self.send_header(
                "Content-Security-Policy",
                "default-src 'none'; script-src 'unsafe-inline'; style-src 'unsafe-inline'; img-src 'self' blob: data:; "
                "connect-src 'self'; frame-src %s://*.%s; base-uri 'none'; form-action 'none'; frame-ancestors 'none'"
                % (self.skema(), CFG["pratinjau"]),
            )
        for k, v in (tambahan or {}).items():
            self.send_header(k, v)
        self.end_headers()
        if self.command != "HEAD":
            self.wfile.write(tubuh)

    def galat(self, kode, pesan):
        self.kirim(kode, {"galat": pesan if isinstance(pesan, list) else [pesan]})

    def ip(self):
        if CFG["proxy"]:
            x = self.headers.get("X-Forwarded-For", "")
            if x:
                return x.split(",")[-1].strip()
        return self.client_address[0]

    def tubuh(self, batas):
        try:
            n = int(self.headers.get("Content-Length") or 0)
        except ValueError:
            raise GalatData("Permintaan tidak valid.")
        if n < 0:
            raise GalatData("Permintaan tidak valid.")
        if n > batas:
            raise GalatData("Berkas terlalu besar (maks %s)." % ("%d MB" % (batas // 1048576) if batas >= 1048576 else "%d KB" % (batas // 1024)))
        return self.rfile.read(n)

    def json_tubuh(self, batas):
        d = json.loads(self.tubuh(batas) or b"{}")
        if not isinstance(d, dict):
            raise GalatData("Data harus berupa objek.")
        return d

    def kuki(self, nama):
        try:
            c = SimpleCookie()
            c.load(self.headers.get("Cookie", ""))
            return c[nama].value if nama in c else None
        except Exception:
            return None

    def admin_ok(self):
        return cek_tanda("sesi", self.kuki("sesi") or "")

    def butuh_admin(self):
        if not self.admin_ok():
            raise Tidak(401, "Masuk dulu sebagai admin.")

    def do_GET(self):
        self.rute("GET")

    def do_HEAD(self):
        self.rute("GET")

    def do_POST(self):
        self.rute("POST")

    def rute(self, metode):
        host = (self.headers.get("Host") or "").lower()
        u = urlparse(self.path)
        q = {k: v[0] for k, v in parse_qs(u.query).items()}
        p = unquote(u.path)
        if p == "/healthz":
            return self.kirim(200, b"ok", "text/plain; charset=utf-8")
        try:
            if host == CFG["host"]:
                return self.app(metode, p, q)
            if host.endswith("." + CFG["pratinjau"]):
                return self.pratinjau(host[: -len(CFG["pratinjau"]) - 1], p, q)
            self.kirim(421, b"Host tidak dikenal.", "text/plain; charset=utf-8")
        except Tidak as ex:
            self.galat(ex.kode, ex.pesan)
        except GalatData as ex:
            self.galat(400, list(ex.daftar))
        except (ValueError, KeyError) as ex:
            self.galat(400, "Permintaan tidak valid.")
        except Exception:
            traceback.print_exc()
            self.galat(500, "Terjadi kesalahan di server.")

    def halaman(self):
        with open(os.path.join(AKAR, "dashboard.html"), "rb") as f:
            return self.kirim(200, f.read(), "text/html; charset=utf-8")

    def app(self, metode, p, q):
        if metode == "POST":
            asal = self.headers.get("Origin")
            if asal:
                sama = urlparse(asal).netloc.lower() == CFG["host"]
            else:
                sama = self.headers.get("Sec-Fetch-Site") == "same-origin"
            if not sama:
                raise Tidak(403, "Asal permintaan tidak diizinkan.")
        if metode == "GET":
            if p == "/":
                return self.kirim(200, "<!doctype html><meta charset=utf-8><meta name=robots content=noindex><title>Isi data usaha</title><p style=\"font:16px system-ui;padding:24px\">Layanan pengisian data usaha. Buka tautan yang Anda terima dari pengelola situs.".encode("utf-8"), "text/html; charset=utf-8")
            if p == "/robots.txt":
                return self.kirim(200, b"User-agent: *\nDisallow: /\n", "text/plain; charset=utf-8")
            if p == "/admin":
                return self.halaman()
            if re.match(r"^/isi/[^/]+$", p):
                return self.halaman()
            m = re.match(r"^/demo/([a-z]+)/([a-z0-9-]+)\.jpg$", p)
            if m:
                return self.demo(m.group(1), m.group(2))
            m = re.match(r"^/klien-foto/([^/]+)/([^/]+)$", p)
            if m:
                return self.foto_klien(m.group(1), m.group(2))
        if p == "/api/masuk" and metode == "POST":
            return self.masuk()
        if p == "/api/keluar" and metode == "POST":
            return self.kirim(200, {"ok": True}, tambahan={"Set-Cookie": self.cookie_sesi("", 0)})
        if p.startswith("/api/klien/"):
            return self.klien(metode, p[len("/api/klien/"):], q)
        return self.admin(metode, p, q)

    def demo(self, jenis, skin):
        jalur = os.path.join(dash.ROOT, jenis, "img", "skin-%s.jpg" % skin)
        if jenis not in SKIN or skin not in SKIN[jenis] or not os.path.isfile(jalur):
            raise Tidak(404, "Pratinjau skin tidak ada.")
        with open(jalur, "rb") as f:
            return self.kirim(200, f.read(), "image/jpeg")

    def cookie_sesi(self, nilai, umur):
        s = "sesi=%s; Path=/; HttpOnly; SameSite=Strict; Max-Age=%d" % (nilai, umur)
        return s + ("; Secure" if CFG["aman"] else "")

    def masuk(self):
        ip = self.ip()
        if terlalu_sering("masuk|" + ip, 5, 900, catat=False):
            raise Tidak(429, "Terlalu banyak percobaan. Coba lagi 15 menit lagi.")
        d = self.json_tubuh(4096)
        pw = d.get("password")
        ok = isinstance(pw, str) and hmac.compare_digest(hashlib.sha256(pw.encode("utf-8")).digest(), CFG["pw_hash"])
        if not ok:
            terlalu_sering("masuk|" + ip, 5, 900)
            raise Tidak(401, "Password salah.")
        return self.kirim(200, {"ok": True}, tambahan={"Set-Cookie": self.cookie_sesi(buat_tanda("sesi", 12 * 3600), 12 * 3600)})

    def slug_klien(self, token):
        ip = self.ip()
        if terlalu_sering("token|" + ip, 30, 600, catat=False):
            raise Tidak(429, "Terlalu banyak permintaan. Coba lagi beberapa menit lagi.")
        slug = cari_token(token)
        if not slug or not os.path.isfile(dash.jalur_data(slug)):
            terlalu_sering("token|" + ip, 30, 600)
            raise Tidak(404, "Tautan tidak berlaku. Minta tautan baru dari pengelola situs.")
        return slug

    def foto_klien(self, token, nama):
        slug = self.slug_klien(token)
        if not RE_FOTO_KLIEN.match(nama):
            raise Tidak(404, "Foto tidak ada.")
        jalur = os.path.join(dash.jalur_foto(slug), nama)
        if not os.path.isfile(jalur):
            raise Tidak(404, "Foto tidak ada.")
        with open(jalur, "rb") as f:
            return self.kirim(200, f.read(), "image/jpeg")

    def klien(self, metode, rute, q):
        slug = self.slug_klien(q.get("t", ""))
        status = baca_meta(slug).get("status", "buka")
        if metode == "GET":
            if rute == "meta":
                return self.kirim(200, meta_klien(slug))
            if rute == "data":
                return self.kirim(200, data_klien(slug))
            raise Tidak(404, "Rute tidak ada.")
        if rute == "cek":
            return self.kirim(200, cek_klien(slug))
        if status != "buka":
            raise Tidak(403, "Data sudah dikirim dan terkunci. Hubungi pengelola situs bila perlu mengubah.")
        if rute == "simpan":
            simpan_klien(slug, self.json_tubuh(BATAS_JSON_KLIEN))
            return self.kirim(200, {"ok": True})
        if rute == "foto":
            nama = q.get("nama", "")
            if not RE_FOTO_KLIEN.match(nama):
                raise GalatData("Nama berkas foto tidak valid.")
            if terlalu_sering("foto|" + slug, 60, 3600):
                raise Tidak(429, "Terlalu banyak unggahan. Coba lagi nanti.")
            isi = self.tubuh(BATAS_FOTO_KLIEN)
            if not isi.startswith(b"\xff\xd8"):
                raise GalatData("Berkas bukan foto JPG yang valid.")
            with TULIS:
                tulis_foto(slug, nama, isi, True)
            return self.kirim(200, {"ok": True, "berkas": nama})
        if rute == "kirim":
            hasil = cek_klien(slug)
            if hasil["galat"]:
                return self.kirim(400, {"galat": hasil["galat"]})
            with TULIS:
                m = baca_meta(slug)
                m["status"] = "terkirim"
                m["dikirim"] = time.strftime("%Y-%m-%dT%H:%M:%S")
                tulis_meta(slug, m)
            return self.kirim(200, {"ok": True})
        raise Tidak(404, "Rute tidak ada.")

    def slug_admin(self, q):
        slug = q.get("slug", "")
        if not RE_SLUG.match(slug) or not os.path.isfile(dash.jalur_data(slug)):
            raise GalatData("Proyek '%s' tidak ditemukan." % slug)
        return slug

    def admin(self, metode, p, q):
        if p == "/api/meta" and metode == "GET":
            if not self.admin_ok():
                raise Tidak(401, "Masuk dulu sebagai admin.")
            m = dash.meta()
            m.pop("pratinjau", None)
            m["folder"] = ""
            m["peran"] = "admin"
            return self.kirim(200, m)
        self.butuh_admin()
        if metode == "GET":
            if p == "/api/proyek":
                return self.kirim(200, daftar_admin())
            if p == "/api/data":
                return self.kirim(200, dash.baca_json(self.slug_admin(q)))
            m = re.match(r"^/foto/([a-z0-9-]+)/([^/]+)$", p)
            if m:
                slug, nama = m.groups()
                jalur = os.path.join(dash.jalur_foto(slug), nama)
                if not RE_SLUG.match(slug) or not dash.RE_FOTO.match(nama) or not os.path.isfile(jalur):
                    raise Tidak(404, "Foto tidak ada.")
                with open(jalur, "rb") as f:
                    return self.kirim(200, f.read(), dash.TIPE[os.path.splitext(nama)[1].lower()])
            m = re.match(r"^/unduh/([a-z0-9-]+)\.zip$", p)
            if m:
                jalur = os.path.join(folder(), "dist", m.group(1) + ".zip")
                if not RE_SLUG.match(m.group(1)) or not os.path.isfile(jalur):
                    raise Tidak(404, "Zip belum ada. Bangun situs dulu.")
                with open(jalur, "rb") as f:
                    return self.kirim(200, f.read(), "application/zip", {"Content-Disposition": 'attachment; filename="%s.zip"' % m.group(1)})
            raise Tidak(404, "Halaman tidak ada.")
        if p == "/api/baru":
            d = self.json_tubuh(BATAS_JSON_ADMIN)
            jenis, slug = str(d.get("jenis", "")), str(d.get("slug", ""))
            proyek_baru(jenis, slug)
            return self.kirim(200, {"slug": slug})
        slug = self.slug_admin(q)
        if p == "/api/simpan":
            d = self.json_tubuh(BATAS_JSON_ADMIN)
            periksa_bentuk(d)
            if d.get("jenis") != dash.baca_json(slug).get("jenis"):
                raise GalatData("Data tidak valid: jenis usaha tidak boleh diubah.")
            with TULIS:
                dash.tulis_json(slug, d)
            return self.kirim(200, {"ok": True})
        if p == "/api/cek":
            return self.kirim(200, dash.cek(slug))
        if p == "/api/build":
            hasil = dash.bangun(slug)
            hasil.pop("folder", None)
            return self.kirim(200, hasil)
        if p == "/api/pratinjau":
            ada = os.path.isdir(dash.jalur_dist(slug))
            url = "%s://%s.%s/?k=%s" % (self.skema(), slug, CFG["pratinjau"], buat_tanda("pr|" + slug, 4 * 3600)) if ada else None
            return self.kirim(200, {"ada": ada, "url": url})
        if p == "/api/buka-kunci":
            with TULIS:
                m = baca_meta(slug)
                m["status"] = "buka"
                m.pop("dikirim", None)
                tulis_meta(slug, m)
            return self.kirim(200, {"ok": True})
        if p == "/api/token-baru":
            with TULIS:
                m = baca_meta(slug)
                m["token"] = secrets.token_urlsafe(24)
                tulis_meta(slug, m)
            return self.kirim(200, {"tautan": "/isi/" + m["token"]})
        if p == "/api/foto":
            nama = q.get("nama", "")
            if not dash.RE_FOTO.match(nama):
                raise GalatData("Nama berkas foto tidak valid. Pakai huruf, angka, titik, atau tanda hubung; ekstensi jpg atau png.")
            isi = self.tubuh(BATAS_FOTO_ADMIN)
            ext = os.path.splitext(nama)[1].lower()
            if ext == ".png" and not isi.startswith(b"\x89PNG\r\n\x1a\n"):
                raise GalatData("Berkas bukan PNG yang valid.")
            if ext in (".jpg", ".jpeg") and not isi.startswith(b"\xff\xd8"):
                raise GalatData("Berkas bukan JPG yang valid.")
            with TULIS:
                tulis_foto(slug, nama, isi, False)
            return self.kirim(200, {"ok": True, "berkas": nama})
        raise Tidak(404, "Rute tidak ada.")

    def pratinjau(self, slug, p, q):
        if not RE_SLUG.match(slug):
            raise Tidak(404, "Tidak ada.")
        ekstra = {"Content-Security-Policy": "frame-ancestors %s://%s" % (self.skema(), CFG["host"])}
        k = q.get("k")
        if k and cek_tanda("pr|" + slug, k):
            kuki = "pk=%s; Path=/; HttpOnly; SameSite=Lax; Max-Age=%d" % (k, 4 * 3600) + ("; Secure" if CFG["aman"] else "")
            self.send_response(302)
            self.send_header("Location", "/")
            self.send_header("Set-Cookie", kuki)
            self.send_header("Content-Length", "0")
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            return
        if not cek_tanda("pr|" + slug, self.kuki("pk") or ""):
            return self.kirim(401, "Pratinjau pribadi. Buka dari halaman admin.".encode("utf-8"), "text/plain; charset=utf-8", tanpa_csp=True)
        akar = os.path.realpath(dash.jalur_dist(slug))
        rel = p.lstrip("/")
        if rel == "" or rel.endswith("/"):
            rel += "index.html"
        penuh = os.path.realpath(os.path.join(akar, rel))
        if not (penuh == akar or penuh.startswith(akar + os.sep)) or not os.path.isfile(penuh):
            return self.kirim(404, "Tidak ada.".encode("utf-8"), "text/plain; charset=utf-8", tanpa_csp=True)
        tipe = mimetypes.guess_type(penuh)[0] or "application/octet-stream"
        if tipe.startswith("text/") or tipe in ("application/javascript", "application/json", "application/xml"):
            tipe += "; charset=utf-8"
        with open(penuh, "rb") as f:
            return self.kirim(200, f.read(), tipe, ekstra, tanpa_csp=True)


class Tidak(Exception):
    def __init__(self, kode, pesan):
        Exception.__init__(self, pesan)
        self.kode, self.pesan = kode, pesan


def atur():
    pw = os.environ.get("ISI_PASSWORD", "")
    if len(pw) < 12:
        raise GalatData("ISI_PASSWORD wajib diisi, minimal 12 karakter.")
    host = os.environ.get("ISI_HOST", "").strip().lower()
    pratinjau = os.environ.get("ISI_PRATINJAU", "").strip().lower()
    if not host or not pratinjau:
        raise GalatData("ISI_HOST dan ISI_PRATINJAU wajib diisi (contoh isi.rioeka.com dan pratinjau.rioeka.com).")
    CFG.update(
        folder=os.path.abspath(os.environ.get("ISI_DATA", "/data")),
        host=host,
        pratinjau=pratinjau,
        pw_hash=hashlib.sha256(pw.encode("utf-8")).digest(),
        kunci=hashlib.sha256(("isi-v1|" + (os.environ.get("ISI_SECRET") or pw)).encode("utf-8")).digest(),
        aman=os.environ.get("ISI_AMAN", "1") != "0",
        proxy=os.environ.get("ISI_PROXY", "1") != "0",
    )
    os.makedirs(CFG["folder"], exist_ok=True)
    dash.KEADAAN["folder"] = CFG["folder"]


def jalan():
    atur()
    port = int(os.environ.get("ISI_PORT", "8000"))
    s = ThreadingHTTPServer((os.environ.get("ISI_BIND", "0.0.0.0"), port), Penanganan)
    print("Layanan isi data: port %d, host %s, pratinjau *.%s, data %s" % (port, CFG["host"], CFG["pratinjau"], CFG["folder"]), flush=True)
    try:
        s.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        s.server_close()


if __name__ == "__main__":
    try:
        jalan()
    except GalatData as ex:
        print("GALAT:", ex, file=sys.stderr)
        sys.exit(1)
