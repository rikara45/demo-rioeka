import json, os, sys
from html import escape as e
from urllib.parse import quote
sys.path.insert(0, os.path.dirname(__file__))
from css import FONT, THEME_SALON, THEME_BARBER, BASE, BOOKING, INDEX_TOKENS, INDEX, ERR
from data import SALON, BARBER, URUT_HARI
from js import STATUS_JS, BAR_JS, BOOKING_JS

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NH = {0: "Minggu", 1: "Senin", 2: "Selasa", 3: "Rabu", 4: "Kamis", 5: "Jumat", 6: "Sabtu"}


def ikon(path, extra=""):
    return '<svg class="ikon" viewBox="0 0 24 24" aria-hidden="true"%s>%s</svg>' % (extra, path)


I_KANAN = ikon('<path d="m9 18 6-6-6-6"/>')
I_KIRI = ikon('<path d="m15 18-6-6 6-6"/>')
I_BAWAH = ikon('<path d="m6 9 6 6 6-6"/>')
I_CENTANG = ikon('<path d="M20 6 9 17l-5-5"/>')
I_WA = ikon('<path d="M21 11.5a8.4 8.4 0 0 1-12.4 7.4L3 20.5l1.6-5.4A8.4 8.4 0 1 1 21 11.5Z"/>')
I_PETA = ikon('<path d="M20 10c0 6-8 12-8 12S4 16 4 10a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/>')
I_KALENDER = ikon('<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/>')


def rp(n):
    return "Rp " + f"{n:,}".replace(",", ".")


def jam_teks(blok):
    return "tutup" if not blok else "%s sampai %s" % (blok[0], blok[1])


def wa_link(u):
    return "https://wa.me/%s?text=%s" % (u["wa"], quote(u["wa_pesan"], safe=""))


def head(title, desc, css, robots=True, warna=None):
    return (
        '<!DOCTYPE html>\n<html lang="id">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        + ('<meta name="robots" content="noindex, nofollow">\n' if robots else "")
        + '<meta name="theme-color" content="%s">\n' % (warna or ("#141210" if "E9A23B" in css else "#FBF6F2"))
        + "<title>%s</title>\n" % e(title)
        + '<meta name="description" content="%s">\n' % e(desc)
        + "<style>\n" + css + "\n</style>\n</head>\n"
    )


def kunci_tema(u):
    return THEME_SALON if u["tema"] == "salon" else THEME_BARBER


def opsi_radio(name, value, nama, harga, ket):
    return (
        '<label class="opsi"><input type="radio" name="%s" value="%s"><span class="opsi-kotak">'
        '<span class="opsi-tanda"></span><span class="opsi-nama">%s</span><span class="opsi-harga">%s</span>'
        '<span class="opsi-ket">%s</span></span></label>' % (name, value, nama, harga, ket)
    )


