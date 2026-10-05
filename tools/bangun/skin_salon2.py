FONT_BIGSHOULDERS = "@font-face{font-family:'Big Shoulders Display';font-style:normal;font-weight:100 900;font-display:swap;src:url(/font/big-shoulders-display-latin.woff2) format('woff2')}"
FONT_SYNE = "@font-face{font-family:'Syne';font-style:normal;font-weight:400 800;font-display:swap;src:url(/font/syne-latin.woff2) format('woff2')}"
FONT_MONO = "@font-face{font-family:'Space Mono';font-style:normal;font-weight:400;font-display:swap;src:url(/font/space-mono-latin-400.woff2) format('woff2')}"
FONT_MONO_B = "@font-face{font-family:'Space Mono';font-style:normal;font-weight:700;font-display:swap;src:url(/font/space-mono-latin-700.woff2) format('woff2')}"
FONT_CAVEAT = "@font-face{font-family:'Caveat';font-style:normal;font-weight:400 700;font-display:swap;src:url(/font/caveat-600-latin.woff2) format('woff2')}"

TEMA_LOOKBOOK = """
  --latar:#EDEAE1;
  --kartu:#F8F6F0;
  --kartu-turun:#DED9CC;
  --tinta:#151E18;
  --tinta-redup:#4B544C;
  --garis:#CFC9BA;
  --garis-halus:#DFDACC;
  --garis-kuat:#6E756C;
  --sinyal:#1C5738;
  --sinyal-gelap:#123A26;
  --sinyal-lembut:#DCE6DA;
  --di-atas-sinyal:#F5F8F2;
  --fokus:#1C5738;
  --salah:#9C2410;
  --ok:#2F6B4F;
  --r:0px;
  --r-kecil:0px;
  --r-tombol:0px;
  --lengkung:0px;
  --serif:"Big Shoulders Display","Arial Narrow",system-ui,sans-serif;
  --bayang:0 1px 0 rgba(21,30,24,.2);
  --h-berat:800;
  --h-lebar:100%;
  --h-huruf:uppercase;
  --h-ls:-.005em;
  --pole-tinggi:0px;
  --pole:none;
"""

