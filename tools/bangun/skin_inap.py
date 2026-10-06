FONT_UNBOUNDED = "@font-face{font-family:'Unbounded';font-style:normal;font-weight:200 800;font-display:swap;src:url(/font/unbounded-latin.woff2) format('woff2')}"
FONT_FAMILJEN = "@font-face{font-family:'Familjen Grotesk';font-style:normal;font-weight:400 700;font-display:swap;src:url(/font/familjen-grotesk-latin.woff2) format('woff2')}"
FONT_YOUNG = "@font-face{font-family:'Young Serif';font-style:normal;font-weight:400;font-display:swap;src:url(/font/young-serif-latin.woff2) format('woff2')}"
FONT_BODONI = "@font-face{font-family:'Bodoni Moda';font-style:normal;font-weight:400 700;font-display:swap;src:url(/font/bodoni-moda-latin.woff2) format('woff2')}"
FONT_MONO = "@font-face{font-family:'Space Mono';font-style:normal;font-weight:400;font-display:swap;src:url(/font/space-mono-latin-400.woff2) format('woff2')}\n@font-face{font-family:'Space Mono';font-style:normal;font-weight:700;font-display:swap;src:url(/font/space-mono-latin-700.woff2) format('woff2')}"

TEMA_ARSTEK = """
  --latar:#E9ECEA;
  --kartu:#F5F7F5;
  --kartu-turun:#D6DCD8;
  --tinta:#12211B;
  --tinta-redup:#4B5C54;
  --garis:#C3CCC6;
  --garis-halus:#D5DCD7;
  --garis-kuat:#6E8078;
  --sinyal:#1E5A44;
  --sinyal-gelap:#123F2E;
  --sinyal-lembut:#D6E5DD;
  --di-atas-sinyal:#FFFFFF;
  --fokus:#123F2E;
  --salah:#9C2410;
  --ok:#2F6B4F;
  --r:0px;
  --r-kecil:0px;
  --r-tombol:0px;
  --lengkung:0px;
  --serif:"Familjen Grotesk",system-ui,sans-serif;
  --bayang:none;
  --h-berat:600;
  --h-lebar:100%;
  --h-huruf:none;
  --h-ls:-.03em;
  --pole-tinggi:0px;
  --pole:none;
"""

