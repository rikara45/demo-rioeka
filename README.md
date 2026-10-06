# Halaman demo usaha lokal

Contoh halaman web untuk lima jenis usaha lokal, dibuat oleh [Rio Ekaputra Siswa](https://rioeka.com), developer aplikasi web di Bandung. Situs demo: https://devario.rioeka.com

Repo ini berisi **keluaran statis jadi** (HTML, foto, font) + konfigurasi nginx. Tidak ada generator di sini: sumber (generator, skin, layanan isi data) ada di repo privat `isi-rioeka`. Untuk mengubah halaman, ubah di repo privat itu, lalu jalankan generator dan salin hasilnya ke sini.

Halaman statis:

- `/` daftar lima jenis usaha (hub)
- `/salon/`, `/barbershop/`, `/spa/`, `/penginapan/`, `/katering/` daftar paket tiap jenis
- `/{jenis}/paket-{1,2,3}/{skin}/` contoh halaman demo (60 halaman, 4 skin per jenis)
- `404.html` dan `50x.html` halaman galat

Semua nama, alamat, harga layanan, foto, dan nomor di dalam halaman demo masih data contoh. Harga paket di halaman hub dan halaman jenis adalah harga sebenarnya (nomor WhatsApp pemilik juga nomor asli).

Setiap halaman demo menegaskan statusnya lewat strip di atas header, kartu "Di demo ini / Di website Anda", label "Contoh ..." di tiap bagian, dan penutup. Alur pemesanan di paket-2 dan paket-3 mengikuti jenis usaha:

- salon, barbershop, spa: pilih layanan, terapis/barber, lalu jadwal
- penginapan: pilih kamar, tanggal, jumlah malam, dan tamu
- katering: pilih menu dan jumlah, cara terima (antar atau ambil), tanggal dan jam

Paket-3 menambah langkah pembayaran (QRIS atau transfer).

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
