import glob, importlib, os, re
from css import (FONT_SERIF, FONT_FRAUNCES, FONT_INAP, GAYA_SALON, GAYA_SALON_WIZARD, GAYA_SPA, GAYA_SPA_WIZARD,
                 GAYA_KATERING, GAYA_KATERING_WIZARD, GAYA_BARBER, GAYA_BARBER_WIZARD, GAYA_INAP, GAYA_INAP_WIZARD,
                 TEMA, WARNA_TEMA)
from data import USAHABY

# Kunci tiap skin:
#   nama, ringkas (satu kalimat tampilan), cocok (lanjutan "Cocok untuk usaha yang ...")
#   tema (blok token CSS lengkap), warna (theme-color), css, css_wizard, font (@font-face), preload (berkas woff2 atau "")
#   hero_foto=(berkas, alt), galeri=[(berkas, alt)...] atau None (pakai galeri data.py), galeri_dulu (bool)
#   varian: dict flag kecil untuk perbedaan markup yang tak bisa lewat CSS


def _lama(jenis, nama, ringkas, cocok, tema, css, css_wizard, font, preload):
    u = USAHABY[jenis]
    return dict(
        nama=nama, ringkas=ringkas, cocok=cocok,
        tema=TEMA[tema], warna=WARNA_TEMA[tema],
        css=css, css_wizard=css_wizard, font=font, preload=preload,
        hero_foto=u["hero_foto"], galeri=None, galeri_dulu=bool(u.get("galeri_dulu")), varian={}, lama=True,
    )


SKIN = {
    "salon": {
        "butik": _lama("salon", "Butik", "Serif klasik, foto hero lengkung, warna rose yang hangat.",
                       "ingin kesan anggun, rapi, dan hangat", "salon", GAYA_SALON, GAYA_SALON_WIZARD, FONT_SERIF, "cormorant-garamond-latin.woff2"),
    },
    "barbershop": {
        "karcis": _lama("barbershop", "Karcis", "Gelap dengan aksen amber, kapital tegas, dan tiket antrean.",
                        "ingin kesan maskulin, tegas, dan rapi", "barber", GAYA_BARBER, GAYA_BARBER_WIZARD, "", "archivo-latin.woff2"),
    },
    "spa": {
        "tenang": _lama("spa", "Tenang", "Serba tengah, foto oval, dan ranting daun di atas judul.",
                        "ingin kesan tenang, bersih, dan menenangkan", "spa", GAYA_SPA, GAYA_SPA_WIZARD, FONT_SERIF, "cormorant-garamond-latin.woff2"),
    },
    "penginapan": {
        "kartukunci": _lama("penginapan", "Kartu Kunci", "Krem dan teal, jendela lengkung, serta foto lebar bergaya buku tamu.",
                            "ingin kesan hangat seperti penginapan butik", "inap", GAYA_INAP, GAYA_INAP_WIZARD, FONT_INAP, "instrument-serif-latin.woff2"),
    },
    "katering": {
        "hajatan": _lama("katering", "Hajatan", "Krem dan kunyit, tepi bergerigi, stempel, dan daftar harga bentuk nota.",
                         "ingin kesan meriah dan akrab seperti hajatan", "pesan", GAYA_KATERING, GAYA_KATERING_WIZARD, FONT_FRAUNCES, "fraunces-latin.woff2"),
    },
}

_DIR = os.path.dirname(os.path.abspath(__file__))
for _berkas in sorted(glob.glob(os.path.join(_DIR, "skin_*.py"))):
    _mod = importlib.import_module(os.path.splitext(os.path.basename(_berkas))[0])
    for _jenis, _skins in _mod.SKINS.items():
        SKIN[_jenis].update(_skins)

URUTAN = {
    "salon": ["butik", "swatch", "lookbook", "industri"],
    "barbershop": ["karcis", "poster", "lembar", "stiker"],
    "spa": ["tenang", "lilin", "jamu", "bening"],
    "penginapan": ["kartukunci", "arsitek", "paspor", "senja"],
    "katering": ["hajatan", "warung", "daun", "kotak"],
}
for _jenis, _urut in URUTAN.items():
    _ada = SKIN[_jenis]
    SKIN[_jenis] = {k: _ada[k] for k in _urut if k in _ada} | {k: v for k, v in _ada.items() if k not in _urut}

