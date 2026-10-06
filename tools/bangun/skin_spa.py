FONT_MARCELLUS = "@font-face{font-family:'Marcellus';font-style:normal;font-weight:400;font-display:swap;src:url(/font/marcellus-latin.woff2) format('woff2')}"
FONT_YOUNG = "@font-face{font-family:'Young Serif';font-style:normal;font-weight:400;font-display:swap;src:url(/font/young-serif-latin.woff2) format('woff2')}"
FONT_EPILOGUE = "@font-face{font-family:'Epilogue';font-style:normal;font-weight:300 600;font-display:swap;src:url(/font/epilogue-latin.woff2) format('woff2')}"

TEMA_LILIN = """
  --latar:#1A1411;
  --kartu:#241C18;
  --kartu-turun:#30251F;
  --tinta:#F4ECE3;
  --tinta-redup:#C4B4A7;
  --garis:#3D3029;
  --garis-halus:#2F251F;
  --garis-kuat:#93816F;
  --sinyal:#E7A87C;
  --sinyal-gelap:#F0BE9B;
  --sinyal-lembut:#34241A;
  --di-atas-sinyal:#1A1411;
  --fokus:#F0BE9B;
  --salah:#FF9C87;
  --ok:#8FE0AE;
  --r:0px;
  --r-kecil:0px;
  --r-tombol:0px;
  --lengkung:999px;
  --serif:"Marcellus",Georgia,serif;
  --bayang:none;
  --h-berat:400;
  --h-lebar:100%;
  --h-huruf:uppercase;
  --h-ls:.06em;
  --pole-tinggi:0px;
  --pole:none;
"""

