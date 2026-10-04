FONT = "@font-face{font-family:Archivo;font-style:normal;font-weight:400 800;font-stretch:62% 125%;font-display:swap;src:url(/font/archivo-latin.woff2) format('woff2')}"

THEME_SALON = """
  --latar:#FBF6F2;
  --kartu:#FFFFFF;
  --kartu-turun:#F4EAE3;
  --tinta:#2B1B24;
  --tinta-redup:#6A5560;
  --garis:#E6D6CE;
  --garis-kuat:#8A7580;
  --sinyal:#B0305A;
  --sinyal-gelap:#8F2147;
  --sinyal-lembut:#FBE6EC;
  --di-atas-sinyal:#FFFFFF;
  --fokus:#B0305A;
  --salah:#A8261A;
  --ok:#2F6B4F;
  --r:20px;
  --r-kecil:14px;
  --r-tombol:999px;
  --bayang:0 1px 2px rgba(43,27,36,.06),0 8px 24px rgba(43,27,36,.06);
  --h-berat:700;
  --h-lebar:100%;
  --h-huruf:none;
  --h-ls:-.01em;
  --pole-tinggi:0px;
  --pole:none;
"""

THEME_BARBER = """
  --latar:#141210;
  --kartu:#1E1B18;
  --kartu-turun:#28241F;
  --tinta:#F4EFE7;
  --tinta-redup:#B5AA9C;
  --garis:#3A342C;
  --garis-kuat:#7E7468;
  --sinyal:#E9A23B;
  --sinyal-gelap:#F2B554;
  --sinyal-lembut:#3A2E18;
  --di-atas-sinyal:#17110A;
  --fokus:#E9A23B;
  --salah:#FF9C87;
  --ok:#7FCB9A;
  --r:10px;
  --r-kecil:8px;
  --r-tombol:8px;
  --bayang:none;
  --h-berat:800;
  --h-lebar:72%;
  --h-huruf:uppercase;
  --h-ls:.01em;
  --pole-tinggi:10px;
  --pole:repeating-linear-gradient(135deg,var(--sinyal) 0 14px,var(--tinta) 14px 28px);
"""

THEME_SPA = """
  --latar:#F3F6F1;
  --kartu:#FFFFFF;
  --kartu-turun:#E6EDE4;
  --tinta:#1D2B24;
  --tinta-redup:#4E5F56;
  --garis:#D5DFD3;
  --garis-kuat:#76887C;
  --sinyal:#2F6B4F;
  --sinyal-gelap:#245640;
  --sinyal-lembut:#E1EEE3;
  --di-atas-sinyal:#FFFFFF;
  --fokus:#2F6B4F;
  --salah:#A8261A;
  --ok:#2F6B4F;
  --r:24px;
  --r-kecil:16px;
  --r-tombol:999px;
  --bayang:0 1px 2px rgba(29,43,36,.05),0 10px 28px rgba(29,43,36,.06);
  --h-berat:600;
  --h-lebar:100%;
  --h-huruf:none;
  --h-ls:-.015em;
  --pole-tinggi:0px;
  --pole:none;
"""

THEME_INAP = """
  --latar:#F7F4EE;
  --kartu:#FFFFFF;
  --kartu-turun:#ECE7DB;
  --tinta:#1B2A33;
  --tinta-redup:#52626B;
  --garis:#DDD7C8;
  --garis-kuat:#7C8A90;
  --sinyal:#1F5F7A;
  --sinyal-gelap:#174B61;
  --sinyal-lembut:#DFEDF2;
  --di-atas-sinyal:#FFFFFF;
  --fokus:#1F5F7A;
  --salah:#A8261A;
  --ok:#2F6B4F;
  --r:14px;
  --r-kecil:10px;
  --r-tombol:12px;
  --bayang:0 1px 2px rgba(27,42,51,.06),0 6px 18px rgba(27,42,51,.06);
  --h-berat:700;
  --h-lebar:92%;
  --h-huruf:none;
  --h-ls:-.01em;
  --pole-tinggi:0px;
  --pole:none;
"""

THEME_PESAN = """
  --latar:#FBF5EA;
  --kartu:#FFFFFF;
  --kartu-turun:#F2E7D3;
  --tinta:#2E1D14;
  --tinta-redup:#6A5444;
  --garis:#E8DAC0;
  --garis-kuat:#8A7660;
  --sinyal:#A8431A;
  --sinyal-gelap:#8A3514;
  --sinyal-lembut:#FBE6D6;
  --di-atas-sinyal:#FFFFFF;
  --fokus:#A8431A;
  --salah:#A8261A;
  --ok:#2F6B4F;
  --r:18px;
  --r-kecil:12px;
  --r-tombol:999px;
  --bayang:0 1px 2px rgba(46,29,20,.06),0 8px 22px rgba(46,29,20,.07);
  --h-berat:800;
  --h-lebar:86%;
  --h-huruf:none;
  --h-ls:-.01em;
  --pole-tinggi:0px;
  --pole:none;
"""