GAYA_ARSTEK = r"""
[data-s=arsitek] :is(.hero h1,.bagian h2,.penutup h2){font-family:var(--serif);font-weight:600;font-stretch:100%;letter-spacing:-.03em}
[data-s=arsitek] .hero{padding:14px 0 4px}
[data-s=arsitek] .hero-isi{position:relative;padding-bottom:6px}
[data-s=arsitek] .hero-isi::before{display:none}
[data-s=arsitek] .hero .eyebrow{font-family:'Space Mono',monospace;font-size:11px;letter-spacing:.16em;color:var(--sinyal-gelap)}
[data-s=arsitek] .hero h1{margin:8px 0 10px;font-size:clamp(30px,9vw,48px);font-weight:600;line-height:1.02}
[data-s=arsitek] .hero h1 em{font-style:normal;font-weight:300}
[data-s=arsitek] .hero .lead{max-width:48ch}
[data-s=arsitek] .hero-foto{position:relative;margin:16px -16px 30px;background:var(--kartu-turun)}
[data-s=arsitek] .hero-foto img{display:block;width:100%;height:auto;aspect-ratio:16/10;object-fit:cover;filter:saturate(.9) contrast(1.02)}
[data-s=arsitek] .lencana{position:absolute;left:12px;bottom:12px;padding:5px 10px;background:var(--tinta);color:var(--latar);font-family:'Space Mono',monospace;font-size:11px;letter-spacing:.06em}
[data-s=arsitek] .status{border:1px solid var(--garis-kuat);border-radius:0;background:var(--kartu);font-family:'Space Mono',monospace;font-size:12px}
[data-s=arsitek] .fakta{gap:0;margin-top:20px;border-top:1px solid var(--garis-kuat);border-bottom:1px solid var(--garis-kuat)}
[data-s=arsitek] .fakta li{padding:14px 10px;border:0;border-left:1px solid var(--garis);border-radius:0;background:none}
[data-s=arsitek] .fakta li:first-child{border-left:0;padding-left:0}
[data-s=arsitek] .fakta .f-label{font-family:'Space Mono',monospace;font-size:11px;letter-spacing:.1em;color:var(--sinyal-gelap)}
[data-s=arsitek] .fakta .f-nilai{font-size:clamp(15px,4.4vw,20px);font-weight:600;line-height:1.05}
[data-s=arsitek] .loncat a{border:1px solid var(--tinta);border-radius:0;background:none;font-family:'Space Mono',monospace;font-size:13px}
[data-s=arsitek] .loncat a:hover{background:var(--tinta);color:var(--latar)}
[data-s=arsitek] .demo-kartu{border:1px solid var(--tinta);border-radius:0;background:var(--kartu-turun)}
[data-s=arsitek] .bagian{padding:56px 0 4px}
[data-s=arsitek] .bagian h2{font-size:clamp(26px,7.5vw,38px);font-weight:600;line-height:1.05}
[data-s=arsitek] .bagian:not(.penutup) h2::before{content:"";display:block;width:28px;height:3px;margin-bottom:14px;background:var(--sinyal)}
[data-s=arsitek] .bagian-lead{margin-top:12px}
[data-s=arsitek] .kartu{border:1px solid var(--garis);border-radius:0;background:var(--kartu);box-shadow:none}
[data-s=arsitek] #harga .kartu{margin-top:24px;padding:0;border:1px solid var(--garis-kuat);background:var(--kartu)}
[data-s=arsitek] #harga .kartu > h3{padding:12px 14px;border-bottom:1px solid var(--garis-kuat);font-family:'Space Mono',monospace;font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--sinyal-gelap)}
[data-s=arsitek] .harga{margin:0}
[data-s=arsitek] .harga li{grid-template-columns:minmax(0,1fr) auto;gap:2px 12px;padding:16px 14px;border-top:1px solid var(--garis-halus);align-items:baseline}
[data-s=arsitek] .harga li:first-child{border-top:0}
[data-s=arsitek] .harga .nm{font-size:19px;font-weight:600}
[data-s=arsitek] .harga .hr{font-family:'Space Mono',monospace;font-size:18px;font-weight:700;white-space:nowrap;color:var(--sinyal-gelap)}
[data-s=arsitek] .harga .ket{grid-column:1 / -1;font-size:14px;color:var(--tinta-redup)}
[data-s=arsitek] .galeri{display:grid;grid-template-columns:1fr;gap:16px;margin-top:22px}
[data-s=arsitek] .petak{aspect-ratio:16/10;border-radius:0;background:var(--kartu-turun)}
[data-s=arsitek] .petak img{filter:saturate(.9)}
[data-s=arsitek] .petak figcaption{padding-top:6px;font-family:'Space Mono',monospace;font-size:11px;color:var(--tinta-redup)}
[data-s=arsitek] .jam li{padding:12px 10px;border-radius:0}
[data-s=arsitek] .jam li.hari-ini{background:var(--sinyal-lembut);box-shadow:inset 3px 0 0 var(--sinyal)}
[data-s=arsitek] .tanya{border-bottom:1px solid var(--garis-kuat)}
[data-s=arsitek] .tanya details{border-top:1px solid var(--garis)}
[data-s=arsitek] .tanya summary{min-height:56px;font-weight:600}
[data-s=arsitek] .tanya summary svg{display:none}
[data-s=arsitek] .tanya summary::after{content:"";margin-left:auto;width:14px;height:14px;border-right:2px solid var(--sinyal);border-bottom:2px solid var(--sinyal);transform:rotate(45deg) translateY(-3px)}
[data-s=arsitek] .tanya details[open] summary::after{transform:rotate(225deg) translateY(-1px)}
[data-s=arsitek] .penutup .kartu{border:1px solid var(--tinta);background:var(--sinyal-lembut);padding:24px 18px}
[data-s=arsitek] .penutup h2{font-size:clamp(24px,7.5vw,34px)}
@media (min-width:900px){
[data-s=arsitek] #harga .kartu{display:grid;grid-template-columns:220px minmax(0,1fr);align-items:start}
[data-s=arsitek] #harga .kartu > h3{position:sticky;top:84px;border-bottom:0;border-right:1px solid var(--garis-kuat);padding:16px 14px;margin:0}
[data-s=arsitek] .harga li:first-child{border-top:0}
[data-s=arsitek] .galeri{grid-template-columns:1fr}
}
@keyframes arsitek-rel{0%,35%,65%,100%{background-color:transparent;box-shadow:inset 0 0 0 0 var(--sinyal)}45%,55%{background-color:var(--sinyal-lembut);box-shadow:inset 4px 0 0 0 var(--sinyal)}}
@supports (animation-timeline:view()){
@media (min-width:900px) and (prefers-reduced-motion:no-preference){
[data-s=arsitek] .harga li{animation:arsitek-rel linear both;animation-timeline:view()}
}
}
"""