GAYA_LOOKBOOK = r"""
[data-s=lookbook] :is(.hero h1,.bagian h2,.panel h3,.selesai h3,#harga .kartu > h3,.kartu.pesan-buka > h3,.harga .hr,.hari .tg,.tinjau .total dd,.kode,.penutup h2,.lencana){font-family:var(--serif);font-weight:800;font-stretch:100%}
[data-s=lookbook] :is(.eyebrow,.f-label,.dur,.harga .hr,.langkah-no,.tag-anda,.petak figcaption){font-family:'Space Mono',monospace}
[data-s=lookbook] .hero{padding:18px 0 4px}
[data-s=lookbook] .hero-isi{position:relative;padding:0 0 4px;border-top:6px solid var(--tinta);border-bottom:2px solid var(--tinta)}
[data-s=lookbook] .hero-isi::before{display:none}
[data-s=lookbook] .hero .eyebrow{display:block;padding:6px 0;border-bottom:1px solid var(--garis-kuat);font-size:11px;letter-spacing:.16em;color:var(--sinyal-gelap)}
[data-s=lookbook] .hero h1{margin:10px 0 8px;font-size:clamp(52px,19vw,120px);font-weight:800;line-height:.82;letter-spacing:-.01em}
[data-s=lookbook] .hero h1 em{font-style:normal;color:var(--sinyal)}
[data-s=lookbook] .hero .lead{max-width:44ch;font-size:17px}
[data-s=lookbook] .hero-foto{position:relative;margin:16px 0 30px;border-top:2px solid var(--tinta);border-bottom:2px solid var(--tinta);padding:6px 0}
[data-s=lookbook] .hero-foto img{display:block;width:100%;height:auto;aspect-ratio:5/4;object-fit:cover;object-position:50% 45%;filter:grayscale(.12) contrast(1.05)}
[data-s=lookbook] .lencana{display:block;margin-top:6px;font-family:'Space Mono',monospace;font-size:12px;letter-spacing:.04em;color:var(--tinta-redup)}
[data-s=lookbook] .status{border:0;border-top:1px solid var(--garis-kuat);border-radius:0;background:none;font-family:'Space Mono',monospace;font-size:13px}
[data-s=lookbook] .fakta{gap:0;margin-top:20px;border-top:2px solid var(--tinta);border-bottom:2px solid var(--tinta)}
[data-s=lookbook] .fakta li{padding:12px 10px;border:0;border-left:1px solid var(--garis);border-radius:0;background:none}
[data-s=lookbook] .fakta li:first-child{border-left:0;padding-left:0}
[data-s=lookbook] .fakta .f-label{font-size:11px;letter-spacing:.1em}
[data-s=lookbook] .fakta .f-nilai{font-family:var(--serif);font-size:clamp(20px,6vw,30px);font-weight:800;line-height:1}
[data-s=lookbook] .loncat a{border:1px solid var(--tinta);border-radius:0;background:none}
[data-s=lookbook] .loncat a:hover{background:var(--tinta);color:var(--latar)}
[data-s=lookbook] .demo-kartu{border:0;border-top:2px solid var(--tinta);border-radius:0;background:none;padding:14px 0 0}
[data-s=lookbook] .bagian{padding:44px 0 4px}
[data-s=lookbook] .bagian h2{font-size:clamp(38px,13vw,72px);font-weight:800;line-height:.86;border-bottom:3px solid var(--tinta);padding-bottom:8px}
[data-s=lookbook] .bagian:not(.penutup) h2::before{content:"";display:none}
[data-s=lookbook] .bagian-lead{margin-top:12px}
[data-s=lookbook] .kartu{border:0;border-radius:0;background:none;box-shadow:none;padding:0}
[data-s=lookbook] #harga .kartu{margin-top:26px;border-top:2px solid var(--tinta);padding-top:8px}
[data-s=lookbook] #harga .kartu > h3{font-family:'Space Mono',monospace;font-size:12px;font-weight:700;letter-spacing:.14em;color:var(--sinyal-gelap)}
[data-s=lookbook] .harga{margin-top:4px}
[data-s=lookbook] .harga li{grid-template-columns:minmax(0,1fr) auto;gap:0 10px;padding:12px 0;border-top:1px solid var(--garis);align-items:baseline}
[data-s=lookbook] .harga li:first-child{border-top:0}
[data-s=lookbook] .harga .nm{display:flex;align-items:baseline;gap:8px;font-family:var(--serif);font-size:22px;font-weight:700;line-height:1.05;text-transform:uppercase}
[data-s=lookbook] .harga .nm::after{content:"";flex:1;min-width:14px;border-bottom:2px dotted var(--garis-kuat);transform:translateY(-4px)}
[data-s=lookbook] .harga .hr{font-size:15px;color:var(--tinta);white-space:nowrap}
[data-s=lookbook] .harga .ket{grid-column:1 / -1}
[data-s=lookbook] .dur{display:inline;margin:0;padding:0;background:none;color:var(--sinyal-gelap);font-size:12px;font-weight:400}
[data-s=lookbook] .dur + .ket-teks::before{content:"\00A0\00B7\00A0"}
[data-s=lookbook] .galeri{grid-template-columns:repeat(2,minmax(0,1fr));gap:0;margin-top:20px;border-top:1px solid var(--tinta)}
[data-s=lookbook] .petak{position:relative;aspect-ratio:4/3;border:0;border-bottom:1px solid var(--garis-kuat);border-radius:0;background:var(--kartu-turun);padding-bottom:26px}
[data-s=lookbook] .petak img{filter:grayscale(.15)}
[data-s=lookbook] .petak figcaption{position:absolute;left:0;bottom:4px;font-size:11px;color:var(--tinta-redup)}
[data-s=lookbook] .petak:nth-child(odd){border-right:1px solid var(--garis-kuat)}
[data-s=lookbook] .petak:first-child,[data-s=lookbook] .petak:last-child{grid-column:1 / -1;aspect-ratio:16/9;border-right:0}
[data-s=lookbook] .jam li{padding:12px 0;border-radius:0}
[data-s=lookbook] .jam li.hari-ini{background:none;box-shadow:inset 4px 0 0 var(--sinyal);font-weight:700}
[data-s=lookbook] .tanya{border-bottom:2px solid var(--tinta)}
[data-s=lookbook] .tanya details{border-top:1px solid var(--garis)}
[data-s=lookbook] .tanya summary{min-height:60px;font-family:var(--serif);font-size:26px;font-weight:700;text-transform:uppercase}
[data-s=lookbook] .tanya summary svg{display:none}
[data-s=lookbook] .tanya summary::after{content:"";margin-left:auto;width:16px;height:16px;border-right:3px solid var(--tinta);border-bottom:3px solid var(--tinta);transform:rotate(45deg) translateY(-4px)}
[data-s=lookbook] .tanya details[open] summary::after{transform:rotate(225deg) translateY(-2px)}
[data-s=lookbook] .penutup .kartu{border:2px solid var(--tinta);background:var(--kartu-turun);padding:24px 18px}
[data-s=lookbook] .penutup h2{font-size:clamp(40px,14vw,76px);line-height:.84}
"""

