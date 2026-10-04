import json, os, sys
from html import escape as e
from urllib.parse import quote
sys.path.insert(0, os.path.dirname(__file__))
from css import FONT, FONT_SERIF, BASE, BOOKING, GAYA, GAYA_UMUM, GAYA_SALON, GAYA_SALON_WIZARD, GAYA_SPA, GAYA_SPA_WIZARD, TEMA, WARNA_TEMA, WARNA_INDEX, AKSEN_JENIS, INDEX_TOKENS, INDEX, ERR
from data import USAHA, URUT_HARI
from js import STATUS_JS, BAR_JS, BOOKING_JS, WIZARD_JS

GAYA_HALAMAN = {"butik": (GAYA_SALON, GAYA_SALON_WIZARD), "tenang": (GAYA_SPA, GAYA_SPA_WIZARD)}

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NH = {0: "Minggu", 1: "Senin", 2: "Selasa", 3: "Rabu", 4: "Kamis", 5: "Jumat", 6: "Sabtu"}
DOMAIN = "devario.rioeka.com"
MERK = "Devario"


def ikon(path, extra=""):
    return '<svg class="ikon" viewBox="0 0 24 24" aria-hidden="true"%s>%s</svg>' % (extra, path)


I_KANAN = ikon('<path d="m9 18 6-6-6-6"/>')
I_KIRI = ikon('<path d="m15 18-6-6 6-6"/>')
I_BAWAH = ikon('<path d="m6 9 6 6 6-6"/>')
I_CENTANG = ikon('<path d="M20 6 9 17l-5-5"/>')
I_WA = ikon('<path d="M21 11.5a8.4 8.4 0 0 1-12.4 7.4L3 20.5l1.6-5.4A8.4 8.4 0 1 1 21 11.5Z"/>')
I_PETA = ikon('<path d="M20 10c0 6-8 12-8 12S4 16 4 10a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/>')
I_KALENDER = ikon('<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/>')
I_GUNTING = ikon('<circle cx="6" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><path d="M20 4 8.12 15.88M14.47 14.48 20 20M8.12 8.12 12 12"/>')
I_STAF = ikon('<rect x="9" y="2" width="6" height="20" rx="3"/><path d="M9 7 15 4.4M9 11.6 15 9M9 16.2 15 13.6"/>')
I_DAUN = ikon('<path d="M12 3c2.5 3 6 5 6 9a6 6 0 0 1-12 0c0-4 3.5-6 6-9z"/><path d="M12 12v9"/>')
I_RANJANG = ikon('<path d="M3 18V8a2 2 0 0 1 2-2h11a3 3 0 0 1 3 3v9"/><path d="M3 14h18"/><path d="M3 18v2M21 18v2"/><path d="M7 10h3v4H7z"/>')
I_MANGKUK = ikon('<path d="M4 11a8 8 0 0 1 16 0z"/><path d="M3 15h18"/><path d="M6 19h12"/>')
I_RUMAH = ikon('<path d="m3 11 9-8 9 8"/><path d="M5 10v10h14V10"/>')
IKON = {"salon": I_GUNTING, "barbershop": I_STAF, "spa": I_DAUN, "penginapan": I_RANJANG, "katering": I_MANGKUK}


def rp(n):
    return "Rp " + f"{n:,}".replace(",", ".")


def jam_teks(blok):
    return "tutup" if not blok else "%s sampai %s" % (blok[0], blok[1])


def wa_link(u):
    return "https://wa.me/%s?text=%s" % (u["wa"], quote(u["wa_pesan"], safe=""))


def head(title, desc, css, robots=True, warna=None, extra=""):
    return (
        '<!DOCTYPE html>\n<html lang="id">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        + ('<meta name="robots" content="noindex, nofollow">\n' if robots else "")
        + '<meta name="theme-color" content="%s">\n' % (warna or "#FBF6F2")
        + "<title>%s</title>\n" % e(title)
        + '<meta name="description" content="%s">\n' % e(desc)
        + extra
        + "<style>\n" + css + "\n</style>\n</head>\n"
    )


def opsi_radio(name, value, nama, harga, ket):
    return (
        '<label class="opsi"><input type="radio" name="%s" value="%s"><span class="opsi-kotak">'
        '<span class="opsi-tanda"></span><span class="opsi-nama">%s</span><span class="opsi-harga">%s</span>'
        '<span class="opsi-ket">%s</span></span></label>' % (name, value, nama, harga, ket)
    )


def tag(teks):
    return '<p class="tag-baris"><span class="tag-anda">%s</span></p>\n' % e(teks)


def kartu_demo(u, n):
    j = u["jenis"].lower()
    item = u["grup"][0][1][0]
    baris = [(u["nama"], "Nama %s Anda" % j), (u["alamat"][0], "Alamat %s Anda" % j)]
    if u.get("mode", "jadwal") == "jadwal" and n >= 2:
        baris.append(("%s: %s" % (u["noun"], ", ".join(s[0] for s in u["stylist"])), "Nama %s di tempat Anda" % u["noun"].lower()))
    baris.append(("%s, %s" % (item[0], rp(item[1])), u["label_item"]))
    baris.append((u["wa_tampil"], "Nomor WhatsApp Anda"))
    baris.append((DOMAIN, u["contoh_domain"]))
    if n == 1:
        baris.append(("Foto contoh", "Foto asli %s Anda" % j))
    li = "".join(
        '<li><span class="kini">%s</span>%s<span class="nanti"><span class="sr">jadi </span>%s</span></li>' % (e(a), I_KANAN, e(c))
        for a, c in baris
    )
    if n == 1:
        paket = "Paket 1: halaman informasi, tanpa booking. Untuk melihat versi yang bisa menerima pesanan, buka demo Paket 2."
    elif n == 2:
        paket = "Paket 2: pesanan di halaman ini tidak tersimpan, hanya memperlihatkan alurnya. Di website Anda, pesanan masuk ke WhatsApp atau ke catatan %s." % j
    else:
        paket = "Paket 3: pembayaran di halaman ini simulasi. Tidak ada uang yang berpindah, dan tidak ada data kartu yang diminta."
    return (
        '<section class="demo-kartu" aria-label="Penjelasan halaman demo">'
        '<span class="tanda-contoh">Demo Paket %d</span>'
        '<p class="demo-judul">Ini halaman demo, bukan %s sungguhan</p>'
        '<p class="demo-teks">Beginilah tampilan website Anda nanti kalau memakai jasa Rio Ekaputra Siswa. Bayangkan isinya jadi milik %s Anda.</p>'
        '<div class="ganti-kepala" aria-hidden="true"><span>Di demo ini</span><span></span><span>Di website Anda</span></div>'
        '<ul class="ganti-daftar">%s</ul>'
        '<p class="demo-paket">%s</p></section>\n' % (n, j, j, li, e(paket))
    )


