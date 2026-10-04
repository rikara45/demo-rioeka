# Halaman demo usaha lokal

Contoh halaman web untuk salon dan barbershop, dibuat oleh [Rio Ekaputra Siswa](https://rioeka.com).

Situs ini berisi tiga halaman statis:

- `/` daftar demo
- `/salon/` contoh halaman salon
- `/barbershop/` contoh halaman barbershop

Semua nama, alamat, harga, foto, dan nomor di dalamnya masih data contoh.

## Disajikan bagaimana

Dockerfile memakai nginx dan menyalin berkas yang perlu saja. Wadahnya mendengarkan di port 80.

```
docker build -t demo-rioeka .
docker run -p 8080:80 demo-rioeka
```

## Catatan

Kedua halaman contoh dipasang `noindex, nofollow`, dan `robots.txt` menolak semua mesin pencari. Jadi halaman contoh ini tidak muncul di hasil pencarian.