GAYA_LOOKBOOK_WIZARD = r"""
[data-s=lookbook] .kartu.pesan,[data-s=lookbook] .kartu.pesan-buka{border:1px solid var(--tinta);border-radius:0;background:var(--kartu)}
[data-s=lookbook] .kartu.pesan-buka > h3{font-size:34px;line-height:.9}
[data-s=lookbook] .panel h3{font-size:34px;line-height:.9;text-transform:uppercase}
[data-s=lookbook] .langkah-no{font-size:11px;letter-spacing:.14em;color:var(--sinyal-gelap)}
[data-s=lookbook] .progres{height:4px;border-radius:0;background:var(--kartu-turun)}
[data-s=lookbook] .progres i{border-radius:0}
[data-s=lookbook] .sub{color:var(--sinyal-gelap)}
[data-s=lookbook] .opsi-kotak{border-width:1px;border-radius:0}
[data-s=lookbook] .opsi input:checked + .opsi-kotak{border-color:var(--sinyal);background:var(--sinyal-lembut)}
[data-s=lookbook] .opsi-nama{font-weight:700}
[data-s=lookbook] .opsi-harga{font-family:var(--serif);font-size:22px;font-weight:700;color:var(--sinyal-gelap)}
[data-s=lookbook] .panel[data-langkah=bayar] .opsi-harga{font-family:'Space Mono',monospace;font-size:13px}
[data-s=lookbook] .hari{border-radius:0}
[data-s=lookbook] .hari .tg{font-size:26px}
[data-s=lookbook] .jam-grid button{border-radius:0}
[data-s=lookbook] .stepper{border-radius:0}
[data-s=lookbook] .kolom input,[data-s=lookbook] .kolom textarea{border-radius:0}
[data-s=lookbook] .tinjau .total{border-top:2px solid var(--tinta)}
[data-s=lookbook] .tinjau .total dd{font-size:30px}
[data-s=lookbook] .selesai h3{font-size:36px;line-height:.9}
[data-s=lookbook] .kode{font-family:'Space Mono',monospace;font-size:36px;letter-spacing:.1em;color:var(--sinyal-gelap)}
"""