def penutup_demo(u):
    j = u["jenis"].lower()
    return (
        '<section class="bagian penutup" aria-label="Penutup">\n<div class="kartu"><h2>Bayangkan ini website %s Anda</h2>\n'
        '<p class="bagian-lead">Nama, alamat, daftar harga, jam buka, dan foto di halaman ini nanti diganti dengan milik %s Anda. %s hanya nama contoh. Alamat websitenya didaftarkan atas nama usaha Anda sendiri, misalnya %s.</p>\n'
        '<div class="aksi"><a class="tombol" href="/%s/#paket">Lihat paket dan harga</a>'
        '<a class="tombol garis" href="https://rioeka.com">Kunjungi rioeka.com</a></div></div>\n</section>\n' % (j, j, e(u["nama"]), e(u["contoh_domain"]), u["slug"])
    )


def seksi_pesan(u, n):
    mode = u.get("mode", "jadwal")
    if mode == "inap":
        return seksi_pesan_inap(u, n)
    if mode == "pesan":
        return seksi_pesan_menu(u, n)
    return seksi_pesan_jadwal(u, n)


def seksi_pesan_jadwal(u, n):
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
    buka = (
        '<div class="kartu pesan-buka" id="pesan-buka"><h3>Coba alurnya sendiri</h3>'
        '<p>Pilih layanan, %s, tanggal, dan jam dalam %d langkah singkat. Pesanan di halaman contoh ini tidak tersimpan.</p>'
        '<button class="tombol" id="buka-pesan" type="button" aria-controls="pesan" aria-expanded="false">%s Mulai coba pesan</button></div>'
    ) % (e(nom.lower()), total, I_KALENDER)
    return (
        '<section class="bagian" id="bagian-pesan" aria-labelledby="j-pesan">\n'
        '<p class="tag-baris"><span class="tag-anda">Layanan dan jam sesuai usaha Anda</span></p>\n<h2 id="j-pesan">Coba pesan sendiri</h2>\n<p class="bagian-lead">%s</p>\n'
        '%s\n'
        '<div class="kartu pesan" id="pesan" hidden>\n'
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
        '%s\n'
        '%s\n'
        '%s\n'
        '%s\n'
        '%s\n'
        '</div>\n'
        '</section>\n'
    ) % (e(lead), buka, total, total, e(u["tip_layanan"]), e(nom.lower()), e(u["siapa_saja"]),
         panel_data_html(), panel_tinjau_html(), panel_bayar, aksi_langkah_html(), selesai_html())


def panel_data_html():
    return (
        '<div class="panel" data-langkah="data" hidden><h3 tabindex="-1">Nama dan nomor</h3>'
        '<p class="tip">Kami memakai nomor ini hanya untuk mengabari pesanan yang dikonfirmasi.</p>'
        '<div class="kolom"><label for="nama">Nama</label><input id="nama" name="nama" type="text" autocomplete="name" placeholder="Nama Anda"></div>'
        '<div class="kolom"><label for="wa">Nomor WhatsApp</label><input id="wa" name="wa" type="tel" inputmode="tel" autocomplete="tel" placeholder="0812 3456 7890"></div></div>'
    )


def panel_tinjau_html():
    return (
        '<div class="panel" data-langkah="tinjau" hidden><h3 tabindex="-1">Periksa pesanan</h3>'
        '<p class="tip">Ketuk "Ubah" untuk memperbaiki. Pesanan di halaman contoh ini tidak tersimpan.</p>'
        '<dl class="tinjau" id="tinjau"></dl></div>'
    )


def panel_bayar_html(sisa, tempat_ket):
    return (
        '<div class="panel" data-langkah="bayar" hidden><h3 tabindex="-1">Cara bayar</h3>'
        '<p class="tip">Total <b id="b-total"></b>. Bayar muka <b id="b-muka"></b>, %s.</p>'
        '<div class="opsi-daftar">'
        + opsi_radio("cara", "qris", "QRIS", "semua bank", "Pindai kode dari bank atau e-wallet apa pun.")
        + opsi_radio("cara", "transfer", "Transfer bank", "BCA, Mandiri", "Kode bayar diberikan setelah memilih.")
        + opsi_radio("cara", "tempat", "Bayar di tempat", "saat tiba", tempat_ket)
        + '</div>'
        '<div id="panel-qris" class="panel-bayar" hidden><div class="qris" aria-hidden="true"></div>'
        '<p>Kode di atas hanya gambar, bukan kode bayar sungguhan.</p></div>'
        '<div id="panel-transfer" class="panel-bayar" hidden><p>Di halaman sungguhan, di sini muncul nomor rekening dan kode bayar khusus pesanan ini.</p></div></div>'
    ) % (e(sisa))


def aksi_langkah_html():
    return (
        '<div class="aksi-langkah">'
        '<p class="ringkas-mini" id="mini" hidden></p>'
        '<p class="pesan-sistem" id="pesan-sistem" role="status" aria-live="polite"></p>'
        '<div class="baris-aksi tanpa-kembali" id="baris-aksi">'
        '<button class="tombol garis" id="kembali" type="button" hidden>Kembali</button>'
        '<button class="tombol" id="lanjut" type="button" aria-disabled="true">Lanjut</button></div></div>'
        '</div>'
    )


def selesai_html():
    return (
        '<div id="selesai" class="selesai" hidden>'
        '<div id="k-centang" class="centang" aria-hidden="true"></div>'
        '<h3 tabindex="-1">Pesanan dicatat</h3><p class="langkah-nama">Kode pesanan</p><p class="kode" id="k-kode"></p>'
        '<dl class="tinjau" id="k-ringkas"></dl>'
        '<p class="catatan">Halaman contoh. Pesanan ini tidak tersimpan di mana pun.</p>'
        '<div class="aksi"><a class="tombol" id="k-wa" href="#">Kirim ke WhatsApp</a><button class="tombol garis" id="ulang" type="button">Pesan lagi</button></div>'
        '</div>'
    )