GAYA_ARSTEK_WIZARD = r"""
[data-s=arsitek] .kartu.pesan,[data-s=arsitek] .kartu.pesan-buka{border:1px solid var(--garis-kuat);background:var(--kartu)}
[data-s=arsitek] .kartu.pesan-buka > h3{font-size:24px;font-weight:600}
[data-s=arsitek] .panel h3{font-size:26px;font-weight:600}
[data-s=arsitek] .langkah-no{font-family:'Space Mono',monospace;font-size:11px;letter-spacing:.14em;color:var(--sinyal-gelap)}
[data-s=arsitek] .progres{height:3px;border-radius:0;background:var(--kartu-turun)}
[data-s=arsitek] .progres i{border-radius:0}
[data-s=arsitek] .sub{color:var(--sinyal-gelap)}
[data-s=arsitek] .opsi-kotak{border-width:1px;border-radius:0}
[data-s=arsitek] .opsi input:checked + .opsi-kotak{border-color:var(--sinyal);box-shadow:inset 4px 0 0 var(--sinyal)}
[data-s=arsitek] .opsi-nama{font-weight:600}
[data-s=arsitek] .opsi-harga{font-family:'Space Mono',monospace;font-size:15px;font-weight:700;color:var(--sinyal-gelap)}
[data-s=arsitek] .panel[data-langkah=bayar] .opsi-harga{font-size:13px}
[data-s=arsitek] .hari{border-radius:0}
[data-s=arsitek] .hari .tg{font-size:22px;font-family:'Space Mono',monospace}
[data-s=arsitek] .jam-grid button{border-radius:0;font-family:'Space Mono',monospace}
[data-s=arsitek] .stepper{border-radius:0}
[data-s=arsitek] .st-nilai{font-family:'Space Mono',monospace}
[data-s=arsitek] .kolom input,[data-s=arsitek] .kolom textarea{border-radius:0}
[data-s=arsitek] .tinjau .total{border-top:2px solid var(--tinta)}
[data-s=arsitek] .tinjau .total dd{font-size:26px;font-family:'Space Mono',monospace;font-weight:700}
[data-s=arsitek] .selesai h3{font-size:28px;font-weight:600}
[data-s=arsitek] .kode{font-family:'Space Mono',monospace;font-size:32px;letter-spacing:.08em;color:var(--sinyal-gelap)}
"""

TEMA_PASPOR = """
  --latar:#DCC9A8;
  --kartu:#F4EAD8;
  --kartu-turun:#CBB28C;
  --tinta:#241A10;
  --tinta-redup:#52402A;
  --garis:#BCA47E;
  --garis-halus:#CDB894;
  --garis-kuat:#7E6440;
  --sinyal:#A32B1E;
  --sinyal-gelap:#7E1F14;
  --sinyal-lembut:#F0D9CF;
  --di-atas-sinyal:#FFF6EE;
  --fokus:#7E1F14;
  --salah:#9C2410;
  --ok:#3E6B3A;
  --r:3px;
  --r-kecil:3px;
  --r-tombol:3px;
  --lengkung:0px;
  --serif:"Young Serif",Georgia,serif;
  --bayang:0 1px 0 rgba(36,26,16,.2);
  --h-berat:400;
  --h-lebar:100%;
  --h-huruf:none;
  --h-ls:-.005em;
  --pole-tinggi:0px;
  --pole:none;
"""

