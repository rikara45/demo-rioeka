FONT_CAVEATBRUSH = "@font-face{font-family:'Caveat Brush';font-style:normal;font-weight:400;font-display:swap;src:url(/font/caveat-brush-latin.woff2) format('woff2')}"
FONT_BRICOLAGE = "@font-face{font-family:'Bricolage Grotesque';font-style:normal;font-weight:300 800;font-display:swap;src:url(/font/bricolage-grotesque-latin.woff2) format('woff2')}"
FONT_RUBIK = "@font-face{font-family:'Rubik';font-style:normal;font-weight:300 700;font-display:swap;src:url(/font/rubik-latin.woff2) format('woff2')}"

TEMA_WARUNG = """
  --latar:#1B2A23;
  --kartu:#243530;
  --kartu-turun:#2E423A;
  --tinta:#F0F4EF;
  --tinta-redup:#B7C6BC;
  --garis:#3A4F44;
  --garis-kuat:#8AA396;
  --sinyal:#9CC7E0;
  --sinyal-gelap:#C3DDF0;
  --sinyal-lembut:#2B3E45;
  --di-atas-sinyal:#1B2A23;
  --fokus:#C3DDF0;
  --salah:#FF9C87;
  --ok:#8FE0AE;
  --r:2px;
  --r-kecil:2px;
  --r-tombol:2px;
  --lengkung:0px;
  --serif:"Caveat Brush",cursive;
  --bayang:none;
  --h-berat:400;
  --h-lebar:100%;
  --h-huruf:none;
  --h-ls:0;
  --pole-tinggi:0px;
  --pole:none;
"""