TEMA = {
    "salon": THEME_SALON,
    "barber": THEME_BARBER,
    "spa": THEME_SPA,
    "inap": THEME_INAP,
    "pesan": THEME_PESAN,
}

WARNA_TEMA = {
    "salon": "#FBF6F2",
    "barber": "#141210",
    "spa": "#F3F6F1",
    "inap": "#F7F4EE",
    "pesan": "#FBF5EA",
}

WARNA_INDEX = "#16221E"

BASE = """
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%;scroll-padding-top:104px;background:var(--latar);accent-color:var(--sinyal)}
@media (prefers-reduced-motion:no-preference){html{scroll-behavior:smooth}}
body{margin:0;overflow-x:clip;background:var(--latar);color:var(--tinta);font-family:Archivo,system-ui,-apple-system,"Segoe UI",sans-serif;font-size:16px;line-height:1.55;padding-bottom:calc(84px + env(safe-area-inset-bottom))}
h1,h2,h3,p,ul,ol,dl,dd,figure{margin:0}
ul,ol{padding:0;list-style:none}
a{color:inherit}
svg{display:block;flex:none}
:focus-visible{outline:3px solid var(--fokus);outline-offset:2px}
::selection{background:var(--sinyal);color:var(--di-atas-sinyal)}
[hidden]{display:none !important}
.wadah{width:100%;max-width:760px;margin:0 auto;padding:0 16px}
.ikon{width:20px;height:20px;fill:none;stroke:currentColor;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}

.tombol{display:inline-flex;align-items:center;justify-content:center;gap:8px;min-height:52px;padding:0 22px;border:2px solid var(--sinyal);border-radius:var(--r-tombol);background:var(--sinyal);color:var(--di-atas-sinyal);font:inherit;font-weight:700;text-decoration:none;text-align:center;cursor:pointer;transition:background-color .15s,border-color .15s}
.tombol:hover{background:var(--sinyal-gelap);border-color:var(--sinyal-gelap)}
.tombol.garis{background:transparent;border-color:var(--garis-kuat);color:var(--tinta)}
.tombol.garis:hover{background:var(--kartu-turun)}
.tombol[aria-disabled="true"]{background:var(--kartu-turun);border-color:var(--kartu-turun);color:var(--tinta-redup);cursor:not-allowed}
.tombol[aria-busy="true"]{cursor:progress}

.atas{position:sticky;top:0;z-index:30;background:var(--latar);border-bottom:1px solid var(--garis)}
.atas .wadah{display:flex;align-items:center;gap:10px;min-height:56px}
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
.balik{display:inline-flex;align-items:center;gap:2px;min-height:44px;padding:0 12px 0 6px;margin-left:-6px;border-radius:var(--r-tombol);font-weight:600;font-size:15px;text-decoration:none;white-space:nowrap}
.balik:hover{background:var(--kartu-turun)}
.nama-atas{margin-left:auto;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;font-weight:700;font-size:15px;color:var(--tinta-redup)}

.pole{height:var(--pole-tinggi);background:var(--pole)}
.hero{padding:28px 0 4px}
.eyebrow{font-size:13px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--tinta-redup)}
.hero h1{margin:8px 0 14px;font-size:clamp(36px,11vw,56px);font-weight:var(--h-berat);font-stretch:var(--h-lebar);text-transform:var(--h-huruf);letter-spacing:var(--h-ls);line-height:1.02;text-wrap:balance}
.status{display:inline-flex;align-items:center;gap:9px;padding:8px 14px;border:1px solid var(--garis);border-radius:999px;background:var(--kartu);font-size:15px;font-weight:600}
.titik{width:10px;height:10px;border-radius:50%;background:var(--ok);flex:none}
.titik.tutup{background:var(--tinta-redup)}
.lead{margin-top:14px;max-width:46ch;color:var(--tinta-redup)}
.aksi{display:grid;gap:10px;margin-top:20px}
@media (min-width:520px){.aksi{grid-template-columns:auto auto;justify-content:start}}
.demo-strip{display:flex;justify-content:center;align-items:center;gap:8px;min-height:32px;padding:4px 16px;background:var(--sinyal);color:var(--di-atas-sinyal);font-size:13px;font-weight:600;text-align:center}
.demo-strip .tanda-contoh{background:var(--di-atas-sinyal);color:var(--sinyal-gelap)}
.demo-kartu{margin-bottom:22px;padding:16px;border:2px dashed var(--sinyal);border-radius:var(--r);background:var(--sinyal-lembut)}
.demo-judul{margin-top:10px;font-size:21px;font-weight:800;line-height:1.2;text-wrap:balance}
.demo-teks{margin-top:8px;font-size:15px}
.ganti-kepala,.ganti-daftar li{display:grid;grid-template-columns:minmax(0,1fr) 20px minmax(0,1fr);gap:8px;align-items:center}
.ganti-kepala{margin-top:14px;font-size:12px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--tinta-redup)}
.ganti-daftar{margin-top:4px}
.ganti-daftar li{padding:10px 0;border-top:1px solid var(--garis);font-size:14px;line-height:1.35}
.ganti-daftar .kini{color:var(--tinta-redup)}
.ganti-daftar .nanti{font-weight:700}
.ganti-daftar .ikon{width:18px;height:18px;color:var(--sinyal-gelap)}
.demo-paket{margin-top:12px;padding-top:12px;border-top:1px solid var(--garis);font-size:14px}
.tag-baris{margin-bottom:10px}
.tag-anda{display:inline-flex;align-items:center;min-height:28px;padding:2px 10px;border:1.5px dashed var(--sinyal);border-radius:999px;background:var(--sinyal-lembut);color:var(--sinyal-gelap);font-size:13px;font-weight:700}
.hero .tag-baris{margin:0 0 4px}
.penutup .kartu{padding:20px}
.penutup h2{font-size:clamp(22px,6vw,28px)}
.tanda-contoh{flex:none;padding:2px 9px;border-radius:999px;background:var(--sinyal);color:var(--di-atas-sinyal);font-size:12px;font-weight:700;letter-spacing:.04em;text-transform:uppercase}
.loncat{display:flex;gap:8px;overflow-x:auto;margin:20px -16px 0;padding:2px 16px 6px;scrollbar-width:none}
.loncat::-webkit-scrollbar{display:none}
.loncat a{flex:none;display:inline-flex;align-items:center;min-height:44px;padding:0 16px;border:1px solid var(--garis-kuat);border-radius:999px;font-weight:600;font-size:15px;text-decoration:none}
.loncat a:hover{background:var(--kartu-turun)}

.bagian{padding:36px 0 4px}
.bagian h2{font-size:clamp(26px,7vw,34px);font-weight:var(--h-berat);font-stretch:var(--h-lebar);text-transform:var(--h-huruf);letter-spacing:var(--h-ls);line-height:1.08;text-wrap:balance}
.bagian-lead{margin-top:8px;max-width:56ch;color:var(--tinta-redup)}
.kartu{margin-top:16px;padding:16px;border:1px solid var(--garis);border-radius:var(--r);background:var(--kartu);box-shadow:var(--bayang)}
.kartu > h3{font-size:13px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--tinta-redup)}
.harga{margin-top:6px}
.harga li{display:grid;grid-template-columns:1fr auto;gap:2px 16px;padding:14px 0;border-top:1px solid var(--garis)}
.harga li:first-child{border-top:0}
.harga .nm{font-weight:600}
.harga .hr{font-weight:700;white-space:nowrap}
.harga .ket{grid-column:1 / -1;font-size:14px;color:var(--tinta-redup)}
.catatan{margin-top:14px;font-size:14px;color:var(--tinta-redup);max-width:60ch}
.jam li{display:flex;justify-content:space-between;gap:12px;padding:12px 10px;margin:0 -10px;border-radius:var(--r-kecil)}
.jam li + li{border-top:1px solid var(--garis);border-top-left-radius:0;border-top-right-radius:0}
.jam li.hari-ini{background:var(--sinyal-lembut);border-top-color:transparent;font-weight:700}
.jam li.hari-ini + li{border-top-color:transparent}
.jam .tanda-hari{margin-left:8px;padding:1px 8px;border-radius:999px;background:var(--sinyal);color:var(--di-atas-sinyal);font-size:12px;font-weight:700}
.alamat{margin-top:16px;font-style:normal;line-height:1.7}
.aksi-lokasi{display:grid;gap:10px;margin-top:16px}
@media (min-width:520px){.aksi-lokasi{grid-template-columns:auto auto;justify-content:start}}
.galeri{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px;margin-top:16px}
@media (min-width:600px){.galeri{grid-template-columns:repeat(3,minmax(0,1fr))}}
.petak{margin:0;aspect-ratio:4/3;overflow:hidden;border-radius:var(--r-kecil);background:var(--kartu-turun)}
.petak img{display:block;width:100%;height:100%;object-fit:cover}
.kredit{margin-top:12px;font-size:13px;color:var(--tinta-redup)}
.kredit a{color:inherit;text-decoration:underline;display:inline-block;padding:12px 0}
.tanya{margin-top:12px;border-bottom:1px solid var(--garis)}
.tanya details{border-top:1px solid var(--garis)}
.tanya summary{display:flex;justify-content:space-between;align-items:center;gap:12px;min-height:56px;padding:12px 0;font-weight:600;cursor:pointer;list-style:none}
.tanya summary::-webkit-details-marker{display:none}
.tanya summary svg{transition:transform .2s}
.tanya details[open] summary svg{transform:rotate(180deg)}
.tanya details p{padding:0 0 16px;color:var(--tinta-redup);max-width:60ch}
.ganti-paket{margin-top:28px;padding:16px;border:1px solid var(--garis);border-radius:var(--r);background:var(--kartu)}
.ganti-paket p{margin-bottom:12px}
.kaki{margin-top:36px;padding:28px 0 32px;border-top:1px solid var(--garis);font-size:14px;color:var(--tinta-redup)}
.kaki p + p{margin-top:10px}
.kaki a{display:inline-flex;align-items:center;min-height:44px;color:var(--tinta);font-weight:600}
.bar-bawah{position:fixed;left:0;right:0;bottom:0;z-index:40;display:flex;gap:10px;padding:10px 16px calc(10px + env(safe-area-inset-bottom));background:var(--latar);border-top:1px solid var(--garis);transition:transform .25s}
.bar-bawah.sembunyi{transform:translateY(110%);visibility:hidden}
.bar-bawah .tombol{flex:1 1 auto;min-height:52px;padding:0 14px;white-space:nowrap}
.bar-bawah .tombol.garis{flex:0 0 auto}
@media (min-width:760px){.bar-bawah{display:none}body{padding-bottom:0}}
@media (prefers-reduced-motion:reduce){*{transition-duration:.001ms !important;animation-duration:.001ms !important}}
"""

