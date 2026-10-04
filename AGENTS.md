# AGENTS.md

Situs statis demo (salon + barbershop) untuk https://demo.rioeka.com. Tanpa build, package manager, test, atau linter. Semua UI Bahasa Indonesia, data contoh (nama, harga, nomor WA) fiktif.

## Struktur
- `index.html`: daftar paket (halaman utama, CSS dan JS inline).
- `salon/paket-{1,2,3}/index.html`, `barbershop/paket-{1,2,3}/index.html`: halaman demo nyata. Masing-masing berkas mandiri (CSS inline, 1-2 `<script>` inline), tanpa shared stylesheet. Perubahan gaya bersama harus diterapkan manual ke tiap berkas.
- `salon/index.html`, `barbershop/index.html`: hanya redirect (`meta refresh` ke `/`) untuk alamat lama. Jangan diisi konten lagi.
- `font/`: Archivo self-hosted. Halaman memuat font lewat `@font-face` inline dengan URL mutlak `/font/archivo-latin.woff2`, jadi harus disajikan dari root domain; buka via `file://` tidak memuat font.
- Alur booking di `salon/paket-{2,3}` dan `barbershop/paket-{2,3}` (`#langkah-isi`): satu langkah terbuka, langkah selesai diringkas satu baris + tombol "Ubah". Blok JS "langkah booking" di akhir script kedua identik di keempat berkas; ubah di semuanya. Berkas ini memakai CRLF.
- README.md menyebut "tiga halaman"; sudah usang, struktur sebenarnya seperti di atas.

## Konvensi
- Semua halaman demo `noindex, nofollow`; `robots.txt` = `Disallow: /`. Jangan hapus.
- Link internal pakai path mutlak (`/salon/paket-2/`), bukan relatif.
- Tidak ada hex mentah bebas: pakai variabel CSS di `:root` (`--papan`, `--tulang`, `--kertas`, `--tinta`, `--sinyal`, dst.). Satu aksen saja (`--sinyal`).
- Kalau menambah berkas/folder baru, tambahkan `COPY` di `Dockerfile`; hanya `index.html`, `robots.txt`, `salon/`, `barbershop/`, `font/` yang disalin ke image.

## Menjalankan
```
docker build -t demo-rioeka .
docker run -p 8080:80 demo-rioeka
```
Alternatif tanpa Docker (path font mutlak tetap jalan): `npx serve .` atau `python -m http.server 8080` dari root repo.

## Lainnya
- `logs/` berisi log lokal puppeteer; tidak dilacak git sengaja (`*.log`), jangan di-commit.
- `.gitignore` adalah template Python generik; tidak relevan dengan repo ini.