GAYA_WARUNG = r"""
[data-s=warung] :is(.hero h1,.penutup h2,.harga .hr,.lencana){font-family:var(--serif);font-weight:400;font-stretch:100%;letter-spacing:0;text-transform:none}
[data-s=warung] :is(.bagian h2,.panel h3,.selesai h3,.f-nilai,.hari .tg,.tinjau .total dd,.kode,.kartu.pesan-buka > h3,#harga .kartu > h3,.tanya summary){font-family:var(--serif);font-weight:400;letter-spacing:0;text-transform:none;font-stretch:100%}
[data-s=warung] .hero{padding:20px 0 4px}
[data-s=warung] .hero-isi{position:relative;padding:20px 16px;border:6px solid #6B4E2E;background:var(--kartu);box-shadow:inset 0 0 60px rgba(0,0,0,.35),0 2px 0 rgba(0,0,0,.3)}
[data-s=warung] .hero-isi::before{content:"";position:absolute;width:auto;height:auto;inset:0;opacity:.5;background-image:radial-gradient(rgba(255,255,255,.05) 0 1px,transparent 1px);background-size:9px 9px;pointer-events:none}
[data-s=warung] .hero .eyebrow{font-size:12px;letter-spacing:.16em;color:var(--sinyal-gelap)}
[data-s=warung] .hero h1{margin:10px 0 8px;font-size:clamp(46px,16vw,84px);line-height:1}
[data-s=warung] .hero h1 em{font-style:normal;color:var(--sinyal)}
[data-s=warung] .hero .lead{max-width:44ch}
[data-s=warung] .hero-foto{position:relative;margin:18px 0 30px;padding:8px;border:2px solid var(--garis-kuat);background:#31463D;rotate:-1deg}
[data-s=warung] .hero-foto img{display:block;width:100%;height:auto;aspect-ratio:4/3;object-fit:cover;filter:brightness(.92) saturate(.95)}
[data-s=warung] .lencana{position:absolute;right:10px;bottom:10px;font-size:24px;color:var(--sinyal-gelap);transform:rotate(-3deg)}
[data-s=warung] .status{border:1px solid var(--garis-kuat);border-radius:0;background:none}
[data-s=warung] .fakta{gap:10px;margin-top:20px}
[data-s=warung] .fakta li{padding:10px 12px;border:1px dashed var(--garis-kuat);border-radius:0;background:none}
[data-s=warung] .fakta .f-label{font-size:11px;letter-spacing:.12em;color:var(--sinyal-gelap)}
[data-s=warung] .fakta .f-nilai{font-size:clamp(20px,6.5vw,28px);line-height:1.05}
[data-s=warung] .loncat a{border:1px solid var(--garis-kuat);border-radius:0;background:none}
[data-s=warung] .loncat a:hover{border-color:var(--sinyal);background:var(--sinyal);color:var(--di-atas-sinyal)}
[data-s=warung] .demo-kartu{border:1px dashed var(--garis-kuat);border-radius:0;background:none}
[data-s=warung] .bagian{padding:48px 0 4px}
[data-s=warung] .bagian h2{font-size:clamp(38px,12.5vw,66px);line-height:1}
[data-s=warung] .bagian:not(.penutup) h2::after{content:"";display:block;width:80px;height:3px;margin-top:10px;background:var(--sinyal);border-radius:99px}
[data-s=warung] .bagian-lead{margin-top:12px}
[data-s=warung] .kartu{border:1px dashed var(--garis-kuat);border-radius:0;background:none;box-shadow:none}
[data-s=warung] #harga .kartu{margin-top:24px;padding:16px;border:1px dashed var(--garis-kuat)}
[data-s=warung] #harga .kartu > h3{font-size:26px;color:var(--sinyal-gelap)}
[data-s=warung] .harga{margin-top:6px}
[data-s=warung] .harga li{grid-template-columns:minmax(0,1fr) auto;gap:2px 10px;padding:10px 0;border-top:1px dashed var(--garis)}
[data-s=warung] .harga li:first-child{border-top:0}
[data-s=warung] .harga .nm{font-weight:600}
[data-s=warung] .harga .hr{font-size:26px;line-height:1;color:var(--tinta);white-space:nowrap;transform:rotate(-2deg)}
[data-s=warung] .harga li:nth-child(even) .hr{color:var(--sinyal-gelap);transform:rotate(1.5deg)}
[data-s=warung] .harga .ket{grid-column:1 / -1;font-size:14px;color:var(--tinta-redup)}
[data-s=warung] .dur{display:inline;margin:0;padding:0;background:none;color:var(--sinyal-gelap);font-size:14px}
[data-s=warung] .dur + .ket-teks::before{content:"\00A0\00B7\00A0"}
[data-s=warung] .galeri{grid-template-columns:repeat(2,minmax(0,1fr));gap:16px;margin-top:24px}
[data-s=warung] .petak{position:relative;aspect-ratio:4/3;border:1px solid var(--garis-kuat);border-radius:0;background:var(--kartu-turun);box-shadow:3px 3px 0 rgba(0,0,0,.35)}
[data-s=warung] .petak::before{content:"";position:absolute;z-index:2;top:-10px;left:50%;transform:translateX(-50%) rotate(-2deg);width:34px;height:20px;border:2px solid var(--garis-kuat);border-bottom:0;border-radius:8px 8px 0 0;background:var(--latar)}
[data-s=warung] .petak figcaption{padding-top:5px;font-size:12px;color:var(--tinta-redup)}
[data-s=warung] .petak:first-child,[data-s=warung] .petak:last-child{grid-column:1 / -1;aspect-ratio:16/10}
[data-s=warung] .jam li{padding:12px 10px;border-radius:0}
[data-s=warung] .jam li.hari-ini{background:var(--sinyal-lembut);box-shadow:inset 3px 0 0 var(--sinyal);color:var(--tinta)}
[data-s=warung] .tanya{border-bottom:1px dashed var(--garis-kuat)}
[data-s=warung] .tanya details{border-top:1px dashed var(--garis)}
[data-s=warung] .tanya summary{min-height:58px;font-size:24px}
[data-s=warung] .tanya summary svg{display:none}
[data-s=warung] .tanya summary::after{content:"+";margin-left:auto;font-size:26px;color:var(--sinyal)}
[data-s=warung] .tanya details[open] summary::after{content:"\2212"}
[data-s=warung] .penutup .kartu{border:1px dashed var(--garis-kuat);background:var(--sinyal-lembut);padding:26px 18px}
[data-s=warung] .penutup h2{font-size:clamp(34px,12vw,60px)}
[data-s=warung] .menu-baris{border-style:dashed;border-radius:0;background:none}
[data-s=warung] .menu-baris.aktif{border-style:solid}
[data-s=warung] .menu-sub{color:var(--sinyal-gelap)}
"""

