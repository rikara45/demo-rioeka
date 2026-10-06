FONT_ALFA = "@font-face{font-family:'Alfa Slab One';font-style:normal;font-weight:400;font-display:swap;src:url(/font/alfa-slab-one-latin.woff2) format('woff2')}"
FONT_FAMILJEN = "@font-face{font-family:'Familjen Grotesk';font-style:normal;font-weight:400 700;font-display:swap;src:url(/font/familjen-grotesk-latin.woff2) format('woff2')}"
FONT_MONO = ("@font-face{font-family:'Space Mono';font-style:normal;font-weight:400;font-display:swap;src:url(/font/space-mono-latin-400.woff2) format('woff2')}\n"
             "@font-face{font-family:'Space Mono';font-style:normal;font-weight:700;font-display:swap;src:url(/font/space-mono-latin-700.woff2) format('woff2')}")
FONT_BOWLBY = "@font-face{font-family:'Bowlby One';font-style:normal;font-weight:400;font-display:swap;src:url(/font/bowlby-one-latin.woff2) format('woff2')}"

TEMA_POSTER = """
  --latar:#F2E4C9;
  --kartu:#FBF3E2;
  --kartu-turun:#E8D6B4;
  --tinta:#2B1708;
  --tinta-redup:#6B4A2A;
  --garis:#D6BE94;
  --garis-halus:#E3CFAC;
  --garis-kuat:#8A6A42;
  --sinyal:#B23A1B;
  --sinyal-gelap:#8C2A11;
  --sinyal-lembut:#F4D9C9;
  --di-atas-sinyal:#FFF6E9;
  --fokus:#B23A1B;
  --salah:#9C2410;
  --ok:#3E6B3A;
  --r:2px;
  --r-kecil:2px;
  --r-tombol:2px;
  --lengkung:999px;
  --serif:"Alfa Slab One",Georgia,serif;
  --bayang:0 2px 0 rgba(43,23,8,.25);
  --h-berat:400;
  --h-lebar:100%;
  --h-huruf:uppercase;
  --h-ls:.01em;
  --pole-tinggi:14px;
  --pole:repeating-linear-gradient(45deg,#B23A1B 0 10px,#F2E4C9 10px 20px,#2B1708 20px 30px,#F2E4C9 30px 40px);
"""