GAYA_LILIN = r"""
[data-s=lilin] :is(.hero h1,.bagian h2,.panel h3,.selesai h3,#harga .kartu > h3,.kartu.pesan-buka > h3,.f-nilai,.harga .hr,.hari .tg,.tinjau .total dd,.kode,.penutup h2,.lencana,.tanya summary,.status){font-family:var(--serif);font-weight:400;font-stretch:100%;text-transform:uppercase;letter-spacing:.06em}
[data-s=lilin] .hero{padding:22px 0 4px}
[data-s=lilin] .hero-isi{position:relative;padding:24px 18px;text-align:center}
[data-s=lilin] .hero-isi::before{content:"";position:absolute;z-index:0;left:50%;top:40px;width:260px;height:260px;margin-left:-130px;border-radius:50%;background:radial-gradient(circle,rgba(231,168,124,.28),transparent 68%);pointer-events:none}
[data-s=lilin] .hero-isi > *{position:relative;z-index:1}
[data-s=lilin] .hero .eyebrow{font-size:11px;letter-spacing:.3em;color:var(--sinyal-gelap)}
[data-s=lilin] .hero h1{margin:14px 0 10px;font-size:clamp(40px,13vw,66px);line-height:1.05}
[data-s=lilin] .hero h1 em{font-style:normal;color:var(--sinyal)}
[data-s=lilin] .hero .lead{margin-left:auto;margin-right:auto;max-width:44ch}
[data-s=lilin] .hero .aksi{justify-items:stretch}
[data-s=lilin] .hero-foto{position:relative;isolation:isolate;margin:22px 0 30px}
[data-s=lilin] .hero-foto::after{content:"";position:absolute;inset:0;background:radial-gradient(ellipse at 50% 42%,transparent 34%,rgba(26,20,17,.72));pointer-events:none}
[data-s=lilin] .hero-foto img{display:block;width:100%;height:auto;aspect-ratio:4/5;object-fit:cover;filter:brightness(.78) contrast(1.08) saturate(.92);border-radius:var(--lengkung) var(--lengkung) 0 0}
[data-s=lilin] .lencana{position:absolute;z-index:2;left:50%;bottom:14px;transform:translateX(-50%);font-size:12px;letter-spacing:.2em;color:var(--sinyal-gelap)}
[data-s=lilin] .status{border:1px solid var(--garis-kuat);border-radius:999px;background:rgba(26,20,17,.6);font-size:12px}
[data-s=lilin] .fakta{gap:0;margin-top:22px;border-top:1px solid var(--garis);border-bottom:1px solid var(--garis)}
[data-s=lilin] .fakta li{text-align:center;padding:14px 8px;border:0;border-left:1px solid var(--garis);border-radius:0;background:none}
[data-s=lilin] .fakta li:first-child{border-left:0}
[data-s=lilin] .fakta .f-label{font-size:11px;letter-spacing:.2em;color:var(--sinyal-gelap)}
[data-s=lilin] .fakta .f-nilai{font-size:clamp(16px,4.6vw,21px)}
[data-s=lilin] .loncat{justify-content:safe center}
[data-s=lilin] .loncat a{border:1px solid var(--garis-kuat);border-radius:999px;background:none}
[data-s=lilin] .loncat a:hover{border-color:var(--sinyal);background:var(--sinyal);color:var(--di-atas-sinyal)}
[data-s=lilin] .demo-kartu{border:1px solid var(--garis-kuat);border-radius:0;background:var(--kartu)}
[data-s=lilin] .bagian{padding:50px 0 4px}
[data-s=lilin] .bagian-lead,[data-s=lilin] .bagian > .tag-baris{text-align:center;margin-left:auto;margin-right:auto}
[data-s=lilin] .bagian h2{font-size:clamp(30px,9vw,44px);text-align:center;line-height:1.05}
[data-s=lilin] .bagian:not(.penutup) h2::after{content:"";display:block;width:44px;height:1px;margin:14px auto 0;background:var(--sinyal)}
[data-s=lilin] .kartu{border:1px solid var(--garis);border-radius:0;background:none;box-shadow:none}
[data-s=lilin] #harga .kartu{margin-top:24px;padding:0;border:0}
[data-s=lilin] #harga .kartu > h3{text-align:center;padding-bottom:10px;border-bottom:1px solid var(--garis-kuat);font-size:14px}
[data-s=lilin] .harga{margin-top:2px}
[data-s=lilin] .harga li{display:flex;flex-wrap:wrap;align-items:baseline;gap:2px 12px;padding:14px 0;border-top:0;border-bottom:1px solid var(--garis)}
[data-s=lilin] .harga .nm{display:flex;flex:1 1 auto;flex-direction:column;gap:2px;order:1;min-width:60%}
[data-s=lilin] .harga .nm{font-family:var(--serif);font-size:19px;letter-spacing:.04em;text-transform:uppercase}
[data-s=lilin] .harga .dur{display:block;order:2;flex:1 1 100%;font-family:'Marcellus',serif;font-size:13px;letter-spacing:.16em;color:var(--sinyal-gelap);background:none;padding:0;margin:0}
[data-s=lilin] .harga .hr{order:3;margin-left:auto;font-size:22px;color:var(--tinta);white-space:nowrap}
[data-s=lilin] .harga .ket{order:4;flex:1 1 100%;font-size:13px;color:var(--tinta-redup)}
[data-s=lilin] .ket-teks{display:block}
[data-s=lilin] .harga .dur:empty{display:none}
[data-s=lilin] .galeri{grid-template-columns:repeat(3,minmax(0,1fr));gap:10px;margin-top:24px;align-items:start}
[data-s=lilin] .petak{aspect-ratio:3/4;border-radius:var(--lengkung) var(--lengkung) 0 0;background:var(--kartu-turun)}
[data-s=lilin] .petak img{filter:brightness(.85) contrast(1.06)}
[data-s=lilin] .petak:nth-child(2){margin-top:26px}
[data-s=lilin] .petak:nth-child(5){margin-top:26px}
[data-s=lilin] .petak figcaption{padding-top:6px;font-size:11px;line-height:1.35;color:var(--tinta-redup);text-align:center}
[data-s=lilin] .petak:first-child,[data-s=lilin] .petak:last-child{grid-column:1 / -1;aspect-ratio:16/9;margin-top:0}
[data-s=lilin] .jam li{padding:12px 10px;border-radius:0}
[data-s=lilin] .jam li.hari-ini{background:var(--sinyal-lembut);box-shadow:inset 3px 0 0 var(--sinyal)}
[data-s=lilin] .tanya{border-bottom:1px solid var(--garis-kuat)}
[data-s=lilin] .tanya details{border-top:1px solid var(--garis)}
[data-s=lilin] .tanya summary{min-height:58px;font-size:16px}
[data-s=lilin] .tanya summary svg{display:none}
[data-s=lilin] .tanya summary::after{content:"+";margin-left:auto;font-size:22px;color:var(--sinyal)}
[data-s=lilin] .tanya details[open] summary::after{content:"\2212"}
[data-s=lilin] .penutup .kartu{border:1px solid var(--garis-kuat);background:var(--sinyal-lembut);padding:26px 18px;text-align:center}
[data-s=lilin] .penutup h2{font-size:clamp(28px,8.5vw,40px)}
"""

