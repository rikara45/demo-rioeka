STATUS_JS = r"""
(function(){
  var J=__JAM__;
  var NH=["Minggu","Senin","Selasa","Rabu","Kamis","Jumat","Sabtu"];
  var kini=new Date(), hari=kini.getDay(), menitKini=kini.getHours()*60+kini.getMinutes();
  function mnt(t){var p=t.split(".");return (+p[0])*60+(+p[1])}
  function f(m){var j=Math.floor(m/60),s=m%60;return (j<10?"0":"")+j+"."+(s<10?"0":"")+s}
  var teks=document.getElementById("status-teks"), titik=document.getElementById("titik");
  var baris=document.querySelector('#kartu-jam [data-hari="'+hari+'"]');
  if(baris){baris.className="hari-ini";var t=document.createElement("span");t.className="tanda-hari";t.textContent="hari ini";baris.firstElementChild.appendChild(t)}
  var blok=J[hari];
  function berikut(){
    for(var n=1;n<=7;n++){var h=(hari+n)%7;if(J[h]){return NH[h]+" pukul "+J[h][0]}}
    return "";
  }
  if(blok&&menitKini>=mnt(blok[0])&&menitKini<mnt(blok[1])){
    teks.textContent="Buka sekarang, tutup pukul "+blok[1];titik.className="titik";
  }else if(blok&&menitKini<mnt(blok[0])){
    teks.textContent="Tutup. Buka hari ini pukul "+blok[0];titik.className="titik tutup";
  }else{
    teks.textContent="Tutup. Buka lagi "+berikut();titik.className="titik tutup";
  }
})();
"""

BAR_JS = r"""
(function(){
  var bar=document.getElementById("bar-bawah"), kartu=document.getElementById("pesan");
  if(!bar||!kartu||!window.IntersectionObserver){return}
  new IntersectionObserver(function(e){bar.classList.toggle("sembunyi",e[0].isIntersecting)}).observe(kartu);
})();
"""