GAYA_POSTER = r"""
[data-s=poster]{background-image:repeating-linear-gradient(0deg,rgba(43,23,8,.05) 0 1px,transparent 1px 3px)}
[data-s=poster] :is(.hero h1,.bagian h2,.panel h3,.selesai h3,#harga .kartu > h3,.kartu.pesan-buka > h3,.f-nilai,.harga .hr,.hari .tg,.tinjau .total dd,.kode,.penutup h2,.lencana){font-family:var(--serif);font-weight:400;font-stretch:100%;text-transform:uppercase;letter-spacing:.01em}
[data-s=poster] .hero{padding:22px 0 4px}
[data-s=poster] .hero-isi{position:relative;padding:16px;border:3px solid var(--tinta);outline:1px solid var(--tinta);outline-offset:4px;background:var(--kartu)}
[data-s=poster] .hero-isi::before{display:none}
[data-s=poster] .hero .eyebrow{display:inline-block;padding:3px 8px;background:var(--tinta);color:var(--latar);font-family:'Space Mono',monospace;font-size:12px;letter-spacing:.12em}
[data-s=poster] .hero h1{margin:12px 0 8px;font-size:clamp(34px,11vw,64px);line-height:.95}
[data-s=poster] .hero h1 em{font-style:normal}
[data-s=poster] .hero .lead{max-width:42ch}
[data-s=poster] .hero-foto{position:relative;margin:18px 0 28px;border:3px solid var(--tinta)}
[data-s=poster] .hero-foto img{display:block;width:100%;height:auto;aspect-ratio:4/3;object-fit:cover;filter:sepia(.35) contrast(1.15) saturate(.85)}
[data-s=poster] .lencana{position:absolute;left:50%;bottom:-18px;transform:translateX(-50%);display:grid;place-content:center;min-width:104px;padding:6px 12px;border:2px solid var(--tinta);background:var(--sinyal);color:var(--di-atas-sinyal);font-size:13px}
[data-s=poster] .status{border:2px solid var(--tinta);border-radius:0;background:var(--kartu);font-family:'Space Mono',monospace;font-size:13px}
[data-s=poster] .fakta{gap:0;margin-top:22px;border:2px solid var(--tinta)}
[data-s=poster] .fakta li{padding:12px 10px;border:0;border-radius:0;background:var(--kartu)}
[data-s=poster] .fakta li + li{border-left:2px solid var(--tinta)}
[data-s=poster] .fakta .f-label{font-family:'Space Mono',monospace;font-size:11px;color:var(--tinta-redup)}
[data-s=poster] .fakta .f-nilai{font-size:clamp(15px,4.4vw,20px);line-height:1.1}
[data-s=poster] .loncat a{border:2px solid var(--tinta);border-radius:0;background:var(--kartu)}
[data-s=poster] .loncat a:hover{background:var(--sinyal);border-color:var(--sinyal);color:var(--di-atas-sinyal)}
[data-s=poster] .demo-kartu{border:2px solid var(--tinta);border-radius:0;background:var(--kartu-turun)}
[data-s=poster] .bagian{padding:48px 0 4px}
[data-s=poster] .bagian h2{font-size:clamp(28px,8.5vw,42px);line-height:1}
[data-s=poster] .bagian:not(.penutup) h2::after{content:"";display:block;width:100%;max-width:120px;height:10px;margin-top:12px;background:repeating-linear-gradient(90deg,var(--sinyal) 0 6px,transparent 6px 12px)}
[data-s=poster] .bagian-lead{margin-top:12px}
[data-s=poster] .kartu{border:2px solid var(--tinta);border-radius:0;box-shadow:none}
[data-s=poster] #harga .kartu{margin-top:24px;padding:14px 14px 6px;background:var(--kartu)}
[data-s=poster] #harga .kartu > h3{padding-bottom:8px;border-bottom:3px double var(--tinta);font-size:22px;text-align:center}
[data-s=poster] .harga li{grid-template-columns:minmax(0,1fr) auto;padding:11px 0;border-top:1px dashed var(--garis-kuat)}
[data-s=poster] .harga li:first-child{border-top:0}
[data-s=poster] .harga .nm{display:flex;align-items:baseline;gap:8px;font-weight:700}
[data-s=poster] .harga .nm::after{content:"";flex:1;min-width:16px;border-bottom:2px dotted var(--garis-kuat);transform:translateY(-3px)}
[data-s=poster] .harga .hr{font-family:var(--serif);font-size:19px;color:var(--sinyal-gelap)}
[data-s=poster] .harga .ket{grid-column:1 / -1}
[data-s=poster] .dur{display:inline;margin:0;padding:0;background:none;color:var(--tinta-redup);font-family:'Space Mono',monospace;font-size:13px;font-weight:400}
[data-s=poster] .dur + .ket-teks::before{content:"\00A0\00B7\00A0"}
[data-s=poster] .galeri{grid-template-columns:repeat(2,minmax(0,1fr));gap:16px 12px;margin-top:26px}
[data-s=poster] .petak{aspect-ratio:3/4;border:3px solid var(--tinta);border-radius:var(--lengkung);background:var(--kartu)}
[data-s=poster] .petak img{filter:sepia(.4) contrast(1.15) grayscale(.3)}
[data-s=poster] .petak figcaption{padding:4px 6px;font-family:'Space Mono',monospace;font-size:12px;line-height:1.3;color:var(--tinta-redup);text-align:center}
[data-s=poster] .petak:nth-child(even){border-radius:2px}
[data-s=poster] .petak:first-child,[data-s=poster] .petak:last-child{grid-column:1 / -1;aspect-ratio:16/10;border-radius:2px}
[data-s=poster] .jam li{padding:12px 10px;border-radius:0}
[data-s=poster] .jam li.hari-ini{background:var(--sinyal);color:var(--di-atas-sinyal)}
[data-s=poster] .jam li.hari-ini .tanda-hari{background:var(--di-atas-sinyal);color:var(--sinyal-gelap)}
[data-s=poster] .tanya{border-bottom:3px double var(--tinta)}
[data-s=poster] .tanya details{border-top:1px solid var(--tinta)}
[data-s=poster] .tanya summary{min-height:58px;font-family:var(--serif);font-size:17px}
[data-s=poster] .tanya summary::after{content:"+";margin-left:auto;color:var(--sinyal-gelap)}
[data-s=poster] .tanya summary svg{display:none}
[data-s=poster] .tanya details[open] summary::after{content:"\2212"}
[data-s=poster] .penutup .kartu{border:3px double var(--tinta);background:var(--kartu-turun)}
[data-s=poster] .penutup h2{font-size:clamp(26px,8vw,38px)}
"""