GAYA_LILIN_WIZARD = r"""
[data-s=lilin] .kartu.pesan,[data-s=lilin] .kartu.pesan-buka{border:1px solid var(--garis-kuat);background:var(--kartu)}
[data-s=lilin] .kartu.pesan-buka > h3{font-size:24px}
[data-s=lilin] .panel h3{font-size:26px}
[data-s=lilin] .langkah-no{letter-spacing:.2em;color:var(--sinyal-gelap)}
[data-s=lilin] .progres{height:2px;border-radius:0;background:var(--kartu-turun)}
[data-s=lilin] .progres i{border-radius:0}
[data-s=lilin] .sub{color:var(--sinyal-gelap)}
[data-s=lilin] .opsi-kotak{border-width:1px;border-radius:0}
[data-s=lilin] .opsi input:checked + .opsi-kotak{border-color:var(--sinyal);background:var(--sinyal-lembut)}
[data-s=lilin] .opsi-nama{font-family:var(--serif);letter-spacing:.03em}
[data-s=lilin] .opsi-harga{font-family:var(--serif);font-size:22px;color:var(--sinyal-gelap)}
[data-s=lilin] .panel[data-langkah=bayar] .opsi-harga{font-family:Archivo,system-ui,sans-serif;font-size:14px}
[data-s=lilin] .hari{border-radius:0}
[data-s=lilin] .hari .tg{font-size:26px}
[data-s=lilin] .jam-grid button{border-radius:0}
[data-s=lilin] .stepper{border-radius:0}
[data-s=lilin] .st-nilai{font-family:var(--serif);font-size:26px}
[data-s=lilin] .kolom input,[data-s=lilin] .kolom textarea{border-radius:0}
[data-s=lilin] .tinjau .total{border-top:1px solid var(--sinyal)}
[data-s=lilin] .tinjau .total dd{font-size:28px;color:var(--sinyal-gelap)}
[data-s=lilin] .selesai h3{font-size:30px}
[data-s=lilin] .kode{font-size:34px;letter-spacing:.1em;color:var(--sinyal-gelap)}
"""

TEMA_JAMU = """
  --latar:#EAD7BF;
  --kartu:#F8EFE1;
  --kartu-turun:#DCC4A5;
  --tinta:#2A1A12;
  --tinta-redup:#5C4231;
  --garis:#CBAB88;
  --garis-halus:#DCC3A2;
  --garis-kuat:#8A6446;
  --sinyal:#B8542A;
  --sinyal-gelap:#8A3A18;
  --sinyal-lembut:#F3DACB;
  --di-atas-sinyal:#FFF6EE;
  --fokus:#8A3A18;
  --salah:#9C2410;
  --ok:#3E6B3A;
  --r:4px;
  --r-kecil:3px;
  --r-tombol:3px;
  --lengkung:0px;
  --serif:"Young Serif",Georgia,serif;
  --bayang:0 1px 0 rgba(42,26,18,.18);
  --h-berat:400;
  --h-lebar:100%;
  --h-huruf:none;
  --h-ls:-.005em;
  --pole-tinggi:0px;
  --pole:none;
"""