GAYA_WARUNG_WIZARD = r"""
[data-s=warung] .kartu.pesan,[data-s=warung] .kartu.pesan-buka{border:1px dashed var(--garis-kuat);background:var(--kartu)}
[data-s=warung] .kartu.pesan-buka > h3{font-size:34px}
[data-s=warung] .panel h3{font-size:34px}
[data-s=warung] .langkah-no{letter-spacing:.16em;color:var(--sinyal-gelap)}
[data-s=warung] .progres{height:6px;border-radius:0;background:var(--kartu-turun)}
[data-s=warung] .progres i{border-radius:0}
[data-s=warung] .sub{color:var(--sinyal-gelap);font-family:var(--serif);font-size:20px;text-transform:none;letter-spacing:0}
[data-s=warung] .opsi-kotak{border-width:1px;border-style:dashed;border-radius:0}
[data-s=warung] .opsi input:checked + .opsi-kotak{border-style:solid;border-color:var(--sinyal);background:var(--sinyal-lembut)}
[data-s=warung] .opsi-nama{font-weight:600}
[data-s=warung] .opsi-harga{font-family:var(--serif);font-size:26px;color:var(--sinyal-gelap)}
[data-s=warung] .panel[data-langkah=bayar] .opsi-harga{font-family:Archivo,system-ui,sans-serif;font-size:14px}
[data-s=warung] .hari{border-radius:0}
[data-s=warung] .hari .tg{font-size:28px}
[data-s=warung] .jam-grid button{border-radius:0}
[data-s=warung] .stepper{border-radius:0}
[data-s=warung] .st-nilai{font-family:var(--serif);font-size:28px}
[data-s=warung] .kolom input,[data-s=warung] .kolom textarea{border-radius:0}
[data-s=warung] .tinjau .total{border-top:1px dashed var(--sinyal)}
[data-s=warung] .tinjau .total dd{font-size:34px;color:var(--sinyal-gelap)}
[data-s=warung] .selesai h3{font-size:38px}
[data-s=warung] .kode{font-family:var(--serif);font-size:40px;letter-spacing:.04em;color:var(--sinyal-gelap)}
"""

TEMA_DAUN = """
  --latar:#EAF3E1;
  --kartu:#F8FBF3;
  --kartu-turun:#D6E6C7;
  --tinta:#15220F;
  --tinta-redup:#45543B;
  --garis:#C6D8B5;
  --garis-halus:#D9E7CD;
  --garis-kuat:#6E8459;
  --sinyal:#C0341C;
  --sinyal-gelap:#8F2410;
  --sinyal-lembut:#F6DCD4;
  --di-atas-sinyal:#FFF6EE;
  --fokus:#8F2410;
  --salah:#9C2410;
  --ok:#3E6B3A;
  --r:16px;
  --r-kecil:12px;
  --r-tombol:999px;
  --lengkung:999px;
  --serif:"Bricolage Grotesque",system-ui,sans-serif;
  --bayang:0 1px 2px rgba(21,34,15,.05),0 10px 24px rgba(21,34,15,.06);
  --h-berat:700;
  --h-lebar:100%;
  --h-huruf:none;
  --h-ls:-.02em;
  --pole-tinggi:0px;
  --pole:none;
"""