BOOKING = """
.pesan{padding:16px 16px 16px}
.kartu.pesan-buka > h3{font-size:20px;font-weight:800;line-height:1.2;letter-spacing:0;text-transform:none;color:var(--tinta)}
.pesan-buka p{margin:8px 0 16px;max-width:52ch;color:var(--tinta-redup)}
.pesan-buka .tombol{width:100%}
@media (min-width:520px){.pesan-buka .tombol{width:auto}}
.langkah-kepala{display:flex;justify-content:space-between;align-items:baseline;gap:12px}
.langkah-no{font-size:13px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--tinta-redup)}
.langkah-nama{font-size:13px;font-weight:600;color:var(--tinta-redup)}
.progres{height:6px;margin:10px 0 20px;border-radius:99px;background:var(--kartu-turun);overflow:hidden}
.progres i{display:block;height:100%;width:0;border-radius:99px;background:var(--sinyal);transition:width .3s}
.panel h3{font-size:24px;font-weight:var(--h-berat);font-stretch:var(--h-lebar);text-transform:var(--h-huruf);letter-spacing:var(--h-ls);line-height:1.1}
.panel h3:focus{outline:0}
.panel .tip{margin:6px 0 14px;font-size:14px;color:var(--tinta-redup)}
.sub{margin:18px 0 8px;font-size:13px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--tinta-redup)}
.opsi-daftar{display:grid;gap:8px}
.opsi{display:block;position:relative}
.opsi input{position:absolute;opacity:0;width:1px;height:1px;margin:0}
.opsi-kotak{display:grid;grid-template-columns:auto 1fr auto;gap:2px 12px;align-items:center;min-height:64px;padding:12px 14px;border:2px solid var(--garis);border-radius:var(--r-kecil);background:var(--kartu);cursor:pointer;transition:border-color .15s,background-color .15s}
.opsi-kotak:hover{border-color:var(--garis-kuat)}
.opsi-tanda{grid-row:1 / 3;display:grid;place-items:center;width:24px;height:24px;border:2px solid var(--garis-kuat);border-radius:50%}
.opsi-tanda::after{content:"";width:10px;height:10px;border-radius:50%;background:var(--di-atas-sinyal);transform:scale(0);transition:transform .15s}
.opsi-nama{grid-column:2;font-weight:700}
.opsi-ket{grid-column:2 / 4;font-size:14px;color:var(--tinta-redup)}
.opsi-harga{grid-column:3;grid-row:1;font-weight:700;white-space:nowrap}
.opsi.cek .opsi-tanda{border-radius:6px}
.opsi.cek .opsi-tanda::after{width:6px;height:11px;margin-top:-2px;border-radius:0;background:none;border:solid var(--di-atas-sinyal);border-width:0 2.5px 2.5px 0;transform:rotate(45deg) scale(0)}
.opsi.cek input:checked + .opsi-kotak .opsi-tanda::after{transform:rotate(45deg) scale(1)}
.opsi input:disabled + .opsi-kotak{border-style:dashed;background:var(--kartu-turun);cursor:not-allowed}
.opsi input:disabled + .opsi-kotak:hover{border-color:var(--garis)}
.opsi input:disabled + .opsi-kotak .opsi-nama,.opsi input:disabled + .opsi-kotak .opsi-tanda{opacity:.55}
.info-stylist{padding:10px 12px;border-left:3px solid var(--sinyal);background:var(--sinyal-lembut);border-radius:var(--r-kecil);color:var(--tinta)}
.opsi input:checked + .opsi-kotak{border-color:var(--sinyal);background:var(--sinyal-lembut)}
.opsi input:checked + .opsi-kotak .opsi-tanda{border-color:var(--sinyal);background:var(--sinyal)}
.opsi input:checked + .opsi-kotak .opsi-tanda::after{transform:scale(1)}
.opsi input:focus-visible + .opsi-kotak{outline:3px solid var(--fokus);outline-offset:2px}

.hari-strip{position:relative;display:flex;gap:8px;overflow-x:auto;margin:0 -16px;padding:4px 16px 12px;scroll-snap-type:x proximity;scrollbar-width:thin}
.hari{flex:0 0 70px;display:grid;place-content:center;min-height:80px;padding:6px 4px;border:2px solid var(--garis);border-radius:var(--r-kecil);background:var(--kartu);color:var(--tinta);font:inherit;text-align:center;line-height:1.2;cursor:pointer;scroll-snap-align:start}
.hari:hover:not(:disabled){border-color:var(--garis-kuat)}
.hari .hr{font-size:12px;font-weight:600;color:var(--tinta-redup)}
.hari .tg{font-size:24px;font-weight:800}
.hari .bl{font-size:12px;color:var(--tinta-redup)}
.hari[aria-pressed="true"]{border-color:var(--sinyal);background:var(--sinyal);color:var(--di-atas-sinyal)}
.hari[aria-pressed="true"] .hr,.hari[aria-pressed="true"] .bl{color:var(--di-atas-sinyal)}
.hari:disabled{border-style:dashed;cursor:not-allowed;opacity:.6}
.petunjuk{font-size:13px;color:var(--tinta-redup)}
.jam-label{margin:12px 0 10px;font-weight:700}
.jam-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px}
@media (min-width:480px){.jam-grid{grid-template-columns:repeat(4,minmax(0,1fr))}}
.jam-grid button{min-height:52px;border:2px solid var(--garis);border-radius:var(--r-kecil);background:var(--kartu);color:var(--tinta);font:inherit;font-weight:600;font-variant-numeric:tabular-nums;cursor:pointer}
.jam-grid button:hover:not(:disabled){border-color:var(--garis-kuat)}
.jam-grid button[aria-pressed="true"]{border-color:var(--sinyal);background:var(--sinyal);color:var(--di-atas-sinyal)}
.jam-grid button:disabled{border-style:dashed;background:transparent;color:var(--tinta-redup);text-decoration:line-through;cursor:not-allowed}

.kolom{display:grid;gap:6px;margin-top:14px}
.kolom label{font-weight:600}
.kolom input{min-height:52px;padding:0 14px;border:2px solid var(--garis-kuat);border-radius:var(--r-kecil);background:var(--kartu);color:var(--tinta);font:inherit;font-size:16px}
.kolom input::placeholder{color:var(--tinta-redup);opacity:.8}
.kolom input[aria-invalid="true"]{border-color:var(--salah)}
.kolom .bantu{font-size:14px;color:var(--tinta-redup)}
.kolom .salah{font-size:14px;font-weight:600;color:var(--salah)}

.tinjau{margin-top:4px}
.tinjau > div{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:0 12px;align-items:center;padding:10px 0;border-top:1px solid var(--garis)}
.tinjau > div:first-child{border-top:0}
.tinjau dt{grid-column:1;grid-row:1;font-size:13px;color:var(--tinta-redup)}
.tinjau dd{grid-column:1;grid-row:2;font-weight:700;overflow-wrap:anywhere;white-space:pre-line}
.tinjau .ubah{grid-column:2;grid-row:1 / 3;min-height:44px;padding:0 10px;border:0;border-radius:var(--r-tombol);background:transparent;color:var(--sinyal);font:inherit;font-weight:700;text-decoration:underline;text-underline-offset:3px;cursor:pointer}
.tinjau .ubah:hover{background:var(--sinyal-lembut)}
.tinjau .total,.tinjau .rw{padding:12px 0}
.tinjau .total dt,.tinjau .rw dt,.tinjau .total dd,.tinjau .rw dd{grid-row:1}
.tinjau .total dd,.tinjau .rw dd{grid-column:2;text-align:right}
.tinjau .total{border-top:2px solid var(--tinta)}
.tinjau .total dt{font-size:15px;font-weight:700;color:var(--tinta)}
.tinjau .total dd{font-size:20px}
.tinjau .rw dd{font-weight:600}

.qris{width:min(220px,60vw);aspect-ratio:1;margin:16px 0 8px;border:10px solid var(--kartu);outline:2px solid var(--tinta);background:repeating-conic-gradient(var(--tinta) 0 25%,var(--kartu) 0 50%) 0 0/22px 22px;position:relative}
.qris::after{content:"CONTOH";position:absolute;inset:0;display:grid;place-items:center;background:var(--kartu-turun);color:var(--salah);font-weight:800;letter-spacing:.14em}
.panel-bayar{margin-top:14px;padding:14px;border-radius:var(--r-kecil);background:var(--kartu-turun);font-size:14px}
.panel-bayar p + p{margin-top:8px}

.aksi-langkah{position:sticky;bottom:0;z-index:5;margin:20px -16px -16px;padding:12px 16px calc(12px + env(safe-area-inset-bottom));border-top:1px solid var(--garis);border-radius:0 0 var(--r) var(--r);background:var(--kartu)}
.ringkas-mini{margin-bottom:8px;overflow:hidden;font-size:14px;color:var(--tinta-redup);text-overflow:ellipsis;white-space:nowrap}
.ringkas-mini b{color:var(--tinta)}
.pesan-sistem{margin-bottom:8px;font-size:14px;font-weight:600;color:var(--salah)}
.pesan-sistem:empty{display:none}
.baris-aksi{display:grid;grid-template-columns:auto 1fr;gap:10px}
.baris-aksi .tombol{padding:0 16px}
#lanjut{white-space:nowrap}
.baris-aksi.tanpa-kembali{grid-template-columns:1fr}

.selesai h3{margin:14px 0 4px;font-size:26px;font-weight:var(--h-berat);font-stretch:var(--h-lebar);text-transform:var(--h-huruf);letter-spacing:var(--h-ls)}
.selesai h3:focus{outline:0}
.centang{display:grid;place-items:center;width:56px;height:56px;border-radius:50%;background:var(--sinyal);color:var(--di-atas-sinyal)}
.centang .ikon{width:28px;height:28px;stroke-width:3}
.kode{margin:6px 0 14px;font-size:30px;font-weight:800;font-variant-numeric:tabular-nums;letter-spacing:.06em}
.selesai .aksi{margin-top:18px}

.st-baris{display:flex;justify-content:space-between;align-items:center;gap:12px;margin-top:12px}
.st-label{font-weight:600}
.stepper{display:grid;grid-template-columns:52px minmax(44px,64px) 52px;align-items:center;flex:none;border:2px solid var(--garis-kuat);border-radius:var(--r-kecil);overflow:hidden}
.st-btn{min-height:52px;border:0;background:var(--kartu);color:var(--tinta);font:inherit;font-size:22px;font-weight:700;cursor:pointer}
.st-btn:hover:not(:disabled){background:var(--kartu-turun)}
.st-btn:disabled{color:var(--tinta-redup);cursor:not-allowed}
.st-nilai{display:block;min-height:52px;border-left:2px solid var(--garis-kuat);border-right:2px solid var(--garis-kuat);background:var(--kartu);color:var(--tinta);font:inherit;font-weight:700;text-align:center;line-height:52px}
.menu-baris{display:flex;justify-content:space-between;align-items:center;gap:12px;min-height:64px;padding:12px 14px;border:2px solid var(--garis);border-radius:var(--r-kecil);background:var(--kartu)}
.menu-baris.aktif{border-color:var(--sinyal);background:var(--sinyal-lembut)}
.menu-info{display:grid;gap:2px;min-width:0}
.menu-info .opsi-nama,.menu-info .opsi-harga,.menu-info .opsi-ket{grid-column:auto;grid-row:auto}
.menu-sub{font-size:14px;font-weight:700;color:var(--sinyal-gelap)}
.kolom textarea{min-height:88px;padding:12px 14px;border:2px solid var(--garis-kuat);border-radius:var(--r-kecil);background:var(--kartu);color:var(--tinta);font:inherit;font-size:16px;resize:vertical}
"""