GAYA_PASPOR = r"""
[data-s=paspor] :is(.hero h1,.bagian h2,.panel h3,.selesai h3,#harga .kartu > h3,.kartu.pesan-buka > h3,.f-nilai,.harga .hr,.hari .tg,.tinjau .total dd,.kode,.penutup h2,.lencana,.tanya summary,.harga .nm){font-family:var(--serif);font-weight:400;font-stretch:100%}
[data-s=paspor] .hero{padding:20px 0 4px}
[data-s=paspor] .hero-isi{position:relative;padding:16px;border:1px double var(--garis-kuat);background:var(--kartu)}
[data-s=paspor] .hero-isi::before{content:"";position:absolute;z-index:-1;inset:4px;width:auto;height:auto;border:1px solid var(--garis-kuat);pointer-events:none}
[data-s=paspor] .hero .eyebrow{font-family:'Space Mono',monospace;font-size:11px;letter-spacing:.2em;color:var(--sinyal-gelap)}
[data-s=paspor] .hero h1{margin:10px 0 10px;font-size:clamp(34px,10.5vw,52px);line-height:1.04}
[data-s=paspor] .hero h1 em{font-style:normal;color:var(--sinyal)}
[data-s=paspor] .hero .lead{max-width:44ch}
[data-s=paspor] .hero-foto{position:relative;margin:18px 0 30px;border:1px solid var(--garis-kuat);background:var(--kartu);padding:6px}
[data-s=paspor] .hero-foto img{display:block;width:100%;height:auto;aspect-ratio:4/3;object-fit:cover;filter:sepia(.18) saturate(.95)}
[data-s=paspor] .hero-foto::after{content:"";position:absolute;z-index:2;right:2px;bottom:2px;width:98px;height:98px;border-radius:50%;border:3px solid var(--sinyal);opacity:.85;transform:rotate(-14deg);background:radial-gradient(circle,transparent 52%,rgba(163,43,30,.18) 53% 100%)}
[data-s=paspor] .lencana{display:inline-block;margin-top:6px;font-family:'Space Mono',monospace;font-size:11px;letter-spacing:.08em;color:var(--sinyal-gelap);text-transform:uppercase}
[data-s=paspor] .status{border:1px solid var(--garis-kuat);border-radius:0;background:var(--kartu);font-family:'Space Mono',monospace;font-size:12px}
[data-s=paspor] .fakta{gap:8px;margin-top:20px}
[data-s=paspor] .fakta li{padding:12px 10px;border:1px dashed var(--garis-kuat);border-radius:0;background:var(--kartu)}
[data-s=paspor] .fakta .f-label{font-family:'Space Mono',monospace;font-size:10px;letter-spacing:.12em;color:var(--sinyal-gelap);text-transform:uppercase}
[data-s=paspor] .fakta .f-nilai{font-size:clamp(16px,4.6vw,21px);line-height:1.05}
[data-s=paspor] .loncat a{border:1px solid var(--garis-kuat);border-radius:0;background:var(--kartu);font-family:'Space Mono',monospace;font-size:12px}
[data-s=paspor] .loncat a:hover{background:var(--sinyal);border-color:var(--sinyal);color:var(--di-atas-sinyal)}
[data-s=paspor] .demo-kartu{border:1px solid var(--garis-kuat);border-radius:0;background:var(--sinyal-lembut)}
[data-s=paspor] .bagian{padding:46px 0 4px}
[data-s=paspor] .bagian h2{font-size:clamp(28px,8.5vw,40px);line-height:1.08}
[data-s=paspor] .bagian:not(.penutup) h2::after{content:"";display:block;width:100%;max-width:160px;height:1px;margin-top:12px;background:var(--garis-kuat)}
[data-s=paspor] .bagian-lead{margin-top:12px}
[data-s=paspor] .kartu{border:1px solid var(--garis-kuat);border-radius:0;background:var(--kartu);box-shadow:none}
[data-s=paspor] #harga .kartu{margin-top:22px;padding:0;border:1px solid var(--garis-kuat);background:var(--kartu)}
[data-s=paspor] #harga .kartu > h3{padding:12px 14px;border-bottom:1px dashed var(--garis-kuat);font-family:'Space Mono',monospace;font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--sinyal-gelap)}
[data-s=paspor] .harga{margin:0;padding:0 14px}
[data-s=paspor] .harga li{grid-template-columns:minmax(0,1fr) auto;gap:2px 12px;padding:14px 0;border-top:1px dashed var(--garis-halus)}
[data-s=paspor] .harga li:first-child{border-top:0}
[data-s=paspor] .harga .nm{font-size:19px}
[data-s=paspor] .harga .nm::before{content:"TIPE KAMAR";display:block;font-family:'Space Mono',monospace;font-size:9px;letter-spacing:.16em;color:var(--sinyal-gelap)}
[data-s=paspor] .harga .hr{font-family:'Space Mono',monospace;font-size:17px;font-weight:700;color:var(--sinyal-gelap);white-space:nowrap}
[data-s=paspor] .harga .ket{grid-column:1 / -1;font-size:14px}
[data-s=paspor] .galeri{grid-template-columns:repeat(2,minmax(0,1fr));gap:14px;margin-top:24px}
[data-s=paspor] .petak{position:relative;aspect-ratio:4/3;border:1px solid var(--garis-kuat);border-radius:0;background:var(--kartu);padding:6px 6px 22px}
[data-s=paspor] .petak img{filter:sepia(.15) saturate(.95)}
[data-s=paspor] .petak::after{content:"";position:absolute;right:8px;bottom:8px;width:34px;height:34px;border-radius:50%;border:2px solid var(--sinyal);opacity:.7;transform:rotate(-12deg)}
[data-s=paspor] .petak figcaption{position:absolute;left:8px;bottom:6px;font-family:'Space Mono',monospace;font-size:10px;color:var(--tinta-redup)}
[data-s=paspor] .petak:first-child,[data-s=paspor] .petak:last-child{grid-column:1 / -1;aspect-ratio:16/10}
[data-s=paspor] .jam li{padding:12px 10px;border-radius:0}
[data-s=paspor] .jam li.hari-ini{background:var(--sinyal-lembut);box-shadow:inset 3px 0 0 var(--sinyal)}
[data-s=paspor] .tanya{border-bottom:1px solid var(--garis-kuat)}
[data-s=paspor] .tanya details{border-top:1px solid var(--garis)}
[data-s=paspor] .tanya summary{min-height:58px;font-size:18px}
[data-s=paspor] .tanya summary svg{display:none}
[data-s=paspor] .tanya summary::after{content:"+";margin-left:auto;font-family:'Space Mono',monospace;color:var(--sinyal-gelap)}
[data-s=paspor] .tanya details[open] summary::after{content:"\2212"}
[data-s=paspor] .penutup .kartu{border:1px double var(--garis-kuat);background:var(--sinyal-lembut);padding:24px 18px}
[data-s=paspor] .penutup h2{font-size:clamp(26px,8vw,36px)}
"""

