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

BASE = """
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%;scroll-padding-top:72px;background:var(--latar);accent-color:var(--sinyal)}
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
.catatan-demo{display:flex;gap:10px;align-items:flex-start;margin-top:20px;padding:12px 14px;border-radius:var(--r-kecil);background:var(--sinyal-lembut);font-size:14px}
.tanda-contoh{flex:none;padding:2px 9px;border-radius:999px;background:var(--sinyal);color:var(--di-atas-sinyal);font-size:12px;font-weight:700;letter-spacing:.04em;text-transform:uppercase}
.paket-nav{margin-top:22px}
.paket-nav p{font-size:13px;font-weight:600;color:var(--tinta-redup);margin-bottom:6px}
.paket-nav ul{display:grid;grid-template-columns:repeat(3,1fr);gap:4px;padding:4px;border:1px solid var(--garis);border-radius:var(--r-kecil);background:var(--kartu)}
.paket-nav a{display:grid;place-content:center;min-height:52px;padding:4px 6px;border-radius:calc(var(--r-kecil) - 4px);text-align:center;text-decoration:none;line-height:1.2}
.paket-nav a b{display:block;font-size:13px;color:var(--tinta-redup)}
.paket-nav a span{font-weight:700}
.paket-nav a:hover{background:var(--kartu-turun)}
.paket-nav a[aria-current="page"]{background:var(--tinta);color:var(--latar)}
.paket-nav a[aria-current="page"] b{color:var(--latar)}
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
.petak{display:flex;align-items:flex-end;aspect-ratio:4/3;padding:10px;border:1px dashed var(--garis-kuat);border-radius:var(--r-kecil);background:var(--kartu-turun);font-size:13px;color:var(--tinta-redup)}
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
.pesan{padding:16px 16px 16px;scroll-margin-top:68px}
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
.tinjau dd{grid-column:1;grid-row:2;font-weight:700;overflow-wrap:anywhere}
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
.fitur{display:flex;flex-wrap:wrap;gap:8px;margin-top:22px}
.fitur li{display:inline-flex;align-items:center;gap:8px;padding:8px 14px;border:1px solid var(--garis-hijau);border-radius:999px;font-size:14px}
.fitur .ikon{width:16px;height:16px;color:var(--jingga)}
.bagian{padding:40px 0 8px}
.bagian h2{font-size:clamp(28px,7.5vw,40px);font-weight:800;font-stretch:80%;line-height:1.05;letter-spacing:-.005em;text-wrap:balance}
.pilih-usaha{display:grid;grid-template-columns:1fr 1fr;gap:6px;margin-top:20px;padding:6px;border:1px solid var(--garis);border-radius:var(--r-kecil);background:var(--kartu)}
.pilih-usaha button{min-height:56px;padding:0 8px;border:0;border-radius:calc(var(--r-kecil) - 4px);background:transparent;color:var(--tinta);font:inherit;font-weight:700;cursor:pointer}
.pilih-usaha button:hover{background:var(--kartu-turun)}
.pilih-usaha button[aria-pressed="true"]{background:var(--hijau);color:var(--krem)}
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
.catatan-akhir{margin-top:24px;font-size:14px;color:var(--tinta-redup);max-width:60ch}
.kaki{margin-top:40px;padding:28px 0 36px;border-top:1px solid var(--garis);font-size:14px;color:var(--tinta-redup)}
.kaki p + p{margin-top:10px}
.kaki a{display:inline-flex;align-items:center;min-height:44px;color:var(--tinta);font-weight:600}
body{padding-bottom:0}
"""