GAYA_POSTER_WIZARD = r"""
[data-s=poster] .kartu.pesan,[data-s=poster] .kartu.pesan-buka{border:2px solid var(--tinta);background:var(--kartu)}
[data-s=poster] .kartu.pesan-buka > h3{font-size:26px;line-height:1}
[data-s=poster] .panel h3{font-size:28px;line-height:1}
[data-s=poster] .langkah-no{font-family:'Space Mono',monospace;color:var(--tinta-redup)}
[data-s=poster] .progres{height:8px;border-radius:0;background:var(--kartu-turun)}
[data-s=poster] .progres i{border-radius:0}
[data-s=poster] .sub{color:var(--sinyal-gelap)}
[data-s=poster] .opsi-kotak{border-width:2px;border-radius:0}
[data-s=poster] .opsi input:checked + .opsi-kotak{border-color:var(--sinyal);background:var(--sinyal-lembut)}
[data-s=poster] .opsi-nama{font-weight:700}
[data-s=poster] .opsi-harga{font-family:var(--serif);font-size:16px;color:var(--sinyal-gelap)}
[data-s=poster] .panel[data-langkah=bayar] .opsi-harga{font-family:'Space Mono',monospace;font-size:13px}
[data-s=poster] .hari{border-radius:0}
[data-s=poster] .hari .tg{font-size:22px}
[data-s=poster] .jam-grid button{border-radius:0}
[data-s=poster] .stepper{border-radius:0}
[data-s=poster] .kolom input,[data-s=poster] .kolom textarea{border-radius:0}
[data-s=poster] .tinjau .total{border-top:3px double var(--tinta)}
[data-s=poster] .tinjau .total dd{font-size:26px}
[data-s=poster] .selesai h3{font-size:30px}
[data-s=poster] .kode{font-family:'Space Mono',monospace;font-size:34px;letter-spacing:.1em;color:var(--sinyal-gelap)}
"""

TEMA_LEMBAR = """
  --latar:#FFFFFF;
  --kartu:#F7F9F4;
  --kartu-turun:#E9EFE2;
  --tinta:#14210F;
  --tinta-redup:#4C5A45;
  --garis:#D6DECB;
  --garis-halus:#E4EADC;
  --garis-kuat:#7C8A72;
  --sinyal:#527E14;
  --sinyal-gelap:#33530A;
  --sinyal-lembut:#EAF3D6;
  --di-atas-sinyal:#FFFFFF;
  --fokus:#33530A;
  --salah:#9C2410;
  --ok:#3E6B3A;
  --r:0px;
  --r-kecil:0px;
  --r-tombol:0px;
  --lengkung:0px;
  --serif:"Familjen Grotesk",system-ui,sans-serif;
  --bayang:none;
  --h-berat:700;
  --h-lebar:100%;
  --h-huruf:uppercase;
  --h-ls:-.01em;
  --pole-tinggi:0px;
  --pole:none;
"""