TEMA_INDUSTRI = """
  --latar:#16171A;
  --kartu:#202124;
  --kartu-turun:#2A2B2F;
  --tinta:#F1EEE6;
  --tinta-redup:#B7B2A5;
  --garis:#3A3B40;
  --garis-halus:#2E2F34;
  --garis-kuat:#8C877A;
  --sinyal:#D6A21F;
  --sinyal-gelap:#E7BE55;
  --sinyal-lembut:#33291A;
  --di-atas-sinyal:#16171A;
  --fokus:#E7BE55;
  --salah:#FF9C87;
  --ok:#8FE0AE;
  --r:2px;
  --r-kecil:2px;
  --r-tombol:2px;
  --lengkung:0px;
  --serif:"Syne",system-ui,sans-serif;
  --bayang:none;
  --h-berat:800;
  --h-lebar:100%;
  --h-huruf:none;
  --h-ls:-.01em;
  --pole-tinggi:0px;
  --pole:none;
"""

GAYA_INDUSTRI = r"""
[data-s=industri] :is(.hero h1,.bagian h2,.panel h3,.selesai h3,.f-nilai,.harga .hr,.hari .tg,.tinjau .total dd,.kode,.penutup h2){font-family:var(--serif);font-weight:800;font-stretch:100%}
[data-s=industri] .hero-isi{position:relative;padding:22px 16px;border:1px solid var(--garis-kuat);background:linear-gradient(180deg,transparent,rgba(0,0,0,.15))}
[data-s=industri] .hero-isi::before{content:"";position:absolute;z-index:-1;width:auto;height:auto;inset:0;opacity:.5;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 120 104'%3E%3Cg fill='none' stroke='%23D6A21F' stroke-width='1.2'%3E%3Cpath d='M30 2 60 20v36L30 74 0 56V20z'/%3E%3Cpath d='M90 2l30 18v36L90 74 60 56V20z'/%3E%3Cpath d='M60 56l30 18v36L60 128 30 110V74z'/%3E%3C/g%3E%3C/svg%3E") right top/150px 130px no-repeat;pointer-events:none}
[data-s=industri] .hero .eyebrow{font-family:'Caveat',cursive;font-size:22px;font-weight:600;letter-spacing:0;text-transform:none;color:var(--sinyal-gelap)}
[data-s=industri] .hero h1{margin:6px 0 10px;font-size:clamp(38px,12vw,68px);line-height:.98;letter-spacing:-.02em}
[data-s=industri] .hero h1 em{font-style:normal;color:var(--sinyal)}
[data-s=industri] .hero .lead{max-width:46ch}
[data-s=industri] .hero-foto{position:relative;margin:18px 0 28px;border:1px solid var(--garis-kuat)}
[data-s=industri] .hero-foto img{display:block;width:100%;height:auto;aspect-ratio:16/10;object-fit:cover;filter:brightness(.72) contrast(1.1) saturate(.9)}
[data-s=industri] .lencana{position:absolute;left:10px;bottom:10px;padding:5px 10px;border:1px solid var(--sinyal);background:rgba(22,23,26,.72);color:var(--sinyal-gelap);font-size:12px;font-weight:700;letter-spacing:.08em;text-transform:uppercase}
[data-s=industri] .status{border:1px solid var(--garis-kuat);border-radius:0;background:var(--kartu)}
[data-s=industri] .fakta{gap:0;margin-top:20px;border:1px solid var(--garis-kuat)}
[data-s=industri] .fakta li{padding:12px 10px;border:0;border-radius:0;background:var(--kartu)}
[data-s=industri] .fakta li + li{border-left:1px solid var(--garis)}
[data-s=industri] .fakta .f-label{font-size:11px;letter-spacing:.14em;color:var(--sinyal-gelap)}
[data-s=industri] .fakta .f-nilai{font-size:clamp(16px,4.6vw,22px);font-weight:700;line-height:1.05;color:var(--tinta)}
[data-s=industri] .loncat a{border:1px solid var(--garis-kuat);border-radius:0;background:none}
[data-s=industri] .loncat a:hover{border-color:var(--sinyal);background:var(--sinyal);color:var(--di-atas-sinyal)}
[data-s=industri] .demo-kartu{border:1px solid var(--sinyal);border-radius:0;background:var(--kartu)}
[data-s=industri] .bagian{padding:46px 0 4px}
[data-s=industri] .bagian h2{font-size:clamp(28px,8.5vw,42px);line-height:1}
[data-s=industri] .bagian:not(.penutup) h2::after{content:"";display:block;width:56px;height:3px;margin-top:12px;background:var(--sinyal)}
[data-s=industri] .bagian-lead{margin-top:12px}
[data-s=industri] .kartu{border:1px solid var(--garis);border-radius:0;background:var(--kartu);box-shadow:none}
[data-s=industri] #harga .kartu{margin-top:24px;padding:0;border:1px solid var(--garis-kuat);background:none}
[data-s=industri] #harga .kartu > h3{padding:10px 12px;border-bottom:1px solid var(--garis-kuat);font-family:var(--serif);font-size:15px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--sinyal-gelap)}
[data-s=industri] .harga{margin:0;padding:0 12px}
[data-s=industri] .harga li{grid-template-columns:minmax(0,1fr) auto;gap:2px 12px;padding:13px 0;border-top:1px solid var(--garis-halus)}
[data-s=industri] .harga li:first-child{border-top:0}
[data-s=industri] .harga .nm{font-weight:600}
[data-s=industri] .harga .hr{font-size:19px;font-weight:800;color:var(--sinyal);white-space:nowrap}
[data-s=industri] .harga .ket{grid-column:1 / -1}
[data-s=industri] .dur{display:inline;margin:0;padding:0;background:none;color:var(--sinyal-gelap);font-size:13px;font-weight:700}
[data-s=industri] .dur + .ket-teks::before{content:"\00A0\00B7\00A0"}
[data-s=industri] .galeri{display:flex;gap:12px;overflow-x:auto;margin:24px -16px 0;padding:0 16px 12px;scroll-snap-type:x mandatory;scrollbar-width:thin}
[data-s=industri] .galeri .petak{flex:0 0 76%;max-width:320px;aspect-ratio:4/3;border:1px solid var(--garis-kuat);border-radius:0;background:var(--kartu-turun);scroll-snap-align:start}
[data-s=industri] .petak img{filter:brightness(.8) contrast(1.05) saturate(.85)}
[data-s=industri] .petak figcaption{padding-top:5px;font-size:12px;color:var(--tinta-redup)}
[data-s=industri] .jam li{padding:12px 10px;border-radius:0}
[data-s=industri] .jam li.hari-ini{background:var(--sinyal-lembut);box-shadow:inset 3px 0 0 var(--sinyal)}
[data-s=industri] .tanya{border-bottom:1px solid var(--garis-kuat)}
[data-s=industri] .tanya details{border-top:1px solid var(--garis)}
[data-s=industri] .tanya summary{min-height:58px;font-weight:700}
[data-s=industri] .tanya summary svg{display:none}
[data-s=industri] .tanya summary::after{content:"+";margin-left:auto;font-size:22px;color:var(--sinyal)}
[data-s=industri] .tanya details[open] summary::after{content:"\2212"}
[data-s=industri] .penutup .kartu{border:1px solid var(--garis-kuat);background:none;padding:24px 18px}
[data-s=industri] .penutup h2{font-size:clamp(28px,9vw,44px)}
[data-s=industri] .penutup .tombol{background:var(--sinyal);border-color:var(--sinyal);color:var(--di-atas-sinyal)}
@supports (animation-timeline:view()){
@media (prefers-reduced-motion:no-preference){
@keyframes ind{from{opacity:0;transform:translateY(16px)}to{opacity:1;transform:none}}
[data-s=industri] .bagian > h2{animation:ind linear both;animation-timeline:view();animation-range:entry 0% entry 60%}
}
}
"""