def seksi_pesan(u, n):
    bayar = n == 3
    total = 6 if bayar else 5
    nom = u["noun"]
    lead = u["pesan_lead"]
    panel_bayar = ""
    if bayar:
        panel_bayar = (
            '<div class="panel" data-langkah="bayar" hidden>'
            '<h3 tabindex="-1">Cara bayar</h3>'
            '<p class="tip">Total layanan <b id="b-total"></b>. Bayar muka <b id="b-muka"></b>, sisanya dibayar di kasir.</p>'
            '<div class="opsi-daftar">'
            + opsi_radio("cara", "qris", "QRIS", "semua bank", "Pindai kode dari bank atau e-wallet apa pun.")
            + opsi_radio("cara", "transfer", "Transfer bank", "BCA, Mandiri", "Kode bayar diberikan setelah memilih.")
            + opsi_radio("cara", "tempat", "Bayar di tempat", "saat datang", "Pesanan tetap dicatat, dibayar di kasir.")
            + "</div>"
            '<div id="panel-qris" class="panel-bayar" hidden><div class="qris" aria-hidden="true"></div>'
            "<p>Kode di atas hanya gambar, bukan kode bayar sungguhan.</p></div>"
            '<div id="panel-transfer" class="panel-bayar" hidden><p>Di halaman sungguhan, di sini muncul nomor rekening dan kode bayar khusus pesanan ini.</p></div>'
            "</div>"
        )
    return (
        '<section class="bagian" id="bagian-pesan" aria-labelledby="j-pesan">\n'
        '<h2 id="j-pesan">Isi pesanan</h2>\n<p class="bagian-lead">%s</p>\n'
        '<div class="kartu pesan" id="pesan">\n'
        '<div id="alur">\n'
        '<div class="langkah-kepala"><span class="langkah-no" id="l-no">Langkah 1 dari %d</span><span class="langkah-nama" id="l-nama">Layanan</span></div>\n'
        '<div class="progres" id="progres" role="progressbar" aria-label="Kemajuan pesanan" aria-valuemin="1" aria-valuemax="%d" aria-valuenow="1"><i id="progres-isi"></i></div>\n'
        '<div class="panel" data-langkah="layanan"><h3 tabindex="-1">Pilih layanan</h3><p class="tip">%s</p><div id="pilih-layanan"></div></div>\n'
        '<div class="panel" data-langkah="stylist" hidden><h3 tabindex="-1">Pilih %s</h3><p class="tip">Tidak punya pilihan? Pilih "%s".</p><div id="pilih-stylist"></div></div>\n'
        '<div class="panel" data-langkah="waktu" hidden><h3 tabindex="-1">Pilih tanggal dan jam</h3>'
        '<p class="tip">Dua minggu ke depan. Tanggal bergaris putus-putus berarti tutup.</p>'
        '<div class="hari-strip" id="pilih-hari" role="group" aria-label="Tanggal"></div>'
        '<p class="jam-label" id="jam-judul">Pilih tanggal dulu</p>'
        '<div class="jam-grid" id="pilih-jam" role="group" aria-labelledby="jam-judul"></div>'
        '<p class="petunjuk" style="margin-top:12px">Jam bergaris coret sudah terisi.</p></div>\n'
        '<div class="panel" data-langkah="data" hidden><h3 tabindex="-1">Nama dan nomor</h3>'
        '<p class="tip">Kami memakai nomor ini hanya untuk mengabari jam yang dikonfirmasi.</p>'
        '<div class="kolom"><label for="nama">Nama</label><input id="nama" name="nama" type="text" autocomplete="name" placeholder="Nama Anda"></div>'
        '<div class="kolom"><label for="wa">Nomor WhatsApp</label><input id="wa" name="wa" type="tel" inputmode="tel" autocomplete="tel" placeholder="0812 3456 7890"></div></div>\n'
        '<div class="panel" data-langkah="tinjau" hidden><h3 tabindex="-1">Periksa pesanan</h3>'
        '<p class="tip">Ketuk "Ubah" untuk memperbaiki. Pesanan di halaman contoh ini tidak tersimpan.</p>'
        '<dl class="tinjau" id="tinjau"></dl></div>\n'
        '%s\n'
        '<div class="aksi-langkah">'
        '<p class="ringkas-mini" id="mini" hidden></p>'
        '<p class="pesan-sistem" id="pesan-sistem" role="status" aria-live="polite"></p>'
        '<div class="baris-aksi tanpa-kembali" id="baris-aksi">'
        '<button class="tombol garis" id="kembali" type="button" hidden>Kembali</button>'
        '<button class="tombol" id="lanjut" type="button" aria-disabled="true">Lanjut</button></div></div>\n'
        '</div>\n'
        '<div id="selesai" class="selesai" hidden>'
        '<div id="k-centang" class="centang" aria-hidden="true"></div>'
        '<h3 tabindex="-1">Pesanan dicatat</h3><p class="langkah-nama">Kode pesanan</p><p class="kode" id="k-kode"></p>'
        '<dl class="tinjau" id="k-ringkas"></dl>'
        '<p class="catatan">Halaman contoh. Pesanan ini tidak tersimpan di mana pun.</p>'
        '<div class="aksi"><a class="tombol" id="k-wa" href="#">Kirim ke WhatsApp</a><button class="tombol garis" id="ulang" type="button">Pesan lagi</button></div>'
        '</div>\n'
        '</div>\n</section>\n'
    ) % (e(lead), total, total, e(u["tip_layanan"]), e(nom.lower()), e(u["siapa_saja"]), panel_bayar)


def seksi_harga(u):
    out = ['<section class="bagian" id="harga">\n<h2>Daftar harga</h2>\n<p class="bagian-lead">%s</p>\n' % e(u["harga_lead"])]
    for nama, item in u["grup"]:
        out.append('<div class="kartu"><h3>%s</h3><ul class="harga">' % e(nama))
        for nm, hr, _, ket in item:
            out.append('<li><span class="nm">%s</span><span class="hr">%s</span>%s</li>' % (e(nm), rp(hr), '<span class="ket">%s</span>' % e(ket) if ket else ""))
        out.append("</ul></div>")
    out.append('<p class="catatan">%s</p>\n</section>\n' % e(u["harga_catatan"]))
    return "".join(out)