GAYA_JAMU = r"""
[data-s=jamu] :is(.hero h1,.bagian h2,.panel h3,.selesai h3,#harga .kartu > h3,.kartu.pesan-buka > h3,.f-nilai,.harga .hr,.hari .tg,.tinjau .total dd,.kode,.penutup h2,.lencana,.tanya summary,.harga .nm){font-family:var(--serif);font-weight:400;font-stretch:100%}
[data-s=jamu] .hero{padding:20px 0 4px}
[data-s=jamu] .hero-isi{position:relative;padding:16px;border:1px solid var(--garis-kuat);background:var(--kartu)}
[data-s=jamu] .hero-isi::before{content:"";position:absolute;z-index:-1;width:auto;height:auto;inset:-8px;border:1px solid var(--garis-kuat);pointer-events:none}
[data-s=jamu] .hero .eyebrow{font-size:12px;letter-spacing:.12em;color:var(--sinyal-gelap)}
[data-s=jamu] .hero h1{margin:10px 0 10px;font-size:clamp(34px,10.5vw,54px);line-height:1.03}
[data-s=jamu] .hero h1 em{font-style:normal;color:var(--sinyal)}
[data-s=jamu] .hero .lead{max-width:44ch}
[data-s=jamu] .hero-foto{position:relative;margin:18px 8px 30px 0;border:1px solid var(--garis-kuat);background:var(--kartu)}
[data-s=jamu] .hero-foto::before{content:"";position:absolute;z-index:1;top:-1px;right:-1px;width:56px;height:56px;background:var(--sinyal);-webkit-mask:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 56 56'%3E%3Cg fill='black'%3E%3Ccircle cx='28' cy='12' r='7'/%3E%3Ccircle cx='44' cy='28' r='7'/%3E%3Ccircle cx='28' cy='44' r='7'/%3E%3Ccircle cx='12' cy='28' r='7'/%3E%3C/g%3E%3C/svg%3E") center/contain no-repeat;mask:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 56 56'%3E%3Cg fill='black'%3E%3Ccircle cx='28' cy='12' r='7'/%3E%3Ccircle cx='44' cy='28' r='7'/%3E%3Ccircle cx='28' cy='44' r='7'/%3E%3Ccircle cx='12' cy='28' r='7'/%3E%3C/g%3E%3C/svg%3E") center/contain no-repeat}
[data-s=jamu] .hero-foto img{display:block;width:100%;height:auto;aspect-ratio:1;object-fit:cover;filter:saturate(.95) contrast(1.03)}
[data-s=jamu] .lencana{display:inline-block;margin-top:6px;padding:3px 9px;background:var(--sinyal-lembut);color:var(--sinyal-gelap);font-size:12px}
[data-s=jamu] .status{border:1px solid var(--garis-kuat);border-radius:0;background:var(--kartu)}
[data-s=jamu] .fakta{gap:8px;margin-top:20px}
[data-s=jamu] .fakta li{padding:12px 10px;border:1px solid var(--garis-kuat);border-radius:0;background:var(--kartu)}
[data-s=jamu] .fakta .f-label{font-size:11px;letter-spacing:.1em;color:var(--sinyal-gelap)}
[data-s=jamu] .fakta .f-nilai{font-size:clamp(16px,4.6vw,21px);line-height:1.05}
[data-s=jamu] .loncat a{border:1px solid var(--garis-kuat);border-radius:0;background:var(--kartu)}
[data-s=jamu] .loncat a:hover{background:var(--sinyal);border-color:var(--sinyal);color:var(--di-atas-sinyal)}
[data-s=jamu] .demo-kartu{border:1px solid var(--garis-kuat);border-radius:0;background:var(--sinyal-lembut)}
[data-s=jamu] .bagian{padding:46px 0 4px}
[data-s=jamu] .bagian h2{font-size:clamp(28px,8.5vw,40px);line-height:1.08}
[data-s=jamu] .bagian:not(.penutup) h2::after{content:"";display:block;width:48px;height:8px;margin-top:12px;background:var(--sinyal);-webkit-mask:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 48 8'%3E%3Cg fill='black'%3E%3Ccircle cx='4' cy='4' r='3.4'/%3E%3Ccircle cx='16' cy='4' r='3.4'/%3E%3Ccircle cx='28' cy='4' r='3.4'/%3E%3Ccircle cx='40' cy='4' r='3.4'/%3E%3C/g%3E%3C/svg%3E") left center/contain no-repeat;mask:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 48 8'%3E%3Cg fill='black'%3E%3Ccircle cx='4' cy='4' r='3.4'/%3E%3Ccircle cx='16' cy='4' r='3.4'/%3E%3Ccircle cx='28' cy='4' r='3.4'/%3E%3Ccircle cx='40' cy='4' r='3.4'/%3E%3C/g%3E%3C/svg%3E") left center/contain no-repeat}
[data-s=jamu] .bagian-lead{margin-top:12px}
[data-s=jamu] .kartu{border:1px solid var(--garis-kuat);border-radius:0;background:var(--kartu);box-shadow:none}
[data-s=jamu] #harga .kartu{margin-top:22px;background:var(--kartu)}
[data-s=jamu] #harga .kartu > h3{padding-bottom:8px;border-bottom:1px solid var(--garis-kuat);font-size:20px}
[data-s=jamu] .harga{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:0;margin-top:0}
[data-s=jamu] .harga li{grid-template-columns:auto minmax(0,1fr);align-items:baseline;gap:2px 8px;padding:12px 10px;border-top:1px solid var(--garis-halus)}
[data-s=jamu] .harga li::before{content:"";grid-column:1;grid-row:1;width:14px;height:14px;background:var(--sinyal);border-radius:50% 0}
[data-s=jamu] .harga li:nth-child(4n+2)::before{border-radius:0 50%;background:var(--sinyal-gelap)}
[data-s=jamu] .harga li:nth-child(4n+3)::before{background:none;border:2px solid var(--sinyal);transform:rotate(45deg)}
[data-s=jamu] .harga li:nth-child(4n+4)::before{border-radius:50%;background:linear-gradient(var(--sinyal),var(--sinyal-gelap))}
[data-s=jamu] .harga .nm{grid-column:2;font-size:15px;line-height:1.15}
[data-s=jamu] .harga .hr{grid-column:2;font-size:17px;color:var(--sinyal-gelap)}
[data-s=jamu] .harga .ket{grid-column:1 / -1;font-size:13px}
[data-s=jamu] .dur{display:inline;margin:0;padding:0;background:none;color:var(--tinta-redup);font-family:Archivo,sans-serif;font-size:12px}
[data-s=jamu] .dur + .ket-teks::before{content:"\00A0\00B7\00A0"}
[data-s=jamu] #harga .kartu:first-of-type .harga li:nth-child(n+5){display:grid}
@media (max-width:519px){[data-s=jamu] .harga{grid-template-columns:1fr}}
[data-s=jamu] .galeri{grid-template-columns:repeat(2,minmax(0,1fr));gap:18px 14px;margin-top:24px}
[data-s=jamu] .petak{aspect-ratio:auto;border-radius:0;background:none;overflow:visible}
[data-s=jamu] .petak img{height:auto;aspect-ratio:1;object-fit:cover;clip-path:polygon(50% 0,100% 50%,50% 100%,0 50%)}
[data-s=jamu] .petak figcaption{padding-top:6px;font-size:12px;text-align:center;color:var(--tinta-redup)}
[data-s=jamu] .jam li{padding:12px 10px;border-radius:0}
[data-s=jamu] .jam li.hari-ini{background:var(--sinyal-lembut);box-shadow:inset 3px 0 0 var(--sinyal)}
[data-s=jamu] .tanya{border-bottom:1px solid var(--garis-kuat)}
[data-s=jamu] .tanya details{border-top:1px solid var(--garis)}
[data-s=jamu] .tanya summary{min-height:58px;font-size:18px}
[data-s=jamu] .tanya summary svg{display:none}
[data-s=jamu] .tanya summary::after{content:"";margin-left:auto;width:12px;height:12px;background:var(--sinyal);border-radius:50% 0}
[data-s=jamu] .tanya details[open] summary::after{border-radius:50%}
[data-s=jamu] .penutup .kartu{border:1px solid var(--garis-kuat);background:var(--sinyal-lembut);padding:24px 18px}
[data-s=jamu] .penutup h2{font-size:clamp(26px,8vw,36px)}
"""

