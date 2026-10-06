# AGENTS.md

Repo publik: **keluaran statis jadi** situs demo lima jenis usaha lokal untuk https://devario.rioeka.com, disajikan nginx. Tidak ada generator, package manager, test, atau linter di sini.

Sumber (generator, skin, layanan isi data online, aset mentah) ada di **repo privat `isi-rioeka`**. Jangan mengedit HTML di sini secara manual sebagai alur normal: ubah di repo privat, jalankan `python tools/bangun/build.py`, lalu salin berkas HTML hasil ke repo ini. Perubahan langsung di sini hanya untuk perbaikan darurat satu berkas.

## Isi repo
- `index.html`: hub daftar lima jenis usaha. `{jenis}/index.html` untuk `salon`, `barbershop`, `spa`, `penginapan`, `katering`: daftar 3 paket jenis itu.
- `{jenis}/paket-{1,2,3}/{skin}/index.html`: 60 halaman demo (5 jenis x 3 paket x 4 skin). Tiap berkas mandiri (CSS inline, 1-2 `<script>` inline), tanpa shared stylesheet.
- `{jenis}/img/`: foto galeri `g1-g6.jpg` (720x540, Unsplash License, kredit di `.kredit`) + pratinjau skin `skin-{slug}.jpg` (600x450).
- `font/`: font self-hosted (Fontsource, OFL) dimuat lewat `@font-face` dengan URL mutlak `/font/...`.
- `404.html`, `50x.html`: halaman galat bertema index. Disajikan nginx lewat `nginx.conf` (`error_page`, 403 dipetakan ke 404, keduanya `internal`). Semua link dan aset harus mutlak karena disajikan di path apa pun. Keduanya `noindex`.
- `nginx.conf`, `robots.txt` (`Disallow: /`), `Dockerfile` (nginx, port 80).
- `klien/` (jika ada) dan `logs/` tidak dilacak git.

## Konvensi saat mengubah (via repo privat)
- Semua halaman `noindex, nofollow`. Jangan hapus.
- Link internal pakai path mutlak (`/salon/paket-2/`), bukan relatif.
- Tidak ada hex mentah bebas: pakai variabel CSS di `:root`. Satu aksen per halaman (`--sinyal`).
- Mobile-first: target sentuh min 44px, kontras min 4.5:1, hormati `prefers-reduced-motion`, tanpa scroll horizontal di 375px.
- Keluaran generator memakai CRLF dan idempoten.
- Kalau menambah berkas/folder baru, tambahkan `COPY` di `Dockerfile`. Yang disalin ke image: `index.html`, `404.html`, `50x.html`, `nginx.conf`, `robots.txt`, `salon/`, `barbershop/`, `spa/`, `penginapan/`, `katering/`, `font/`.

## Menjalankan
```
docker build -t demo-rioeka .
docker run -p 8080:80 demo-rioeka
```
Alternatif tanpa Docker (path font mutlak tetap jalan): `npx serve .` atau `python -m http.server 8080` dari root repo.

## Deploy
Coolify: build pack Dockerfile, port 80, domain `devario.rioeka.com`. Hanya berkas statis; tanpa volume.

## Lainnya
- `logs/` berisi log lokal; tidak dilacak git (`*.log`), jangan di-commit.
- `.gitignore` adalah template Python generik; tidak relevan untuk repo statis ini.