GAYA_PASPOR_WIZARD = r"""
[data-s=paspor] .kartu.pesan,[data-s=paspor] .kartu.pesan-buka{border:1px solid var(--garis-kuat);background:var(--kartu)}
[data-s=paspor] .kartu.pesan-buka > h3{font-size:22px}
[data-s=paspor] .panel h3{font-size:24px}
[data-s=paspor] .langkah-no{font-family:'Space Mono',monospace;font-size:11px;letter-spacing:.14em;color:var(--sinyal-gelap)}
[data-s=paspor] .progres{height:5px;border-radius:0;background:var(--kartu-turun)}
[data-s=paspor] .progres i{border-radius:0}
[data-s=paspor] .sub{color:var(--sinyal-gelap)}
[data-s=paspor] .opsi-kotak{border-width:1px;border-radius:0}
[data-s=paspor] .opsi input:checked + .opsi-kotak{border-color:var(--sinyal);background:var(--sinyal-lembut)}
[data-s=paspor] .opsi-nama{font-weight:700}
[data-s=paspor] .opsi-harga{font-family:'Space Mono',monospace;font-size:15px;font-weight:700;color:var(--sinyal-gelap)}
[data-s=paspor] .panel[data-langkah=bayar] .opsi-harga{font-size:13px}
[data-s=paspor] .hari{border-radius:0}
[data-s=paspor] .hari .tg{font-size:22px;font-family:'Space Mono',monospace}
[data-s=paspor] .jam-grid button{border-radius:0;font-family:'Space Mono',monospace}
[data-s=paspor] .stepper{border-radius:0}
[data-s=paspor] .st-nilai{font-family:'Space Mono',monospace}
[data-s=paspor] .kolom input,[data-s=paspor] .kolom textarea{border-radius:0;font-family:'Space Mono',monospace}
[data-s=paspor] .tinjau .total{border-top:1px solid var(--sinyal)}
[data-s=paspor] .tinjau .total dd{font-size:26px;font-family:'Space Mono',monospace}
[data-s=paspor] .tinjau .ubah{color:var(--sinyal-gelap)}
[data-s=paspor] .selesai h3{font-size:28px}
[data-s=paspor] .kode{font-family:'Space Mono',monospace;font-size:32px;letter-spacing:.08em;color:var(--sinyal-gelap)}
"""

