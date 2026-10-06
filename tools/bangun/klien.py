import glob, hashlib, json, os, re, struct, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data import USAHA, USAHABY, URUT_HARI
from skin import SKIN, DEFAULT

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

RE_SLUG = re.compile(r"^[a-z0-9][a-z0-9-]*$")
RE_DOMAIN = re.compile(r"^(?=.{4,253}$)[a-z0-9]([a-z0-9-]*[a-z0-9])?(\.[a-z0-9]([a-z0-9-]*[a-z0-9])?)+$")
RE_JAM = re.compile(r"^(\d{2})\.(\d{2})$")
RE_WA = re.compile(r"^62\d{8,13}$")
RE_SISA = re.compile(r"\b(contoh|demo)\b", re.I)

SIAP_TEKS = ("harga_lead", "jam_lead", "tip_layanan", "pesan_lead")
WAJIB_BEDA = ("nama", "area", "wa", "wa_tampil", "alamat", "peta", "lead", "harga_catatan")
MODE_DATA = {"jadwal": ("grup", "stylist"), "inap": ("kamar",), "pesan": ("menu",)}


class GalatData(Exception):
    def __init__(self, pesan):
        Exception.__init__(self, "\n".join(pesan) if isinstance(pesan, list) else pesan)
        self.daftar = pesan if isinstance(pesan, list) else [pesan]


def ukuran_jpeg(path):
    with open(path, "rb") as f:
        d = f.read()
    if d[:2] != b"\xff\xd8":
        raise ValueError("bukan berkas JPEG")
    i = 2
    while i + 9 < len(d):
        if d[i] != 0xFF:
            i += 1
            continue
        m = d[i + 1]
        if m == 0xFF:
            i += 1
            continue
        if m in (0xD8, 0x01) or 0xD0 <= m <= 0xD7:
            i += 2
            continue
        panjang = struct.unpack(">H", d[i + 2:i + 4])[0]
        if 0xC0 <= m <= 0xCF and m not in (0xC4, 0xC8, 0xCC):
            h, w = struct.unpack(">HH", d[i + 5:i + 9])
            return w, h
        i += 2 + panjang
    raise ValueError("ukuran JPEG tidak terbaca")