def seksi_lokasi(u):
    li = "".join(
        '<li data-hari="%d"><span>%s</span><span>%s</span></li>' % (h, NH[h], jam_teks(u["jam"][h])) for h in URUT_HARI
    )
    peta = "https://www.google.com/maps/search/?api=1&amp;query=" + quote(u["peta"])
    return (
        '<section class="bagian" id="lokasi">\n<h2>Lokasi dan jam buka</h2>\n<p class="bagian-lead">%s</p>\n'
        '<div class="kartu"><h3>Jam buka</h3><ul class="jam" id="kartu-jam">%s</ul></div>\n'
        '<div class="kartu"><h3>Alamat</h3><address class="alamat">%s</address>'
        '<div class="aksi-lokasi"><a class="tombol garis" href="%s">%s Buka di Google Maps</a></div></div>\n</section>\n'
    ) % (e(u["jam_lead"]), li, "<br>".join(e(x) for x in u["alamat"]), peta, I_PETA)


def seksi_galeri(u):
    p = "".join(
        '<figure class="petak"><img src="/%s/img/%s.jpg" alt="%s" width="720" height="540" loading="lazy" decoding="async"></figure>' % (u["slug"], f, e(a))
        for f, a in u["galeri"]
    )
    return (
        '<section class="bagian" id="galeri">\n<h2>Galeri</h2>\n<p class="bagian-lead">%s</p>\n<div class="galeri">%s</div>\n'
        '<p class="kredit">Foto contoh dari <a href="https://unsplash.com/license" rel="noopener">Unsplash</a>, bebas dipakai.</p>\n</section>\n'
    ) % (e(u["galeri_lead"]), p)


def seksi_tanya(u):
    d = "".join('<details><summary>%s%s</summary><p>%s</p></details>' % (e(q), I_BAWAH, e(a)) for q, a in u["faq"])
    return '<section class="bagian" id="tanya">\n<h2>Pertanyaan yang sering masuk</h2>\n<div class="tanya">%s</div>\n</section>\n' % d