DEFAULT = {j: next(iter(s)) for j, s in SKIN.items()}


def chip(tema_css):
    out = []
    for kunci in ("--latar", "--sinyal", "--tinta"):
        m = re.search(re.escape(kunci) + r":\s*(#[0-9A-Fa-f]{3,8})", tema_css)
        out.append(m.group(1) if m else "transparent")
    return out


PILIH = """
.skin-daftar{display:grid;gap:16px;margin-top:22px}
@media (min-width:640px){.skin-daftar{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (min-width:1000px){.skin-daftar{grid-template-columns:repeat(4,minmax(0,1fr))}}
.skin-kartu{display:flex}
.skin-kartu > a{display:flex;flex-direction:column;flex:1;border:1px solid var(--garis);border-top:4px solid var(--jenis-aksen,var(--sinyal));border-radius:var(--r);background:var(--kartu);box-shadow:var(--bayang);color:inherit;text-decoration:none;overflow:hidden;transition:transform .15s,box-shadow .15s}
.skin-kartu > a:hover{transform:translateY(-3px);box-shadow:0 12px 28px rgba(22,34,30,.12)}
.skin-kartu > a:focus-visible{outline:3px solid var(--jenis-aksen,var(--sinyal));outline-offset:2px}
.skin-pratinjau{display:block;aspect-ratio:4/3;background:var(--kartu-turun);overflow:hidden}
.skin-pratinjau img{display:block;width:100%;height:100%;object-fit:cover;object-position:top}
.skin-contoh{display:grid;align-content:end;gap:8px;height:100%;padding:16px;background:var(--c1);color:var(--c3)}
.skin-contoh i{display:block;height:10px;width:60%;border-radius:99px;background:var(--c3);opacity:.7}
.skin-contoh i + i{width:40%;opacity:.4}
.skin-contoh b{display:block;width:64%;height:34px;border-radius:8px;background:var(--c2)}
.skin-isi{display:flex;flex-direction:column;gap:10px;flex:1;padding:16px}
.skin-nama{font-size:24px;font-weight:800;font-stretch:80%;line-height:1.1}
.skin-ringkas{font-size:15px;color:var(--tinta-redup)}
.skin-cocok{font-size:14px}
.skin-chip{display:flex;gap:6px}
.skin-chip i{display:block;width:22px;height:22px;border:1px solid var(--garis-kuat);border-radius:50%}
.skin-tombol{display:inline-flex;align-items:center;justify-content:center;gap:8px;min-height:48px;margin-top:auto;border-radius:var(--r-tombol);background:var(--jenis-aksen,var(--sinyal));color:var(--di-atas-sinyal);font-weight:700}
.skin-tombol .ikon{width:18px;height:18px}
.skin-satu{max-width:420px}
@media (prefers-reduced-motion:reduce){.skin-kartu > a{transition:none}.skin-kartu > a:hover{transform:none}}
"""

GANTI_SKIN = """
.demo-strip{flex-wrap:wrap;column-gap:12px;row-gap:0}
.demo-strip a{display:inline-flex;align-items:center;margin:-12px 0;padding:12px 4px;min-height:44px;color:inherit;font-weight:700;text-decoration:underline;text-underline-offset:3px;white-space:nowrap}
"""

KASAR = """
.hero h1{overflow-wrap:break-word;word-break:break-word}
.ganti-daftar li,.demo-judul,.demo-teks,.demo-paket,.tanya details p{overflow-wrap:anywhere;min-width:0}
.ganti-daftar .kini,.ganti-daftar .nanti{min-width:0;overflow-wrap:anywhere}
.fakta li,.harga li,.harga .nm,.harga .ket,.status{min-width:0}
.status{max-width:100%}
.status span{overflow-wrap:anywhere}
"""