def _md5(path):
    with open(path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()


def _foto_demo():
    hasil = set()
    for berkas in glob.glob(os.path.join(ROOT, "*", "img", "*.jpg")):
        hasil.add(_md5(berkas))
    return hasil


def _ke_json(v):
    return json.dumps(v, ensure_ascii=False, sort_keys=True)


def _jadwal_dari_data(u):
    return {
        "grup": [{"nama": g, "item": [{"nama": a, "harga": b, "menit": c, "ket": d} for a, b, c, d in it]} for g, it in u["grup"]],
        "stylist": [{"nama": a, "keahlian": b, "rinci": c, "bisa": list(d)} for a, b, c, d in u["stylist"]],
    }


def _ke_internal(mode, bagian):
    if mode == "jadwal":
        grup = [(g["nama"], [(i["nama"], i["harga"], i["menit"], i.get("ket", "")) for i in g["item"]]) for g in bagian["grup"]]
        stylist = [(s["nama"], s["keahlian"], s["rinci"], list(s["bisa"])) for s in bagian["stylist"]]
        return {"grup": grup, "stylist": stylist}
    if mode == "inap":
        kamar = [(k["nama"], k["harga"], k["kap"], k["ket"]) for k in bagian["kamar"]]
        grup = [("Tipe kamar", [(k[0], k[1], "Maks. %d tamu, per malam" % k[2]) for k in kamar])]
        return {"kamar": kamar, "grup": grup}
    menu = [(g["nama"], [dict(i) for i in g["item"]]) for g in bagian["menu"]]
    grup = [(g, [(it["nama"], it["harga"], it["ket"]) for it in items]) for g, items in menu]
    return {"menu": menu, "grup": grup}


def kerangka(jenis, slug, folder):
    if jenis not in USAHABY:
        raise GalatData("Jenis '%s' tidak dikenal. Pilihan: %s." % (jenis, ", ".join(USAHABY)))
    if not RE_SLUG.match(slug):
        raise GalatData("Slug '%s' tidak valid. Pakai huruf kecil, angka, dan tanda hubung." % slug)
    u = USAHABY[jenis]
    mode = u.get("mode", "jadwal")
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, slug + ".json")
    if os.path.exists(path):
        raise GalatData("Berkas %s sudah ada. Hapus dulu kalau mau membuat ulang." % path)
    d = {
        "_petunjuk": "Ganti semua isi yang masih berupa teks bawaan (nama, alamat, nomor WA, harga, FAQ, dan seterusnya). "
                     "Foto ditaruh di folder %s/ di samping berkas ini, JPG 720x540. Kunci berawalan _ diabaikan." % slug,
        "jenis": jenis,
        "skin": DEFAULT[jenis],
        "_skin_tersedia": list(SKIN[jenis]),
        "paket": 1,
        "domain": "GANTI-namausaha.com",
        "nama": u["nama"],
        "area": u["area"],
        "wa": u["wa"],
        "wa_tampil": u["wa_tampil"],
        "alamat": list(u["alamat"]),
        "peta": u["peta"],
        "jam": {str(h): u["jam"][h] for h in range(7)},
        "lead": u["lead"],
        "harga_lead": u["harga_lead"],
        "harga_catatan": u["harga_catatan"],
        "jam_lead": u["jam_lead"],
    }
    if mode == "jadwal":
        d.update(_jadwal_dari_data(u))
        d["tip_layanan"] = u["tip_layanan"]
        d["pesan_lead"] = u["pesan_lead"]
    elif mode == "inap":
        d["kamar"] = [{"nama": a, "harga": b, "kap": c, "ket": e} for a, b, c, e in u["kamar"]]
        d["checkin"] = u["checkin"]
        d["checkout"] = u["checkout"]
    else:
        d["menu"] = [{"nama": g, "item": [dict(i) for i in items]} for g, items in u["menu"]]
        d["ongkir"] = u["ongkir"]
        d["areaAntar"] = u["areaAntar"]
        d["tempatAmbil"] = u["tempatAmbil"]
    d["faq"] = [{"tanya": q, "jawab": a} for q, a in u["faq"]]
    d["foto"] = {
        "hero": {"berkas": "hero.jpg", "alt": "GANTI: deskripsi foto utama"},
        "galeri": [{"berkas": "foto1.jpg", "alt": "GANTI: deskripsi foto 1"}],
    }
    d["_bayar_paket_3"] = {"bank": "BCA", "rekening": "0000000000", "atas_nama": "Nama pemilik rekening", "qris": "qris.png"}
    d["muka"] = u.get("muka", 0.3)
    d["mukaTeks"] = u.get("mukaTeks", "30 persen")
    os.makedirs(os.path.join(folder, slug), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
        f.write("\n")
    return path


def kerangka_kosong(jenis, slug, folder):
    if jenis not in USAHABY:
        raise GalatData("Jenis '%s' tidak dikenal. Pilihan: %s." % (jenis, ", ".join(USAHABY)))
    if not RE_SLUG.match(slug):
        raise GalatData("Slug '%s' tidak valid. Pakai huruf kecil, angka, dan tanda hubung." % slug)
    u = USAHABY[jenis]
    mode = u.get("mode", "jadwal")
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, slug + ".json")
    if os.path.exists(path):
        raise GalatData("Berkas %s sudah ada." % path)
    d = {
        "jenis": jenis,
        "skin": DEFAULT[jenis],
        "paket": 1,
        "domain": "",
        "nama": "",
        "area": "",
        "wa": "",
        "wa_tampil": "",
        "alamat": ["", ""],
        "peta": "",
        "jam": {str(h): None for h in range(7)},
        "lead": "",
        "harga_lead": "",
        "harga_catatan": "",
        "jam_lead": "",
    }
    if mode == "jadwal":
        d["grup"] = [{"nama": "", "item": [{"nama": "", "harga": "", "menit": 30, "ket": ""}]}]
        d["stylist"] = [{"nama": "", "keahlian": "", "rinci": "", "bisa": []}]
        d["tip_layanan"] = ""
        d["pesan_lead"] = ""
    elif mode == "inap":
        d["kamar"] = [{"nama": "", "harga": "", "kap": 2, "ket": ""}]
        d["checkin"] = "14.00"
        d["checkout"] = "12.00"
    else:
        d["menu"] = [{"nama": "", "item": [{"nama": "", "harga": "", "min": 10, "maks": 100, "satuan": "box", "ket": "", "lead": 2}]}]
        d["ongkir"] = 0
        d["areaAntar"] = ""
        d["tempatAmbil"] = ""
    d["faq"] = [{"tanya": "", "jawab": ""}]
    d["foto"] = {"hero": {"berkas": "", "alt": ""}, "galeri": []}
    d["muka"] = u.get("muka", 0.3)
    d["mukaTeks"] = u.get("mukaTeks", "30 persen")
    os.makedirs(os.path.join(folder, slug), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
        f.write("\n")
    return path


def _jam_ok(blok, nama, galat):
    if blok is None:
        return
    if not (isinstance(blok, list) and len(blok) == 2 and all(isinstance(x, str) for x in blok)):
        galat.append("jam %s: isi null (tutup) atau [\"HH.MM\", \"HH.MM\"]." % nama)
        return
    menit = []
    for x in blok:
        m = RE_JAM.match(x)
        if not m or int(m.group(1)) > 23 or int(m.group(2)) > 59:
            galat.append("jam %s: '%s' bukan format HH.MM yang valid (contoh 09.00)." % (nama, x))
            return
        menit.append(int(m.group(1)) * 60 + int(m.group(2)))
    if menit[0] >= menit[1]:
        galat.append("jam %s: jam tutup harus lebih akhir dari jam buka. Buka 24 jam atau lewat tengah malam belum didukung." % nama)


def _angka(v, nama, galat, minimal=1, bulat=True):
    if isinstance(v, bool) or not isinstance(v, int if bulat else (int, float)) or v < minimal:
        galat.append("%s harus angka %s minimal %s." % (nama, "bulat" if bulat else "", minimal))
        return False
    return True


def _teks(v, nama, galat):
    if not isinstance(v, str) or not v.strip():
        galat.append("%s wajib diisi (teks tidak kosong)." % nama)
        return False
    return True


def _daftar(v, nama, galat):
    if not isinstance(v, list) or not v:
        galat.append("%s wajib berupa daftar yang tidak kosong." % nama)
        return False
    return True


def _cek_jadwal(d, galat):
    if not _daftar(d.get("grup"), "grup", galat) or not _daftar(d.get("stylist"), "stylist", galat):
        return
    nama_layanan = []
    for g in d["grup"]:
        if not isinstance(g, dict) or not _teks(g.get("nama"), "grup[].nama", galat) or not _daftar(g.get("item"), "grup '%s' item" % g.get("nama"), galat):
            continue
        for it in g["item"]:
            ket = "layanan '%s'" % it.get("nama")
            if not isinstance(it, dict) or not _teks(it.get("nama"), "layanan.nama", galat):
                continue
            _angka(it.get("harga"), "harga " + ket, galat)
            _angka(it.get("menit"), "menit " + ket, galat)
            nama_layanan.append(it["nama"])
    ulang = {n for n in nama_layanan if nama_layanan.count(n) > 1}
    for n in sorted(ulang):
        galat.append("nama layanan '%s' dipakai lebih dari sekali. Nama harus unik." % n)
    stylist = set()
    for s in d["stylist"]:
        if not isinstance(s, dict) or not _teks(s.get("nama"), "stylist.nama", galat):
            continue
        if s["nama"] in stylist:
            galat.append("nama stylist '%s' dipakai lebih dari sekali." % s["nama"])
        stylist.add(s["nama"])
        _teks(s.get("keahlian"), "keahlian %s" % s["nama"], galat)
        _teks(s.get("rinci"), "rinci %s" % s["nama"], galat)
        if not _daftar(s.get("bisa"), "bisa %s" % s["nama"], galat):
            continue
        for b in s["bisa"]:
            if b not in nama_layanan:
                galat.append("stylist '%s': nama '%s' di 'bisa' tidak sama persis dengan nama layanan mana pun." % (s["nama"], b))
    dikerjakan = {b for s in d["stylist"] if isinstance(s, dict) and isinstance(s.get("bisa"), list) for b in s["bisa"]}
    for n in nama_layanan:
        if n not in dikerjakan:
            galat.append("layanan '%s' tidak dikerjakan stylist mana pun (tidak ada di 'bisa')." % n)


def _cek_inap(d, galat):
    if not _daftar(d.get("kamar"), "kamar", galat):
        return
    nama = []
    for k in d["kamar"]:
        if not isinstance(k, dict) or not _teks(k.get("nama"), "kamar.nama", galat):
            continue
        nama.append(k["nama"])
        _angka(k.get("harga"), "harga kamar '%s'" % k["nama"], galat)
        _angka(k.get("kap"), "kap (kapasitas tamu) kamar '%s'" % k["nama"], galat)
        _teks(k.get("ket"), "ket kamar '%s'" % k["nama"], galat)
    for n in sorted({n for n in nama if nama.count(n) > 1}):
        galat.append("nama kamar '%s' dipakai lebih dari sekali." % n)
    for kunci in ("checkin", "checkout"):
        v = d.get(kunci)
        if not isinstance(v, str) or not RE_JAM.match(v) or int(v[:2]) > 23 or int(v[3:]) > 59:
            galat.append("%s harus berformat HH.MM (contoh 14.00)." % kunci)


def _cek_menu(d, galat):
    if not _daftar(d.get("menu"), "menu", galat):
        return
    nama = []
    for g in d["menu"]:
        if not isinstance(g, dict) or not _teks(g.get("nama"), "menu[].nama", galat) or not _daftar(g.get("item"), "menu '%s' item" % g.get("nama"), galat):
            continue
        for it in g["item"]:
            if not isinstance(it, dict) or not _teks(it.get("nama"), "menu.item.nama", galat):
                continue
            k = "menu '%s'" % it["nama"]
            nama.append(it["nama"])
            _angka(it.get("harga"), "harga " + k, galat)
            ok_min = _angka(it.get("min"), "min " + k, galat)
            ok_maks = _angka(it.get("maks"), "maks " + k, galat)
            if ok_min and ok_maks and it["maks"] < it["min"]:
                galat.append("%s: maks tidak boleh lebih kecil dari min." % k)
            _angka(it.get("lead"), "lead (hari pesan lebih awal) " + k, galat, minimal=0)
            _teks(it.get("satuan"), "satuan " + k, galat)
            _teks(it.get("ket"), "ket " + k, galat)
    for n in sorted({n for n in nama if nama.count(n) > 1}):
        galat.append("nama menu '%s' dipakai lebih dari sekali." % n)
    _angka(d.get("ongkir"), "ongkir", galat, minimal=0)
    _teks(d.get("areaAntar"), "areaAntar", galat)
    _teks(d.get("tempatAmbil"), "tempatAmbil", galat)


def _cek_foto(d, folder_foto, galat, aset):
    foto = d.get("foto")
    if not isinstance(foto, dict) or not isinstance(foto.get("hero"), dict):
        galat.append("foto.hero wajib diisi: {\"berkas\": \"hero.jpg\", \"alt\": \"...\"}.")
        return None, []
    demo = _foto_demo()
    sudah = {}

    def periksa(item, nama_keluar, label):
        if not isinstance(item, dict) or not _teks(item.get("berkas"), label + ".berkas", galat) or not _teks(item.get("alt"), label + ".alt", galat):
            return False
        if item["alt"].startswith("GANTI"):
            galat.append("%s.alt masih berisi teks petunjuk. Tulis deskripsi foto yang sebenarnya." % label)
        sumber = os.path.join(folder_foto, item["berkas"])
        if not os.path.isfile(sumber):
            galat.append("%s: berkas foto tidak ada: %s" % (label, sumber))
            return False
        if os.path.basename(item["berkas"]) != item["berkas"] or item["berkas"].startswith("."):
            galat.append("%s: nama berkas tidak valid (tanpa folder)." % label)
            return False
        if not item["berkas"].lower().endswith((".jpg", ".jpeg")):
            galat.append("%s: foto harus JPG (%s)." % (label, item["berkas"]))
            return False
        try:
            w, h = ukuran_jpeg(sumber)
        except ValueError as ex:
            galat.append("%s: %s (%s)." % (label, ex, item["berkas"]))
            return False
        if (w, h) != (720, 540):
            galat.append("%s: ukuran %s harus 720x540, sekarang %dx%d." % (label, item["berkas"], w, h))
            return False
        md5 = _md5(sumber)
        if md5 in demo:
            galat.append("%s: %s sama dengan foto demo bawaan. Situs klien wajib memakai foto klien sendiri." % (label, item["berkas"]))
            return False
        if md5 in sudah:
            galat.append("%s: %s sama dengan foto %s (dipakai dua kali)." % (label, item["berkas"], sudah[md5]))
        sudah[md5] = label
        aset[nama_keluar] = sumber
        return True

    hero = None
    if periksa(foto["hero"], "hero.jpg", "foto.hero"):
        hero = ("hero.jpg", foto["hero"]["alt"])
    galeri = []
    g = foto.get("galeri", [])
    if not isinstance(g, list):
        galat.append("foto.galeri harus berupa daftar (boleh kosong).")
        g = []
    for n, item in enumerate(g, 1):
        if periksa(item, "g%d.jpg" % n, "foto.galeri[%d]" % n):
            galeri.append(("g%d.jpg" % n, item["alt"]))
    return hero, galeri


def _cek_bayar(d, folder_foto, galat, aset):
    b = d.get("bayar")
    if not isinstance(b, dict):
        galat.append("Paket 3 butuh 'bayar': {\"bank\", \"rekening\", \"atas_nama\"} dan/atau {\"qris\": \"berkas.png\"}.")
        return None
    hasil = {}
    ada_transfer = any(b.get(k) for k in ("bank", "rekening", "atas_nama"))
    if ada_transfer:
        for k in ("bank", "rekening", "atas_nama"):
            if not _teks(b.get(k), "bayar." + k, galat):
                break
        else:
            hasil.update(bank=b["bank"], rekening=b["rekening"], atas_nama=b["atas_nama"])
    if b.get("qris"):
        if not isinstance(b["qris"], str) or os.path.basename(b["qris"]) != b["qris"] or b["qris"].startswith("."):
            galat.append("bayar.qris: nama berkas tidak valid (tanpa folder).")
            return hasil or None
        sumber = os.path.join(folder_foto, b["qris"])
        ext = os.path.splitext(b["qris"])[1].lower()
        if not os.path.isfile(sumber):
            galat.append("bayar.qris: berkas tidak ada: %s" % sumber)
        elif ext not in (".png", ".jpg", ".jpeg"):
            galat.append("bayar.qris harus PNG atau JPG.")
        else:
            aset["qris" + ext] = sumber
            hasil["qris"] = "qris" + ext
    if not hasil and not galat:
        galat.append("bayar: isi data rekening (bank, rekening, atas_nama) dan/atau qris.")
    return hasil or None


def _kumpul_teks(v, keluar):
    if isinstance(v, str):
        keluar.append(v)
    elif isinstance(v, dict):
        for k, x in v.items():
            if not str(k).startswith("_"):
                _kumpul_teks(x, keluar)
    elif isinstance(v, list):
        for x in v:
            _kumpul_teks(x, keluar)


def _inisial(nama):
    kata = [w for w in re.split(r"\s+", nama.strip()) if w[:1].isalnum()]
    kode = "".join(w[0] for w in kata)[:3].upper()
    return kode or "XX"


def muat(slug, folder, d=None):
    path = os.path.join(folder, slug + ".json")
    if d is None:
        if not os.path.isfile(path):
            raise GalatData("Berkas data tidak ada: %s. Buat dulu dengan --baru." % path)
        try:
            with open(path, "r", encoding="utf-8") as f:
                d = json.load(f)
        except ValueError as ex:
            raise GalatData("Berkas %s bukan JSON yang valid: %s" % (path, ex))
    if not isinstance(d, dict):
        raise GalatData("Isi %s harus berupa objek JSON." % path)
    galat = []
    jenis = d.get("jenis")
    if jenis not in USAHABY:
        raise GalatData("jenis '%s' tidak dikenal. Pilihan: %s." % (jenis, ", ".join(USAHABY)))
    asal = USAHABY[jenis]
    mode = asal.get("mode", "jadwal")
    if not RE_SLUG.match(slug):
        galat.append("Slug '%s' tidak valid. Pakai huruf kecil, angka, dan tanda hubung." % slug)
    skin = d.get("skin")
    if skin not in SKIN[jenis]:
        galat.append("skin '%s' tidak ada untuk %s. Pilihan: %s." % (skin, jenis, ", ".join(SKIN[jenis])))
    paket = d.get("paket")
    try:
        paket = int(paket)
    except (TypeError, ValueError):
        paket = None
    if paket not in (1, 2, 3):
        galat.append("paket harus 1, 2, atau 3.")
    domain = d.get("domain")
    if not isinstance(domain, str) or not RE_DOMAIN.match(domain) or domain.startswith("ganti"):
        galat.append("domain '%s' tidak valid. Tulis hanya nama domain, tanpa https:// dan tanpa garis miring." % domain)
    for k in ("nama", "area", "peta", "lead", "wa_tampil"):
        _teks(d.get(k, asal.get(k)), k, galat)
    if not isinstance(d.get("wa"), str) or not RE_WA.match(d.get("wa", "")):
        galat.append("wa harus angka saja berawalan 62 (contoh 6281234567890), tanpa spasi, tanda hubung, atau +.")
    alamat = d.get("alamat")
    if not isinstance(alamat, list) or len(alamat) < 2 or not all(isinstance(x, str) and x.strip() for x in alamat):
        galat.append("alamat harus daftar teks minimal 2 baris: jalan, lalu kecamatan dan kota. Baris ketiga (patokan) opsional.")
    jam = d.get("jam")
    if not isinstance(jam, dict) or {str(h) for h in range(7)} - set(jam):
        galat.append("jam harus punya kunci \"0\" sampai \"6\" (0 = Minggu).")
        jam = {}
    for h in range(7):
        if str(h) in jam:
            _jam_ok(jam[str(h)], str(h), galat)
    if jam and all(jam.get(str(h)) is None for h in range(7)):
        galat.append("jam: minimal satu hari harus buka.")
    faq = d.get("faq")
    if _daftar(faq, "faq", galat):
        for i, q in enumerate(faq, 1):
            if not (isinstance(q, dict) and _teks(q.get("tanya"), "faq[%d].tanya" % i, galat) and _teks(q.get("jawab"), "faq[%d].jawab" % i, galat)):
                break
    if "harga_catatan" in d and d["harga_catatan"] is not None and not isinstance(d["harga_catatan"], str):
        galat.append("harga_catatan harus teks (boleh kosong).")
    if mode == "jadwal":
        _cek_jadwal(d, galat)
    elif mode == "inap":
        _cek_inap(d, galat)
    else:
        _cek_menu(d, galat)
    muka = d.get("muka", asal.get("muka", 0.3))
    if isinstance(muka, bool) or not isinstance(muka, (int, float)) or not 0 < muka <= 1:
        galat.append("muka harus angka lebih dari 0 dan paling besar 1 (contoh 0.3).")
    folder_foto = os.path.join(folder, slug)
    aset = {}
    hero, galeri = _cek_foto(d, folder_foto, galat, aset)
    bayar = _cek_bayar(d, folder_foto, galat, aset) if paket == 3 else None

    semua = []
    _kumpul_teks({k: v for k, v in d.items() if k not in ("domain", "foto", "bayar", "skin", "jenis")}, semua)
    for t in semua:
        m = RE_SISA.search(t)
        if m:
            galat.append("Sisa teks contoh: '%s' ada di \"%s\". Ganti dengan isi klien." % (m.group(0), t[:60]))
    nama_bawaan = {x["nama"] for x in USAHA}
    if d.get("nama") in nama_bawaan:
        galat.append("nama '%s' masih nama usaha bawaan demo." % d.get("nama"))
    wa_bawaan = {x["wa"] for x in USAHA}
    if d.get("wa") in wa_bawaan:
        galat.append("wa %s adalah nomor contoh bawaan demo." % d.get("wa"))
    tampil_bawaan = {x["wa_tampil"] for x in USAHA}
    if d.get("wa_tampil") in tampil_bawaan:
        galat.append("wa_tampil %s adalah nomor contoh bawaan demo." % d.get("wa_tampil"))
    ada_galat_bentuk = bool(galat)
    for k in WAJIB_BEDA:
        if k in ("nama", "wa", "wa_tampil"):
            continue
        if k in d and _ke_json(d[k]) == _ke_json(asal[k] if k != "alamat" else list(asal["alamat"])):
            galat.append("%s masih sama dengan teks bawaan demo. Ganti dengan isi klien." % k)
    if mode == "jadwal":
        bagian_asli = _jadwal_dari_data(asal)
        for k in ("grup", "stylist"):
            if k in d and _ke_json(d[k]) == _ke_json(bagian_asli[k]):
                galat.append("%s masih sama dengan data bawaan demo. Ganti dengan isi klien." % k)
    elif mode == "inap":
        if "kamar" in d and _ke_json(d["kamar"]) == _ke_json([{"nama": a, "harga": b, "kap": c, "ket": e} for a, b, c, e in asal["kamar"]]):
            galat.append("kamar masih sama dengan data bawaan demo. Ganti dengan isi klien.")
    else:
        if "menu" in d and _ke_json(d["menu"]) == _ke_json([{"nama": g, "item": it} for g, it in asal["menu"]]):
            galat.append("menu masih sama dengan data bawaan demo. Ganti dengan isi klien.")
    if "faq" in d and _ke_json(d["faq"]) == _ke_json([{"tanya": q, "jawab": a} for q, a in asal["faq"]]):
        galat.append("faq masih sama dengan data bawaan demo. Ganti dengan isi klien.")

    if galat:
        raise GalatData(galat)

    u = dict(asal)
    u["mode"] = mode
    u["nama"] = d["nama"].strip()
    u["area"] = d["area"].strip()
    u["wa"] = d["wa"]
    u["wa_tampil"] = d["wa_tampil"]
    u["alamat"] = list(alamat)
    u["peta"] = d["peta"]
    u["jam"] = {h: jam[str(h)] for h in range(7)}
    u["lead"] = d["lead"]
    u["faq"] = [(q["tanya"], q["jawab"]) for q in faq]
    u["harga_catatan"] = (d.get("harga_catatan") if "harga_catatan" in d else asal["harga_catatan"]) or ""
    for k in SIAP_TEKS:
        if d.get(k):
            u[k] = d[k]
    u.update(_ke_internal(mode, d))
    if mode == "inap":
        u["checkin"], u["checkout"] = d["checkin"], d["checkout"]
    if mode == "pesan":
        u["ongkir"], u["areaAntar"], u["tempatAmbil"] = d["ongkir"], d["areaAntar"], d["tempatAmbil"]
    u["muka"] = muka
    u["mukaTeks"] = d.get("mukaTeks") or ("%d persen" % round(muka * 100))
    if d.get("bayarNanti"):
        u["bayarNanti"] = d["bayarNanti"]
    nama = u["nama"]
    kota = u["area"].split(",")[0]
    u["kode"] = d.get("kode") or _inisial(nama)
    u["wa_pesan"] = d.get("wa_pesan") or {
        "jadwal": "Halo, saya mau tanya soal booking di %s." % nama,
        "inap": "Halo, saya mau tanya ketersediaan kamar di %s." % nama,
        "pesan": "Halo, saya mau tanya soal pesanan di %s." % nama,
    }[mode]
    u["title_p1"] = d.get("title") or "%s, %s" % (nama, kota)
    if mode == "jadwal":
        desc = "Harga, jam buka, alamat, dan cara menghubungi %s." % nama
        book = "Pesan layanan, pilih %s, tanggal, dan jam di %s." % (u["noun"].lower(), nama)
    elif mode == "inap":
        desc = "Tipe kamar, harga per malam, fasilitas, lokasi, dan cara menghubungi %s." % nama
        book = "Pesan kamar, pilih tanggal, jumlah malam, dan tamu di %s." % nama
    else:
        desc = "Menu, harga, jumlah minimal, dan cara memesan di %s." % nama
        book = "Pesan menu, tanggal, dan cara terima di %s." % nama
    u["desc_p1"] = d.get("deskripsi") or desc
    u["desc_book"] = d.get("deskripsi") or book
    u["galeri_lead"] = d.get("galeri_lead") or "Foto suasana dan layanan di %s." % nama
    u["hero_foto"] = hero
    u["galeri"] = galeri
    u["domain"] = domain
    u["paket"] = paket
    u["skin"] = skin
    u["bayar"] = bayar
    u["_aset"] = aset
    u["_peringatan"] = [
        "%s memakai teks bawaan demo. Periksa apakah cocok untuk klien ini." % k
        for k in SIAP_TEKS if k in asal and not d.get(k)
    ]
    return u