GAYA_DAUN = r"""
[data-s=daun] :is(.hero h1,.bagian h2,.penutup h2,.harga .hr,.lencana){font-family:var(--serif);font-weight:700;font-stretch:100%;letter-spacing:-.02em}
[data-s=daun] .hero{padding:20px 0 4px}
[data-s=daun] .hero-isi{position:relative;padding-bottom:6px}
[data-s=daun] .hero-isi::before{content:"";position:absolute;z-index:-1;left:-8px;top:-8px;width:110px;height:110px;border-radius:50%;border:16px solid var(--sinyal-lembut);opacity:.9}
[data-s=daun] .hero .eyebrow{font-size:12px;letter-spacing:.16em;color:var(--sinyal-gelap)}
[data-s=daun] .hero h1{margin:10px 0 10px;font-size:clamp(34px,10.5vw,56px);line-height:1.03}
[data-s=daun] .hero h1 em{font-style:normal;color:var(--sinyal)}
[data-s=daun] .hero .lead{max-width:44ch}
[data-s=daun] .hero-foto{position:relative;width:min(320px,86%);margin:20px auto 30px;border-radius:50%;background:var(--kartu-turun);box-shadow:var(--bayang)}
[data-s=daun] .hero-foto::after{content:"";position:absolute;inset:-10px;border-radius:50%;border:1px dashed var(--sinyal);opacity:.6;pointer-events:none}
[data-s=daun] .hero-foto img{display:block;width:100%;height:auto;aspect-ratio:1;object-fit:cover;border-radius:50%}
[data-s=daun] .lencana{position:absolute;left:50%;bottom:-6px;transform:translateX(-50%);padding:4px 12px;border-radius:999px;background:var(--sinyal);color:var(--di-atas-sinyal);font-size:12px;white-space:nowrap}
[data-s=daun] .status{border:0;border-radius:999px;background:var(--kartu);box-shadow:var(--bayang)}
[data-s=daun] .fakta{gap:10px;margin-top:20px}
[data-s=daun] .fakta li{border-radius:999px;border:1px solid var(--garis);background:var(--kartu);padding:10px 16px;box-shadow:var(--bayang)}
[data-s=daun] .fakta .f-label{font-size:11px;letter-spacing:.1em;color:var(--sinyal-gelap)}
[data-s=daun] .fakta .f-nilai{font-size:clamp(16px,4.6vw,21px);font-weight:700;line-height:1.05}
[data-s=daun] .loncat a{border:1px solid var(--garis-kuat);border-radius:999px;background:var(--kartu)}
[data-s=daun] .loncat a:hover{background:var(--sinyal);border-color:var(--sinyal);color:var(--di-atas-sinyal)}
[data-s=daun] .demo-kartu{border:1px solid var(--garis);border-radius:var(--r);background:var(--kartu)}
[data-s=daun] .bagian{padding:46px 0 4px}
[data-s=daun] .bagian h2{font-size:clamp(28px,8.5vw,40px);font-weight:700;line-height:1.06}
[data-s=daun] .bagian:not(.penutup) h2::after{content:"";display:block;width:34px;height:16px;margin-top:12px;border-radius:0 100% 0 100%;background:var(--sinyal)}
[data-s=daun] .bagian-lead{margin-top:12px}
[data-s=daun] .kartu{border:1px solid var(--garis);border-radius:var(--r);background:var(--kartu);box-shadow:var(--bayang)}
[data-s=daun] #harga .kartu{margin-top:22px;background:var(--kartu)}
[data-s=daun] #harga .kartu > h3{padding-bottom:10px;border-bottom:1px solid var(--garis);font-size:13px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--tinta-redup)}
[data-s=daun] .harga{margin-top:6px}
[data-s=daun] .harga li{grid-template-columns:48px minmax(0,1fr) auto;align-items:center;gap:2px 12px;padding:12px 0;border-top:1px solid var(--garis-halus)}
[data-s=daun] .harga li:first-child{border-top:0}
[data-s=daun] .harga li::before{content:"";grid-column:1;grid-row:1 / 3;width:48px;height:48px;border-radius:50%;background:var(--sinyal-lembut) center/cover no-repeat;box-shadow:inset 0 0 0 1px var(--garis)}
[data-s=daun] .harga li:nth-child(6n+1)::before{background-image:url(/katering/img/g2.jpg)}
[data-s=daun] .harga li:nth-child(6n+2)::before{background-image:url(/katering/img/g3.jpg)}
[data-s=daun] .harga li:nth-child(6n+3)::before{background-image:url(/katering/img/g5.jpg)}
[data-s=daun] .harga li:nth-child(6n+4)::before{background-image:url(/katering/img/g4.jpg)}
[data-s=daun] .harga li:nth-child(6n+5)::before{background-image:url(/katering/img/g6.jpg)}
[data-s=daun] .harga li:nth-child(6n+6)::before{background-image:url(/katering/img/g1.jpg)}
[data-s=daun] .harga .nm{grid-column:2;font-weight:700}
[data-s=daun] .harga .hr{grid-column:3;grid-row:1;font-weight:700;color:var(--sinyal-gelap);white-space:nowrap}
[data-s=daun] .harga .ket{grid-column:2 / -1;font-size:13px}
[data-s=daun] .dur{display:inline;margin:0;padding:0;background:none;color:var(--tinta-redup);font-size:12px}
[data-s=daun] .dur + .ket-teks::before{content:"\00A0\00B7\00A0"}
[data-s=daun] .galeri{grid-template-columns:repeat(2,minmax(0,1fr));gap:16px;margin-top:24px}
[data-s=daun] .petak{aspect-ratio:1;border-radius:50%;background:var(--kartu-turun);box-shadow:var(--bayang)}
[data-s=daun] .petak img{filter:saturate(1.02)}
[data-s=daun] .petak figcaption{padding-top:8px;font-size:12px;text-align:center;color:var(--tinta-redup)}
[data-s=daun] .petak:nth-child(even){margin-top:22px}
[data-s=daun] .petak:first-child,[data-s=daun] .petak:last-child{grid-column:1 / -1;aspect-ratio:16/9;border-radius:var(--r);margin-top:0}
[data-s=daun] .jam li{padding:12px 10px;border-radius:999px}
[data-s=daun] .jam li.hari-ini{background:var(--sinyal);color:var(--di-atas-sinyal)}
[data-s=daun] .jam li.hari-ini .tanda-hari{background:var(--di-atas-sinyal);color:var(--sinyal-gelap)}
[data-s=daun] .tanya{border-bottom:1px solid var(--garis)}
[data-s=daun] .tanya details{border-top:1px solid var(--garis)}
[data-s=daun] .tanya summary{min-height:56px;font-weight:700}
[data-s=daun] .tanya summary svg{display:none}
[data-s=daun] .tanya summary::after{content:"";margin-left:auto;width:12px;height:12px;border-radius:50%;background:var(--sinyal)}
[data-s=daun] .tanya details[open] summary::after{background:none;border:3px solid var(--sinyal)}
[data-s=daun] .penutup .kartu{border:1px solid var(--sinyal);border-radius:var(--r);background:var(--sinyal-lembut);padding:24px 18px}
[data-s=daun] .penutup h2{font-size:clamp(28px,8.5vw,38px)}
[data-s=daun] .menu-baris{border-radius:999px}
"""