def halaman_demo(u, n):
    css = FONT + "\n:root{" + kunci_tema(u) + "}\n" + BASE + (BOOKING if n >= 2 else "")
    judul = {1: u["title_p1"], 2: u["nama"] + ", booking", 3: u["nama"] + ", booking dan pembayaran"}[n]
    desc = u["desc_p1"] if n == 1 else (u["desc_book"] if n == 2 else u["desc_book"].rstrip(".") + ", lalu bayar muka.")
    wa = wa_link(u)
    jam_json = json.dumps({str(h): u["jam"][h] for h in range(7)})

    loncat = ['<a href="#harga">Harga</a>', '<a href="#lokasi">Lokasi</a>']
    if n == 1:
        loncat.append('<a href="#galeri">Galeri</a>')
    loncat.append('<a href="#tanya">Tanya jawab</a>')
    if n >= 2:
        loncat.insert(0, '<a href="#pesan">Pesan</a>')

    if n == 1:
        aksi = '<a class="tombol" href="%s">%s Tanya lewat WhatsApp</a><a class="tombol garis" href="/%s/paket-2/">Buka demo Paket 2, dengan booking %s</a>' % (wa, I_WA, u["slug"], I_KANAN)
    else:
        aksi = '<a class="tombol" href="#pesan">%s Pesan sekarang</a><a class="tombol garis" href="%s">%s Tanya lewat WhatsApp</a>' % (I_KALENDER, wa, I_WA)

    if n == 1:
        demo = '<p class="catatan-demo"><span class="tanda-contoh">Demo Paket 1</span><span>Anda sedang membuka demo halaman informasi, tanpa booking. Untuk melihat versi yang bisa menerima pesanan, buka demo Paket 2.</span></p>'
    elif n == 2:
        demo = '<p class="catatan-demo"><span class="tanda-contoh">Demo Paket 2</span><span>Pesanan di halaman ini tidak tersimpan. Halaman contoh ini hanya memperlihatkan alurnya. Setelah halaman ini terpasang di tempat Anda, pesanan masuk ke WhatsApp atau ke catatan %s.</span></p>' % e(u["jenis"].lower())
    else:
        demo = '<p class="catatan-demo"><span class="tanda-contoh">Demo Paket 3</span><span>Pembayaran di halaman ini simulasi. Tidak ada uang yang berpindah, dan tidak ada data kartu yang diminta.</span></p>'

    kontak = "Pesan dan pertanyaan:" if u["tema"] == "barber" else "Booking dan pertanyaan:"

    body = [
        "<body>\n",
        '<header class="atas"><div class="wadah"><a class="balik" href="/">%s Daftar paket</a><span class="nama-atas">%s</span></div></header>\n' % (I_KIRI, e(u["nama"])),
        '<div class="pole" aria-hidden="true"></div>\n',
        "<main>\n",
        '<div class="wadah">\n',
        '<section class="hero">\n<p class="eyebrow">%s &middot; %s</p>\n<h1>%s</h1>\n' % (e(u["jenis"]), e(u["area"]), e(u["nama"])),
        '<p class="status" id="status"><span class="titik" id="titik"></span><span id="status-teks">Memuat jam buka</span></p>\n',
        '<p class="lead">%s</p>\n<div class="aksi">%s</div>\n%s\n' % (e(u["lead"]), aksi, demo),
        '<nav class="loncat" aria-label="Loncat ke bagian">%s</nav>\n</section>\n' % "".join(loncat),
    ]
    if n >= 2:
        body.append(seksi_pesan(u, n))
    body.append(seksi_harga(u))
    body.append(seksi_lokasi(u))
    if n == 1:
        body.append(seksi_galeri(u))
    body.append(seksi_tanya(u))
    body.append("</div>\n</main>\n")
    body.append(
        '<footer class="kaki"><div class="wadah"><p>%s</p><p><a href="%s">WhatsApp %s</a></p>'
        "<p>Halaman ini contoh peragaan, bukan usaha sungguhan. Dibuat oleh Rio Ekaputra Siswa, developer aplikasi web di Bandung yang membuat website untuk usaha lokal. <a href=\"https://rioeka.com\">rioeka.com</a></p></div></footer>\n" % (kontak, wa, e(u["wa_tampil"]))
    )
    if n == 1:
        bar = '<a class="tombol" href="%s">%s Tanya lewat WhatsApp</a>' % (wa, I_WA)
    else:
        bar = '<a class="tombol" href="#pesan">Pesan sekarang</a><a class="tombol garis" href="%s">WhatsApp</a>' % wa
    body.append('<div class="bar-bawah" id="bar-bawah">%s</div>\n' % bar)

    scripts = "<script>\n" + STATUS_JS.replace("__JAM__", jam_json) + "</script>\n"
    if n >= 2:
        D = {
            "noun": u["noun"],
            "kode": u["kode"],
            "wa": u["wa"],
            "bayar": n == 3,
            "siapaSaja": u["siapa_saja"],
            "siapaSajaKet": u["siapa_saja_ket"],
            "grup": [{"nama": g, "item": [{"nama": a, "harga": b, "menit": c, "ket": d} for a, b, c, d in it]} for g, it in u["grup"]],
            "stylist": [{"nama": a, "keahlian": b, "rinci": c, "bisa": d} for a, b, c, d in u["stylist"]],
            "jam": {str(h): u["jam"][h] for h in range(7)},
        }
        scripts += "<script>\n" + BOOKING_JS.replace("__DATA__", json.dumps(D, ensure_ascii=False)) + BAR_JS + "</script>\n"
    return head(judul, desc, css) + "".join(body) + scripts + "</body>\n</html>\n"


PAKET = [
    ("1", "Halaman informasi", "Harga layanan, jam buka, alamat, dan tombol WhatsApp. Yang paling cepat jadi dan paling murah.",
     "Kalau yang dibutuhkan hanya supaya orang menemukan salon dan bisa bertanya.",
     ["Daftar harga layanan", "Jam buka dan hari tutup", "Alamat lengkap dengan tombol peta", "Tombol WhatsApp di setiap layar", "Status buka dihitung dari jam sebenarnya"]),
    ("2", "Tambah sistem booking", "Pengunjung memilih layanan, stylist, tanggal, dan jam sendiri. Tidak perlu bolak-balik WhatsApp.",
     "Kalau jadwal sudah ramai dan pesanan sering bertabrakan.",
     ["Semua isi paket 1", "Pilih layanan dan stylist", "Pilih tanggal dan jam yang tersedia", "Jam yang sudah penuh tertutup sendiri", "Ringkasan sebelum dikonfirmasi"]),
    ("3", "Tambah pembayaran", "Pengunjung membayar muka saat memesan, supaya yang memesan tidak hilang begitu saja.",
     "Kalau sering ada yang memesan lalu tidak datang.",
     ["Semua isi paket 2", "Bayar muka saat memesan", "Pilihan QRIS, transfer, atau bayar di tempat", "Nota pemesanan otomatis"]),
]