GAYA_LEMBAR = r"""
[data-s=lembar] :is(.hero h1,.bagian h2,.panel h3,.selesai h3,#harga .kartu > h3,.kartu.pesan-buka > h3,.harga .hr,.hari .tg,.tinjau .total dd,.kode,.penutup h2,.lencana){font-family:var(--serif);font-stretch:100%}
[data-s=lembar] :is(.eyebrow,.f-label,.langkah-no,.dur,.harga .nm::before,.petak figcaption,.sub,.tag-anda){font-family:'Space Mono',monospace}
[data-s=lembar] .hero{padding:20px 0 4px}
[data-s=lembar] .hero-isi{position:relative;padding-left:18px;border-left:8px solid var(--sinyal)}
[data-s=lembar] .hero-isi::before{display:none}
[data-s=lembar] .hero .eyebrow{font-size:11px;letter-spacing:.14em;color:var(--sinyal-gelap)}
[data-s=lembar] .hero h1{margin:10px 0 10px;font-size:clamp(32px,10.5vw,58px);font-weight:700;line-height:.98;letter-spacing:-.02em}
[data-s=lembar] .hero h1 em{font-style:normal;color:var(--sinyal-gelap)}
[data-s=lembar] .hero .lead{max-width:44ch}
[data-s=lembar] .hero-foto{position:relative;float:right;width:38%;max-width:190px;margin:6px 0 12px 16px;border:1px solid var(--tinta)}
[data-s=lembar] .hero-foto img{display:block;width:100%;height:auto;aspect-ratio:1;object-fit:cover}
[data-s=lembar] .lencana{margin-top:6px;font-family:'Space Mono',monospace;font-size:11px;letter-spacing:.08em;color:var(--tinta-redup)}
[data-s=lembar] .status{border:1px solid var(--garis-kuat);border-radius:0;background:var(--kartu);font-family:'Space Mono',monospace;font-size:13px}
[data-s=lembar] .fakta{gap:0;margin-top:20px;border:1px solid var(--tinta)}
[data-s=lembar] .fakta li{padding:10px;border:0;border-radius:0;background:var(--kartu)}
[data-s=lembar] .fakta li + li{border-left:1px solid var(--garis-kuat)}
[data-s=lembar] .fakta .f-label{font-size:11px;color:var(--tinta-redup)}
[data-s=lembar] .fakta .f-nilai{font-family:var(--serif);font-size:clamp(15px,4.4vw,19px);font-weight:700;line-height:1.1}
[data-s=lembar] .loncat a{border:1px solid var(--tinta);border-radius:0;background:var(--kartu)}
[data-s=lembar] .loncat a:hover{background:var(--sinyal);border-color:var(--sinyal);color:var(--di-atas-sinyal)}
[data-s=lembar] .demo-kartu{border:1px solid var(--tinta);border-radius:0;background:var(--kartu)}
[data-s=lembar] .bagian{padding:44px 0 4px}
[data-s=lembar] .bagian h2{font-size:clamp(26px,8vw,38px);font-weight:700;line-height:1}
[data-s=lembar] .bagian:not(.penutup) h2::before{content:"";display:inline-block;width:14px;height:14px;margin-right:10px;background:var(--sinyal)}
[data-s=lembar] .bagian-lead{margin-top:10px}
[data-s=lembar] .kartu{border:1px solid var(--garis);border-radius:0;box-shadow:none}
[data-s=lembar] #harga .kartu{margin-top:22px;padding:0;border:1px solid var(--tinta);background:var(--kartu)}
[data-s=lembar] #harga .kartu > h3{padding:10px;background:var(--tinta);color:var(--latar);font-size:13px;font-weight:700;letter-spacing:.08em;text-transform:uppercase}
[data-s=lembar] #harga .harga{margin:0;counter-reset:n}
[data-s=lembar] .harga li{grid-template-columns:34px minmax(0,1fr) auto auto;align-items:baseline;gap:2px 10px;padding:12px 10px;border-top:1px solid var(--garis)}
[data-s=lembar] .harga li:first-child{border-top:0}
[data-s=lembar] .harga li::before{counter-increment:n;content:counter(n,decimal-leading-zero);grid-column:1;grid-row:1;font-family:'Space Mono',monospace;font-size:13px;color:var(--sinyal-gelap)}
[data-s=lembar] .harga .nm{grid-column:2;font-weight:700}
[data-s=lembar] .harga .hr{grid-column:3;grid-row:1;font-family:'Space Mono',monospace;font-size:15px;font-weight:700;white-space:nowrap}
[data-s=lembar] .harga .ket{grid-column:2 / -1}
[data-s=lembar] .dur{display:none}
[data-s=lembar] .harga .ket-teks{display:block;font-family:'Space Mono',monospace;font-size:12px;color:var(--tinta-redup)}
[data-s=lembar] .harga .ket:empty{display:none}
[data-s=lembar] .galeri{grid-template-columns:repeat(2,minmax(0,1fr));gap:0;margin-top:24px;border:1px solid var(--tinta);background:var(--tinta)}
[data-s=lembar] .petak{aspect-ratio:4/3;border:8px solid var(--tinta);border-radius:0;background:var(--kartu-turun)}
[data-s=lembar] .petak img{filter:grayscale(1) contrast(1.05)}
[data-s=lembar] .petak figcaption{font-size:12px;color:var(--tinta-redup);padding-top:4px}
[data-s=lembar] .galeri{counter-reset:fr}
[data-s=lembar] .petak{counter-increment:fr;position:relative}
[data-s=lembar] .petak::before{content:"F" counter(fr,decimal-leading-zero);position:absolute;z-index:1;top:-8px;left:-8px;padding:2px 5px;background:var(--sinyal);color:var(--di-atas-sinyal);font-family:'Space Mono',monospace;font-size:10px}
[data-s=lembar] .petak:first-child,[data-s=lembar] .petak:last-child{grid-column:1 / -1;aspect-ratio:16/9}
[data-s=lembar] .jam li{padding:12px 10px;border-radius:0}
[data-s=lembar] .jam li.hari-ini{background:var(--sinyal-lembut);box-shadow:inset 4px 0 0 var(--sinyal)}
[data-s=lembar] .tanya{border-bottom:1px solid var(--tinta)}
[data-s=lembar] .tanya details{border-top:1px solid var(--garis)}
[data-s=lembar] .tanya summary{min-height:56px;font-family:var(--serif);font-size:18px;font-weight:700}
[data-s=lembar] .tanya summary svg{display:none}
[data-s=lembar] .tanya summary::after{content:"[ + ]";margin-left:auto;font-family:'Space Mono',monospace;font-size:13px;color:var(--sinyal-gelap)}
[data-s=lembar] .tanya details[open] summary::after{content:"[ \2212 ]"}
[data-s=lembar] .penutup .kartu{border:1px solid var(--tinta);background:var(--sinyal-lembut)}
[data-s=lembar] .penutup h2{font-size:clamp(24px,7.5vw,34px)}
@supports (animation-timeline:view()){
@media (prefers-reduced-motion:no-preference){
@keyframes lmb{from{opacity:0}to{opacity:1}}
[data-s=lembar] .petak{animation:lmb linear both;animation-timeline:view();animation-range:entry 0% entry 60%}
}
}
"""

