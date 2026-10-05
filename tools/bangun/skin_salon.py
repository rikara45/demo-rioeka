FONT_BRICOLAGE = "@font-face{font-family:'Bricolage Grotesque';font-style:normal;font-weight:200 800;font-display:swap;src:url(/font/bricolage-grotesque-latin.woff2) format('woff2')}"

TEMA_SWATCH = """
  --latar:#F6F4EE;
  --kartu:#FFFFFF;
  --kartu-turun:#E9E6DC;
  --tinta:#14182B;
  --tinta-redup:#4A4F66;
  --garis:#D9D5C8;
  --garis-halus:#E5E1D5;
  --garis-kuat:#7A7F96;
  --sinyal:#2447D6;
  --sinyal-gelap:#1A35A8;
  --sinyal-lembut:#E3E8FB;
  --di-atas-sinyal:#FFFFFF;
  --fokus:#2447D6;
  --salah:#A8261A;
  --ok:#2F6B4F;
  --r:4px;
  --r-kecil:3px;
  --r-tombol:4px;
  --lengkung:0px;
  --serif:"Bricolage Grotesque",system-ui,sans-serif;
  --bayang:none;
  --h-berat:800;
  --h-lebar:100%;
  --h-huruf:none;
  --h-ls:-.02em;
  --pole-tinggi:0px;
  --pole:none;
"""