GAYA_JAMU_WIZARD = r"""
[data-s=jamu] .kartu.pesan,[data-s=jamu] .kartu.pesan-buka{border:1px solid var(--garis-kuat);background:var(--kartu)}
[data-s=jamu] .kartu.pesan-buka > h3{font-size:22px}
[data-s=jamu] .panel h3{font-size:24px}
[data-s=jamu] .langkah-no{color:var(--sinyal-gelap)}
[data-s=jamu] .progres{height:5px;border-radius:0;background:var(--kartu-turun)}
[data-s=jamu] .progres i{border-radius:0}
[data-s=jamu] .sub{color:var(--sinyal-gelap)}
[data-s=jamu] .opsi-kotak{border-width:1px;border-radius:0}
[data-s=jamu] .opsi input:checked + .opsi-kotak{border-color:var(--sinyal);background:var(--sinyal-lembut)}
[data-s=jamu] .opsi-nama{font-weight:700}
[data-s=jamu] .opsi-harga{font-family:var(--serif);font-size:18px;color:var(--sinyal-gelap)}
[data-s=jamu] .panel[data-langkah=bayar] .opsi-harga{font-family:Archivo,system-ui,sans-serif;font-size:14px}
[data-s=jamu] .hari{border-radius:0}
[data-s=jamu] .hari .tg{font-size:24px}
[data-s=jamu] .jam-grid button{border-radius:0}
[data-s=jamu] .stepper{border-radius:0}
[data-s=jamu] .kolom input,[data-s=jamu] .kolom textarea{border-radius:0}
[data-s=jamu] .tinjau .total{border-top:2px solid var(--sinyal)}
[data-s=jamu] .tinjau .total dd{font-size:26px}
[data-s=jamu] .tinjau .ubah{color:var(--sinyal-gelap)}
[data-s=jamu] .selesai h3{font-size:28px}
[data-s=jamu] .kode{font-size:32px;letter-spacing:.05em;color:var(--sinyal-gelap)}
"""