GAYA_LEMBAR_WIZARD = r"""
[data-s=lembar] .kartu.pesan,[data-s=lembar] .kartu.pesan-buka{border:1px solid var(--tinta);background:var(--kartu)}
[data-s=lembar] .kartu.pesan-buka > h3{font-size:24px;line-height:1}
[data-s=lembar] .panel h3{font-size:24px;line-height:1}
[data-s=lembar] .langkah-no{font-size:12px;letter-spacing:.1em;color:var(--sinyal-gelap)}
[data-s=lembar] .progres{height:6px;border-radius:0;background:var(--kartu-turun)}
[data-s=lembar] .progres i{border-radius:0}
[data-s=lembar] .sub{color:var(--sinyal-gelap)}
[data-s=lembar] .opsi-kotak{border-width:1px;border-radius:0}
[data-s=lembar] .opsi input:checked + .opsi-kotak{border-color:var(--sinyal);box-shadow:inset 4px 0 0 var(--sinyal)}
[data-s=lembar] .opsi-nama{font-weight:700}
[data-s=lembar] .opsi-harga{font-family:'Space Mono',monospace;font-size:14px;color:var(--sinyal-gelap)}
[data-s=lembar] .panel[data-langkah=bayar] .opsi-harga{font-size:13px}
[data-s=lembar] .hari{border-radius:0;font-family:'Space Mono',monospace}
[data-s=lembar] .hari .tg{font-size:22px}
[data-s=lembar] .jam-grid button{border-radius:0;font-family:'Space Mono',monospace}
[data-s=lembar] .stepper{border-radius:0}
[data-s=lembar] .st-nilai{font-family:'Space Mono',monospace}
[data-s=lembar] .kolom input,[data-s=lembar] .kolom textarea{border-radius:0}
[data-s=lembar] .tinjau .total{border-top:2px solid var(--tinta)}
[data-s=lembar] .tinjau .total dd{font-size:24px}
[data-s=lembar] .selesai h3{font-size:28px}
[data-s=lembar] .kode{font-family:'Space Mono',monospace;font-size:34px;letter-spacing:.08em;color:var(--sinyal-gelap)}
"""

TEMA_STIKER = """
  --latar:#DCDAD3;
  --kartu:#F2F1EC;
  --kartu-turun:#C9C7BE;
  --tinta:#191813;
  --tinta-redup:#4F4D44;
  --garis:#A9A79D;
  --garis-halus:#BEBCB2;
  --garis-kuat:#5E5C52;
  --sinyal:#E8DE17;
  --sinyal-gelap:#57520A;
  --sinyal-lembut:#F6F2C4;
  --di-atas-sinyal:#191813;
  --fokus:#57520A;
  --salah:#B01B0E;
  --ok:#2F6B4F;
  --r:6px;
  --r-kecil:4px;
  --r-tombol:4px;
  --lengkung:999px;
  --serif:"Bowlby One",system-ui,sans-serif;
  --bayang:3px 3px 0 rgba(25,24,19,.35);
  --h-berat:400;
  --h-lebar:100%;
  --h-huruf:uppercase;
  --h-ls:0;
  --pole-tinggi:0px;
  --pole:none;
"""