def bagian_pesan(tag_anda, judul, lead, isi):
    return (
        '<section class="bagian" id="bagian-pesan" aria-labelledby="j-pesan">\n'
        '<p class="tag-baris"><span class="tag-anda">%s</span></p>\n<h2 id="j-pesan">%s</h2>\n<p class="bagian-lead">%s</p>\n'
        "%s</section>\n" % (e(tag_anda), e(judul), e(lead), isi)
    )


def kartu_pesan_buka(total, kalimat):
    return (
        '<div class="kartu pesan-buka" id="pesan-buka"><h3>Coba alurnya sendiri</h3>'
        '<p>%s Pesanan di halaman contoh ini tidak tersimpan.</p>'
        '<button class="tombol" id="buka-pesan" type="button" aria-controls="pesan" aria-expanded="false">%s Mulai coba pesan</button></div>'
    ) % (e(kalimat), I_KALENDER)


def seksi_pesan_inap(u, n):
    bayar = n == 3
    total = 6 if bayar else 5
    isi = (
        kartu_pesan_buka(total, "Pilih kamar, tanggal, jumlah malam, dan tamu dalam %d langkah singkat." % total)
        + "\n"
        + '<div class="kartu pesan" id="pesan" hidden>\n<div id="alur">\n'
        '<div class="langkah-kepala"><span class="langkah-no" id="l-no">Langkah 1 dari %d</span><span class="langkah-nama" id="l-nama">Kamar</span></div>\n' % total
        + '<div class="progres" id="progres" role="progressbar" aria-label="Kemajuan pesanan" aria-valuemin="1" aria-valuemax="%d" aria-valuenow="1"><i id="progres-isi"></i></div>\n' % total
        + '<div class="panel" data-langkah="kamar"><h3 tabindex="-1">Pilih kamar</h3><p class="tip">Harga tertera per malam. Kapasitas tamu ada di tiap kamar.</p><div id="pilih-kamar"></div></div>\n'
        + '<div class="panel" data-langkah="tanggal" hidden><h3 tabindex="-1">Tanggal menginap</h3>'
        + '<p class="tip">Dua minggu ke depan. Tanggal bergaris putus-putus berarti kamar sudah penuh. Check-in pukul %s, check-out pukul %s.</p>' % (e(u["checkin"]), e(u["checkout"]))
        + '<div class="hari-strip" id="pilih-hari" role="group" aria-label="Tanggal check-in"></div>'
        + '<div id="st-malam"></div><p class="petunjuk" id="info-tgl" style="margin-top:12px"></p></div>\n'
        + '<div class="panel" data-langkah="tamu" hidden><h3 tabindex="-1">Jumlah tamu</h3>'
        + '<p class="tip">Jumlah tamu mengikuti kapasitas kamar yang dipilih.</p>'
        + '<div id="st-tamu"></div><p class="petunjuk" id="info-tamu" style="margin-top:12px"></p></div>\n'
        + panel_data_html() + "\n" + panel_tinjau_html() + "\n"
        + ((panel_bayar_html("sisanya dibayar saat tiba", "Pesanan dicatat, dibayar saat tiba.") + "\n") if bayar else "")
        + aksi_langkah_html() + "\n"
        + selesai_html() + "\n</div>\n"
    )
    return bagian_pesan("Kamar dan tanggal sesuai usaha Anda", "Pesan kamar sendiri",
                        "Tanpa aplikasi dan tanpa formulir panjang. Selesai di halaman ini juga.", isi)


def seksi_pesan_menu(u, n):
    bayar = n == 3
    total = 6 if bayar else 5
    isi = (
        kartu_pesan_buka(total, "Pilih menu dan jumlah, tanggal, dan cara terima dalam %d langkah singkat." % total)
        + "\n"
        + '<div class="kartu pesan" id="pesan" hidden>\n<div id="alur">\n'
        '<div class="langkah-kepala"><span class="langkah-no" id="l-no">Langkah 1 dari %d</span><span class="langkah-nama" id="l-nama">Menu</span></div>\n' % total
        + '<div class="progres" id="progres" role="progressbar" aria-label="Kemajuan pesanan" aria-valuemin="1" aria-valuemax="%d" aria-valuenow="1"><i id="progres-isi"></i></div>\n' % total
        + '<div class="panel" data-langkah="menu"><h3 tabindex="-1">Pilih menu</h3>'
        + '<p class="tip">Atur jumlah tiap menu. Angka minimal dan maksimal mengikuti ketentuan tiap menu.</p><div id="pilih-menu"></div></div>\n'
        + '<div class="panel" data-langkah="terima" hidden><h3 tabindex="-1">Tanggal dan cara terima</h3>'
        + '<p class="tip" id="tip-lead">Dua minggu ke depan. Tanggal bergaris putus-putus berarti toko tutup.</p>'
        + '<div class="hari-strip" id="pilih-hari" role="group" aria-label="Tanggal"></div>'
        + '<h4 class="sub">Cara terima</h4><div id="pilih-cara"></div>'
        + '<div class="kolom" id="kolom-alamat" hidden><label for="alamat">Alamat antar</label><input id="alamat" name="alamat" type="text" autocomplete="street-address" placeholder="Alamat lengkap untuk diantar"></div>'
        + '<p class="jam-label" id="jam-judul">Pilih tanggal dulu</p>'
        + '<div class="jam-grid" id="pilih-jam" role="group" aria-labelledby="jam-judul"></div>'
        + '<p class="petunjuk" style="margin-top:12px">Jam bergaris coret sudah terisi.</p></div>\n'
        + '<div class="panel" data-langkah="catatan" hidden><h3 tabindex="-1">Catatan</h3>'
        + '<p class="tip">Tulis permintaan khusus, misalnya tanpa kacang, tanpa pedas, atau tulisan di kue.</p>'
        + '<div class="kolom"><label for="catatan">Catatan (opsional)</label><textarea id="catatan" rows="3"></textarea></div></div>\n'
        + panel_data_html() + "\n" + panel_tinjau_html() + "\n"
        + ((panel_bayar_html("sisanya dibayar saat serah terima", "Pesanan dicatat, dibayar saat serah terima.") + "\n") if bayar else "")
        + aksi_langkah_html() + "\n"
        + "</div>\n" + selesai_html() + "</div>\n"
    )
    return bagian_pesan("Menu dan tanggal sesuai usaha Anda", "Pesan sendiri",
                        "Tanpa aplikasi dan tanpa formulir panjang. Selesai di halaman ini juga.", isi)