TEMA_BENING = """
  --latar:#F1F6F8;
  --kartu:#FFFFFF;
  --kartu-turun:#E2ECF1;
  --tinta:#0F1F2A;
  --tinta-redup:#47606E;
  --garis:#CBDBE3;
  --garis-halus:#DCE7EC;
  --garis-kuat:#78929F;
  --sinyal:#1F6C93;
  --sinyal-gelap:#154C68;
  --sinyal-lembut:#DBECF4;
  --di-atas-sinyal:#FFFFFF;
  --fokus:#154C68;
  --salah:#9C2410;
  --ok:#2F6B4F;
  --r:12px;
  --r-kecil:8px;
  --r-tombol:8px;
  --lengkung:0px;
  --serif:"Epilogue",system-ui,sans-serif;
  --bayang:0 1px 2px rgba(15,31,42,.04),0 8px 22px rgba(15,31,42,.05);
  --h-berat:500;
  --h-lebar:100%;
  --h-huruf:none;
  --h-ls:-.02em;
  --pole-tinggi:0px;
  --pole:none;
"""

GAYA_BENING = r"""
[data-s=bening] :is(.hero h1,.bagian h2,.panel h3,.selesai h3,.f-nilai,.harga .hr,.hari .tg,.tinjau .total dd,.kode,.penutup h2){font-family:var(--serif);font-weight:500;font-stretch:100%;letter-spacing:-.02em}
[data-s=bening] .hero{padding:20px 0 4px}
[data-s=bening] .hero-isi{position:relative}
[data-s=bening] .hero-isi::before{content:"";position:absolute;z-index:-1;left:-10px;top:-10px;width:120px;height:120px;background:var(--sinyal);opacity:.08;-webkit-mask:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 120 120'%3E%3Cg fill='none' stroke='black' stroke-width='4'%3E%3Cpath d='M2 60c20-16 40-16 60 0s40 16 58 0'/%3E%3Cpath d='M2 76c20-16 40-16 60 0s40 16 58 0'/%3E%3Cpath d='M2 92c20-16 40-16 60 0s40 16 58 0'/%3E%3C/g%3E%3C/svg%3E") left top/contain no-repeat;mask:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 120 120'%3E%3Cg fill='none' stroke='black' stroke-width='4'%3E%3Cpath d='M2 60c20-16 40-16 60 0s40 16 58 0'/%3E%3Cpath d='M2 76c20-16 40-16 60 0s40 16 58 0'/%3E%3Cpath d='M2 92c20-16 40-16 60 0s40 16 58 0'/%3E%3C/g%3E%3C/svg%3E") left top/contain no-repeat}
[data-s=bening] .hero .eyebrow{font-size:12px;letter-spacing:.18em;color:var(--sinyal-gelap)}
[data-s=bening] .hero h1{margin:10px 0 10px;font-size:clamp(34px,10.5vw,56px);font-weight:600;line-height:1.04}
[data-s=bening] .hero h1 em{font-style:normal;font-weight:300;color:var(--sinyal)}
[data-s=bening] .hero .lead{max-width:44ch}
[data-s=bening] .hero-foto{position:relative;margin:20px 0 28px;overflow:hidden;border-radius:var(--r);background:var(--kartu-turun)}
[data-s=bening] .hero-foto img{display:block;width:100%;height:auto;aspect-ratio:4/5;object-fit:cover;filter:saturate(.92) brightness(1.03)}
[data-s=bening] .lencana{position:absolute;left:10px;bottom:10px;padding:5px 10px;border-radius:999px;background:rgba(241,246,248,.86);color:var(--sinyal-gelap);font-size:12px;font-weight:600}
[data-s=bening] .status{border:0;border-radius:999px;background:var(--sinyal-lembut);color:var(--sinyal-gelap);font-weight:600}
[data-s=bening] .fakta{gap:10px;margin-top:20px}
[data-s=bening] .fakta li{padding:14px 12px;border:0;border-left:2px solid var(--sinyal);border-radius:0;background:var(--kartu)}
[data-s=bening] .fakta .f-label{font-size:11px;letter-spacing:.12em;color:var(--sinyal-gelap)}
[data-s=bening] .fakta .f-nilai{font-size:clamp(16px,4.6vw,21px);font-weight:600;line-height:1.05}
[data-s=bening] .loncat a{border:1px solid var(--garis-kuat);border-radius:999px;background:var(--kartu)}
[data-s=bening] .loncat a:hover{background:var(--sinyal);border-color:var(--sinyal);color:var(--di-atas-sinyal)}
[data-s=bening] .demo-kartu{border:1px solid var(--garis);border-radius:var(--r);background:var(--kartu)}
[data-s=bening] .bagian{padding:48px 0 4px;position:relative}
[data-s=bening] .bagian h2{font-size:clamp(26px,8vw,38px);font-weight:600;line-height:1.08}
[data-s=bening] .bagian:not(.penutup) h2::before{content:"";display:block;width:70px;height:8px;margin-bottom:12px;border-top:2px solid var(--sinyal);border-bottom:1px solid var(--sinyal);opacity:.5}
[data-s=bening] .bagian-lead{margin-top:10px}
[data-s=bening] .kartu{border:1px solid var(--garis);border-radius:var(--r);background:var(--kartu)}
[data-s=bening] #harga .kartu{margin-top:22px;background:var(--kartu)}
[data-s=bening] #harga .kartu > h3{padding-bottom:10px;border-bottom:2px solid var(--sinyal);font-size:15px;letter-spacing:.02em}
[data-s=bening] .harga{margin-top:4px}
[data-s=bening] .harga li{grid-template-columns:minmax(0,1fr) auto auto;align-items:baseline;gap:4px 14px;padding:14px 0;border-top:1px solid var(--garis-halus)}
[data-s=bening] .harga li:first-child{border-top:0}
[data-s=bening] .harga .nm{grid-column:1;font-weight:500;font-size:17px}
[data-s=bening] .harga .dur{display:block;grid-column:1;font-family:Archivo,sans-serif;font-size:12px;font-weight:400;color:var(--tinta-redup);background:none;padding:0;margin:0}
[data-s=bening] .harga .dur:empty{display:none}
[data-s=bening] .harga .hr{grid-column:3;grid-row:1;font-weight:600;color:var(--sinyal-gelap);white-space:nowrap}
[data-s=bening] .harga .ket{grid-column:1 / -1;font-size:13px}
[data-s=bening] .ket-teks{display:block}
[data-s=bening] .galeri{grid-template-columns:repeat(2,minmax(0,1fr));gap:10px;margin-top:24px}
[data-s=bening] .petak{aspect-ratio:1;border-radius:var(--r-kecil);background:var(--kartu-turun)}
[data-s=bening] .petak img{filter:saturate(.92)}
[data-s=bening] .petak figcaption{padding-top:5px;font-size:12px;color:var(--tinta-redup)}
[data-s=bening] .petak:first-child{grid-column:1 / -1;aspect-ratio:16/9}
[data-s=bening] .jam li{padding:12px 10px;border-radius:var(--r-kecil)}
[data-s=bening] .jam li.hari-ini{background:var(--sinyal-lembut);color:var(--sinyal-gelap);font-weight:600}
[data-s=bening] .tanya{border-bottom:1px solid var(--garis)}
[data-s=bening] .tanya details{border-top:1px solid var(--garis)}
[data-s=bening] .tanya summary{min-height:56px;font-weight:500}
[data-s=bening] .tanya summary svg{display:none}
[data-s=bening] .tanya summary::after{content:"";margin-left:auto;width:12px;height:12px;border-right:2px solid var(--sinyal);border-bottom:2px solid var(--sinyal);transform:rotate(45deg) translateY(-3px)}
[data-s=bening] .tanya details[open] summary::after{transform:rotate(225deg) translateY(-1px)}
[data-s=bening] .penutup .kartu{border:1px solid var(--garis-kuat);background:var(--sinyal-lembut);padding:24px 18px}
[data-s=bening] .penutup h2{font-size:clamp(26px,8vw,36px)}
@media (min-width:900px){
[data-s=bening] .hero-isi{display:grid;grid-template-columns:1.1fr .9fr;column-gap:32px;align-items:start}
[data-s=bening] .hero-isi > *{grid-column:1}
[data-s=bening] .hero-isi > .hero-foto{grid-column:2;grid-row:1 / span 30;position:sticky;top:84px;margin:0}
[data-s=bening] .hero-foto img{aspect-ratio:3/4}
}
@supports (animation-timeline:view()){
@media (prefers-reduced-motion:no-preference){
@keyframes ben{from{opacity:0;transform:translateY(14px)}to{opacity:1;transform:none}}
[data-s=bening] .bagian > h2{animation:ben linear both;animation-timeline:view();animation-range:entry 0% entry 60%}
}
}
"""