GAYA_STIKER = r"""
[data-s=stiker]{background-image:radial-gradient(circle at 20% 30%,rgba(25,24,19,.05) 0 1px,transparent 1px),radial-gradient(circle at 70% 60%,rgba(25,24,19,.05) 0 1px,transparent 1px);background-size:22px 22px,26px 26px}
[data-s=stiker] :is(.hero h1,.bagian h2,.penutup h2,.lencana){font-family:var(--serif);font-weight:400;font-stretch:100%;letter-spacing:0;text-transform:uppercase;line-height:.95}
[data-s=stiker] .hero{padding:22px 0 4px}
[data-s=stiker] .hero-isi{position:relative;padding:18px 14px;background:var(--kartu);border:2px solid var(--tinta);box-shadow:6px 6px 0 var(--tinta);rotate:-.6deg}
[data-s=stiker] .hero-isi::before{display:none}
[data-s=stiker] .hero .eyebrow{display:inline-block;padding:3px 9px;background:var(--sinyal);color:var(--di-atas-sinyal);border:2px solid var(--tinta);font-weight:700;font-size:12px;letter-spacing:.06em;rotate:-1.5deg}
[data-s=stiker] .hero h1{margin:12px 0 10px;font-size:clamp(32px,10.5vw,60px)}
[data-s=stiker] .hero h1 em{font-style:normal;color:var(--di-atas-sinyal);background:var(--sinyal);padding:0 .12em;box-shadow:2px 2px 0 var(--tinta);-webkit-box-decoration-break:clone;box-decoration-break:clone}
[data-s=stiker] .hero .lead{max-width:42ch}
[data-s=stiker] .hero-foto{position:relative;margin:20px 8px 30px 0;border:3px solid var(--tinta);background:var(--kartu);box-shadow:6px 6px 0 var(--tinta);rotate:.8deg}
[data-s=stiker] .hero-foto img{display:block;width:100%;height:auto;aspect-ratio:4/3;object-fit:cover;filter:grayscale(1) contrast(1.25)}
[data-s=stiker] .hero-foto::after{content:"";position:absolute;inset:0;background-image:radial-gradient(circle,rgba(25,24,19,.5) 0 1px,transparent 1.6px);background-size:4px 4px;mix-blend-mode:multiply;pointer-events:none}
[data-s=stiker] .lencana{position:absolute;right:-6px;bottom:-16px;display:grid;place-content:center;min-width:96px;padding:8px 12px;background:var(--sinyal);color:var(--di-atas-sinyal);border:2px solid var(--tinta);font-size:13px;rotate:-4deg;box-shadow:2px 2px 0 var(--tinta)}
[data-s=stiker] .status{border:2px solid var(--tinta);border-radius:0;background:var(--kartu);font-weight:700;box-shadow:2px 2px 0 var(--tinta)}
[data-s=stiker] .fakta{gap:8px;margin-top:22px}
[data-s=stiker] .fakta li{padding:12px 10px;border:2px solid var(--tinta);border-radius:0;background:var(--kartu);box-shadow:3px 3px 0 var(--tinta)}
[data-s=stiker] .fakta li:nth-child(2){rotate:-1.2deg}
[data-s=stiker] .fakta li:nth-child(3){rotate:1.4deg}
[data-s=stiker] .fakta .f-label{font-size:11px;color:var(--tinta-redup)}
[data-s=stiker] .fakta .f-nilai{font-size:clamp(15px,4.4vw,20px);font-weight:800;line-height:1.05}
[data-s=stiker] .loncat a{border:2px solid var(--tinta);border-radius:0;background:var(--kartu);font-weight:700;box-shadow:2px 2px 0 var(--tinta)}
[data-s=stiker] .loncat a:hover{background:var(--sinyal)}
[data-s=stiker] .demo-kartu{border:2px dashed var(--tinta);border-radius:0;background:var(--sinyal-lembut);box-shadow:4px 4px 0 var(--tinta)}
[data-s=stiker] .bagian{padding:48px 0 4px}
[data-s=stiker] .bagian h2{font-size:clamp(30px,9vw,46px)}
[data-s=stiker] .bagian:not(.penutup) h2::after{content:"";display:block;width:70px;height:14px;margin-top:12px;background:var(--sinyal);border:2px solid var(--tinta);box-shadow:3px 3px 0 var(--tinta);rotate:-1deg}
[data-s=stiker] .bagian-lead{margin-top:12px}
[data-s=stiker] .kartu{border:2px solid var(--tinta);border-radius:0;box-shadow:4px 4px 0 var(--tinta)}
[data-s=stiker] #harga .kartu{margin-top:24px;background:var(--kartu)}
[data-s=stiker] #harga .kartu > h3{display:inline-block;padding:4px 10px;background:var(--tinta);color:var(--latar);font-size:14px;font-weight:800}
[data-s=stiker] .harga li{grid-template-columns:minmax(0,1fr) auto;align-items:center;padding:12px 0;border-top:2px dotted var(--garis-kuat)}
[data-s=stiker] .harga li:first-child{border-top:0}
[data-s=stiker] .harga .nm{font-weight:700}
[data-s=stiker] .harga .hr{display:grid;place-content:center;min-width:66px;min-height:66px;padding:4px;border:2px solid var(--tinta);border-radius:50%;background:var(--sinyal);color:var(--di-atas-sinyal);font-weight:800;font-size:14px;text-align:center;rotate:3deg;box-shadow:2px 2px 0 var(--tinta)}
[data-s=stiker] .harga li:nth-child(even) .hr{rotate:-3deg}
[data-s=stiker] .harga .ket{grid-column:1 / -1}
[data-s=stiker] .dur{display:inline;margin:0;padding:0;background:none;color:var(--tinta-redup);font-size:13px;font-weight:700}
[data-s=stiker] .dur + .ket-teks::before{content:"\00A0\00B7\00A0"}
[data-s=stiker] .galeri{grid-template-columns:repeat(2,minmax(0,1fr));gap:18px 14px;margin-top:28px}
[data-s=stiker] .petak{position:relative;aspect-ratio:4/3;border:6px solid var(--kartu);border-radius:0;background:var(--kartu);box-shadow:3px 3px 0 var(--tinta)}
[data-s=stiker] .petak img{filter:grayscale(1) contrast(1.2)}
[data-s=stiker] .petak::before{content:"";position:absolute;z-index:2;top:-14px;left:50%;transform:translateX(-50%) rotate(-3deg);width:66px;height:22px;background:rgba(232,222,23,.55);border:1px solid rgba(25,24,19,.25)}
[data-s=stiker] .petak:nth-child(odd){rotate:-1.6deg}
[data-s=stiker] .petak:nth-child(even){rotate:1.8deg}
[data-s=stiker] .petak figcaption{font-size:12px;color:var(--tinta-redup);padding-top:2px}
[data-s=stiker] .petak:first-child,[data-s=stiker] .petak:last-child{grid-column:1 / -1;aspect-ratio:16/10;rotate:0deg}
[data-s=stiker] .jam li{padding:12px 10px;border-radius:0}
[data-s=stiker] .jam li.hari-ini{background:var(--sinyal);font-weight:700;box-shadow:inset 0 0 0 2px var(--tinta)}
[data-s=stiker] .tanya{border-bottom:2px solid var(--tinta)}
[data-s=stiker] .tanya details{border-top:2px solid var(--tinta)}
[data-s=stiker] .tanya summary{min-height:58px;font-weight:800}
[data-s=stiker] .tanya summary svg{display:none}
[data-s=stiker] .tanya summary::after{content:"\002B";margin-left:auto;font-size:24px;color:var(--sinyal-gelap)}
[data-s=stiker] .tanya details[open] summary::after{content:"\2212"}
[data-s=stiker] .penutup .kartu{border:2px solid var(--tinta);background:var(--sinyal-lembut);box-shadow:4px 4px 0 var(--tinta)}
[data-s=stiker] .penutup h2{font-size:clamp(28px,8.5vw,40px)}
@supports (animation-timeline:view()){
@media (prefers-reduced-motion:no-preference){
@keyframes stk{from{opacity:0;transform:translateY(14px) rotate(-1deg)}to{opacity:1;transform:none}}
[data-s=stiker] .petak{animation:stk linear both;animation-timeline:view();animation-range:entry 0% entry 60%}
}
}
"""