TEMA_SENJA = """
  --latar:#141B2B;
  --kartu:#1D2740;
  --kartu-turun:#27324E;
  --tinta:#F1ECE2;
  --tinta-redup:#B7BCCB;
  --garis:#33405C;
  --garis-halus:#28334C;
  --garis-kuat:#8A93AD;
  --sinyal:#E4795A;
  --sinyal-gelap:#F0A88E;
  --sinyal-lembut:#3A2A2C;
  --di-atas-sinyal:#141B2B;
  --fokus:#F0A88E;
  --salah:#FF9C87;
  --ok:#8FE0AE;
  --r:2px;
  --r-kecil:2px;
  --r-tombol:2px;
  --lengkung:0px;
  --serif:"Bodoni Moda",Georgia,serif;
  --bayang:none;
  --h-berat:500;
  --h-lebar:100%;
  --h-huruf:none;
  --h-ls:-.01em;
  --pole-tinggi:0px;
  --pole:none;
"""

GAYA_SENJA = r"""
[data-s=senja] :is(.hero h1,.bagian h2,.panel h3,.selesai h3,.f-nilai,.harga .hr,.tinjau .total dd,.kode,.penutup h2){font-family:var(--serif);font-weight:500;font-stretch:100%;letter-spacing:0}
[data-s=senja] .hero{padding:20px 0 4px}
[data-s=senja] .hero-isi{position:relative;padding-bottom:8px}
[data-s=senja] .hero-isi::before{display:none}
[data-s=senja] .hero .eyebrow{font-size:12px;letter-spacing:.16em;color:var(--sinyal-gelap)}
[data-s=senja] .hero h1{margin:10px 0 10px;font-size:clamp(36px,11.5vw,62px);font-weight:500;line-height:1.04}
[data-s=senja] .hero h1 em{font-style:normal;color:var(--sinyal)}
[data-s=senja] .hero .lead{max-width:44ch}
[data-s=senja] .hero-foto{position:relative;isolation:isolate;margin:18px 0 28px;background:var(--kartu-turun)}
[data-s=senja] .hero-foto img{display:block;width:100%;height:auto;aspect-ratio:16/9;object-fit:cover;filter:brightness(.82) contrast(1.05) saturate(.85)}
[data-s=senja] .hero-foto::after{content:"";position:absolute;z-index:1;left:50%;bottom:0;width:120px;height:60px;margin-left:-60px;border-radius:60px 60px 0 0;background:var(--sinyal);pointer-events:none}
[data-s=senja] .lencana{position:absolute;z-index:2;left:10px;top:10px;padding:4px 9px;background:rgba(20,27,43,.72);color:var(--sinyal-gelap);font-size:12px}
[data-s=senja] .status{border:1px solid var(--garis-kuat);border-radius:0;background:var(--kartu)}
[data-s=senja] .fakta{gap:0;margin-top:20px;border-top:1px solid var(--sinyal);border-bottom:1px solid var(--garis-kuat)}
[data-s=senja] .fakta li{text-align:center;padding:14px 8px;border:0;border-left:1px solid var(--garis);border-radius:0;background:none}
[data-s=senja] .fakta li:first-child{border-left:0}
[data-s=senja] .fakta .f-label{font-size:10px;letter-spacing:.16em;color:var(--sinyal-gelap)}
[data-s=senja] .fakta .f-nilai{font-family:var(--serif);font-size:clamp(16px,4.6vw,21px);font-weight:500;line-height:1.05}
[data-s=senja] .loncat a{border:1px solid var(--garis-kuat);border-radius:0;background:none}
[data-s=senja] .loncat a:hover{border-color:var(--sinyal);background:var(--sinyal);color:var(--di-atas-sinyal)}
[data-s=senja] .demo-kartu{border:1px solid var(--garis-kuat);border-radius:0;background:var(--kartu)}
[data-s=senja] .bagian{padding:48px 0 4px}
[data-s=senja] .bagian h2{font-size:clamp(28px,8.5vw,42px);font-weight:500;line-height:1.06}
[data-s=senja] .bagian:not(.penutup) h2::after{content:"";display:block;width:52px;height:2px;margin-top:12px;background:var(--sinyal)}
[data-s=senja] .bagian-lead{margin-top:12px}
[data-s=senja] .kartu{border:1px solid var(--garis);border-radius:0;background:var(--kartu);box-shadow:none}
[data-s=senja] #harga .kartu{margin-top:22px;padding:14px;border:1px solid var(--garis-kuat);background:none}
[data-s=senja] #harga .kartu > h3{padding:8px 10px;background:var(--sinyal);color:var(--di-atas-sinyal);font-family:'Space Mono',monospace;font-size:11px;font-weight:700;letter-spacing:.16em;text-transform:uppercase}
[data-s=senja] .harga{margin-top:4px}
[data-s=senja] .harga li{grid-template-columns:minmax(0,1fr) auto;gap:2px 12px;padding:13px 10px;border-top:1px solid var(--garis-halus);align-items:baseline;font-family:'Space Mono',monospace}
[data-s=senja] .harga li:nth-child(odd){background:rgba(255,255,255,.02)}
[data-s=senja] .harga li:first-child{border-top:0}
[data-s=senja] .harga .nm{font-family:var(--serif);font-size:18px;font-weight:500}
[data-s=senja] .harga .hr{font-size:16px;font-weight:700;color:var(--sinyal-gelap);white-space:nowrap}
[data-s=senja] .harga .ket{grid-column:1 / -1;font-family:Archivo,system-ui,sans-serif;font-size:13px;color:var(--tinta-redup)}
[data-s=senja] .galeri{grid-template-columns:repeat(3,minmax(0,1fr));gap:8px;margin-top:22px}
[data-s=senja] .petak{aspect-ratio:9/16;border-radius:0;background:var(--kartu-turun)}
[data-s=senja] .petak img{filter:brightness(.85) saturate(.9)}
[data-s=senja] .petak figcaption{padding-top:5px;font-size:11px;line-height:1.3;color:var(--tinta-redup)}
[data-s=senja] .petak:nth-child(2){margin-top:24px}
[data-s=senja] .petak:nth-child(5){margin-top:24px}
[data-s=senja] .petak:first-child,[data-s=senja] .petak:last-child{grid-column:1 / -1;aspect-ratio:16/9;margin-top:0}
[data-s=senja] .jam li{padding:12px 10px;border-radius:0}
[data-s=senja] .jam li.hari-ini{background:var(--sinyal-lembut);box-shadow:inset 3px 0 0 var(--sinyal)}
[data-s=senja] .tanya{border-bottom:1px solid var(--sinyal)}
[data-s=senja] .tanya details{border-top:1px solid var(--garis)}
[data-s=senja] .tanya summary{min-height:56px;font-family:var(--serif);font-size:17px}
[data-s=senja] .tanya summary svg{display:none}
[data-s=senja] .tanya summary::after{content:"+";margin-left:auto;color:var(--sinyal)}
[data-s=senja] .tanya details[open] summary::after{content:"\2212"}
[data-s=senja] .penutup .kartu{border:1px solid var(--sinyal);background:var(--sinyal-lembut);padding:26px 18px}
[data-s=senja] .penutup h2{font-size:clamp(26px,8vw,38px)}
"""