GAYA_INDUSTRI_WIZARD = r"""
[data-s=industri] .kartu.pesan,[data-s=industri] .kartu.pesan-buka{border:1px solid var(--garis-kuat);background:var(--kartu)}
[data-s=industri] .kartu.pesan-buka > h3{font-size:28px;line-height:1}
[data-s=industri] .panel h3{font-size:30px;line-height:1}
[data-s=industri] .langkah-no{letter-spacing:.14em;color:var(--sinyal-gelap)}
[data-s=industri] .progres{height:4px;border-radius:0;background:var(--kartu-turun)}
[data-s=industri] .progres i{border-radius:0}
[data-s=industri] .sub{color:var(--sinyal-gelap)}
[data-s=industri] .opsi-kotak{border-width:1px;border-radius:0}
[data-s=industri] .opsi input:checked + .opsi-kotak{border-color:var(--sinyal);background:var(--sinyal-lembut)}
[data-s=industri] .opsi-nama{font-weight:700}
[data-s=industri] .opsi-harga{font-family:var(--serif);font-size:18px;font-weight:700;color:var(--sinyal-gelap)}
[data-s=industri] .panel[data-langkah=bayar] .opsi-harga{font-family:Archivo,system-ui,sans-serif;font-size:14px}
[data-s=industri] .hari{border-radius:0}
[data-s=industri] .hari .tg{font-size:24px}
[data-s=industri] .jam-grid button{border-radius:0}
[data-s=industri] .stepper{border-radius:0}
[data-s=industri] .kolom input,[data-s=industri] .kolom textarea{border-radius:0}
[data-s=industri] .tinjau .total{border-top:1px solid var(--sinyal)}
[data-s=industri] .tinjau .total dd{font-size:28px;color:var(--sinyal-gelap)}
[data-s=industri] .selesai h3{font-size:32px}
[data-s=industri] .kode{font-size:36px;letter-spacing:.05em;color:var(--sinyal-gelap)}
"""