GAYA_DAUN_WIZARD = r"""
[data-s=daun] .kartu.pesan,[data-s=daun] .kartu.pesan-buka{border:1px solid var(--garis);background:var(--kartu)}
[data-s=daun] .kartu.pesan-buka > h3{font-size:24px;font-weight:700}
[data-s=daun] .panel h3{font-size:26px;font-weight:700}
[data-s=daun] .langkah-no{color:var(--sinyal-gelap)}
[data-s=daun] .progres{height:8px;border-radius:999px;background:var(--kartu-turun)}
[data-s=daun] .progres i{border-radius:999px}
[data-s=daun] .sub{color:var(--sinyal-gelap)}
[data-s=daun] .opsi-kotak{border-width:1px;border-radius:999px}
[data-s=daun] .opsi input:checked + .opsi-kotak{border-color:var(--sinyal);background:var(--sinyal-lembut)}
[data-s=daun] .opsi-nama{font-weight:700}
[data-s=daun] .opsi-harga{font-weight:700;color:var(--sinyal-gelap)}
[data-s=daun] .hari{border-radius:999px}
[data-s=daun] .hari .tg{font-size:24px;font-weight:700}
[data-s=daun] .jam-grid button{border-radius:999px}
[data-s=daun] .stepper{border-radius:999px}
[data-s=daun] .kolom input,[data-s=daun] .kolom textarea{border-radius:var(--r-kecil)}
[data-s=daun] .tinjau .total{border-top:2px solid var(--sinyal)}
[data-s=daun] .tinjau .total dd{font-size:26px;font-weight:700}
[data-s=daun] .selesai h3{font-size:28px;font-weight:700}
[data-s=daun] .kode{font-size:32px;font-weight:700;color:var(--sinyal-gelap)}
[data-s=daun] .menu-baris{border-radius:999px}
"""