INDEX_JS = r"""
(function(){
  var NAMA={salon:"Salon Melati",barbershop:"Barbershop Cukur Rapi"};
  var tombol=[].slice.call(document.querySelectorAll("#pilih-usaha button"));
  var tautan=[].slice.call(document.querySelectorAll("[data-buka]"));
  var nama=document.getElementById("nama-demo");
  function gambar(usaha){
    tombol.forEach(function(b){b.setAttribute("aria-pressed",b.dataset.usaha===usaha?"true":"false")});
    tautan.forEach(function(a){a.href="/"+usaha+"/paket-"+a.dataset.buka+"/"});
    nama.textContent=NAMA[usaha];
  }
  tombol.forEach(function(b){b.addEventListener("click",function(){gambar(b.dataset.usaha)})});
  gambar("salon");
})();
"""


def halaman_index():
    css = FONT + "\n:root{" + INDEX_TOKENS + "}\n" + BASE + INDEX
    cards = []
    for no, nama, rinci, cocok, isi in PAKET:
        li = "".join("<li>%s<span>%s</span></li>" % (I_CENTANG, e(x)) for x in isi)
        cards.append(
            '<li class="paket"><article><div><span class="no">Paket %s</span><h3>%s</h3></div><p class="ket">%s</p>'
            '<p class="cocok"><b>Cocok</b> %s</p><ul class="isi" aria-label="Isi paket %s">%s</ul>'
            '<div class="bawah"><a class="tombol" href="/salon/paket-%s/" data-buka="%s">Buka demo Paket %s</a>'
            '<p class="harga-tag">Harga belum diisi &middot; sekali bayar</p></div></article></li>' % (no, e(nama), e(rinci), e(cocok), no, li, no, no, no)
        )
    body = (
        "<body>\n"
        '<header class="atas atas-hijau"><div class="wadah wadah-lebar"><a class="merek" href="/">Demo website salon dan barbershop</a></div></header>\n'
        "<main>\n"
        '<section class="hero"><div class="wadah wadah-lebar">\n<p class="eyebrow">Situs demo &middot; jasa pembuatan website</p>\n'
        "<h1>Demo website untuk salon dan barbershop</h1>\n"
        '<p class="lead">Ini situs uji coba, bukan usaha sungguhan. Di sini Anda bisa melihat dan mencoba sendiri tampilan dan fitur website yang Anda dapatkan kalau memakai jasa pembuatan website dari Rio Ekaputra Siswa, developer aplikasi web di Bandung.</p>\n'
        '<ul class="fitur"><li>%s Harga dan jam buka</li><li>%s Tombol WhatsApp</li><li>%s Sistem booking</li><li>%s Bayar muka</li></ul>\n'
        '<div class="aksi"><a class="tombol" href="#paket">Coba demonya</a></div>\n</div></section>\n'
        '<section class="bagian" id="paket"><div class="wadah wadah-lebar">\n<h2>Tiga paket yang bisa dipilih</h2>\n'
        '<p class="bagian-lead">Pilih jenis usaha, lalu buka demo tiap paket dan coba langsung di HP. Semua nama usaha, harga, alamat, dan nomor di dalam demo hanya contoh.</p>\n'
        '<div class="pilih-usaha" id="pilih-usaha" role="group" aria-label="Jenis usaha demo">'
        '<button type="button" aria-pressed="true" data-usaha="salon">Untuk salon</button>'
        '<button type="button" aria-pressed="false" data-usaha="barbershop">Untuk barbershop</button></div>\n'
        '<p class="nama-demo" aria-live="polite">Contoh usaha di demo ini: <b id="nama-demo">Salon Melati</b>.</p>\n'
        '<ul class="paket-daftar paket">%s</ul>\n'
        "</div></section>\n</main>\n"
        '<footer class="kaki"><div class="wadah wadah-lebar"><p>Dibuat oleh Rio Ekaputra Siswa, developer aplikasi web di Bandung. <a href="https://rioeka.com">rioeka.com</a></p>'
        "<p>Harga ketiga paket belum diisi karena pemilik usaha belum memutuskan. Angka tidak dikarang.</p></div></footer>\n"
        "<script>\n%s</script>\n</body>\n</html>\n"
    ) % (I_CENTANG, I_WA, I_KALENDER, I_CENTANG, "".join(cards), INDEX_JS)
    return head("Demo website untuk salon dan barbershop, Bandung", "Situs uji coba: lihat dan coba tampilan serta fitur website untuk salon dan barbershop yang bisa Anda dapatkan lewat jasa pembuatan website Rio Ekaputra Siswa, developer aplikasi web di Bandung.", css, robots=False) + body