SKINS = {
    "salon": {
        "lookbook": dict(
            nama="Lookbook",
            ringkas="Koran krem-abu dan hijau tinta, huruf raksasa bertumpuk, daftar harga seperti daftar isi majalah.",
            cocok="ingin kesan editorial, artistik, dan berkelas",
            tema=TEMA_LOOKBOOK, warna="#EDEAE1",
            css=GAYA_LOOKBOOK, css_wizard=GAYA_LOOKBOOK_WIZARD,
            font=FONT_BIGSHOULDERS + "\n" + FONT_MONO, preload="big-shoulders-display-latin.woff2",
            hero_foto=("g6", "Ruang salon dengan cermin berornamen putih dan kursi stylist hitam"),
            galeri=[("g4", "Proses potong rambut"), ("g5", "Proses pewarnaan rambut"), ("g1", "Kursi stylist krem di depan dinding kayu"), ("g2", "Meja cermin dan kursi"), ("g3", "Meja cuci"), ("g6", "Ruang salon dengan cermin berornamen putih dan kursi stylist hitam")],
            galeri_dulu=False, varian={},
        ),
        "industri": dict(
            nama="Ruang Industri",
            ringkas="Arang gelap dan kuningan, garis heksagon, daftar menu rapi, dan galeri geser mendatar.",
            cocok="ingin kesan tegas, modern, dan premium",
            tema=TEMA_INDUSTRI, warna="#16171A",
            css=GAYA_INDUSTRI, css_wizard=GAYA_INDUSTRI_WIZARD,
            font=FONT_SYNE + "\n" + FONT_CAVEAT + "\n" + FONT_MONO, preload="syne-latin.woff2",
            hero_foto=("g1", "Kursi stylist krem di depan dinding kayu"),
            galeri=[("g1", "Kursi stylist krem di depan dinding kayu"), ("g5", "Proses pewarnaan rambut"), ("g2", "Meja cermin dan kursi"), ("g4", "Proses potong rambut"), ("g6", "Ruang salon dengan cermin berornamen putih dan kursi stylist hitam"), ("g3", "Meja cuci")],
            galeri_dulu=False, varian={},
        ),
    },
}