TEMA_KOTAK = """
  --latar:#D8C2A0;
  --kartu:#EFE2CA;
  --kartu-turun:#C3A77E;
  --tinta:#1F180D;
  --tinta-redup:#4F3D26;
  --garis:#B69B71;
  --garis-halus:#C9B189;
  --garis-kuat:#795F3E;
  --sinyal:#1F4E7A;
  --sinyal-gelap:#153A5C;
  --sinyal-lembut:#D5E3EF;
  --di-atas-sinyal:#FFFFFF;
  --fokus:#153A5C;
  --salah:#9C2410;
  --ok:#3E6B3A;
  --r:14px;
  --r-kecil:10px;
  --r-tombol:10px;
  --lengkung:0px;
  --serif:"Rubik",system-ui,sans-serif;
  --bayang:0 1px 0 rgba(31,24,13,.2);
  --h-berat:600;
  --h-lebar:100%;
  --h-huruf:none;
  --h-ls:-.015em;
  --pole-tinggi:0px;
  --pole:none;
"""

GAYA_KOTAK = r"""
[data-s=kotak] :is(.hero h1,.bagian h2,.penutup h2){font-family:var(--serif);font-weight:600;font-stretch:100%;letter-spacing:-.015em}
[data-s=kotak] .hero{padding:20px 0 4px}
[data-s=kotak] .hero-isi{position:relative;padding:16px;border-radius:var(--r);background:var(--kartu);box-shadow:inset 0 0 0 1px var(--garis)}
[data-s=kotak] .hero-isi::before{content:"";position:absolute;width:auto;height:auto;inset:8px;border-radius:var(--r-kecil);border:2px dashed var(--garis-kuat);opacity:.5;pointer-events:none}
[data-s=kotak] .hero .eyebrow{font-size:12px;letter-spacing:.14em;color:var(--sinyal-gelap)}
[data-s=kotak] .hero h1{margin:10px 0 10px;font-size:clamp(32px,10vw,52px);line-height:1.04}
[data-s=kotak] .hero h1 em{font-style:normal;color:var(--sinyal-gelap)}
[data-s=kotak] .hero .lead{max-width:44ch}
[data-s=kotak] .hero-foto{position:relative;margin:18px 0 30px;border-radius:var(--r);overflow:hidden;background:var(--kartu-turun)}
[data-s=kotak] .hero-foto::after{content:"";position:absolute;inset:0;pointer-events:none;background:linear-gradient(var(--tinta) 0 0) center/2px 100% no-repeat,linear-gradient(var(--tinta) 0 0) center/100% 2px no-repeat;opacity:.18}
[data-s=kotak] .hero-foto img{display:block;width:100%;height:auto;aspect-ratio:16/11;object-fit:cover;filter:saturate(.92) contrast(1.02)}
[data-s=kotak] .lencana{position:absolute;left:10px;top:10px;padding:4px 10px;border-radius:999px;background:var(--sinyal);color:var(--di-atas-sinyal);font-size:12px;font-weight:600}
[data-s=kotak] .status{border:0;border-radius:999px;background:var(--kartu);box-shadow:var(--bayang)}
[data-s=kotak] .fakta{grid-template-columns:repeat(2,minmax(0,1fr));gap:8px;margin-top:20px}
[data-s=kotak] .fakta li{border:1px solid var(--garis);border-radius:var(--r-kecil);background:var(--kartu);padding:14px 12px}
[data-s=kotak] .fakta li:last-child{grid-column:1 / -1}
[data-s=kotak] .fakta .f-label{font-size:11px;letter-spacing:.1em;color:var(--sinyal-gelap)}
[data-s=kotak] .fakta .f-nilai{font-size:clamp(16px,4.6vw,21px);font-weight:600;line-height:1.1}
[data-s=kotak] .loncat a{border:1px solid var(--garis-kuat);border-radius:999px;background:var(--kartu)}
[data-s=kotak] .loncat a:hover{background:var(--sinyal);border-color:var(--sinyal);color:var(--di-atas-sinyal)}
[data-s=kotak] .demo-kartu{border:1px solid var(--garis);border-radius:var(--r);background:var(--kartu)}
[data-s=kotak] .bagian{padding:46px 0 4px}
[data-s=kotak] .bagian h2{font-size:clamp(26px,8vw,38px);font-weight:600;line-height:1.08}
[data-s=kotak] .bagian:not(.penutup) h2::after{content:"";display:block;width:100%;max-width:140px;height:8px;margin-top:12px;border-radius:3px;background:repeating-linear-gradient(90deg,var(--sinyal) 0 26px,transparent 26px 40px)}
[data-s=kotak] .bagian-lead{margin-top:12px}
[data-s=kotak] .kartu{border:1px solid var(--garis);border-radius:var(--r);background:var(--kartu);box-shadow:none}
[data-s=kotak] #harga .kartu{margin-top:20px;background:var(--kartu-turun);padding:10px}
[data-s=kotak] #harga .kartu > h3{padding:4px 6px 12px;font-size:13px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:var(--sinyal-gelap)}
[data-s=kotak] .harga{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px;margin-top:0}
[data-s=kotak] .harga li{grid-template-columns:minmax(0,1fr) auto;align-items:baseline;gap:2px 8px;padding:12px;border-radius:var(--r-kecil);background:var(--kartu)}
[data-s=kotak] .harga .nm{grid-column:1;font-weight:600;font-size:15px}
[data-s=kotak] .harga .hr{grid-column:2;font-weight:600;color:var(--sinyal-gelap);white-space:nowrap}
[data-s=kotak] .harga .ket{grid-column:1 / -1;font-size:12px;color:var(--tinta-redup)}
[data-s=kotak] .dur{display:block;grid-column:1;font-size:12px;color:var(--tinta-redup);background:none;padding:0;margin:0}
[data-s=kotak] .dur:empty{display:none}
[data-s=kotak] .ket-teks{display:block}
@media (max-width:519px){[data-s=kotak] .harga{grid-template-columns:1fr}}
[data-s=kotak] .galeri{grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;margin-top:22px}
[data-s=kotak] .petak{aspect-ratio:4/3;border-radius:18px;background:var(--kartu-turun);box-shadow:inset 0 0 0 3px var(--latar)}
[data-s=kotak] .petak img{filter:saturate(.95)}
[data-s=kotak] .petak figcaption{padding-top:6px;font-size:12px;color:var(--tinta-redup)}
[data-s=kotak] .petak:first-child,[data-s=kotak] .petak:last-child{grid-column:1 / -1;aspect-ratio:16/9}
[data-s=kotak] .jam li{padding:12px 10px;border-radius:var(--r-kecil)}
[data-s=kotak] .jam li.hari-ini{background:var(--sinyal-lembut);box-shadow:inset 3px 0 0 var(--sinyal);color:var(--sinyal-gelap)}
[data-s=kotak] .tanya{border-bottom:1px solid var(--garis)}
[data-s=kotak] .tanya details{border-top:1px solid var(--garis)}
[data-s=kotak] .tanya summary{min-height:56px;font-weight:600}
[data-s=kotak] .tanya summary svg{display:none}
[data-s=kotak] .tanya summary::after{content:"";margin-left:auto;width:16px;height:16px;border-radius:3px;background:var(--sinyal)}
[data-s=kotak] .tanya details[open] summary::after{background:none;border:3px solid var(--sinyal)}
[data-s=kotak] .penutup .kartu{border:1px solid var(--sinyal);border-radius:var(--r);background:var(--sinyal-lembut);padding:24px 18px}
[data-s=kotak] .penutup h2{font-size:clamp(26px,8vw,36px)}
[data-s=kotak] .menu-baris{border-radius:var(--r-kecil)}
"""