INDEX_TOKENS = """
  --latar:#F4F1E9;
  --kartu:#FFFFFF;
  --kartu-turun:#E9E5D9;
  --tinta:#16221E;
  --tinta-redup:#4A5852;
  --garis:#DAD5C6;
  --garis-kuat:#7C877F;
  --sinyal:#B03A18;
  --sinyal-gelap:#8F2E12;
  --sinyal-lembut:#FBE3DA;
  --di-atas-sinyal:#FFFFFF;
  --fokus:#B03A18;
  --hijau:#16221E;
  --krem:#F4F1E9;
  --krem-redup:#A9B8B0;
  --garis-hijau:#2A3A35;
  --jingga:#F57A4E;
  --ok:#2F6B4F;
  --r:20px;
  --r-kecil:14px;
  --r-tombol:999px;
"""

INDEX = """
.atas.atas-hijau{border-bottom-color:var(--garis-hijau)}
.merek{display:inline-flex;align-items:baseline;gap:10px;min-height:44px;padding:8px 0;text-decoration:none;font-weight:800;font-size:18px}
.merek span{font-weight:500;font-size:14px;opacity:.75}
.atas-hijau{background:var(--hijau);color:var(--krem)}
.hero{background:var(--hijau);color:var(--krem);padding:20px 0 40px}
.hero .eyebrow{color:var(--krem-redup)}
.hero h1{margin:10px 0 16px;font-size:clamp(38px,11.5vw,68px);font-weight:800;font-stretch:78%;letter-spacing:-.01em;line-height:1}
.hero .lead{color:var(--krem-redup);font-size:17px;max-width:52ch}
.hero .aksi{margin-top:24px}
.hero .tombol{background:var(--jingga);border-color:var(--jingga);color:var(--hijau)}
.hero .tombol:hover{background:var(--krem);border-color:var(--krem)}
.hero .tombol.garis{background:transparent;border-color:var(--krem-redup);color:var(--krem)}
.hero .tombol.garis:hover{background:var(--garis-hijau);border-color:var(--krem)}
.tombol .ikon{width:18px;height:18px}
.fitur{display:flex;flex-wrap:wrap;gap:8px;margin-top:22px}
.fitur li{display:inline-flex;align-items:center;gap:8px;padding:8px 14px;border:1px solid var(--garis-hijau);border-radius:999px;font-size:14px}
.fitur .ikon{width:16px;height:16px;color:var(--jingga)}
.bagian{padding:40px 0 8px}
.bagian h2{font-size:clamp(28px,7.5vw,40px);font-weight:800;font-stretch:80%;line-height:1.05;letter-spacing:-.005em;text-wrap:balance}
.atas-hijau .balik{margin-left:auto;margin-right:-6px;color:var(--krem)}
.atas-hijau .balik:hover{background:var(--garis-hijau)}
.jenis-daftar{display:grid;gap:14px;margin-top:20px}
@media (min-width:700px){.jenis-daftar{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (min-width:1000px){.jenis-daftar{grid-template-columns:repeat(3,minmax(0,1fr))}}
.jenis-kartu{display:flex;flex-direction:column;gap:12px;height:100%;padding:20px;border:1px solid var(--garis);border-radius:var(--r);background:var(--kartu)}
.jenis-ikon{display:grid;place-items:center;width:48px;height:48px;border-radius:var(--r-kecil);background:var(--sinyal-lembut);color:var(--sinyal)}
.jenis-ikon .ikon{width:24px;height:24px}
.jenis-kartu h3{font-size:24px;font-weight:800;font-stretch:80%;line-height:1.1}
.jenis-kartu p{color:var(--tinta-redup)}
.jenis-kartu .tombol{margin-top:auto}
.nama-demo{margin-top:12px;font-size:14px;color:var(--tinta-redup)}
.nama-demo b{color:var(--tinta)}
.paket-daftar{display:grid;gap:16px;margin-top:20px}
@media (min-width:900px){.paket-daftar{grid-template-columns:repeat(3,minmax(0,1fr));align-items:stretch}.wadah-lebar{max-width:1040px}}
.paket article{display:flex;flex-direction:column;gap:14px;height:100%;padding:20px;border:1px solid var(--garis);border-radius:var(--r);background:var(--kartu)}
.paket .no{display:inline-block;padding:3px 11px;border-radius:999px;background:var(--sinyal-lembut);color:var(--sinyal);font-size:13px;font-weight:700}
.paket h3{margin-top:10px;font-size:26px;font-weight:800;font-stretch:80%;line-height:1.05}
.paket .ket{color:var(--tinta-redup)}
.paket .cocok{padding:12px 14px;border-radius:var(--r-kecil);background:var(--kartu-turun);font-size:14px}
.paket .isi{display:grid;gap:10px;font-size:15px}
.paket .isi li{display:grid;grid-template-columns:auto 1fr;gap:10px;align-items:start}
.paket .isi .ikon{width:18px;height:18px;margin-top:3px;color:var(--ok);stroke-width:3}
.paket .bawah{display:grid;gap:10px;margin-top:auto;padding-top:6px}
.harga-tag{font-size:13px;color:var(--tinta-redup);text-align:center}
.harga{display:grid;gap:4px;padding:14px 0;border-top:1px solid var(--garis);border-bottom:1px solid var(--garis)}
.harga-label{font-size:13px;font-weight:700;color:var(--tinta-redup)}
.harga-angka{font-size:34px;font-weight:800;font-stretch:80%;line-height:1.05;color:var(--tinta)}
.harga-ket{font-size:14px;color:var(--tinta-redup)}
.beda{padding-bottom:12px}
.catatan-harga{margin-top:16px;font-size:14px;color:var(--tinta-redup);max-width:60ch}
.kartu-hubungi{padding:24px 20px;border-radius:var(--r);background:var(--hijau);color:var(--krem)}
.kartu-hubungi .bagian-lead{color:var(--krem-redup)}
.kartu-hubungi .tombol{background:var(--jingga);border-color:var(--jingga);color:var(--hijau)}
.kartu-hubungi .tombol:hover{background:var(--krem);border-color:var(--krem)}
@media (min-width:700px){.hero .aksi,.kartu-hubungi .aksi{display:flex;flex-wrap:wrap}}
.alamat-banding{display:grid;gap:12px;margin-top:20px}
@media (min-width:700px){.alamat-banding{grid-template-columns:1fr 1fr}}
.alamat-pil{display:grid;gap:4px;align-content:start;padding:16px 18px;border-radius:var(--r);font-size:14px;overflow-wrap:anywhere}
.alamat-pil b{font-size:19px;font-weight:700}
.alamat-label{font-size:13px;font-weight:700}
.alamat-pil.redup{background:var(--kartu-turun);color:var(--tinta-redup)}
.alamat-pil.redup b{text-decoration:line-through;text-decoration-thickness:1px}
.alamat-pil.unggul{background:var(--hijau);color:var(--krem)}
.alamat-pil.unggul b{color:var(--jingga)}
.alamat-pil.unggul span:last-child{color:var(--krem-redup)}
.banding{width:100%;margin-top:20px;border-collapse:separate;border-spacing:0;border:1px solid var(--garis);border-radius:var(--r);background:var(--kartu);overflow:hidden;font-size:14px}
.banding th,.banding td{padding:12px 14px;text-align:left;vertical-align:top;width:50%}
.banding th{font-size:14px;background:var(--kartu-turun);color:var(--tinta-redup)}
.banding th + th{background:var(--hijau);color:var(--krem)}
.banding td{border-top:1px solid var(--garis);color:var(--tinta-redup)}
.banding td + td{color:var(--tinta);font-weight:600;border-left:1px solid var(--garis)}
.beda-tutup{margin-top:16px;max-width:60ch;font-weight:600}
.kaki{margin-top:40px;padding:28px 0 36px;border-top:1px solid var(--garis);font-size:14px;color:var(--tinta-redup)}
.kaki p + p{margin-top:10px}
.kaki a{display:inline-flex;align-items:center;min-height:44px;color:var(--tinta);font-weight:600}
body{padding-bottom:0}
"""