GAYA_BENING_WIZARD = r"""
[data-s=bening] .kartu.pesan,[data-s=bening] .kartu.pesan-buka{border:1px solid var(--garis);background:var(--kartu)}
[data-s=bening] .kartu.pesan-buka > h3{font-size:22px;font-weight:600}
[data-s=bening] .panel h3{font-size:24px;font-weight:600}
[data-s=bening] .langkah-no{color:var(--sinyal-gelap)}
[data-s=bening] .progres{height:6px;border-radius:999px;background:var(--kartu-turun)}
[data-s=bening] .progres i{border-radius:999px}
[data-s=bening] .sub{color:var(--sinyal-gelap)}
[data-s=bening] .opsi-kotak{border-width:1px;border-radius:var(--r-kecil)}
[data-s=bening] .opsi input:checked + .opsi-kotak{border-color:var(--sinyal);background:var(--sinyal-lembut)}
[data-s=bening] .opsi-nama{font-weight:600}
[data-s=bening] .opsi-harga{font-family:var(--serif);font-size:18px;font-weight:600;color:var(--sinyal-gelap)}
[data-s=bening] .panel[data-langkah=bayar] .opsi-harga{font-family:Archivo,system-ui,sans-serif;font-size:14px}
[data-s=bening] .hari{border-radius:var(--r-kecil)}
[data-s=bening] .hari .tg{font-size:24px;font-weight:600}
[data-s=bening] .jam-grid button{border-radius:var(--r-kecil)}
[data-s=bening] .stepper{border-radius:var(--r-kecil)}
[data-s=bening] .kolom input,[data-s=bening] .kolom textarea{border-radius:var(--r-kecil)}
[data-s=bening] .tinjau .total{border-top:1px solid var(--sinyal)}
[data-s=bening] .tinjau .total dd{font-size:26px;font-weight:600;color:var(--sinyal-gelap)}
[data-s=bening] .selesai h3{font-size:28px;font-weight:600}
[data-s=bening] .kode{font-size:32px;font-weight:600;color:var(--sinyal-gelap)}
"""