GAYA_KOTAK_WIZARD = r"""
[data-s=kotak] .kartu.pesan,[data-s=kotak] .kartu.pesan-buka{border:1px solid var(--garis);background:var(--kartu)}
[data-s=kotak] .kartu.pesan-buka > h3{font-size:24px;font-weight:600}
[data-s=kotak] .panel h3{font-size:26px;font-weight:600}
[data-s=kotak] .langkah-no{color:var(--sinyal-gelap)}
[data-s=kotak] .progres{height:8px;border-radius:4px;background:var(--kartu-turun)}
[data-s=kotak] .progres i{border-radius:4px}
[data-s=kotak] .sub{color:var(--sinyal-gelap)}
[data-s=kotak] .opsi-kotak{border-width:1px;border-radius:var(--r-kecil)}
[data-s=kotak] .opsi input:checked + .opsi-kotak{border-color:var(--sinyal);background:var(--sinyal-lembut)}
[data-s=kotak] .opsi-nama{font-weight:600}
[data-s=kotak] .opsi-harga{font-weight:600;color:var(--sinyal-gelap)}
[data-s=kotak] .hari{border-radius:var(--r-kecil)}
[data-s=kotak] .hari .tg{font-size:24px;font-weight:600}
[data-s=kotak] .jam-grid button{border-radius:var(--r-kecil)}
[data-s=kotak] .stepper{border-radius:var(--r-kecil)}
[data-s=kotak] .kolom input,[data-s=kotak] .kolom textarea{border-radius:var(--r-kecil)}
[data-s=kotak] .tinjau .total{border-top:2px solid var(--sinyal)}
[data-s=kotak] .tinjau .total dd{font-size:26px;font-weight:600}
[data-s=kotak] .selesai h3{font-size:28px;font-weight:600}
[data-s=kotak] .kode{font-size:32px;font-weight:600;color:var(--sinyal-gelap)}
[data-s=kotak] .menu-baris{border-radius:var(--r-kecil)}
"""