ERR = """
html{background:var(--hijau)}
body{display:flex;flex-direction:column;min-height:100vh;min-height:100dvh;background:var(--hijau);color:var(--krem);padding-bottom:0}
main{flex:1;display:flex}
.galat{flex:1;display:flex;align-items:center;padding:32px 0 24px}
.galat .wadah{max-width:640px}
.kode-galat{display:block;font-size:clamp(104px,34vw,208px);font-weight:800;font-stretch:78%;line-height:.86;letter-spacing:-.02em;color:transparent;-webkit-text-stroke:2px var(--jingga);user-select:none}
.galat h1{margin:18px 0 12px;font-size:clamp(30px,8.5vw,48px);font-weight:800;font-stretch:80%;line-height:1.04;text-wrap:balance}
.galat .lead{margin:0;max-width:46ch;color:var(--krem-redup);font-size:17px}
.galat .aksi{margin-top:24px}
.galat .tombol{background:var(--jingga);border-color:var(--jingga);color:var(--hijau)}
.galat .tombol:hover{background:var(--krem);border-color:var(--krem)}
.galat .tombol.garis{background:transparent;border-color:var(--krem-redup);color:var(--krem)}
.galat .tombol.garis:hover{background:var(--garis-hijau);border-color:var(--krem)}
.galat .tombol.garis:focus-visible,.galat .tombol:focus-visible,.alternatif a:focus-visible{outline-color:var(--jingga)}
.alternatif{margin-top:32px;padding-top:20px;border-top:1px solid var(--garis-hijau)}
.alternatif h2{font-size:13px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--krem-redup)}
.alternatif ul{margin-top:8px}
.alternatif li + li{border-top:1px solid var(--garis-hijau)}
.alternatif a{display:flex;justify-content:space-between;align-items:center;gap:12px;min-height:56px;font-weight:600;text-decoration:none}
.alternatif a:hover{color:var(--jingga)}
.kaki{margin-top:0;border-top-color:var(--garis-hijau);color:var(--krem-redup)}
.kaki a{color:var(--krem)}
"""
