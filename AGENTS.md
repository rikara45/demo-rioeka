# AGENTS.md

Situs statis demo (salon + barbershop) untuk https://demo.rioeka.com. Tanpa package manager, test, atau linter. Semua UI Bahasa Indonesia, data contoh (nama, harga, nomor WA) fiktif.

## Struktur
- `tools/bangun/`: generator Python (tanpa dependency) yang menulis 7 berkas HTML di bawah. Berkas HTML adalah hasil generate: ubah sumbernya, lalu jalankan `python tools/bangun/build.py` dari root repo. Jangan edit HTML langsung, perubahan akan tertimpa. `css.py` = gaya dan tema, `data.py` = isi salon dan barbershop, `js.py` = status buka, alur booking, bar bawah, `build.py` = markup. Keluaran memakai CRLF dan idempoten. Folder ini tidak disalin ke image Docker.
- `index.html`: daftar paket (halaman utama, CSS dan JS inline).
- `salon/paket-{1,2,3}/index.html`, `barbershop/paket-{1,2,3}/index.html`: halaman demo nyata. Masing-masing berkas mandiri (CSS inline, 1-2 `<script>` inline), tanpa shared stylesheet. Gaya bersama cukup diubah di `css.py`, lalu generate ulang.
- `salon/index.html`, `barbershop/index.html`: hanya redirect (`meta refresh` ke `/`) untuk alamat lama. Jangan diisi konten lagi.
- `font/`: Archivo self-hosted. Halaman memuat font lewat `@font-face` inline dengan URL mutlak `/font/archivo-latin.woff2`, jadi harus disajikan dari root domain; buka via `file://` tidak memuat font.
- Alur booking di `salon/paket-{2,3}` dan `barbershop/paket-{2,3}` (`#pesan`, `#alur`): wizard satu langkah per layar (paket 2 = 5 langkah, paket 3 = 6 dengan pembayaran), progress bar, tombol Lanjut/Kembali lengket di `.aksi-langkah`, layar "Periksa" dengan tombol "Ubah" per baris. Satu sumber JS (`BOOKING_JS` di `js.py`), data per usaha lewat `var D`. Semua berkas HTML memakai CRLF.

## Konvensi
- Semua halaman demo `noindex, nofollow`; `robots.txt` = `Disallow: /`. Jangan hapus.
- Link internal pakai path mutlak (`/salon/paket-2/`), bukan relatif.
- Tidak ada hex mentah bebas: pakai variabel CSS di `:root` (`--latar`, `--kartu`, `--tinta`, `--tinta-redup`, `--garis`, `--sinyal`, dst.). Satu aksen per halaman (`--sinyal`). Salon = tema terang rose (`THEME_SALON`), barbershop = tema gelap amber (`THEME_BARBER`), index = hijau tua dengan aksen jingga (`INDEX_TOKENS`). Hex hanya didefinisikan di blok tema di `css.py`.
- Mobile-first: target sentuh min 44px, kontras teks min 4.5:1 (cek ulang kalau warna tema diganti), hormati `prefers-reduced-motion`, tanpa scroll horizontal di 375px.
- Kalau menambah berkas/folder baru, tambahkan `COPY` di `Dockerfile`; hanya `index.html`, `robots.txt`, `salon/`, `barbershop/`, `font/` yang disalin ke image (`tools/` sengaja tidak).

## Menjalankan
```
docker build -t demo-rioeka .
docker run -p 8080:80 demo-rioeka
```
Alternatif tanpa Docker (path font mutlak tetap jalan): `npx serve .` atau `python -m http.server 8080` dari root repo.

## Lainnya
- `logs/` berisi log lokal puppeteer; tidak dilacak git sengaja (`*.log`), jangan di-commit.
- `.gitignore` adalah template Python generik; tidak relevan dengan repo ini.