SKINS = {
    "katering": {
        "warung": dict(
            nama="Papan Tulis",
            ringkas="Hijau papan tulis dan kapur biru, judul tulisan tangan, daftar menu kapur, dan foto dijepit klip.",
            cocok="ingin kesan jujur, hangat, dan sederhana",
            tema=TEMA_WARUNG, warna="#1B2A23",
            css=GAYA_WARUNG, css_wizard=GAYA_WARUNG_WIZARD, font=FONT_CAVEATBRUSH, preload="caveat-brush-latin.woff2",
            hero_foto=("g1", "Tumpeng nasi kuning dengan lauk dan sayuran"),
            galeri=[("g3", "Hidangan prasmanan dalam wadah saji"), ("g5", "Kue mini di atas rak saji bertingkat"), ("g2", "Boks makanan siap antar di atas meja kayu"), ("g4", "Kue ulang tahun dengan lilin"), ("g6", "Pai dan roti kecil di atas piring"), ("g1", "Tumpeng nasi kuning dengan lauk dan sayuran")],
            galeri_dulu=False, varian={},
        ),
        "daun": dict(
            nama="Piring Daun",
            ringkas="Hijau muda dan merah cabai, foto bulat besar seperti piring, kartu menu dengan bulatan kecil, dan galeri piring bertumpuk.",
            cocok="ingin kesan segar, berselera, dan ramah",
            tema=TEMA_DAUN, warna="#EAF3E1",
            css=GAYA_DAUN, css_wizard=GAYA_DAUN_WIZARD, font=FONT_BRICOLAGE, preload="bricolage-grotesque-latin.woff2",
            hero_foto=("g1", "Tumpeng nasi kuning dengan lauk dan sayuran"),
            galeri=[("g1", "Tumpeng nasi kuning dengan lauk dan sayuran"), ("g3", "Hidangan prasmanan dalam wadah saji"), ("g2", "Boks makanan siap antar di atas meja kayu"), ("g5", "Kue mini di atas rak saji bertingkat"), ("g6", "Pai dan roti kecil di atas piring"), ("g4", "Kue ulang tahun dengan lilin")],
            galeri_dulu=False, varian={},
        ),
        "kotak": dict(
            nama="Kotak Bekal",
            ringkas="Warna kardus daur ulang dan biru tinta, sekat kotak bekal, dan menu dalam kompartemen rapi.",
            cocok="ingin kesan praktis, rapi, dan kekinian",
            tema=TEMA_KOTAK, warna="#D8C2A0",
            css=GAYA_KOTAK, css_wizard=GAYA_KOTAK_WIZARD, font=FONT_RUBIK, preload="rubik-latin.woff2",
            hero_foto=("g2", "Boks makanan siap antar di atas meja kayu"),
            galeri=[("g2", "Boks makanan siap antar di atas meja kayu"), ("g5", "Kue mini di atas rak saji bertingkat"), ("g3", "Hidangan prasmanan dalam wadah saji"), ("g6", "Pai dan roti kecil di atas piring"), ("g4", "Kue ulang tahun dengan lilin"), ("g1", "Tumpeng nasi kuning dengan lauk dan sayuran")],
            galeri_dulu=False, varian={},
        ),
    },
}