def durasi(m):
    if m < 60:
        return "%d menit" % m
    if m % 60 == 0:
        return "%d jam" % (m // 60)
    return "%d jam %d menit" % (m // 60, m % 60)


def fakta(u):
    mode = u.get("mode", "jadwal")
    semua = [x for _, it in u["grup"] for x in it]
    termurah = rp(min(x[1] for x in semua))
    if mode == "jadwal":
        m = [x[2] for x in semua]
        rentang = "%d menit" % min(m) if min(m) == max(m) else "%d-%d menit" % (min(m), max(m))
        return [("Mulai dari", termurah), (u["noun"], "%d orang" % len(u["stylist"])), ("Lama layanan", rentang)]
    if mode == "inap":
        return [("Mulai dari", termurah + " / malam"), ("Check-in", "Pukul " + u["checkin"]), ("Check-out", "Pukul " + u["checkout"])]
    ld = [it["lead"] for _, items in u["menu"] for it in items]
    return [("Mulai dari", termurah), ("Ongkos antar", rp(u["ongkir"])), ("Pesan sebelum", "H-%d sampai H-%d" % (min(ld), max(ld)))]


def html_fakta(u):
    li = "".join('<li><span class="f-label">%s</span><span class="f-nilai">%s</span></li>' % (e(a), e(c)) for a, c in fakta(u))
    return '<ul class="fakta">%s</ul>\n' % li


def seksi_harga(u):
    mode = u.get("mode", "jadwal")
    butik = u.get("gaya") in GAYA_HALAMAN
    if u.get("mode") == "inap":
        judul, lead = "Daftar kamar dan harga", u["harga_lead"]
    elif u.get("mode") == "pesan":
        judul, lead = "Daftar menu dan harga", u["harga_lead"]
    else:
        judul, lead = "Daftar harga", u["harga_lead"]
    out = ['<section class="bagian" id="harga">\n' + tag("Harga %s Anda" % u["jenis"].lower()) + '<h2>%s</h2>\n<p class="bagian-lead">%s</p>\n' % (e(judul), e(lead))]
    for nama, item in u["grup"]:
        out.append('<div class="kartu"><h3>%s</h3><ul class="harga">' % e(nama))
        for baris in item:
            nm, hr = baris[0], baris[1]
            ket = baris[3] if len(baris) > 3 else (baris[2] if len(baris) > 2 else "")
            dur = ""
            if mode == "jadwal":
                dur = '<span class="dur">%s</span>' % durasi(baris[2])
            elif mode == "inap":
                fas = [k[3] for k in u["kamar"] if k[0] == nm]
                ket = ("%s. %s" % (fas[0].capitalize(), ket)) if fas else ket
            else:
                it = [x for _, items in u["menu"] for x in items if x["nama"] == nm]
                if it:
                    ket = "%s. Minimal %d %s, pesan H-%d." % (it[0]["ket"], it[0]["min"], it[0]["satuan"], it[0]["lead"])
            isi_ket = dur + (('<span class="ket-teks">%s</span>' % e(ket)) if butik and ket else e(ket))
            out.append('<li><span class="nm">%s</span><span class="hr">%s</span>%s</li>' % (e(nm), rp(hr), '<span class="ket">%s</span>' % isi_ket if isi_ket else ""))
        out.append("</ul></div>")
    out.append('<p class="catatan">%s</p>\n</section>\n' % e(u["harga_catatan"]))
    return "".join(out)


def seksi_lokasi(u):
    inap = u.get("mode") == "inap"
    judul = "Lokasi dan jam resepsionis" if inap else "Lokasi dan jam buka"
    label = "Alamat dan jam resepsionis %s Anda" if inap else "Alamat dan jam buka %s Anda"
    li = "".join(
        '<li data-hari="%d"><span>%s</span><span>%s</span></li>' % (h, NH[h], jam_teks(u["jam"][h])) for h in URUT_HARI
    )
    peta = "https://www.google.com/maps/search/?api=1&amp;query=" + quote(u["peta"])
    return (
        '<section class="bagian" id="lokasi">\n' + tag(label % u["jenis"].lower()) + '<h2>%s</h2>\n<p class="bagian-lead">%s</p>\n'
        '<div class="kartu"><h3>%s</h3><ul class="jam" id="kartu-jam">%s</ul></div>\n'
        '<div class="kartu"><h3>Alamat</h3><address class="alamat">%s</address>'
        '<div class="aksi-lokasi"><a class="tombol garis" href="%s">%s Buka di Google Maps</a></div></div>\n</section>\n'
    ) % (e(judul), e(u["jam_lead"]), "Jam resepsionis" if inap else "Jam buka", li, "<br>".join(e(x) for x in u["alamat"]), peta, I_PETA)


def seksi_galeri(u):
    if u.get("gaya") in GAYA_HALAMAN:
        p = "".join(
            '<figure class="petak"><img src="/%s/img/%s.jpg" alt="" width="720" height="540" loading="lazy" decoding="async"><figcaption>%s</figcaption></figure>' % (u["slug"], f, e(a))
            for f, a in u["galeri"]
        )
    else:
        p = "".join(
            '<figure class="petak"><img src="/%s/img/%s.jpg" alt="%s" width="720" height="540" loading="lazy" decoding="async"></figure>' % (u["slug"], f, e(a))
            for f, a in u["galeri"]
        )
    return (
        '<section class="bagian" id="galeri">\n' + tag("Foto asli %s Anda" % u["jenis"].lower()) + '<h2>Galeri</h2>\n<p class="bagian-lead">%s</p>\n<div class="galeri">%s</div>\n'
        '<p class="kredit">Foto contoh dari <a href="https://unsplash.com/license" rel="noopener">Unsplash</a>, bebas dipakai.</p>\n</section>\n'
    ) % (e(u["galeri_lead"]), p)


def seksi_tanya(u):
    d = "".join('<details><summary>%s%s</summary><p>%s</p></details>' % (e(q), I_BAWAH, e(a)) for q, a in u["faq"])
    return '<section class="bagian" id="tanya">\n<h2>Pertanyaan yang sering masuk</h2>\n<div class="tanya">%s</div>\n</section>\n' % d


def halaman_demo(u, n):
    mode = u.get("mode", "jadwal")
    butik = u.get("gaya") in GAYA_HALAMAN
    if butik:
        g_utama, g_wizard = GAYA_HALAMAN[u["gaya"]]
        css = FONT + "\n" + FONT_SERIF + "\n:root{" + TEMA[u["tema"]] + "}\n" + BASE + (BOOKING if n >= 2 else "") + GAYA_UMUM + g_utama + (g_wizard if n >= 2 else "")
        preload = '<link rel="preload" href="/font/cormorant-garamond-latin.woff2" as="font" type="font/woff2" crossorigin>\n'
    else:
        css = FONT + "\n:root{" + TEMA[u["tema"]] + "}\n" + BASE + (BOOKING if n >= 2 else "") + GAYA
        preload = ""
    judul = {1: u["title_p1"], 2: u["nama"] + ", booking", 3: u["nama"] + ", booking dan pembayaran"}[n]
    desc = u["desc_p1"] if n == 1 else (u["desc_book"] if n == 2 else u["desc_book"].rstrip(".") + ", lalu bayar muka.")
    wa = wa_link(u)
    jam_json = json.dumps({str(h): u["jam"][h] for h in range(7)})

    dulu = n == 1 and u.get("galeri_dulu")
    l_harga, l_lokasi, l_galeri = '<a href="#harga">Harga</a>', '<a href="#lokasi">Lokasi</a>', '<a href="#galeri">Galeri</a>'
    if dulu:
        loncat = [l_galeri, l_harga, l_lokasi]
    elif n == 1:
        loncat = [l_harga, l_lokasi, l_galeri]
    else:
        loncat = [l_harga, l_lokasi]
    loncat.append('<a href="#tanya">Tanya jawab</a>')
    if n >= 2:
        loncat.insert(0, '<a href="#pesan">Pesan</a>')

    if mode == "jadwal":
        kata2 = "booking"
    elif mode == "inap":
        kata2 = "reservasi kamar"
    else:
        kata2 = "pemesanan"
    if n == 1:
        aksi = '<a class="tombol" href="%s">%s Tanya lewat WhatsApp</a><a class="tombol garis" href="/%s/paket-2/">Buka demo Paket 2, dengan %s %s</a>' % (wa, I_WA, u["slug"], kata2, I_KANAN)
    else:
        aksi = '<a class="tombol" href="#pesan">%s Pesan sekarang</a><a class="tombol garis" href="%s">%s Tanya lewat WhatsApp</a>' % (I_KALENDER, wa, I_WA)

    if n == 1:
        demo = '<p class="catatan-demo"><span class="tanda-contoh">Demo Paket 1</span><span>Anda sedang membuka demo halaman informasi, tanpa booking. Untuk melihat versi yang bisa menerima pesanan, buka demo Paket 2.</span></p>'
    elif n == 2:
        demo = '<p class="catatan-demo"><span class="tanda-contoh">Demo Paket 2</span><span>Pesanan di halaman ini tidak tersimpan. Halaman contoh ini hanya memperlihatkan alurnya. Setelah halaman ini terpasang di tempat Anda, pesanan masuk ke WhatsApp atau ke catatan %s.</span></p>' % e(u["jenis"].lower())
    else:
        demo = '<p class="catatan-demo"><span class="tanda-contoh">Demo Paket 3</span><span>Pembayaran di halaman ini simulasi. Tidak ada uang yang berpindah, dan tidak ada data kartu yang diminta.</span></p>'

    if mode == "inap":
        status = '<p class="status"><span class="titik"></span><span id="status-teks">Resepsionis buka %s sampai %s</span></p>\n' % (u["jam"][1][0], u["jam"][1][1])
    else:
        status = '<p class="status" id="status"><span class="titik" id="titik"></span><span id="status-teks">Memuat jam buka</span></p>\n'

    body = [
        '<body data-j="%s">\n' % u["slug"],
        '<header class="atas"><div class="demo-strip" role="note"><span class="tanda-contoh">Demo</span><span>Contoh website untuk %s Anda</span></div><div class="wadah"><a class="balik" href="/%s/#paket">%s Semua paket %s</a><span class="nama-atas">%s</span></div></header>\n' % (u["jenis"].lower(), u["slug"], I_KIRI, u["jenis"].lower(), e(u["nama"])),
        '<div class="pole" aria-hidden="true"></div>\n',
        "<main>\n",
        '<div class="wadah">\n',
    ]
    nav = '<nav class="loncat" aria-label="Loncat ke bagian">%s</nav>\n' % "".join(loncat)
    if butik:
        kata = u["nama"].rsplit(" ", 1)
        h1 = "%s <em>%s</em>" % (e(kata[0]), e(kata[1])) if len(kata) == 2 else e(u["nama"])
        foto, alt_foto = u["hero_foto"]
        body += [
            '<section class="hero">\n<div class="hero-isi">\n<p class="eyebrow">%s &middot; %s</p>\n<h1>%s</h1>\n' % (e(u["jenis"]), e(u["area"]), h1),
            tag("Nama %s Anda tampil di sini" % u["jenis"].lower()),
            '<figure class="hero-foto"><img src="/%s/img/%s.jpg" alt="%s" width="720" height="540" fetchpriority="high" decoding="async"><span class="lencana">%s</span></figure>\n' % (u["slug"], foto, e(alt_foto), e(u["area"].split(",")[0])),
            tag("Foto %s Anda tampil di sini" % u["jenis"].lower()),
            status,
            '<p class="lead">%s</p>\n<div class="aksi">%s</div>\n</div>\n' % (e(u["lead"]), aksi),
            html_fakta(u),
            nav,
            kartu_demo(u, n),
            "</section>\n",
        ]
    else:
        body += [
            '<section class="hero">\n' + kartu_demo(u, n) + '<div class="hero-isi">\n<p class="eyebrow">%s &middot; %s</p>\n<h1>%s</h1>\n' % (e(u["jenis"]), e(u["area"]), e(u["nama"])),
            tag("Nama %s Anda tampil di sini" % u["jenis"].lower()),
            status,
            '<p class="lead">%s</p>\n<div class="aksi">%s</div>\n</div>\n' % (e(u["lead"]), aksi),
            html_fakta(u),
            nav + "</section>\n",
        ]
    if n >= 2:
        body.append(seksi_pesan(u, n))
    if dulu:
        body.append(seksi_galeri(u))
    body.append(seksi_harga(u))
    body.append(seksi_lokasi(u))
    if n == 1 and not dulu:
        body.append(seksi_galeri(u))
    body.append(seksi_tanya(u))
    body.append(penutup_demo(u))
    body.append("</div>\n</main>\n")
    body.append(
        '<footer class="kaki"><div class="wadah"><p>%s</p><p><a href="%s">WhatsApp %s</a></p>'
        "<p>Halaman ini contoh peragaan, bukan usaha sungguhan. Dibuat oleh Rio Ekaputra Siswa, developer aplikasi web di Bandung yang membuat website untuk usaha lokal. <a href=\"https://rioeka.com\">rioeka.com</a></p></div></footer>\n" % (u["kontak"], wa, e(u["wa_tampil"]))
    )
    if n == 1:
        bar = '<a class="tombol" href="%s">%s Tanya lewat WhatsApp</a>' % (wa, I_WA)
    else:
        bar = '<a class="tombol" href="#pesan">Pesan sekarang</a><a class="tombol garis" href="%s">WhatsApp</a>' % wa
    body.append('<div class="bar-bawah" id="bar-bawah">%s</div>\n' % bar)

    scripts = ""
    if mode != "inap":
        scripts += "<script>\n" + STATUS_JS.replace("__JAM__", jam_json) + "</script>\n"
    if n >= 2:
        if mode == "jadwal":
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
        elif mode == "inap":
            D = {
                "mode": "inap",
                "kode": u["kode"], "wa": u["wa"], "bayar": n == 3,
                "muka": u["muka"], "mukaTeks": u["mukaTeks"], "bayarNanti": u["bayarNanti"],
                "checkin": u["checkin"], "checkout": u["checkout"],
                "jam": {str(h): u["jam"][h] for h in range(7)},
                "kamar": [{"nama": a, "harga": b, "kap": c, "ket": d} for a, b, c, d in u["kamar"]],
            }
            scripts += "<script>\n" + WIZARD_JS.replace("__DATA__", json.dumps(D, ensure_ascii=False)) + BAR_JS + "</script>\n"
        else:
            D = {
                "mode": "pesan",
                "kode": u["kode"], "wa": u["wa"], "bayar": n == 3,
                "muka": u["muka"], "mukaTeks": u["mukaTeks"], "bayarNanti": u["bayarNanti"],
                "ongkir": u["ongkir"], "areaAntar": u["areaAntar"], "tempatAmbil": u["tempatAmbil"],
                "jam": {str(h): u["jam"][h] for h in range(7)},
                "menu": [{"nama": g, "item": items} for g, items in u["menu"]],
            }
            scripts += "<script>\n" + WIZARD_JS.replace("__DATA__", json.dumps(D, ensure_ascii=False)) + BAR_JS + "</script>\n"
    return head(judul, desc, css, warna=WARNA_TEMA[u["tema"]], extra=preload) + "".join(body) + scripts + "</body>\n</html>\n"


WA_PEMILIK = "6287834471149"
WA_PEMILIK_TAMPIL = "0878-3447-1149"
WA_PEMILIK_PESAN = "Halo, saya tertarik dengan paket website dari devario.rioeka.com. Boleh tanya-tanya dulu?"
PERAWATAN = "menjaga situs tetap aktif dan aman, serta bantu ubah teks kecil seperti harga dan jam buka"

PAKET = [
    ("1", "Halaman informasi", "Harga layanan, jam buka, alamat, dan tombol WhatsApp. Yang paling cepat jadi dan paling murah.",
     "Kalau usaha Anda hanya perlu supaya orang menemukan dan bisa bertanya.",
     1000000, 300000),
    ("2", "Tambah sistem booking", "Pengunjung memilih layanan, nama staf, tanggal, dan jam sendiri. Tidak perlu bolak-balik WhatsApp.",
     "Kalau jadwal sudah ramai dan pesanan sering bertabrakan.",
     1500000, 500000),
    ("3", "Tambah pembayaran", "Pengunjung membayar muka saat memesan, supaya yang memesan tidak hilang begitu saja.",
     "Kalau sering ada yang memesan lalu tidak datang.",
     1650000, 600000),
]

BEDA = (
    '<section class="bagian beda" id="beda"><div class="wadah wadah-lebar">\n'
    "<h2>Website sendiri, bukan website numpang</h2>\n"
    '<p class="bagian-lead">Website murah sekitar Rp 300 ribu biasanya numpang di alamat orang lain, seperti membuka lapak di teras toko orang. '
    "Website dari saya seperti punya toko sendiri: alamatnya didaftarkan atas nama usaha Anda, tampilannya dibuat khusus untuk usaha Anda.</p>\n"
    '<div class="alamat-banding">'
    '<div class="alamat-pil redup"><span class="alamat-label">Website numpang</span><b>namausaha.layananweb.com</b>'
    "<span>Alamat gratisan, ada nama layanan lain di belakangnya.</span></div>"
    '<div class="alamat-pil unggul"><span class="alamat-label">Website dari saya</span><b>namausaha.com</b>'
    "<span>atau namausaha.id. Alamat web didaftarkan atas nama usaha Anda.</span></div></div>\n"
    '<table class="banding"><caption class="sr">Perbandingan website murah dan website dari saya</caption>'
    '<thead><tr><th scope="col">Website murah (numpang)</th><th scope="col">Website dari saya</th></tr></thead><tbody>'
    "<tr><td>Tampilan memilih dari contoh yang juga dipakai usaha lain</td><td>Dirancang khusus untuk usaha Anda</td></tr>"
    "<tr><td>Alamat ada nama layanan lain di belakangnya</td><td>Alamat .com atau .id atas nama usaha Anda</td></tr>"
    "<tr><td>Terkesan percobaan, orang ragu</td><td>Terkesan usaha yang mapan dan layak dipercaya</td></tr>"
    "<tr><td>Umumnya hanya halaman info</td><td>Bisa booking dan bayar muka (Paket 2 dan 3)</td></tr>"
    "</tbody></table>\n"
    '<p class="beda-tutup">Dari luar sama-sama website. Bedanya terasa saat pelanggan pertama kali melihat alamatnya dan menimbang apakah usaha Anda bisa dipercaya.</p>\n'
    "</div></section>\n"
)


def wa_pemilik():
    return "https://wa.me/%s?text=%s" % (WA_PEMILIK, quote(WA_PEMILIK_PESAN, safe=""))


def kartu_paket(no, nama, rinci, cocok, isi, harga, tahunan, bawah):
    li = "".join("<li>%s<span>%s</span></li>" % (I_CENTANG, e(x)) for x in isi)
    return (
        '<li class="paket"><article><div><span class="no">Paket %s</span><h3>%s</h3></div><p class="ket">%s</p>'
        '<div class="harga"><p class="harga-label">Harga paket</p><p class="harga-angka">%s</p>'
        '<p class="harga-ket">Sudah termasuk alamat web (domain) atas nama Anda dan hosting tahun pertama.</p>'
        '<p class="harga-ket">Tahun berikutnya %s per tahun: alamat web, hosting, dan perawatan.</p></div>'
        '<p class="cocok"><b>Cocok</b> %s</p><ul class="isi" aria-label="Isi paket %s">%s</ul>'
        '<div class="bawah">%s</div></article></li>' % (no, e(nama), e(rinci), rp(harga), rp(tahunan), e(cocok), no, li, bawah)
    )


def halaman_index():
    css = FONT + "\n:root{" + INDEX_TOKENS + "}\n" + BASE + INDEX
    jenis = "".join(
        '<li class="jenis-kartu" style="--jenis-aksen:%s;--jenis-lembut:%s"><span class="jenis-ikon">%s</span><h3>%s</h3><p>%s</p>'
        '<a class="tombol" href="/%s/">Lihat paket dan demo</a></li>' % (AKSEN_JENIS[u["slug"]][0], AKSEN_JENIS[u["slug"]][1], IKON[u["slug"]], e(u["label"]), e(u["ringkas"]), u["slug"])
        for u in USAHA
    )
    harga = []
    for no, nama, rinci, cocok, hrg, tahunan in PAKET:
        bawah = (
            '<div class="harga"><p class="harga-label">Harga paket</p><p class="harga-angka">%s</p>'
            '<p class="harga-ket">Sudah termasuk alamat web (domain) atas nama Anda dan hosting tahun pertama.</p>'
            '<p class="harga-ket">Tahun berikutnya %s per tahun: alamat web, hosting, dan perawatan.</p></div>'
            '<p class="cocok"><b>Cocok</b> %s</p>'
        ) % (rp(hrg), rp(tahunan), e(cocok))
        harga.append(
            '<li class="paket"><article><div><span class="no">Paket %s</span><h3>%s</h3></div><p class="ket">%s</p>%s</article></li>'
            % (no, e(nama), e(rinci), bawah)
        )
    body = (
        "<body>\n"
        '<header class="atas atas-hijau"><div class="wadah wadah-lebar"><a class="merek" href="/">%s</a></div></header>\n'
        "<main>\n"
        '<section class="hero"><div class="wadah wadah-lebar">\n<p class="eyebrow">Situs demo &middot; jasa pembuatan website</p>\n'
        "<h1>Website untuk usaha lokal Anda</h1>\n"
        '<p class="lead">%s adalah situs peragaan, bukan usaha sungguhan. Di sini Anda bisa melihat dan mencoba sendiri tampilan dan fitur website yang Anda dapatkan kalau memakai jasa pembuatan website dari Rio Ekaputra Siswa, developer aplikasi web di Bandung. Pilih jenis usaha Anda di bawah.</p>\n'
        '<div class="aksi"><a class="tombol" href="#jenis">Pilih jenis usaha</a><a class="tombol garis" href="%s">%s Tanya lewat WhatsApp</a></div>\n</div></section>\n'
        '<section class="bagian" id="jenis"><div class="wadah wadah-lebar">\n<h2>Pilih jenis usaha Anda</h2>\n'
        '<p class="bagian-lead">Setiap jenis punya halaman paket sendiri dan tiga demo yang bisa dicoba langsung di HP.</p>\n'
        '<ul class="jenis-daftar">%s</ul>\n</div></section>\n'
        "%s"
        '<section class="bagian" id="harga"><div class="wadah wadah-lebar">\n<h2>Tiga paket yang bisa dipilih</h2>\n'
        '<p class="bagian-lead">Harga paket sama untuk semua jenis usaha. Isi tiap paket menyesuaikan jenis usaha Anda, pilih jenis di atas. Harga di bawah adalah harga sebenarnya.</p>\n'
        '<ul class="paket-daftar paket">%s</ul>\n'
        '<p class="catatan-harga">Perawatan tahunan berarti %s.</p>\n'
        "</div></section>\n"
        '<section class="bagian hubungi" id="hubungi"><div class="wadah wadah-lebar"><div class="kartu-hubungi">\n'
        "<h2>Tertarik atau mau tanya dulu?</h2>\n"
        '<p class="bagian-lead">Kirim pesan lewat WhatsApp. Ceritakan usaha Anda, nanti saya bantu pilih paket yang paling pas. Nomor WhatsApp saya: %s.</p>\n'
        '<div class="aksi"><a class="tombol" href="%s">%s Chat WhatsApp</a></div>\n'
        "</div></div></section>\n</main>\n"
        '<footer class="kaki"><div class="wadah wadah-lebar"><p>Dibuat oleh Rio Ekaputra Siswa, developer aplikasi web di Bandung. <a href="https://rioeka.com">rioeka.com</a></p>'
        "<p>Harga di atas tetap, tanpa biaya tersembunyi. Nama, harga layanan, dan alamat di dalam demo hanya contoh.</p>"
        '<p><a href="%s">WhatsApp %s</a></p></div></footer>\n'
        "</body>\n</html>\n"
    ) % (MERK, MERK, wa_pemilik(), I_WA, jenis, BEDA, "".join(harga), PERAWATAN, WA_PEMILIK_TAMPIL, wa_pemilik(), I_WA, wa_pemilik(), WA_PEMILIK_TAMPIL)
    return head(MERK + ", demo website untuk usaha lokal", "Situs uji coba: lihat dan coba tampilan serta fitur website dengan alamat web sendiri untuk salon, barbershop, spa, penginapan, dan katering, lewat jasa pembuatan website Rio Ekaputra Siswa.", css, warna=WARNA_INDEX) + body


def halaman_jenis(u):
    css = FONT + "\n:root{" + INDEX_TOKENS + "}\n" + BASE + INDEX
    cards = "".join(
        kartu_paket(no, nama, t[1], t[2], u["paket_isi"][idx], harga, tahunan,
                    '<a class="tombol" href="/%s/paket-%s/">Buka demo Paket %s</a>'
                    '<p class="harga-tag">Yang terbuka halaman contoh, bukan usaha sungguhan</p>' % (u["slug"], no, no))
        for idx, (no, nama, rinci, cocok, harga, tahunan) in enumerate(PAKET)
        for t in [u["paket_teks"][idx]]
    )
    body = (
        "<body>\n"
        '<header class="atas atas-hijau"><div class="wadah wadah-lebar"><a class="merek" href="/">%s</a><a class="balik" href="/#jenis">%s Semua jenis usaha</a></div></header>\n'
        '<main style="--jenis-aksen:%s;--jenis-lembut:%s">\n'
        '<section class="hero"><div class="wadah wadah-lebar">\n<span class="jenis-ikon jenis-ikon-hero">%s</span>\n<p class="eyebrow">Paket 1 sampai 3 &middot; demo bisa dicoba</p>\n'
        "<h1>Website untuk %s</h1>\n<p class=\"lead\">%s</p>\n"
        '<div class="aksi"><a class="tombol" href="#paket">Lihat tiga paket</a><a class="tombol garis" href="%s">%s Tanya lewat WhatsApp</a></div>\n</div></section>\n'
        '<section class="bagian" id="paket"><div class="wadah wadah-lebar">\n<h2>Tiga paket untuk %s</h2>\n'
        '<p class="bagian-lead">Pilih paket, lalu buka demonya dan coba langsung di HP. Nama usaha dan harga layanan di dalam demo hanya contoh. Harga paket di bawah adalah harga sebenarnya.</p>\n'
        '<ul class="paket-daftar paket paket-link">%s</ul>\n'
        '<p class="catatan-harga">Perawatan tahunan berarti %s.</p>\n</div></section>\n'
        '<section class="bagian hubungi" id="hubungi"><div class="wadah wadah-lebar"><div class="kartu-hubungi">\n'
        "<h2>Tertarik atau mau tanya dulu?</h2>\n"
        '<p class="bagian-lead">Kirim pesan lewat WhatsApp. Ceritakan usaha Anda, nanti saya bantu pilih paket yang paling pas. Nomor WhatsApp saya: %s.</p>\n'
        '<div class="aksi"><a class="tombol" href="%s">%s Chat WhatsApp</a></div>\n'
        "</div></div></section>\n</main>\n"
        '<footer class="kaki"><div class="wadah wadah-lebar"><p>Dibuat oleh Rio Ekaputra Siswa, developer aplikasi web di Bandung. <a href="https://rioeka.com">rioeka.com</a></p>'
        "<p>Harga di atas tetap, tanpa biaya tersembunyi. Nama, harga layanan, dan alamat di dalam demo hanya contoh.</p>"
        '<p><a href="%s">WhatsApp %s</a></p></div></footer>\n'
        "</body>\n</html>\n"
    ) % (MERK, I_KIRI, AKSEN_JENIS[u["slug"]][0], AKSEN_JENIS[u["slug"]][1], IKON[u["slug"]], e(u["pendek"]), e(u["lihat"]), wa_pemilik(), I_WA, e(u["pendek"].lower()), cards, PERAWATAN, WA_PEMILIK_TAMPIL, wa_pemilik(), I_WA, wa_pemilik(), WA_PEMILIK_TAMPIL)
    return head("%s | %s" % (u["pendek"], MERK), "%s Lihat tiga paket dan coba demonya." % e(u["lihat"]), css, warna=WARNA_INDEX) + body


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
        alt_li = "".join(
            '<li><a href="/%s/paket-1/"><span class="alt-nama"><span class="alt-ikon">%s</span>Demo %s</span>%s</a></li>' % (u["slug"], IKON[u["slug"]], e(u["pendek"].lower()), I_KANAN)
            for u in USAHA
        )
        alt_li += '<li><a href="/"><span class="alt-nama"><span class="alt-ikon">%s</span>Beranda</span>%s</a></li>' % (I_RUMAH, I_KANAN)
        alt = (
            '<nav class="alternatif" aria-labelledby="alt-judul"><h2 id="alt-judul">Atau langsung buka</h2><ul>%s</ul></nav>' % alt_li
        )
        js = "<script>\n" + GALAT_JS + "</script>\n"
    else:
        aksi = '<a class="tombol" href="">Muat ulang</a><a class="tombol garis" href="/">Ke beranda</a>'
        alt = ""
        js = ""
    body = (
        "<body>\n"
        '<header class="atas atas-hijau"><div class="wadah wadah-lebar"><a class="merek" href="/">%s</a></div></header>\n'
        '<main><section class="galat"><div class="wadah">\n'
        '<span class="kode-galat" aria-hidden="true">%s</span>\n'
        "<h1>%s</h1>\n"
        '<p class="lead">%s</p>\n'
        '<div class="aksi">%s</div>\n%s'
        "</div></section></main>\n"
        '<footer class="kaki"><div class="wadah"><p>Dibuat oleh Rio Ekaputra Siswa, developer aplikasi web di Bandung. <a href="https://rioeka.com">rioeka.com</a></p></div></footer>\n'
        "%s</body>\n</html>\n"
    ) % (MERK, e(kode), e(judul), e(teks), aksi, alt, js)
    return head(judul + " | " + MERK, teks, css, warna=WARNA_INDEX) + body


def tulis(rel, isi):
    path = os.path.join(ROOT, rel.replace("/", os.sep))
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\r\n") as f:
        f.write(isi)
    print("tulis", rel, len(isi))


if __name__ == "__main__":
    tulis("index.html", halaman_index())
    for berkas, kode, judul, teks, kembali in GALAT:
        tulis(berkas, halaman_galat(kode, judul, teks, kembali))
    for u in USAHA:
        tulis("%s/index.html" % u["slug"], halaman_jenis(u))
        for n in (1, 2, 3):
            tulis("%s/paket-%d/index.html" % (u["slug"], n), halaman_demo(u, n))