GAYA_SENJA_WIZARD = r"""
[data-s=senja] .kartu.pesan,[data-s=senja] .kartu.pesan-buka{border:1px solid var(--garis-kuat);background:var(--kartu)}
[data-s=senja] .kartu.pesan-buka > h3{font-size:24px}
[data-s=senja] .panel h3{font-size:26px}
[data-s=senja] .langkah-no{letter-spacing:.14em;color:var(--sinyal-gelap)}
[data-s=senja] .progres{height:3px;border-radius:0;background:var(--kartu-turun)}
[data-s=senja] .progres i{border-radius:0}
[data-s=senja] .sub{color:var(--sinyal-gelap)}
[data-s=senja] .opsi-kotak{border-width:1px;border-radius:0}
[data-s=senja] .opsi input:checked + .opsi-kotak{border-color:var(--sinyal);background:var(--sinyal-lembut)}
[data-s=senja] .opsi-nama{font-weight:500}
[data-s=senja] .opsi-harga{font-family:'Space Mono',monospace;font-size:15px;color:var(--sinyal-gelap)}
[data-s=senja] .panel[data-langkah=bayar] .opsi-harga{font-size:13px}
[data-s=senja] .hari{border-radius:0}
[data-s=senja] .hari .tg{font-size:24px;font-family:'Space Mono',monospace}
[data-s=senja] .jam-grid button{border-radius:0;font-family:'Space Mono',monospace}
[data-s=senja] .stepper{border-radius:0}
[data-s=senja] .st-nilai{font-family:'Space Mono',monospace}
[data-s=senja] .kolom input,[data-s=senja] .kolom textarea{border-radius:0}
[data-s=senja] .tinjau .total{border-top:1px solid var(--sinyal)}
[data-s=senja] .tinjau .total dd{font-size:26px;color:var(--sinyal-gelap)}
[data-s=senja] .selesai h3{font-size:30px}
[data-s=senja] .kode{font-size:34px;letter-spacing:.06em;color:var(--sinyal-gelap)}
"""

