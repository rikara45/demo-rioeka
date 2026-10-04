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

  var infoStylist, daftarStylist=[];
  var S={layanan:[],stylist:null,tgl:null,jam:null,nama:"",wa:"",cara:null};
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
  function total(){var t=0;S.layanan.forEach(function(l){t+=l.harga});return t}
  function durasi(){var t=0;S.layanan.forEach(function(l){t+=l.menit});return t}
  function durTeks(m){var j=Math.floor(m/60),s=m%60;return (j?j+" jam":"")+(j&&s?" ":"")+(s?s+" menit":"")}
  function namaLayanan(){return S.layanan.map(function(l){return l.nama})}
  function muka(){return Math.round(total()*0.3/500)*500}

  /* langkah 1: layanan */
  var daftarLayanan=[];
  (function(){
    var kotak=$("#pilih-layanan");
    D.grup.forEach(function(g){
      kotak.appendChild(el("h4","sub",g.nama));
      var daftar=el("div","opsi-daftar");
      g.item.forEach(function(l){
        var lb=el("label","opsi cek"), inp=el("input"), kk=el("span","opsi-kotak");
        inp.type="checkbox";inp.name="layanan";inp.value=l.nama;daftarLayanan.push({l:l,inp:inp});
        kk.appendChild(el("span","opsi-tanda"));
        kk.appendChild(el("span","opsi-nama",l.nama));
        kk.appendChild(el("span","opsi-harga",rp(l.harga)));
        kk.appendChild(el("span","opsi-ket","Sekitar "+l.menit+" menit"+(l.ket?" · "+l.ket:"")));
        lb.appendChild(inp);lb.appendChild(kk);daftar.appendChild(lb);
        inp.addEventListener("change",function(){
          S.layanan=daftarLayanan.filter(function(x){return x.inp.checked}).map(function(x){return x.l});
          selarasStylist();bersih();perbarui();
        });
      });
      kotak.appendChild(daftar);
    });
  })();

  /* langkah 2: stylist */
  (function(){
    var kotak=$("#pilih-stylist"), daftar=el("div","opsi-daftar");
    infoStylist=el("p","tip info-stylist");infoStylist.hidden=true;
    kotak.appendChild(infoStylist);
    [{nama:D.siapaSaja,keahlian:D.siapaSajaKet,rinci:"",bisa:null}].concat(D.stylist).forEach(function(s){
      var lb=el("label","opsi"), inp=el("input"), kk=el("span","opsi-kotak"), ket=el("span","opsi-ket");
      inp.type="radio";inp.name="stylist";inp.value=s.nama;
      kk.appendChild(el("span","opsi-tanda"));
      kk.appendChild(el("span","opsi-nama",s.nama));
      kk.appendChild(ket);
      lb.appendChild(inp);lb.appendChild(kk);daftar.appendChild(lb);
      daftarStylist.push({s:s,inp:inp,ket:ket});
      inp.addEventListener("change",function(){S.stylist=s.nama;bersih();perbarui()});
    });
    kotak.appendChild(daftar);
    selarasStylist();
  })();
  function kurang(s){
    if(!s.bisa){return []}
    return namaLayanan().filter(function(n){return s.bisa.indexOf(n)<0});
  }
  function selarasStylist(){
    var ada=0, semua=0;
    daftarStylist.forEach(function(x){
      if(!x.s.bisa){return}
      semua++;
      var k=kurang(x.s);
      x.inp.disabled=k.length>0;
      if(k.length){
        x.ket.textContent=x.s.keahlian+" · Tidak mengerjakan "+k.join(", ");
        if(x.inp.checked){x.inp.checked=false;S.stylist=null}
      }else{
        ada++;
        x.ket.textContent=[x.s.keahlian,x.s.rinci].filter(Boolean).join(" · ");
      }
    });
    var pecah=S.layanan.length>1&&ada===0;
    var s0=daftarStylist[0];
    if(s0){
      s0.ket.textContent=pecah?"Tiap layanan dikerjakan "+D.noun.toLowerCase()+" yang sesuai":D.siapaSajaKet;
    }
    infoStylist.hidden=!(S.layanan.length&&semua&&ada<semua);
    infoStylist.textContent=pecah
      ?"Layanan yang Anda pilih dikerjakan oleh lebih dari satu "+D.noun.toLowerCase()+". Pilih \""+D.siapaSaja+"\", kami yang mengatur."
      :D.noun+" yang tidak bisa dipilih tidak mengerjakan salah satu layanan Anda.";
  }

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
    tinjauEl.appendChild(barisTinjau("Layanan",S.layanan.map(function(l){return l.nama+", "+rp(l.harga)}).join("\n"),"layanan"));
    tinjauEl.appendChild(barisTinjau(D.noun,S.stylist,"stylist"));
    tinjauEl.appendChild(barisTinjau("Waktu",waktuTeks(),"waktu"));
    tinjauEl.appendChild(barisTinjau("Nama",S.nama,"data"));
    tinjauEl.appendChild(barisTinjau("WhatsApp",S.wa,"data"));
    var dur=barisTinjau("Perkiraan lama",durTeks(durasi()));dur.className="rw";tinjauEl.appendChild(dur);
    var rw=barisTinjau("Bayar muka 30 persen",D.bayar?rp(muka()):"");
    if(D.bayar){rw.className="rw";tinjauEl.appendChild(rw)}
    var tot=barisTinjau(S.layanan.length>1?"Total harga":"Harga layanan",rp(total()));tot.className="total";tinjauEl.appendChild(tot);
  }

  /* langkah 6: bayar (paket 3) */
  function isiBayar(){
    var a=$("#b-total"), b=$("#b-muka");
    if(a){a.textContent=rp(total())}
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
    if(id==="layanan"){return S.layanan.length?"":"Pilih minimal satu layanan untuk lanjut."}
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
  function ringkasLayanan(){
    return S.layanan.length>1?S.layanan.length+" layanan "+rp(total()):S.layanan[0].nama+" "+rp(total());
  }
  function ringkasMini(id){
    var p=[];
    if(S.layanan.length&&id!=="layanan"){p.push(ringkasLayanan())}
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
      else if(id==="layanan"&&S.layanan.length){mini.textContent=ringkasLayanan()+" · sekitar "+durTeks(durasi())}
    }
    mini.hidden=!mini.textContent;
  }
  function pergi(n,fokus){
    i=n;
    LANGKAH.forEach(function(l,k){panel[l[0]].hidden=k!==i});
    var id=LANGKAH[i][0];
    if(id==="waktu"){gulirHari()}
    if(id==="stylist"){selarasStylist()}
    if(id==="tinjau"){isiTinjau()}
    if(id==="bayar"){isiBayar()}
    bersih();perbarui();
    if(mulai){return}
    var h=$("h3",panel[id]);
    if(h){h.focus({preventScroll:true})}
    var r=kartu.getBoundingClientRect();
    if(r.top<96||r.top>window.innerHeight*0.5){kartu.scrollIntoView({block:"start",behavior:redam?"auto":"smooth"})}
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
      [["Layanan",S.layanan.map(function(l){return l.nama+", "+rp(l.harga)}).join("\n")],["Total harga",rp(total())],[D.noun,S.stylist],["Waktu",waktuTeks()],["Nama",S.nama],["Pembayaran",cara]].forEach(function(r){
        var d=el("div");d.appendChild(el("dt",null,r[0]));d.appendChild(el("dd",null,r[1]));rk.appendChild(d);
      });
      $("#k-wa").href="https://wa.me/"+D.wa+"?text="+encodeURIComponent("Halo, saya "+S.nama+". Saya memesan "+namaLayanan().join(", ")+(S.stylist===D.siapaSaja?"":" dengan "+S.stylist)+" pada "+waktuTeks()+". Kode: "+kode());
      var h=$("h3",selesaiEl);h.focus({preventScroll:true});
      kartu.scrollIntoView({block:"start",behavior:redam?"auto":"smooth"});
    },900);
  }
  $("#ulang").addEventListener("click",function(){location.reload()});

  var pembuka=$("#pesan-buka"), tombolBuka=$("#buka-pesan");
  function buka(){
    if(kartu.hidden){
      kartu.hidden=false;pembuka.hidden=true;tombolBuka.setAttribute("aria-expanded","true");
      var h=$("h3",panel[LANGKAH[i][0]]);if(h){h.focus({preventScroll:true})}
    }
    kartu.scrollIntoView({block:"start",behavior:redam?"auto":"smooth"});
  }
  tombolBuka.addEventListener("click",buka);
  $$('a[href="#pesan"]').forEach(function(a){a.addEventListener("click",function(ev){ev.preventDefault();buka()})});
  if(location.hash==="#pesan"){buka()}

  pergi(0);mulai=false;
})();
"""

WIZARD_JS = r"""
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
  function tanggalTeks(d){return NH[d.getDay()]+", "+d.getDate()+" "+NB[d.getMonth()]}
  function tambahHari(d,n){var t=new Date(d.getTime());t.setDate(t.getDate()+n);return t}

  var INAP=D.mode==="inap";
  var S={kamar:null,tgl:null,malam:1,dewasa:2,anak:0,qty:{},terima:null,jam:null,alamat:"",catatan:"",nama:"",wa:"",cara:null};
  var LANGKAH=INAP
    ?[["kamar","Kamar"],["tanggal","Tanggal"],["tamu","Tamu"],["data","Data Anda"],["tinjau","Periksa"]]
    :[["menu","Menu"],["terima","Tanggal dan cara terima"],["catatan","Catatan"],["data","Data Anda"],["tinjau","Periksa"]];
  if(D.bayar){LANGKAH.push(["bayar","Pembayaran"])}
  var IDX={};LANGKAH.forEach(function(l,n){IDX[l[0]]=n});
  var i=0, dariTinjau=false, mulai=true;

  var kartu=$("#pesan"), alur=$("#alur"), selesaiEl=$("#selesai");
  var btnLanjut=$("#lanjut"), btnKembali=$("#kembali"), barisAksi=$("#baris-aksi");
  var mini=$("#mini"), pesanSistem=$("#pesan-sistem");
  var panel={};$$(".panel[data-langkah]",alur).forEach(function(p){panel[p.dataset.langkah]=p});

  function stepper(opt){
    var w=el("div","stepper"), k=el("button","st-btn","\u2212"), v=el("output","st-nilai"), p=el("button","st-btn","+");
    k.type="button";p.type="button";
    k.setAttribute("aria-label","Kurangi "+opt.nama);p.setAttribute("aria-label","Tambah "+opt.nama);
    var n=opt.val;
    function segar(){v.textContent=String(n);k.disabled=opt.turun(n)===null;p.disabled=opt.naik(n)===null}
    function ubah(f){var b=f(n);if(b===null){return}n=b;segar();opt.aksi(n)}
    k.addEventListener("click",function(){ubah(opt.turun)});
    p.addEventListener("click",function(){ubah(opt.naik)});
    w.appendChild(k);w.appendChild(v);w.appendChild(p);
    segar();
    return {root:w,segar:segar,set:function(x){n=x;segar()},get:function(){return n}};
  }
  function bangunHari(kotak,info,pilih){
    kotak.textContent="";
    for(var n=0;n<14;n++){(function(n){
      var t=new Date();t.setHours(0,0,0,0);t.setDate(t.getDate()+n);
      var x=info(t,n);
      var b=el("button","hari");b.type="button";b.disabled=!x.ok;
      b.setAttribute("aria-pressed",S.tgl&&S.tgl.kunci===kunci(t)?"true":"false");
      b.appendChild(el("span","hr",n===0?"Hari ini":NH[t.getDay()].slice(0,3)));
      b.appendChild(el("span","tg",String(t.getDate())));
      b.appendChild(el("span","bl",x.bl));
      b.setAttribute("aria-label",tanggalTeks(t)+(x.ket?", "+x.ket:""));
      b.addEventListener("click",function(){
        $$("button",kotak).forEach(function(y){y.setAttribute("aria-pressed","false")});
        b.setAttribute("aria-pressed","true");pilih(t);
      });
      kotak.appendChild(b);
    })(n)}
  }
  function gulirHari(kotak){
    var p=$('button[aria-pressed="true"]',kotak);
    if(p){kotak.scrollLeft=Math.max(0,p.offsetLeft-16)}
  }
  function opsiRadio(nama,nilai,judul,harga,ket){
    var lb=el("label","opsi"), inp=el("input"), kk=el("span","opsi-kotak");
    inp.type="radio";inp.name=nama;inp.value=nilai;
    kk.appendChild(el("span","opsi-tanda"));
    kk.appendChild(el("span","opsi-nama",judul));
    if(harga){kk.appendChild(el("span","opsi-harga",harga))}
    kk.appendChild(el("span","opsi-ket",ket));
    lb.appendChild(inp);lb.appendChild(kk);
    return {lb:lb,inp:inp};
  }

  var hariKotak, jamKotak, jamJudul, stMalam, stDewasa, stAnak, infoTgl, infoTamu, daftarKamar=[];
  var semuaMenu=[], barisMenu={};

  function total(){
    if(INAP){return S.kamar&&S.tgl?S.kamar.harga*S.malam:0}
    var t=0;semuaMenu.forEach(function(m){t+=m.harga*(S.qty[m.nama]||0)});
    if(S.terima==="antar"){t+=D.ongkir}
    return t;
  }
  function muka(){return Math.round(total()*D.muka/500)*500}
  function pesanan(){return semuaMenu.filter(function(m){return (S.qty[m.nama]||0)>0})}
  function jmlItem(){var t=0;pesanan().forEach(function(m){t+=S.qty[m.nama]});return t}
  function lead(){var t=0;pesanan().forEach(function(m){if(m.lead>t){t=m.lead}});return t}
  function keluar(){return S.tgl?tambahHari(S.tgl.d,S.malam):null}
  function tamuTeks(){return S.dewasa+" dewasa"+(S.anak?", "+S.anak+" anak":"")}
  function waktuTeks(){return S.tgl&&S.jam!==null?tanggalTeks(S.tgl.d)+", pukul "+fmt(S.jam):""}
  function caraTeks(){return S.terima==="antar"?"Diantar":(S.terima==="ambil"?"Diambil sendiri":"")}

  /* inap: langkah kamar */
  function penuh(k,d){return acak(kunci(d)+"#"+k.nama)<0.18}
  function bentrok(){
    if(!S.kamar||!S.tgl){return null}
    for(var n=0;n<S.malam;n++){var d=tambahHari(S.tgl.d,n);if(penuh(S.kamar,d)){return d}}
    return null;
  }
  function infoTanggal(){
    if(!infoTgl){return}
    if(!S.tgl){infoTgl.textContent="Pilih tanggal check-in dulu.";return}
    var b=bentrok();
    if(b){infoTgl.textContent="Malam "+tanggalTeks(b)+" sudah penuh. Kurangi jumlah malam atau pilih tanggal lain.";return}
    infoTgl.textContent="Check-in "+tanggalTeks(S.tgl.d)+" setelah pukul "+D.checkin+", check-out "+tanggalTeks(keluar())+" sebelum pukul "+D.checkout+". "+S.malam+" malam.";
  }
  function gambarHariInap(){
    if(S.tgl&&S.kamar&&penuh(S.kamar,S.tgl.d)){S.tgl=null}
    bangunHari(hariKotak,function(t){
      var p=S.kamar&&penuh(S.kamar,t);
      return {ok:!p,bl:p?"Penuh":NB[t.getMonth()].slice(0,3),ket:p?"penuh":""};
    },function(t){S.tgl={d:t,kunci:kunci(t)};infoTanggal();bersih();perbarui()});
    infoTanggal();
  }
  function selarasTamu(){
    var kap=S.kamar?S.kamar.kap:10;
    if(S.dewasa>kap){S.dewasa=kap}
    if(S.dewasa+S.anak>kap){S.anak=kap-S.dewasa}
    if(stDewasa){stDewasa.set(S.dewasa);stAnak.set(S.anak)}
    if(infoTamu){infoTamu.textContent=S.kamar?"Kamar ini maksimal "+kap+" tamu, termasuk anak-anak.":"Pilih kamar dulu untuk melihat batas tamu."}
  }

  /* pesan: langkah menu dan terima */
  function perbaruiBarisMenu(m){
    var b=barisMenu[m.nama], q=S.qty[m.nama]||0;
    b.root.className="menu-baris"+(q>0?" aktif":"");
    b.sub.textContent=q>0?q+" "+m.satuan+" = "+rp(q*m.harga):"";
    b.sub.hidden=q<=0;
  }
  function gambarHariPesan(){
    var l=lead();
    if(S.tgl){
      var sisa=Math.round((S.tgl.d-new Date(new Date().setHours(0,0,0,0)))/86400000);
      if(sisa<l){S.tgl=null;S.jam=null}
    }
    $("#tip-lead").textContent=l>0
      ?"Pesanan Anda perlu dipesan paling lambat "+l+" hari sebelumnya. Tanggal bergaris putus-putus belum bisa dipilih atau toko tutup."
      :"Dua minggu ke depan. Tanggal bergaris putus-putus berarti toko tutup.";
    bangunHari(hariKotak,function(t,n){
      var blok=D.jam[String(t.getDay())], dekat=n<l;
      return {ok:!!blok&&!dekat,bl:!blok?"Tutup":(dekat?"Belum":NB[t.getMonth()].slice(0,3)),ket:!blok?"toko tutup":(dekat?"terlalu dekat dengan hari ini":"")};
    },function(t){
      S.tgl={d:t,kunci:kunci(t),blok:D.jam[String(t.getDay())]};S.jam=null;gambarJam();bersih();perbarui();
    });
    gambarJam();
  }
  function gambarJam(){
    jamKotak.textContent="";
    if(!S.tgl||!S.terima){jamJudul.textContent=!S.tgl?"Pilih tanggal dulu":"Pilih ambil sendiri atau diantar dulu";return}
    var b=S.tgl.blok, sekarang=new Date(), tersedia=0;
    for(var m=mnt(b[0]);m+60<=mnt(b[1]);m+=60){(function(m){
      var x=el("button",null,fmt(m));x.type="button";x.setAttribute("aria-pressed",S.jam===m?"true":"false");
      var lewat=S.tgl.kunci===kunci(sekarang)&&m<=sekarang.getHours()*60+sekarang.getMinutes();
      var terisi=acak(S.tgl.kunci+"#"+m+S.terima)<0.15;
      x.disabled=lewat||terisi;
      if(terisi){x.setAttribute("aria-label",fmt(m)+", sudah terisi")}
      else if(lewat){x.setAttribute("aria-label",fmt(m)+", sudah lewat")}
      else{tersedia++}
      x.addEventListener("click",function(){
        $$("button",jamKotak).forEach(function(y){y.setAttribute("aria-pressed","false")});
        x.setAttribute("aria-pressed","true");S.jam=m;bersih();perbarui();
      });
      jamKotak.appendChild(x);
    })(m)}
    var kata=S.terima==="antar"?"antar":"ambil";
    jamJudul.textContent=tersedia?"Pilih jam "+kata+", "+tanggalTeks(S.tgl.d):"Semua jam hari ini sudah terisi atau lewat. Pilih hari lain.";
  }

  if(INAP){
    (function(){
      var kotak=$("#pilih-kamar"), daftar=el("div","opsi-daftar");
      D.kamar.forEach(function(k){
        var o=opsiRadio("kamar",k.nama,k.nama,rp(k.harga)+" / malam","Maks. "+k.kap+" tamu"+(k.ket?" \u00b7 "+k.ket:""));
        daftar.appendChild(o.lb);daftarKamar.push({k:k,inp:o.inp});
        o.inp.addEventListener("change",function(){
          S.kamar=k;selarasTamu();gambarHariInap();bersih();perbarui();
        });
      });
      kotak.appendChild(daftar);
    })();
    hariKotak=$("#pilih-hari");infoTgl=$("#info-tgl");
    stMalam=stepper({nama:"jumlah malam",val:1,
      naik:function(n){return n<14?n+1:null},turun:function(n){return n>1?n-1:null},
      aksi:function(n){S.malam=n;infoTanggal();bersih();perbarui()}});
    (function(){
      var b=el("div","st-baris"), t=el("span","st-label","Jumlah malam");
      b.appendChild(t);b.appendChild(stMalam.root);$("#st-malam").appendChild(b);
    })();
    infoTamu=$("#info-tamu");
    stDewasa=stepper({nama:"jumlah dewasa",val:2,
      naik:function(n){return S.dewasa+S.anak<(S.kamar?S.kamar.kap:10)?n+1:null},turun:function(n){return n>1?n-1:null},
      aksi:function(n){S.dewasa=n;stAnak.segar();stDewasa.segar();bersih();perbarui()}});
    stAnak=stepper({nama:"jumlah anak",val:0,
      naik:function(n){return S.dewasa+S.anak<(S.kamar?S.kamar.kap:10)?n+1:null},turun:function(n){return n>0?n-1:null},
      aksi:function(n){S.anak=n;stDewasa.segar();stAnak.segar();bersih();perbarui()}});
    (function(){
      var k=$("#st-tamu");
      var a=el("div","st-baris");a.appendChild(el("span","st-label","Dewasa"));a.appendChild(stDewasa.root);
      var b=el("div","st-baris");b.appendChild(el("span","st-label","Anak-anak"));b.appendChild(stAnak.root);
      k.appendChild(a);k.appendChild(b);
    })();
    selarasTamu();
    gambarHariInap();
  }else{
    (function(){
      var kotak=$("#pilih-menu");
      D.menu.forEach(function(g){
        kotak.appendChild(el("h4","sub",g.nama));
        var daftar=el("div","opsi-daftar");
        g.item.forEach(function(m){
          m.satuan=m.satuan||"porsi";semuaMenu.push(m);S.qty[m.nama]=0;
          var root=el("div","menu-baris"), info=el("div","menu-info"), sub=el("p","menu-sub");
          info.appendChild(el("span","opsi-nama",m.nama));
          info.appendChild(el("span","opsi-harga",rp(m.harga)+" / "+m.satuan));
          info.appendChild(el("span","opsi-ket",(m.ket?m.ket+" \u00b7 ":"")+"Minimal "+m.min+" "+m.satuan+(m.lead?" \u00b7 pesan H-"+m.lead:"")));
          sub.hidden=true;info.appendChild(sub);
          var st=stepper({nama:m.nama,val:0,
            naik:function(n){return n===0?m.min:(n<m.maks?n+1:null)},
            turun:function(n){return n===0?null:(n<=m.min?0:n-1)},
            aksi:function(n){S.qty[m.nama]=n;perbaruiBarisMenu(m);bersih();perbarui()}});
          root.appendChild(info);root.appendChild(st.root);
          barisMenu[m.nama]={root:root,sub:sub,st:st};
          daftar.appendChild(root);
        });
        kotak.appendChild(daftar);
      });
    })();
    hariKotak=$("#pilih-hari");jamKotak=$("#pilih-jam");jamJudul=$("#jam-judul");
    var kotakCara=$("#pilih-cara"), daftarCara=el("div","opsi-daftar");
    var ambil=opsiRadio("terima","ambil","Ambil sendiri","gratis","Di "+D.tempatAmbil+".");
    var antar=opsiRadio("terima","antar","Diantar",rp(D.ongkir),D.areaAntar);
    daftarCara.appendChild(ambil.lb);daftarCara.appendChild(antar.lb);kotakCara.appendChild(daftarCara);
    var inAlamat=$("#alamat"), kolomAlamat=$("#kolom-alamat");
    [ambil,antar].forEach(function(o){o.inp.addEventListener("change",function(){
      S.terima=o.inp.value;S.jam=null;kolomAlamat.hidden=S.terima!=="antar";gambarJam();bersih();perbarui();
    })});
    inAlamat.addEventListener("input",function(){S.alamat=this.value.trim();salahDi(inAlamat,"");bersih();perbarui()});
    $("#catatan").addEventListener("input",function(){S.catatan=this.value.trim();bersih();perbarui()});
    gambarHariPesan();
  }

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
  function baris(kelas,label,nilai){var r=barisTinjau(label,nilai);r.className=kelas;tinjauEl.appendChild(r)}
  function isiTinjau(){
    tinjauEl.textContent="";
    if(INAP){
      tinjauEl.appendChild(barisTinjau("Kamar",S.kamar.nama+", "+rp(S.kamar.harga)+" / malam","kamar"));
      tinjauEl.appendChild(barisTinjau("Check-in",tanggalTeks(S.tgl.d)+", setelah pukul "+D.checkin,"tanggal"));
      tinjauEl.appendChild(barisTinjau("Check-out",tanggalTeks(keluar())+", sebelum pukul "+D.checkout,"tanggal"));
      tinjauEl.appendChild(barisTinjau("Tamu",tamuTeks(),"tamu"));
      tinjauEl.appendChild(barisTinjau("Nama",S.nama,"data"));
      tinjauEl.appendChild(barisTinjau("WhatsApp",S.wa,"data"));
      baris("rw","Lama menginap",S.malam+" malam");
    }else{
      tinjauEl.appendChild(barisTinjau("Pesanan",pesanan().map(function(m){return S.qty[m.nama]+" "+m.satuan+" "+m.nama+", "+rp(S.qty[m.nama]*m.harga)}).join("\n"),"menu"));
      tinjauEl.appendChild(barisTinjau("Penerimaan",waktuTeks()+"\n"+caraTeks(),"terima"));
      if(S.terima==="antar"){tinjauEl.appendChild(barisTinjau("Alamat antar",S.alamat,"terima"))}
      tinjauEl.appendChild(barisTinjau("Catatan",S.catatan||"Tidak ada","catatan"));
      tinjauEl.appendChild(barisTinjau("Nama",S.nama,"data"));
      tinjauEl.appendChild(barisTinjau("WhatsApp",S.wa,"data"));
      if(S.terima==="antar"){baris("rw","Ongkos antar",rp(D.ongkir))}
    }
    if(D.bayar){baris("rw","Bayar muka "+D.mukaTeks,rp(muka()))}
    var tot=barisTinjau(INAP?"Total menginap":"Total pesanan",rp(total()));tot.className="total";tinjauEl.appendChild(tot);
  }
  function isiBayar(){
    var a=$("#b-total"), b=$("#b-muka");
    if(a){a.textContent=rp(total())}
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

  function galat(id){
    if(id==="kamar"){return S.kamar?"":"Pilih satu tipe kamar untuk lanjut."}
    if(id==="tanggal"){
      if(!S.tgl){return "Pilih tanggal check-in dulu."}
      var b=bentrok();
      return b?"Malam "+tanggalTeks(b)+" sudah penuh. Kurangi jumlah malam atau pilih tanggal lain.":"";
    }
    if(id==="tamu"){return ""}
    if(id==="menu"){return pesanan().length?"":"Pilih minimal satu menu untuk lanjut."}
    if(id==="terima"){
      if(!S.tgl){return "Pilih tanggal dulu."}
      if(!S.terima){return "Pilih ambil sendiri atau diantar."}
      if(S.jam===null){return "Pilih jam yang masih kosong."}
      if(S.terima==="antar"&&S.alamat.length<8){return "Isi alamat antar yang lengkap."}
      return "";
    }
    if(id==="catatan"){return ""}
    if(id==="data"){return !namaOk()?"Isi nama Anda untuk lanjut.":(!waOk()?"Nomor WhatsApp belum lengkap.":"")}
    if(id==="bayar"){return S.cara?"":"Pilih cara bayar untuk lanjut."}
    return "";
  }
  function bersih(){pesanSistem.textContent=""}
  function labelLanjut(id){
    if(id==="tinjau"){return D.bayar?"Lanjut ke pembayaran":"Konfirmasi pesanan"}
    if(id==="bayar"){return S.cara==="tempat"?"Konfirmasi, "+D.bayarNanti.toLowerCase():(S.cara==="transfer"?"Saya sudah transfer":(S.cara==="qris"?"Saya sudah bayar":"Konfirmasi pembayaran"))}
    return "Lanjut";
  }
  function ringkasMini(id){
    var p=[];
    if(INAP){
      if(S.kamar&&id!=="kamar"){p.push(S.kamar.nama)}
      if(S.tgl&&IDX[id]>IDX.tanggal){p.push(S.malam+" malam dari "+tanggalTeks(S.tgl.d))}
      if(IDX[id]>IDX.tamu){p.push(tamuTeks())}
    }else{
      if(jmlItem()&&id!=="menu"){p.push(jmlItem()+" item "+rp(total()))}
      if(S.jam!==null&&IDX[id]>IDX.terima){p.push(waktuTeks())}
    }
    return p.join(" \u00b7 ");
  }
  function perbarui(){
    var id=LANGKAH[i][0], g=galat(id), jml=LANGKAH.length;
    $("#l-no").textContent="Langkah "+(i+1)+" dari "+jml;
    $("#l-nama").textContent=LANGKAH[i][1];
    $("#progres-isi").style.width=((i+1)/jml*100)+"%";
    $("#progres").setAttribute("aria-valuenow",String(i+1));
    $("#progres").setAttribute("aria-valuetext","Langkah "+(i+1)+" dari "+jml+", "+LANGKAH[i][1]);
    btnLanjut.textContent=labelLanjut(id);
    btnLanjut.setAttribute("aria-disabled",g?"true":"false");
    barisAksi.className="baris-aksi"+(i===0?" tanpa-kembali":"");
    btnKembali.hidden=i===0;
    if(g){mini.textContent=g}
    else{
      mini.textContent="";var r=ringkasMini(id);
      if(r){mini.textContent=r}
      else if(id==="menu"&&jmlItem()){mini.textContent=jmlItem()+" item "+rp(total())}
      else if(id==="kamar"&&S.kamar){mini.textContent=S.kamar.nama+" "+rp(S.kamar.harga)+" / malam"}
    }
    mini.hidden=!mini.textContent;
  }
  function pergi(n,fokus){
    i=n;
    LANGKAH.forEach(function(l,k){panel[l[0]].hidden=k!==i});
    var id=LANGKAH[i][0];
    if(id==="tanggal"){gambarHariInap();gulirHari(hariKotak)}
    if(id==="tamu"){selarasTamu();stDewasa.segar();stAnak.segar()}
    if(id==="terima"){gambarHariPesan();gulirHari(hariKotak)}
    if(id==="tinjau"){isiTinjau()}
    if(id==="bayar"){isiBayar()}
    bersih();perbarui();
    if(mulai){return}
    var h=$("h3",panel[id]);
    if(h){h.focus({preventScroll:true})}
    var r=kartu.getBoundingClientRect();
    if(r.top<96||r.top>window.innerHeight*0.5){kartu.scrollIntoView({block:"start",behavior:redam?"auto":"smooth"})}
  }
  function fokusKeSalah(id){
    var f=null;
    if(id==="kamar"){f=$('input[name="kamar"]')}
    else if(id==="tanggal"){f=$("button:not(:disabled)",hariKotak)}
    else if(id==="menu"){f=$(".st-btn:not(:disabled)",panel.menu)}
    else if(id==="terima"){
      f=!S.tgl?$("button:not(:disabled)",hariKotak):(!S.terima?$('input[name="terima"]'):(S.jam===null?$("button:not(:disabled)",jamKotak):$("#alamat")));
    }
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
      }else if(id==="terima"&&S.terima==="antar"&&S.jam!==null&&S.alamat.length<8){
        salahDi($("#alamat"),"Isi alamat antar yang lengkap.");
      }else{pesanSistem.textContent=g}
      fokusKeSalah(id);
      return;
    }
    if(id==="tinjau"&&!D.bayar){selesaiPesan(D.bayarNanti,btnLanjut);return}
    if(id==="bayar"){
      var cara=S.cara==="qris"?"QRIS, bayar muka lunas":(S.cara==="transfer"?"Transfer, bayar muka lunas":D.bayarNanti);
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
    var t=S.tgl.d, dm=String(t.getDate()).padStart(2,"0")+String(t.getMonth()+1).padStart(2,"0");
    return INAP?D.kode+"-"+dm+"-"+S.malam+"-malam":D.kode+"-"+dm+"-"+fmt(S.jam).replace(".","");
  }
  function pesanWa(){
    if(INAP){
      return "Halo, saya "+S.nama+". Saya mau memesan "+S.kamar.nama+" untuk "+S.malam+" malam mulai "+tanggalTeks(S.tgl.d)+", "+tamuTeks()+". Kode: "+kode();
    }
    return "Halo, saya "+S.nama+". Saya memesan "+pesanan().map(function(m){return S.qty[m.nama]+" "+m.satuan+" "+m.nama}).join(", ")+" untuk "+caraTeks().toLowerCase()+" pada "+waktuTeks()+". Kode: "+kode();
  }
  function selesaiPesan(cara,tombol){
    tombol.setAttribute("aria-busy","true");tombol.textContent="Memproses\u2026";
    setTimeout(function(){
      tombol.removeAttribute("aria-busy");
      alur.hidden=true;selesaiEl.hidden=false;
      var c=$("#k-centang");c.textContent="";c.appendChild(ikonCentang());
      $("#k-kode").textContent=kode();
      var rk=$("#k-ringkas");rk.textContent="";
      var baris=INAP
        ?[["Kamar",S.kamar.nama],["Menginap",tanggalTeks(S.tgl.d)+" sampai "+tanggalTeks(keluar())+", "+S.malam+" malam"],["Tamu",tamuTeks()],["Total menginap",rp(total())],["Nama",S.nama],["Pembayaran",cara]]
        :[["Pesanan",pesanan().map(function(m){return S.qty[m.nama]+" "+m.satuan+" "+m.nama}).join("\n")],["Penerimaan",waktuTeks()+"\n"+caraTeks()],["Total pesanan",rp(total())],["Nama",S.nama],["Pembayaran",cara]];
      baris.forEach(function(r){
        var d=el("div");d.appendChild(el("dt",null,r[0]));d.appendChild(el("dd",null,r[1]));rk.appendChild(d);
      });
      $("#k-wa").href="https://wa.me/"+D.wa+"?text="+encodeURIComponent(pesanWa());
      var h=$("h3",selesaiEl);h.focus({preventScroll:true});
      kartu.scrollIntoView({block:"start",behavior:redam?"auto":"smooth"});
    },900);
  }
  $("#ulang").addEventListener("click",function(){location.reload()});

  var pembuka=$("#pesan-buka"), tombolBuka=$("#buka-pesan");
  function buka(){
    if(kartu.hidden){
      kartu.hidden=false;pembuka.hidden=true;tombolBuka.setAttribute("aria-expanded","true");
      var h=$("h3",panel[LANGKAH[i][0]]);if(h){h.focus({preventScroll:true})}
    }
    kartu.scrollIntoView({block:"start",behavior:redam?"auto":"smooth"});
  }
  tombolBuka.addEventListener("click",buka);
  $$('a[href="#pesan"]').forEach(function(a){a.addEventListener("click",function(ev){ev.preventDefault();buka()})});
  if(location.hash==="#pesan"){buka()}

  pergi(0);mulai=false;
})();
"""
