# Halaman demo usaha lokal

Contoh halaman web untuk salon dan barbershop, dibuat oleh [Rio Ekaputra Siswa](https://rioeka.com), developer aplikasi web di Bandung.

Situs ini berisi halaman statis:

- `/` daftar paket
- `/salon/paket-1/`, `/salon/paket-2/`, `/salon/paket-3/` contoh halaman salon
- `/barbershop/paket-1/`, `/barbershop/paket-2/`, `/barbershop/paket-3/` contoh halaman barbershop
- `/salon/` dan `/barbershop/` hanya mengalihkan ke `/`

Semua nama, alamat, harga, foto, dan nomor di dalamnya masih data contoh.

## Mengubah halaman

Ketujuh berkas HTML dihasilkan oleh generator di `tools/bangun/`. Ubah sumbernya (`css.py`, `data.py`, `js.py`, `build.py`), lalu jalankan dari root repo:

```
python tools/bangun/build.py
```

## Disajikan bagaimana

Dockerfile memakai nginx dan menyalin berkas yang perlu saja. Wadahnya mendengarkan di port 80.

```
docker build -t demo-rioeka .
docker run -p 8080:80 demo-rioeka
```

## Catatan

Semua halaman contoh dipasang `noindex, nofollow`, dan `robots.txt` menolak semua mesin pencari. Jadi halaman contoh ini tidak muncul di hasil pencarian.