SKINS = {
    "penginapan": {
        "arsitek": dict(
            nama="Arsitektur",
            ringkas="Beton dingin dan hijau hutan, foto lebar tepi ke tepi, rel kamar lengket, dan galeri foto besar.",
            cocok="ingin kesan bersih, arsitektural, dan modern",
            tema=TEMA_ARSTEK, warna="#E9ECEA",
            css=GAYA_ARSTEK, css_wizard=GAYA_ARSTEK_WIZARD, font=FONT_FAMILJEN + "\n" + FONT_MONO, preload="familjen-grotesk-latin.woff2",
            hero_foto=("g4", "Kursi berjemur dan payung di tepi kolam"),
            galeri=[("g2", "Kamar tidur dengan seprai putih"), ("g1", "Ruang tamu terang dengan sofa dan cermin rotan"), ("g6", "Ruang makan teduh dengan tanaman"), ("g5", "Kamar mandi dengan bak mandi dan jendela"), ("g3", "Kamar dengan tempat tidur double dan lampu meja"), ("g4", "Kursi berjemur di tepi kolam")],
            galeri_dulu=False, varian={},
        ),
        "paspor": dict(
            nama="Paspor",
            ringkas="Kraft dan merah stempel, bingkai ganda, label mesin ketik, dan tanda stempel pada tiap foto.",
            cocok="ingin kesan berkelana, hangat, dan berkarakter",
            tema=TEMA_PASPOR, warna="#DCC9A8",
            css=GAYA_PASPOR, css_wizard=GAYA_PASPOR_WIZARD, font=FONT_YOUNG + "\n" + FONT_MONO, preload="young-serif-latin.woff2",
            hero_foto=("g1", "Ruang tamu terang dengan sofa dan cermin rotan"),
            galeri=[("g3", "Kamar dengan tempat tidur double dan lampu meja"), ("g4", "Kursi berjemur di tepi kolam"), ("g2", "Kamar tidur dengan seprai putih"), ("g5", "Kamar mandi dengan bak mandi dan jendela"), ("g6", "Ruang makan teduh dengan tanaman"), ("g1", "Ruang tamu terang dengan sofa dan cermin rotan")],
            galeri_dulu=False, varian={},
        ),
        "senja": dict(
            nama="Senja",
            ringkas="Navy gelap dan koral senja, matahari bulat di garis horizon, papan jadwal kedatangan, dan galeri kolom tinggi.",
            cocok="ingin kesan tenang, elegan, dan romantis",
            tema=TEMA_SENJA, warna="#141B2B",
            css=GAYA_SENJA, css_wizard=GAYA_SENJA_WIZARD, font=FONT_BODONI + "\n" + FONT_MONO, preload="bodoni-moda-latin.woff2",
            hero_foto=("g4", "Kursi berjemur dan payung di tepi kolam"),
            galeri=[("g4", "Kursi berjemur di tepi kolam"), ("g5", "Kamar mandi dengan bak mandi dan jendela"), ("g2", "Kamar tidur dengan seprai putih"), ("g1", "Ruang tamu terang dengan sofa dan cermin rotan"), ("g6", "Ruang makan teduh dengan tanaman"), ("g3", "Kamar dengan tempat tidur double dan lampu meja")],
            galeri_dulu=False, varian={},
        ),
    },
}
