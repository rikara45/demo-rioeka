import contextlib, glob, io, json, os, re, subprocess, sys, threading, traceback, webbrowser
from http.server import BaseHTTPRequestHandler, SimpleHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, unquote, urlparse

AKAR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AKAR)
import build
from data import USAHABY
from klien import ROOT, RE_SLUG, GalatData, kerangka, muat
from skin import DEFAULT, SKIN

RE_FOTO = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,59}\.(jpe?g|png)$", re.I)
BATAS_UNGGAH = 6 * 1024 * 1024
BATAS_JSON = 2 * 1024 * 1024
KUNCI = threading.Lock()
KEADAAN = {"folder": None, "port": 0, "port_pratinjau": 0, "pratinjau": None}
TIPE = {".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".png": "image/png"}


def jalur_data(slug):
    return os.path.join(KEADAAN["folder"], slug + ".json")


def jalur_foto(slug):
    return os.path.join(KEADAAN["folder"], slug)


def jalur_dist(slug):
    return os.path.join(KEADAAN["folder"], "dist", slug)


def baca_json(slug):
    with open(jalur_data(slug), "r", encoding="utf-8") as f:
        return json.load(f)


def tulis_json(slug, d):
    sementara = jalur_data(slug) + ".tmp"
    with open(sementara, "w", encoding="utf-8", newline="\n") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
        f.write("\n")
    os.replace(sementara, jalur_data(slug))


def meta():
    jenis = {}
    for j, u in USAHABY.items():
        jenis[j] = {
            "label": u["label"],
            "mode": u.get("mode", "jadwal"),
            "noun": u.get("noun"),
            "bawaan": DEFAULT[j],
            "skin": {k: {"nama": v["nama"], "ringkas": v["ringkas"], "cocok": v["cocok"], "warna": v["warna"]} for k, v in SKIN[j].items()},
        }
    return {"jenis": jenis, "folder": KEADAAN["folder"], "pratinjau": "http://127.0.0.1:%d" % KEADAAN["port_pratinjau"]}


def daftar_proyek():
    hasil = []
    for p in sorted(glob.glob(os.path.join(KEADAAN["folder"], "*.json"))):
        slug = os.path.basename(p)[:-5]
        if not RE_SLUG.match(slug):
            continue
        try:
            with open(p, "r", encoding="utf-8") as f:
                d = json.load(f)
        except (OSError, ValueError):
            continue
        if not isinstance(d, dict):
            continue
        hasil.append({"slug": slug, "jenis": d.get("jenis"), "nama": d.get("nama"), "paket": d.get("paket"), "dist": os.path.isdir(jalur_dist(slug))})
    return hasil


def cek(slug):
    try:
        u = muat(slug, KEADAAN["folder"])
    except GalatData as ex:
        return {"galat": list(ex.daftar), "peringatan": []}
    return {"galat": [], "peringatan": list(u["_peringatan"])}


def bangun(slug):
    keluaran = io.StringIO()
    with KUNCI, contextlib.redirect_stdout(keluaran):
        try:
            build.build_klien(slug, KEADAAN["folder"])
        except GalatData as ex:
            return {"ok": False, "galat": list(ex.daftar), "peringatan": []}
        except OSError as ex:
            return {"ok": False, "galat": ["Gagal menulis keluaran: %s. Tutup program yang sedang membuka folder dist/%s, lalu coba lagi." % (ex, slug)], "peringatan": []}
    KEADAAN["pratinjau"] = jalur_dist(slug)
    peringatan = [b[len("peringatan: "):] for b in keluaran.getvalue().splitlines() if b.startswith("peringatan: ")]
    return {"ok": True, "galat": [], "peringatan": peringatan, "folder": jalur_dist(slug), "zip": "/unduh/%s.zip" % slug}


def buka_folder(slug):
    jalur = jalur_dist(slug)
    if not os.path.isdir(jalur):
        raise GalatData("Folder keluaran belum ada. Bangun situs dulu.")
    if sys.platform == "win32":
        os.startfile(jalur)
    elif sys.platform == "darwin":
        subprocess.Popen(["open", jalur])
    else:
        subprocess.Popen(["xdg-open", jalur])


class Penanganan(BaseHTTPRequestHandler):
    server_version = "Dashboard"

    def log_message(self, *a):
        pass

    def kirim(self, kode, tubuh, tipe="application/json; charset=utf-8", tambahan=None):
        if not isinstance(tubuh, bytes):
            tubuh = json.dumps(tubuh, ensure_ascii=False).encode("utf-8")
        self.send_response(kode)
        self.send_header("Content-Type", tipe)
        self.send_header("Content-Length", str(len(tubuh)))
        self.send_header("Cache-Control", "no-store")
        for k, v in (tambahan or {}).items():
            self.send_header(k, v)
        self.end_headers()
        if self.command != "HEAD":
            self.wfile.write(tubuh)

    def galat(self, kode, pesan):
        self.kirim(kode, {"galat": pesan if isinstance(pesan, list) else [pesan]})

    def host_ok(self):
        return self.headers.get("Host", "") in ("127.0.0.1:%d" % KEADAAN["port"], "localhost:%d" % KEADAAN["port"])

    def asal_ok(self):
        asal = self.headers.get("Origin")
        return not asal or asal in ("http://127.0.0.1:%d" % KEADAAN["port"], "http://localhost:%d" % KEADAAN["port"])

    def tubuh(self, batas):
        n = int(self.headers.get("Content-Length") or 0)
        if n > batas:
            raise GalatData("Berkas terlalu besar (maks %d MB)." % (batas // 1024 // 1024))
        return self.rfile.read(n)

    def slug_ada(self, q):
        slug = q.get("slug", "")
        if not RE_SLUG.match(slug) or not os.path.isfile(jalur_data(slug)):
            raise GalatData("Proyek '%s' tidak ditemukan." % slug)
        return slug

    def do_GET(self):
        self.rute("GET")

    def do_HEAD(self):
        self.rute("GET")

    def do_POST(self):
        self.rute("POST")

    def rute(self, metode):
        u = urlparse(self.path)
        q = {k: v[0] for k, v in parse_qs(u.query).items()}
        p = unquote(u.path)
        if not self.host_ok():
            return self.galat(403, "Host tidak diizinkan.")
        if metode == "POST" and not self.asal_ok():
            return self.galat(403, "Asal permintaan tidak diizinkan.")
        try:
            if metode == "GET":
                return self.get(p, q)
            return self.post(p, q)
        except GalatData as ex:
            self.galat(400, list(ex.daftar))
        except (ValueError, KeyError) as ex:
            self.galat(400, "Permintaan tidak valid: %s" % ex)
        except Exception as ex:
            traceback.print_exc()
            self.galat(500, "Kesalahan di dashboard: %s" % ex)

    def get(self, p, q):
        if p == "/":
            with open(os.path.join(AKAR, "dashboard.html"), "rb") as f:
                return self.kirim(200, f.read(), "text/html; charset=utf-8")
        if p == "/api/meta":
            return self.kirim(200, meta())
        if p == "/api/proyek":
            return self.kirim(200, daftar_proyek())
        if p == "/api/data":
            return self.kirim(200, baca_json(self.slug_ada(q)))
        m = re.match(r"^/foto/([a-z0-9-]+)/([^/]+)$", p)
        if m:
            slug, nama = m.groups()
            jalur = os.path.join(jalur_foto(slug), nama)
            if not RE_SLUG.match(slug) or not RE_FOTO.match(nama) or not os.path.isfile(jalur):
                return self.galat(404, "Foto tidak ada.")
            with open(jalur, "rb") as f:
                return self.kirim(200, f.read(), TIPE[os.path.splitext(nama)[1].lower()])
        m = re.match(r"^/demo/([a-z]+)/([a-z0-9-]+)\.jpg$", p)
        if m:
            jenis, skin = m.groups()
            jalur = os.path.join(ROOT, jenis, "img", "skin-%s.jpg" % skin)
            if jenis not in SKIN or skin not in SKIN[jenis] or not os.path.isfile(jalur):
                return self.galat(404, "Pratinjau skin tidak ada.")
            with open(jalur, "rb") as f:
                return self.kirim(200, f.read(), "image/jpeg")
        m = re.match(r"^/unduh/([a-z0-9-]+)\.zip$", p)
        if m:
            jalur = os.path.join(KEADAAN["folder"], "dist", m.group(1) + ".zip")
            if not RE_SLUG.match(m.group(1)) or not os.path.isfile(jalur):
                return self.galat(404, "Zip belum ada. Bangun situs dulu.")
            with open(jalur, "rb") as f:
                return self.kirim(200, f.read(), "application/zip", {"Content-Disposition": 'attachment; filename="%s.zip"' % m.group(1)})
        self.galat(404, "Halaman tidak ada.")

    def post(self, p, q):
        if p == "/api/baru":
            d = json.loads(self.tubuh(BATAS_JSON) or b"{}")
            jenis, slug = str(d.get("jenis", "")), str(d.get("slug", ""))
            if RE_SLUG.match(slug) and os.path.isfile(jalur_data(slug)):
                raise GalatData("Proyek '%s' sudah ada. Pakai nama lain." % slug)
            kerangka(jenis, slug, KEADAAN["folder"])
            return self.kirim(200, {"slug": slug})
        slug = self.slug_ada(q)
        if p == "/api/simpan":
            d = json.loads(self.tubuh(BATAS_JSON))
            if not isinstance(d, dict) or d.get("jenis") != baca_json(slug).get("jenis"):
                raise GalatData("Data tidak valid: jenis usaha tidak boleh diubah.")
            tulis_json(slug, d)
            return self.kirim(200, {"ok": True})
        if p == "/api/cek":
            return self.kirim(200, cek(slug))
        if p == "/api/build":
            return self.kirim(200, bangun(slug))
        if p == "/api/pratinjau":
            if os.path.isdir(jalur_dist(slug)):
                KEADAAN["pratinjau"] = jalur_dist(slug)
            return self.kirim(200, {"ada": KEADAAN["pratinjau"] == jalur_dist(slug)})
        if p == "/api/buka":
            buka_folder(slug)
            return self.kirim(200, {"ok": True})
        if p == "/api/foto":
            nama = q.get("nama", "")
            if not RE_FOTO.match(nama):
                raise GalatData("Nama berkas foto tidak valid. Pakai huruf, angka, titik, atau tanda hubung; ekstensi jpg atau png.")
            isi = self.tubuh(BATAS_UNGGAH)
            ext = os.path.splitext(nama)[1].lower()
            if ext == ".png" and not isi.startswith(b"\x89PNG\r\n\x1a\n"):
                raise GalatData("Berkas bukan PNG yang valid.")
            if ext in (".jpg", ".jpeg") and not isi.startswith(b"\xff\xd8"):
                raise GalatData("Berkas bukan JPG yang valid.")
            os.makedirs(jalur_foto(slug), exist_ok=True)
            with open(os.path.join(jalur_foto(slug), nama), "wb") as f:
                f.write(isi)
            return self.kirim(200, {"ok": True, "berkas": nama})
        self.galat(404, "Rute tidak ada.")


class Pratinjau(SimpleHTTPRequestHandler):
    def __init__(self, *a, **k):
        super().__init__(*a, directory=KEADAAN["pratinjau"] or os.path.join(AKAR, "kosong"), **k)

    def log_message(self, *a):
        pass

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()


def ikat(kelas, awal):
    for port in range(awal, awal + 20):
        try:
            return ThreadingHTTPServer(("127.0.0.1", port), kelas), port
        except OSError:
            continue
    raise GalatData("Tidak ada port kosong dari %d sampai %d." % (awal, awal + 19))


def jalan(folder, port=8090, buka=True):
    folder = os.path.abspath(folder)
    os.makedirs(folder, exist_ok=True)
    KEADAAN["folder"] = folder
    utama, KEADAAN["port"] = ikat(Penanganan, port)
    sekunder, KEADAAN["port_pratinjau"] = ikat(Pratinjau, KEADAAN["port"] + 1)
    threading.Thread(target=sekunder.serve_forever, daemon=True).start()
    alamat = "http://127.0.0.1:%d/" % KEADAAN["port"]
    print("Dashboard klien: %s" % alamat)
    print("Folder data     : %s" % folder)
    print("Tekan Ctrl+C untuk berhenti.")
    if buka:
        threading.Timer(0.5, webbrowser.open, args=(alamat,)).start()
    try:
        utama.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        utama.server_close()
        sekunder.shutdown()


if __name__ == "__main__":
    argv = sys.argv[1:]
    folder = os.path.join(ROOT, "klien")
    port = 8090
    tanpa_buka = "--tanpa-buka" in argv
    if "--data" in argv and argv.index("--data") + 1 < len(argv):
        folder = argv[argv.index("--data") + 1]
    if "--port" in argv and argv.index("--port") + 1 < len(argv):
        port = int(argv[argv.index("--port") + 1])
    try:
        jalan(folder, port, not tanpa_buka)
    except GalatData as ex:
        print("GALAT:", ex, file=sys.stderr)
        sys.exit(1)