GAYA_STIKER_WIZARD = r"""
[data-s=stiker] .kartu.pesan,[data-s=stiker] .kartu.pesan-buka{border:2px solid var(--tinta);background:var(--kartu)}
[data-s=stiker] .kartu.pesan-buka > h3{font-size:26px}
[data-s=stiker] .panel h3{font-size:26px}
[data-s=stiker] .langkah-no{color:var(--tinta-redup)}
[data-s=stiker] .progres{height:10px;border-radius:0;background:var(--kartu-turun);border:2px solid var(--tinta)}
[data-s=stiker] .progres i{border-radius:0;background:var(--sinyal)}
[data-s=stiker] .sub{color:var(--sinyal-gelap)}
[data-s=stiker] .opsi-kotak{border-width:2px;border-radius:0;box-shadow:2px 2px 0 var(--tinta)}
[data-s=stiker] .opsi input:checked + .opsi-kotak{border-color:var(--tinta);background:var(--sinyal);color:var(--di-atas-sinyal)}
[data-s=stiker] .opsi input:checked + .opsi-kotak .opsi-ket{color:var(--di-atas-sinyal)}
[data-s=stiker] .opsi input:checked + .opsi-kotak .opsi-tanda{border-color:var(--di-atas-sinyal)}
[data-s=stiker] .opsi-nama{font-weight:800}
[data-s=stiker] .opsi-harga{font-weight:800}
[data-s=stiker] .hari{border-radius:0;border-width:2px}
[data-s=stiker] .hari .tg{font-size:24px}
[data-s=stiker] .jam-grid button{border-radius:0;border-width:2px}
[data-s=stiker] .stepper{border-radius:0;border-width:2px}
[data-s=stiker] .kolom input,[data-s=stiker] .kolom textarea{border-radius:0}
[data-s=stiker] .tinjau .total{border-top:3px solid var(--tinta)}
[data-s=stiker] .tinjau .total dd{font-size:26px;font-weight:800}
[data-s=stiker] .tinjau .ubah{color:var(--sinyal-gelap)}
[data-s=stiker] .selesai h3{font-size:30px}
[data-s=stiker] .kode{font-size:34px;font-weight:800;letter-spacing:.06em}
"""