GAYA_SWATCH = r"""
/* salon, gaya swatch: blok warna datar, foto potong diagonal, bagan warna */
[data-s=swatch] :is(.hero h1,.bagian h2,.panel h3,.selesai h3,#harga .kartu > h3,.kartu.pesan-buka > h3,.f-nilai,.harga .hr,.hari .tg,.tinjau .total dd,.kode,.penutup h2,.lencana,.tanya summary){font-family:var(--serif);font-stretch:100%;letter-spacing:-.02em;text-transform:none}
[data-s=swatch] .hero{padding:20px 0 4px}
[data-s=swatch] .hero-isi::before{display:none}
[data-s=swatch] .hero .eyebrow{font-size:12px;letter-spacing:.16em;color:var(--sinyal-gelap)}
[data-s=swatch] .hero h1{margin:10px 0 6px;font-size:clamp(46px,14vw,84px);font-weight:800;line-height:.92;letter-spacing:-.035em;text-wrap:balance}
[data-s=swatch] .hero h1 em{font-style:normal;color:var(--sinyal)}
[data-s=swatch] .hero .lead{max-width:42ch;font-size:17px}
[data-s=swatch] .hero-foto{position:relative;isolation:isolate;margin:20px 0 34px}
[data-s=swatch] .hero-foto::before{content:"";position:absolute;z-index:-1;top:26%;bottom:-22px;left:22%;right:0;background:var(--sinyal)}
[data-s=swatch] .hero-foto img{display:block;width:100%;height:auto;aspect-ratio:4/3;object-fit:cover;object-position:60% 50%;background:var(--kartu-turun);clip-path:polygon(0 0,100% 0,100% 84%,0 100%)}
[data-s=swatch] .lencana{position:absolute;right:10px;bottom:-14px;max-width:60%;padding:6px 10px;background:var(--tinta);color:var(--latar);font-size:13px;font-weight:700;letter-spacing:.04em;line-height:1.2;text-transform:uppercase}
[data-s=swatch] .hero-foto + .tag-baris{margin-top:6px}
[data-s=swatch] .status{margin-top:8px;border-radius:var(--r);background:var(--kartu)}
[data-s=swatch] .fakta{grid-template-columns:repeat(3,minmax(0,1fr));gap:0;margin-top:24px}
[data-s=swatch] .fakta li{padding:14px 10px;border:0;border-radius:0;background:var(--kartu-turun)}
[data-s=swatch] .fakta li:first-child{background:var(--sinyal);color:var(--di-atas-sinyal)}
[data-s=swatch] .fakta li:first-child .f-label{color:var(--di-atas-sinyal)}
[data-s=swatch] .fakta li:nth-child(2){background:var(--sinyal-lembut)}
[data-s=swatch] .fakta .f-label{font-size:11px;letter-spacing:.1em}
[data-s=swatch] .fakta .f-nilai{font-size:clamp(15px,4.6vw,20px);font-weight:800;line-height:1.05;letter-spacing:-.02em}
[data-s=swatch] .loncat a{border:2px solid var(--tinta);border-radius:var(--r);background:var(--kartu)}
[data-s=swatch] .loncat a:hover{background:var(--sinyal);border-color:var(--sinyal);color:var(--di-atas-sinyal)}
[data-s=swatch] .demo-kartu{margin:24px 0 0;border-radius:var(--r)}

[data-s=swatch] .bagian{padding:52px 0 4px}
[data-s=swatch] .bagian h2{font-size:clamp(32px,9.5vw,46px);font-weight:800;line-height:.98;letter-spacing:-.03em}
[data-s=swatch] .bagian:not(.penutup) h2::before{content:"";display:block;width:54px;height:12px;margin-bottom:14px;background:linear-gradient(90deg,var(--sinyal) 0 33.4%,color-mix(in srgb,var(--sinyal) 55%,var(--latar)) 0 66.7%,color-mix(in srgb,var(--sinyal) 22%,var(--latar)) 0)}
[data-s=swatch] .bagian-lead{margin-top:12px}
[data-s=swatch] .kartu{border:1px solid var(--garis-kuat);border-radius:var(--r);box-shadow:none}

[data-s=swatch] #harga .kartu{margin-top:28px;padding:0;border:0;border-radius:0;background:none}
[data-s=swatch] #harga .kartu > h3{display:inline-block;padding:5px 12px;background:var(--tinta);color:var(--latar);font-size:15px;font-weight:700;letter-spacing:-.01em}
[data-s=swatch] .harga{margin-top:8px;counter-reset:chip}
[data-s=swatch] .harga li{grid-template-columns:22px minmax(0,1fr) auto;align-items:center;gap:2px 14px;padding:14px 0;border-top:0;border-bottom:1px solid var(--garis-kuat)}
[data-s=swatch] .harga li::before{content:"";grid-column:1;grid-row:1;width:22px;height:22px;background:var(--sinyal)}
[data-s=swatch] .harga li:nth-child(5n+2)::before{background:color-mix(in srgb,var(--sinyal) 78%,var(--latar))}
[data-s=swatch] .harga li:nth-child(5n+3)::before{background:color-mix(in srgb,var(--sinyal) 56%,var(--latar))}
[data-s=swatch] .harga li:nth-child(5n+4)::before{background:color-mix(in srgb,var(--sinyal) 34%,var(--latar))}
[data-s=swatch] .harga li:nth-child(5n+5)::before{background:color-mix(in srgb,var(--sinyal) 16%,var(--latar));box-shadow:inset 0 0 0 1px var(--garis-kuat)}
[data-s=swatch] .harga .nm{grid-column:2;font-size:17px;font-weight:700}
[data-s=swatch] .harga .hr{grid-column:3;grid-row:1;font-size:clamp(20px,6vw,26px);font-weight:800;line-height:1;letter-spacing:-.03em;text-align:right}
[data-s=swatch] .harga .ket{grid-column:2 / -1}
[data-s=swatch] .dur{display:inline;margin:0;padding:0;background:none;color:var(--sinyal-gelap);font-size:inherit;font-weight:700}
[data-s=swatch] .dur + .ket-teks::before{content:"\00A0\00B7\00A0"}

[data-s=swatch] #galeri{container-type:inline-size}
[data-s=swatch] .galeri{grid-template-columns:repeat(6,minmax(0,1fr));grid-auto-rows:calc(100cqw / 6 * .8);gap:0;margin-top:24px}
[data-s=swatch] .petak{position:relative;aspect-ratio:auto;overflow:hidden;border:3px solid var(--latar);border-radius:0;background:var(--kartu-turun)}
[data-s=swatch] .petak img{position:absolute;inset:0;width:100%;height:100%}
[data-s=swatch] .petak figcaption{position:absolute;left:0;bottom:0;max-width:100%;padding:4px 8px;background:var(--kartu);color:var(--tinta);font-size:12px;line-height:1.3}
[data-s=swatch] .petak:nth-child(1){grid-column:1 / 5;grid-row:1 / 4}
[data-s=swatch] .petak:nth-child(2){grid-column:4 / 7;grid-row:3 / 6}
[data-s=swatch] .petak:nth-child(3){grid-column:1 / 4;grid-row:5 / 8}
[data-s=swatch] .petak:nth-child(4){grid-column:3 / 7;grid-row:6 / 9}
[data-s=swatch] .petak:nth-child(5){grid-column:1 / 4;grid-row:7 / 10}
[data-s=swatch] .petak:nth-child(6){grid-column:4 / 7;grid-row:8 / 11}
[data-s=swatch] .petak:nth-child(1) img{object-position:50% 40%}

[data-s=swatch] #lokasi .kartu{margin-top:24px}
[data-s=swatch] .jam li{padding:13px 10px;border-radius:0}
[data-s=swatch] .jam li.hari-ini{background:var(--sinyal);color:var(--di-atas-sinyal);border-radius:var(--r)}
[data-s=swatch] .jam li.hari-ini .tanda-hari{background:var(--di-atas-sinyal);color:var(--sinyal-gelap)}

[data-s=swatch] .tanya{border-bottom:2px solid var(--tinta)}
[data-s=swatch] .tanya details{border-top:2px solid var(--tinta)}
[data-s=swatch] .tanya summary{min-height:60px;font-size:19px;font-weight:700;line-height:1.2}

[data-s=swatch] .penutup .kartu{padding:28px 20px;border:0;border-radius:var(--r);background:var(--sinyal);color:var(--di-atas-sinyal)}
[data-s=swatch] .penutup h2{font-size:clamp(30px,8.5vw,42px)}
[data-s=swatch] .penutup .bagian-lead{color:var(--di-atas-sinyal)}
[data-s=swatch] .penutup .tombol{background:var(--kartu);border-color:var(--kartu);color:var(--sinyal-gelap)}
[data-s=swatch] .penutup .tombol:hover{background:var(--sinyal-lembut);border-color:var(--sinyal-lembut)}
[data-s=swatch] .penutup .tombol.garis{background:transparent;border-color:var(--di-atas-sinyal);color:var(--di-atas-sinyal)}
[data-s=swatch] .penutup .tombol.garis:hover{background:var(--sinyal-gelap)}
[data-s=swatch] .penutup :focus-visible{outline-color:var(--di-atas-sinyal)}
"""

