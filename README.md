# Halaman demo usaha lokal

Contoh halaman web untuk lima jenis usaha lokal, dibuat oleh [Rio Ekaputra Siswa](https://rioeka.com), developer aplikasi web di Bandung. Situs demo: https://devario.rioeka.com

Halaman statis:

- `/` daftar lima jenis usaha (hub)
- `/salon/`, `/barbershop/`, `/spa/`, `/penginapan/`, `/katering/` daftar paket tiap jenis
- `/{jenis}/paket-1/`, `/{jenis}/paket-2/`, `/{jenis}/paket-3/` contoh halaman demo (15 halaman)
- `404.html` dan `50x.html` halaman galat
- URL lama `/salon/paket-N/` dan `/barbershop/paket-N/` tetap jalan

Semua nama, alamat, harga layanan, foto, dan nomor di dalam halaman demo masih data contoh. Harga paket di halaman hub dan halaman jenis adalah harga sebenarnya (nomor WhatsApp pemilik juga nomor asli).

Setiap halaman demo menegaskan statusnya lewat strip di atas header, kartu "Di demo ini / Di website Anda", label "Contoh ..." di tiap bagian, dan penutup. Alur pemesanan di paket-2 dan paket-3 mengikuti jenis usaha:

- salon, barbershop, spa: pilih layanan, terapis/barber, lalu jadwal
- penginapan: pilih kamar, tanggal, jumlah malam, dan tamu
- katering: pilih menu dan jumlah, cara terima (antar atau ambil), tanggal dan jam

Paket-3 menambah langkah pembayaran (QRIS atau transfer).

## Mengubah halaman

Kedua puluh tiga berkas HTML dihasilkan generator di `tools/bangun/`. Ubah sumbernya lalu jalankan dari root repo:

```
python tools/bangun/build.py
```

Empat modul sumber: `css.py` (gaya dan tema), `data.py` (isi lima jenis usaha), `js.py` (status buka, alur pesanan, wizard), `build.py` (markup). Berkas HTML adalah hasil generate, jangan diedit langsung.

## Disajikan bagaimana

Dockerfile memakai nginx dan menyalin berkas yang perlu saja. Wadahnya mendengarkan di port 80.

```
docker build -t demo-rioeka .
docker run -p 8080:80 demo-rioeka
```

Tanpa Docker (path font mutlak tetap jalan): `npx serve .` atau `python -m http.server 8080` dari root repo.

## Catatan

Semua halaman dipasang `noindex, nofollow`, dan `robots.txt` menolak semua mesin pencari. Jadi situs ini tidak muncul di hasil pencarian.

Foto galeri memakai foto Unsplash gratis (disimpan lokal, kredit di bagian galeri). Font Archivo, Cormorant Garamond (salon dan spa), dan Fraunces (katering) di-host sendiri di `font/` dan dimuat lewat path mutlak `/font/`, jadi halaman harus disajikan dari root domain.