BOOKING_JS = r"""
(function(){
  var D=__DATA__;
  var $=function(s,r){return (r||document).querySelector(s)};
  var $$=function(s,r){return [].slice.call((r||document).querySelectorAll(s))};
  var NH=["Minggu","Senin","Selasa","Rabu","Kamis","Jumat","Sabtu"];
  var NB=["Januari","Februari","Maret","April","Mei","Juni","Juli","Agustus","September","Oktober","November","Desember"];
  var redam=window.matchMedia&&window.matchMedia("(prefers-reduced-motion:reduce)").matches;
  function rp(n){return "Rp "+n.toLocaleString("id-ID")}
  function fmt(m){var j=Math.floor(m/60),s=m%60;return (j<10?"0":"")+j+"."+(s<10?"0":"")+s}
  function mnt(t){var p=t.split(".");return (+p[0])*60+(+p[1])}
  function kunci(d){return d.getFullYear()+"-"+String(d.getMonth()+1).padStart(2,"0")+"-"+String(d.getDate()).padStart(2,"0")}
  function acak(s){var h=0;for(var k=0;k<s.length;k++){h=(h*31+s.charCodeAt(k))>>>0}return (h%100)/100}
  function el(tag,cls,txt){var e=document.createElement(tag);if(cls){e.className=cls}if(txt!=null){e.textContent=txt}return e}
  function ikonCentang(){var n="http://www.w3.org/2000/svg",s=document.createElementNS(n,"svg");s.setAttribute("class","ikon");s.setAttribute("viewBox","0 0 24 24");s.setAttribute("aria-hidden","true");var p=document.createElementNS(n,"path");p.setAttribute("d","M20 6 9 17l-5-5");s.appendChild(p);return s}

  var S={layanan:null,stylist:null,tgl:null,jam:null,nama:"",wa:"",cara:null};
  var LANGKAH=[["layanan","Layanan"],["stylist",D.noun],["waktu","Waktu"],["data","Data Anda"],["tinjau","Periksa"]];
  if(D.bayar){LANGKAH.push(["bayar","Pembayaran"])}
  var IDX={};LANGKAH.forEach(function(l,n){IDX[l[0]]=n});
  var i=0, dariTinjau=false, mulai=true;

  var kartu=$("#pesan"), alur=$("#alur"), selesaiEl=$("#selesai");
  var btnLanjut=$("#lanjut"), btnKembali=$("#kembali"), barisAksi=$("#baris-aksi");
  var mini=$("#mini"), pesanSistem=$("#pesan-sistem");
  var panel={};$$(".panel[data-langkah]",alur).forEach(function(p){panel[p.dataset.langkah]=p});

  function tanggalTeks(d){return NH[d.getDay()]+", "+d.getDate()+" "+NB[d.getMonth()]}
  function waktuTeks(){return S.tgl&&S.jam!==null?tanggalTeks(S.tgl.d)+", pukul "+fmt(S.jam):""}
  function muka(){return Math.round(S.layanan.harga*0.3/500)*500}

  /* langkah 1: layanan */
  (function(){
    var kotak=$("#pilih-layanan");
    D.grup.forEach(function(g){
      kotak.appendChild(el("h4","sub",g.nama));
      var daftar=el("div","opsi-daftar");
      g.item.forEach(function(l){
        var lb=el("label","opsi"), inp=el("input"), kk=el("span","opsi-kotak");
        inp.type="radio";inp.name="layanan";inp.value=l.nama;
        kk.appendChild(el("span","opsi-tanda"));
        kk.appendChild(el("span","opsi-nama",l.nama));
        kk.appendChild(el("span","opsi-harga",rp(l.harga)));
        kk.appendChild(el("span","opsi-ket","Sekitar "+l.menit+" menit"+(l.ket?" · "+l.ket:"")));
        lb.appendChild(inp);lb.appendChild(kk);daftar.appendChild(lb);
        inp.addEventListener("change",function(){S.layanan=l;bersih();perbarui()});
      });
      kotak.appendChild(daftar);
    });
  })();

  /* langkah 2: stylist */
  (function(){
    var kotak=$("#pilih-stylist"), daftar=el("div","opsi-daftar");
    [{nama:D.siapaSaja,keahlian:D.siapaSajaKet,rinci:""}].concat(D.stylist).forEach(function(s){
      var lb=el("label","opsi"), inp=el("input"), kk=el("span","opsi-kotak");
      inp.type="radio";inp.name="stylist";inp.value=s.nama;
      kk.appendChild(el("span","opsi-tanda"));
      kk.appendChild(el("span","opsi-nama",s.nama));
      kk.appendChild(el("span","opsi-ket",[s.keahlian,s.rinci].filter(Boolean).join(" · ")));
      lb.appendChild(inp);lb.appendChild(kk);daftar.appendChild(lb);
      inp.addEventListener("change",function(){S.stylist=s.nama;bersih();perbarui()});
    });
    kotak.appendChild(daftar);
  })();

  /* langkah 3: tanggal dan jam */
  var hariKotak=$("#pilih-hari"), jamKotak=$("#pilih-jam"), jamJudul=$("#jam-judul");
  for(var n=0;n<14;n++){(function(n){
    var t=new Date();t.setHours(0,0,0,0);t.setDate(t.getDate()+n);
    var blok=D.jam[String(t.getDay())];
    var b=el("button","hari");b.type="button";b.disabled=!blok;b.setAttribute("aria-pressed","false");
    b.appendChild(el("span","hr",n===0?"Hari ini":NH[t.getDay()].slice(0,3)));
    b.appendChild(el("span","tg",String(t.getDate())));
    b.appendChild(el("span","bl",blok?NB[t.getMonth()].slice(0,3):"Tutup"));
    b.setAttribute("aria-label",tanggalTeks(t)+(blok?"":", tutup"));
    b.addEventListener("click",function(){
      $$("button",hariKotak).forEach(function(x){x.setAttribute("aria-pressed","false")});
      b.setAttribute("aria-pressed","true");
      S.tgl={d:t,kunci:kunci(t),blok:blok};S.jam=null;gambarJam();bersih();perbarui();
    });
    hariKotak.appendChild(b);
  })(n)}

  function gambarJam(){
    jamKotak.textContent="";
    if(!S.tgl||!S.tgl.blok){jamJudul.textContent="Pilih tanggal dulu";return}
    var b=S.tgl.blok, sekarang=new Date(), a=[], tersedia=0;
    for(var m=mnt(b[0]);m+30<=mnt(b[1]);m+=30){a.push(m)}
    a.forEach(function(m){
      var x=el("button",null,fmt(m));x.type="button";x.setAttribute("aria-pressed","false");
      var lewat=S.tgl.kunci===kunci(sekarang)&&m<=sekarang.getHours()*60+sekarang.getMinutes();
      var penuh=acak(S.tgl.kunci+"#"+m)<0.22;
      x.disabled=lewat||penuh;
      if(penuh){x.setAttribute("aria-label",fmt(m)+", sudah terisi")}
      else if(lewat){x.setAttribute("aria-label",fmt(m)+", sudah lewat")}
      else{tersedia++}
      x.addEventListener("click",function(){
        $$("button",jamKotak).forEach(function(y){y.setAttribute("aria-pressed","false")});
        x.setAttribute("aria-pressed","true");S.jam=m;bersih();perbarui();
      });
      jamKotak.appendChild(x);
    });
    jamJudul.textContent=tersedia?"Pilih jam, "+tanggalTeks(S.tgl.d):"Semua jam hari ini sudah terisi atau lewat. Pilih hari lain.";
  }
  (function(){
    var tombol=$$("button",hariKotak);
    for(var k=0;k<tombol.length;k++){
      if(tombol[k].disabled){continue}
      tombol[k].click();
      if($$("button:not(:disabled)",jamKotak).length>=2){break}
    }
    S.jam=null;$$("button",jamKotak).forEach(function(y){y.setAttribute("aria-pressed","false")});
  })();
  function gulirHari(){
    var p=$('button[aria-pressed="true"]',hariKotak);
    if(p){hariKotak.scrollLeft=Math.max(0,p.offsetLeft-16)}
  }

  /* langkah 4: data */
  var inNama=$("#nama"), inWa=$("#wa");
  function salahDi(inp,pesan){
    var id=inp.id+"-salah", e=document.getElementById(id);
    if(!pesan){
      inp.removeAttribute("aria-invalid");inp.removeAttribute("aria-describedby");
      if(e){e.remove()}
      return;
    }
    if(!e){e=el("span","salah");e.id=id;inp.parentNode.appendChild(e)}
    e.textContent=pesan;inp.setAttribute("aria-invalid","true");inp.setAttribute("aria-describedby",id);
  }
  function namaOk(){return S.nama.length>=2}
  function waOk(){return S.wa.replace(/\D/g,"").length>=9}
  inNama.addEventListener("input",function(){S.nama=this.value.trim();salahDi(inNama,"");bersih();perbarui()});
  inWa.addEventListener("input",function(){S.wa=this.value.replace(/[^0-9+]/g,"");salahDi(inWa,"");bersih();perbarui()});
  [inNama,inWa].forEach(function(x){x.addEventListener("keydown",function(e){if(e.key==="Enter"){e.preventDefault();btnLanjut.click()}})});

  /* langkah 5: tinjau */
  var tinjauEl=$("#tinjau");
  function barisTinjau(label,nilai,langkah){
    var d=el("div"), dt=el("dt",null,label), dd=el("dd",null,nilai);
    d.appendChild(dt);d.appendChild(dd);
    if(langkah){
      var u=el("button","ubah","Ubah");u.type="button";
      u.setAttribute("aria-label","Ubah "+label.toLowerCase());
      u.addEventListener("click",function(){dariTinjau=true;pergi(IDX[langkah],true)});
      d.appendChild(u);
    }
    return d;
  }
  function isiTinjau(){
    tinjauEl.textContent="";
    tinjauEl.appendChild(barisTinjau("Layanan",S.layanan.nama+", "+rp(S.layanan.harga),"layanan"));
    tinjauEl.appendChild(barisTinjau(D.noun,S.stylist,"stylist"));
    tinjauEl.appendChild(barisTinjau("Waktu",waktuTeks(),"waktu"));
    tinjauEl.appendChild(barisTinjau("Nama",S.nama,"data"));
    tinjauEl.appendChild(barisTinjau("WhatsApp",S.wa,"data"));
    var rw=barisTinjau("Bayar muka 30 persen",D.bayar?rp(muka()):"");
    if(D.bayar){rw.className="rw";tinjauEl.appendChild(rw)}
    var tot=barisTinjau("Harga layanan",rp(S.layanan.harga));tot.className="total";tinjauEl.appendChild(tot);
  }

  /* langkah 6: bayar (paket 3) */
  function isiBayar(){
    var a=$("#b-total"), b=$("#b-muka");
    if(a){a.textContent=rp(S.layanan.harga)}
    if(b){b.textContent=rp(muka())}
  }
  $$('input[name="cara"]').forEach(function(r){
    r.addEventListener("change",function(){
      S.cara=r.value;
      var pq=$("#panel-qris"), pt=$("#panel-transfer");
      if(pq){pq.hidden=r.value!=="qris"}
      if(pt){pt.hidden=r.value!=="transfer"}
      bersih();perbarui();
    });
  });

  /* inti alur */
  function galat(id){
    if(id==="layanan"){return S.layanan?"":"Pilih satu layanan untuk lanjut."}
    if(id==="stylist"){return S.stylist?"":"Pilih "+D.noun.toLowerCase()+", atau pilih "+D.siapaSaja.toLowerCase()+"."}
    if(id==="waktu"){return !S.tgl?"Pilih tanggal dulu.":(S.jam===null?"Pilih jam yang masih kosong.":"")}
    if(id==="data"){return !namaOk()?"Isi nama Anda untuk lanjut.":(!waOk()?"Nomor WhatsApp belum lengkap.":"")}
    if(id==="bayar"){return S.cara?"":"Pilih cara bayar untuk lanjut."}
    return "";
  }
  function bersih(){pesanSistem.textContent=""}
  function labelLanjut(id){
    if(id==="tinjau"){return D.bayar?"Lanjut ke pembayaran":"Konfirmasi pesanan"}
    if(id==="bayar"){return S.cara==="tempat"?"Konfirmasi, bayar di tempat":(S.cara==="transfer"?"Saya sudah transfer":(S.cara==="qris"?"Saya sudah bayar":"Konfirmasi pembayaran"))}
    return "Lanjut";
  }
  function ringkasMini(id){
    var p=[];
    if(S.layanan&&id!=="layanan"){p.push(S.layanan.nama+" "+rp(S.layanan.harga))}
    if(S.stylist&&IDX[id]>IDX.stylist){p.push(S.stylist)}
    if(S.jam!==null&&IDX[id]>IDX.waktu){p.push(waktuTeks())}
    return p.join(" · ");
  }
  function perbarui(){
    var id=LANGKAH[i][0], g=galat(id), total=LANGKAH.length;
    $("#l-no").textContent="Langkah "+(i+1)+" dari "+total;
    $("#l-nama").textContent=LANGKAH[i][1];
    $("#progres-isi").style.width=((i+1)/total*100)+"%";
    $("#progres").setAttribute("aria-valuenow",String(i+1));
    $("#progres").setAttribute("aria-valuetext","Langkah "+(i+1)+" dari "+total+", "+LANGKAH[i][1]);
    btnLanjut.textContent=labelLanjut(id);
    btnLanjut.setAttribute("aria-disabled",g?"true":"false");
    barisAksi.className="baris-aksi"+(i===0?" tanpa-kembali":"");
    btnKembali.hidden=i===0;
    if(g){mini.innerHTML="";mini.textContent=g}
    else{
      mini.textContent="";var r=ringkasMini(id);
      if(r){mini.textContent=r}
      else if(id==="layanan"&&S.layanan){mini.textContent=S.layanan.nama+" · "+rp(S.layanan.harga)}
    }
    mini.hidden=!mini.textContent;
  }
  function pergi(n,fokus){
    i=n;
    LANGKAH.forEach(function(l,k){panel[l[0]].hidden=k!==i});
    var id=LANGKAH[i][0];
    if(id==="waktu"){gulirHari()}
    if(id==="tinjau"){isiTinjau()}
    if(id==="bayar"){isiBayar()}
    bersih();perbarui();
    if(mulai){return}
    var h=$("h3",panel[id]);
    if(h){h.focus({preventScroll:true})}
    var r=kartu.getBoundingClientRect();
    if(r.top<60||r.top>window.innerHeight*0.5){kartu.scrollIntoView({block:"start",behavior:redam?"auto":"smooth"})}
  }
  function fokusKeSalah(id){
    var f=null;
    if(id==="layanan"){f=$('input[name="layanan"]')}
    else if(id==="stylist"){f=$('input[name="stylist"]')}
    else if(id==="waktu"){f=!S.tgl?$("button:not(:disabled)",hariKotak):$("button:not(:disabled)",jamKotak)}
    else if(id==="data"){f=!namaOk()?inNama:inWa}
    else if(id==="bayar"){f=$('input[name="cara"]')}
    if(f){f.focus()}
  }
  btnLanjut.addEventListener("click",function(){
    var id=LANGKAH[i][0];
    if(btnLanjut.getAttribute("aria-busy")==="true"){return}
    var g=galat(id);
    if(g){
      if(id==="data"){
        salahDi(inNama,namaOk()?"":"Isi nama supaya kami tahu harus memanggil siapa.");
        salahDi(inWa,waOk()?"":"Isi nomor yang aktif di WhatsApp. Contoh: 0812 3456 7890");
      }else{pesanSistem.textContent=g}
      fokusKeSalah(id);
      return;
    }
    if(id==="tinjau"&&!D.bayar){selesaiPesan("Bayar di tempat",btnLanjut);return}
    if(id==="bayar"){
      var cara=S.cara==="qris"?"QRIS, bayar muka lunas":(S.cara==="transfer"?"Transfer, bayar muka lunas":"Bayar di tempat");
      selesaiPesan(cara,btnLanjut);return;
    }
    if(dariTinjau){dariTinjau=false;pergi(IDX.tinjau,true);return}
    pergi(i+1,true);
  });
  btnKembali.addEventListener("click",function(){
    if(dariTinjau){dariTinjau=false;pergi(IDX.tinjau,true);return}
    pergi(i-1,true);
  });

  function kode(){
    var t=S.tgl.d;
    return D.kode+"-"+String(t.getDate()).padStart(2,"0")+String(t.getMonth()+1).padStart(2,"0")+"-"+fmt(S.jam).replace(".","");
  }
  function selesaiPesan(cara,tombol){
    tombol.setAttribute("aria-busy","true");tombol.textContent="Memproses…";
    setTimeout(function(){
      tombol.removeAttribute("aria-busy");
      alur.hidden=true;selesaiEl.hidden=false;
      var c=$("#k-centang");c.textContent="";c.appendChild(ikonCentang());
      $("#k-kode").textContent=kode();
      var rk=$("#k-ringkas");rk.textContent="";
      [["Layanan",S.layanan.nama+", "+rp(S.layanan.harga)],[D.noun,S.stylist],["Waktu",waktuTeks()],["Nama",S.nama],["Pembayaran",cara]].forEach(function(r){
        var d=el("div");d.appendChild(el("dt",null,r[0]));d.appendChild(el("dd",null,r[1]));rk.appendChild(d);
      });
      $("#k-wa").href="https://wa.me/"+D.wa+"?text="+encodeURIComponent("Halo, saya "+S.nama+". Saya memesan "+S.layanan.nama+(S.stylist===D.siapaSaja?"":" dengan "+S.stylist)+" pada "+waktuTeks()+". Kode: "+kode());
      var h=$("h3",selesaiEl);h.focus({preventScroll:true});
      kartu.scrollIntoView({block:"start",behavior:redam?"auto":"smooth"});
    },900);
  }
  $("#ulang").addEventListener("click",function(){location.reload()});

  pergi(0);mulai=false;
})();
"""