GAYA_SWATCH_WIZARD = r"""
[data-s=swatch] .kartu.pesan,[data-s=swatch] .kartu.pesan-buka{background:var(--kartu);border:2px solid var(--tinta)}
[data-s=swatch] .kartu.pesan-buka > h3{font-size:30px;font-weight:800;line-height:1;letter-spacing:-.03em}
[data-s=swatch] .panel h3{font-size:32px;font-weight:800;line-height:1;letter-spacing:-.03em}
[data-s=swatch] .langkah-no{color:var(--sinyal-gelap)}
[data-s=swatch] .progres{height:8px;border-radius:0;background:var(--sinyal-lembut)}
[data-s=swatch] .progres i{border-radius:0}
[data-s=swatch] .sub{color:var(--sinyal-gelap)}
[data-s=swatch] .opsi-kotak{border-width:2px;border-radius:var(--r)}
[data-s=swatch] .opsi input:checked + .opsi-kotak{border-color:var(--sinyal);background:var(--sinyal);color:var(--di-atas-sinyal)}
[data-s=swatch] .opsi input:checked + .opsi-kotak .opsi-ket{color:var(--di-atas-sinyal)}
[data-s=swatch] .opsi input:checked + .opsi-kotak .opsi-tanda{border-color:var(--di-atas-sinyal);background:transparent}
[data-s=swatch] .opsi-nama{font-weight:700}
[data-s=swatch] .opsi-harga{font-family:var(--serif);font-size:20px;font-weight:800;letter-spacing:-.02em}
[data-s=swatch] .panel[data-langkah=bayar] .opsi-harga{font-family:Archivo,system-ui,sans-serif;font-size:14px;font-weight:600;letter-spacing:0}
[data-s=swatch] .hari{border-radius:var(--r)}
[data-s=swatch] .hari .tg{font-size:28px;font-weight:800;line-height:1.05;letter-spacing:-.03em}
[data-s=swatch] .jam-grid button{border-radius:var(--r)}
[data-s=swatch] .stepper{border-radius:var(--r)}
[data-s=swatch] .kolom input,[data-s=swatch] .kolom textarea{border-radius:var(--r)}
[data-s=swatch] .tinjau .total{border-top:2px solid var(--tinta)}
[data-s=swatch] .tinjau .total dd{font-size:30px;font-weight:800;line-height:1;letter-spacing:-.03em}
[data-s=swatch] .selesai h3{font-size:38px;font-weight:800;line-height:1;letter-spacing:-.03em}
[data-s=swatch] .kode{font-size:42px;font-weight:800;line-height:1;letter-spacing:-.02em;color:var(--sinyal-gelap)}
"""

SKINS = {
    "salon": {
        "swatch": dict(
            nama="Swatch",
            ringkas="Terang dengan blok warna kobalt, foto dipotong miring, dan daftar harga seperti bagan warna.",
            cocok="ingin kesan berani, segar, dan modern",
            tema=TEMA_SWATCH, warna="#F6F4EE",
            css=GAYA_SWATCH, css_wizard=GAYA_SWATCH_WIZARD, font=FONT_BRICOLAGE, preload="bricolage-grotesque-latin.woff2",
            hero_foto=("g5", "Kuas mengoleskan cat rambut di atas foil aluminium"),
            galeri=[("g4", "Proses potong rambut"), ("g1", "Kursi stylist krem di depan dinding kayu"), ("g5", "Proses pewarnaan rambut"), ("g6", "Ruang salon dengan cermin berornamen putih dan kursi stylist hitam"), ("g2", "Meja cermin dan kursi"), ("g3", "Meja cuci")],
            galeri_dulu=False, varian={},
        ),
    },
}