SKINS = {
    "barbershop": {
        "poster": dict(
            nama="Poster Vintage",
            ringkas="Krem tua dan merah bata, bingkai poster ganda, tiang barber, dan foto sepia bernuansa lama.",
            cocok="ingin kesan klasik, jantan, dan penuh tradisi",
            tema=TEMA_POSTER, warna="#F2E4C9",
            css=GAYA_POSTER, css_wizard=GAYA_POSTER_WIZARD, font=FONT_ALFA + "\n" + FONT_MONO, preload="alfa-slab-one-latin.woff2",
            hero_foto=("g1", "Ruang potong bata merah dengan tiga kursi hitam di depan cermin"),
            galeri=[("g4", "Lengkung bata dan kursi potong"), ("g5", "Kursi klasik kulit"), ("g1", "Ruang potong dengan tiga kursi"), ("g3", "Sudut cermin dan rak produk"), ("g2", "Kursi potong"), ("g6", "Kursi dan wastafel cuci")],
            galeri_dulu=False, varian={},
        ),
        "lembar": dict(
            nama="Lembar Data",
            ringkas="Putih bersih dan hijau limau, teks dulu, tabel spesifikasi, dan galeri lembar kontak film.",
            cocok="ingin kesan presisi, rapi, dan modern",
            tema=TEMA_LEMBAR, warna="#FFFFFF",
            css=GAYA_LEMBAR, css_wizard=GAYA_LEMBAR_WIZARD, font=FONT_FAMILJEN + "\n" + FONT_MONO, preload="familjen-grotesk-latin.woff2",
            hero_foto=("g5", "Kursi klasik kulit"),
            galeri=[("g2", "Kursi potong"), ("g4", "Lengkung bata dan kursi potong"), ("g1", "Ruang potong dengan tiga kursi"), ("g3", "Sudut cermin dan rak produk"), ("g5", "Kursi klasik kulit"), ("g6", "Kursi dan wastafel cuci")],
            galeri_dulu=False, varian={},
        ),
        "stiker": dict(
            nama="Zine Jalanan",
            ringkas="Abu semen dan kuning stabilo, tumpukan stiker miring, foto hitam-putih berbutir, dan label harga bundar.",
            cocok="ingin kesan muda, berani, dan jalanan",
            tema=TEMA_STIKER, warna="#DCDAD3",
            css=GAYA_STIKER, css_wizard=GAYA_STIKER_WIZARD, font=FONT_BOWLBY, preload="bowlby-one-latin.woff2",
            hero_foto=("g4", "Lengkung bata dan kursi potong"),
            galeri=[("g5", "Kursi klasik kulit"), ("g3", "Sudut cermin dan rak produk"), ("g2", "Kursi potong"), ("g6", "Kursi dan wastafel cuci"), ("g1", "Ruang potong dengan tiga kursi"), ("g4", "Lengkung bata dan kursi potong")],
            galeri_dulu=False, varian={},
        ),
    },
}