GALAT_JS = r"""
(function(){
  var k=document.getElementById("kembali"), b=document.getElementById("beranda"), t=document.getElementById("kembali-teks");
  var dari=false;
  try{dari=!!document.referrer&&new URL(document.referrer).origin===location.origin}catch(x){}
  if(dari&&history.length>1){
    k.addEventListener("click",function(ev){ev.preventDefault();history.back()});
  }else{
    t.textContent="Ke beranda";b.hidden=true;
  }
})();
"""

GALAT = [
    ("404.html", "404", "Halaman tidak ditemukan",
     "Alamat yang Anda buka tidak ada. Bisa jadi salah ketik atau halamannya sudah dipindahkan.", True),
    ("50x.html", "Galat", "Server sedang bermasalah",
     "Halaman ini belum bisa dimuat. Ini bukan salah Anda. Tunggu sebentar, lalu muat ulang.", False),
]


def halaman_galat(kode, judul, teks, bisa_kembali):
    css = FONT + "\n:root{" + INDEX_TOKENS + "}\n" + BASE + INDEX + ERR
    if bisa_kembali:
        aksi = (
            '<a class="tombol" id="kembali" href="/">%s<span id="kembali-teks">Kembali</span></a>'
            '<a class="tombol garis" id="beranda" href="/">Ke beranda</a>' % I_KIRI
        )
        alt = (
            '<nav class="alternatif" aria-labelledby="alt-judul"><h2 id="alt-judul">Atau langsung buka</h2><ul>'
            '<li><a href="/salon/paket-1/"><span>Demo salon</span>%s</a></li>'
            '<li><a href="/barbershop/paket-1/"><span>Demo barbershop</span>%s</a></li>'
            '<li><a href="/#paket"><span>Daftar paket</span>%s</a></li></ul></nav>' % (I_KANAN, I_KANAN, I_KANAN)
        )
        js = "<script>\n" + GALAT_JS + "</script>\n"
    else:
        aksi = '<a class="tombol" href="">Muat ulang</a><a class="tombol garis" href="/">Ke beranda</a>'
        alt = ""
        js = ""
    body = (
        "<body>\n"
        '<header class="atas atas-hijau"><div class="wadah wadah-lebar"><a class="merek" href="/">Demo website salon dan barbershop</a></div></header>\n'
        '<main><section class="galat"><div class="wadah">\n'
        '<span class="kode-galat" aria-hidden="true">%s</span>\n'
        "<h1>%s</h1>\n"
        '<p class="lead">%s</p>\n'
        '<div class="aksi">%s</div>\n%s'
        "</div></section></main>\n"
        '<footer class="kaki"><div class="wadah"><p>Dibuat oleh Rio Ekaputra Siswa, developer aplikasi web di Bandung. <a href="https://rioeka.com">rioeka.com</a></p></div></footer>\n'
        "%s</body>\n</html>\n"
    ) % (e(kode), e(judul), e(teks), aksi, alt, js)
    return head(judul + " | Demo website salon dan barbershop", teks, css, warna="#16221E") + body


def tulis(rel, isi):
    path = os.path.join(ROOT, rel.replace("/", os.sep))
    with open(path, "w", encoding="utf-8", newline="\r\n") as f:
        f.write(isi)
    print("tulis", rel, len(isi))


if __name__ == "__main__":
    tulis("index.html", halaman_index())
    for berkas, kode, judul, teks, kembali in GALAT:
        tulis(berkas, halaman_galat(kode, judul, teks, kembali))
    for u in (SALON, BARBER):
        for n in (1, 2, 3):
            tulis("%s/paket-%d/index.html" % (u["slug"], n), halaman_demo(u, n))