SKINS = {
    "spa": {
        "lilin": dict(
            nama="Lilin Malam",
            ringkas="Gelap temaram, aksen persik lilin, huruf kapital berjarak lebar, dan galeri tiga kolom bertingkat.",
            cocok="ingin kesan mewah, tenang, dan intim",
            tema=TEMA_LILIN, warna="#1A1411",
            css=GAYA_LILIN, css_wizard=GAYA_LILIN_WIZARD, font=FONT_MARCELLUS, preload="marcellus-latin.woff2",
            hero_foto=("g4", "Lilin dan handuk gulung di ruang perawatan"),
            galeri=[("g4", "Lilin dan handuk gulung"), ("g1", "Ruang pijat dengan tempat tidur perawatan"), ("g2", "Tangan terapis memijat lengan pelanggan"), ("g3", "Tetesan minyak esensial di telapak tangan"), ("g6", "Bak mandi dengan lilin di rak kayu"), ("g5", "Wadah lulur dan garam mandi")],
            galeri_dulu=False, varian={},
        ),
        "jamu": dict(
            nama="Jamu Nusantara",
            ringkas="Krem hangat dan terakota, bingkai persegi bersudut kawung, kartu rempah dua kolom, dan galeri belah ketupat.",
            cocok="ingin kesan hangat, alami, dan akrab",
            tema=TEMA_JAMU, warna="#EAD7BF",
            css=GAYA_JAMU, css_wizard=GAYA_JAMU_WIZARD, font=FONT_YOUNG, preload="young-serif-latin.woff2",
            hero_foto=("g3", "Tetesan minyak esensial di telapak tangan"),
            galeri=[("g5", "Wadah lulur dan garam mandi"), ("g6", "Bak mandi dengan lilin di rak kayu"), ("g2", "Tangan terapis memijat lengan pelanggan"), ("g1", "Ruang pijat dengan tempat tidur perawatan"), ("g4", "Lilin dan handuk gulung"), ("g3", "Tetesan minyak esensial di telapak tangan")],
            galeri_dulu=False, varian={},
        ),
        "bening": dict(
            nama="Air Bening",
            ringkas="Biru laut dingin, foto tinggi yang menemani saat digulir di desktop, garis tipis, dan garis kontur air.",
            cocok="ingin kesan bersih, profesional, dan lapang",
            tema=TEMA_BENING, warna="#F1F6F8",
            css=GAYA_BENING, css_wizard=GAYA_BENING_WIZARD, font=FONT_EPILOGUE, preload="epilogue-latin.woff2",
            hero_foto=("g1", "Ruang pijat bersih dengan tempat tidur perawatan"),
            galeri=[("g1", "Ruang pijat dengan tempat tidur perawatan"), ("g2", "Tangan terapis memijat lengan pelanggan"), ("g3", "Tetesan minyak esensial di telapak tangan"), ("g6", "Bak mandi dengan lilin di rak kayu"), ("g5", "Wadah lulur dan garam mandi"), ("g4", "Lilin dan handuk gulung")],
            galeri_dulu=False, varian={},
        ),
    },
}
