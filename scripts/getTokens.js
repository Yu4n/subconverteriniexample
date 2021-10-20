// ==UserScript==
// @name         Suda
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match        https://v2.suda.moe/user/agent?*
// @icon         https://www.google.com/s2/favicons?domain=suda.moe
// @grant        none
// ==/UserScript==

(function() {
    'use strict';
    let a = 'https://api.suda.cat/sub?target=v2ray&url=https%3A%2F%2Fsuda.sub.koicloud.pw%2Flink%2F'
        let c = '%3Fsub%3D3%26extend%3D1&config=https%3A//raw.githubusercontent.com/Yu4n/subconverteriniexample/master/Minimalist.ini&include=&emoji=false'
        for (let i = 1; i < 11; i++) {
            if (!document.getElementsByTagName("tr")[i] || !document.getElementById("userName")) {
                break
            }
            if (document.getElementsByTagName("tr")[i].cells[5].innerText.length != 4){
                let link = a + document.getElementsByTagName("tr")[i].cells[4].innerText + c
                document.getElementById("userName").value += link + 'toReplace'
            }
        }
        if (document.getElementById("userName")) {
            let textarea = document.getElementById("userName");
            if (textarea.value) {
                textarea.addEventListener('click', function() {
                textarea.select()
                try {
                   var ok = document.execCommand('copy');
                   if (!ok) {
                       alert('Unable to copy!')
                   }
               } catch (err) {
                   textarea.innerHTML = 'Unsupported Browser!';
               }
            });
            }
        }
})();