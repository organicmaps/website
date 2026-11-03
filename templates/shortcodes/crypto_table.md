{% component crypto_table(lang, config, title) -%}
<details id="crypto" class="donate-method-details">
<summary>{{ title }}</summary>
<div class="donate-table-scroll" tabindex="0" role="region" aria-label="{{ title }}">

<p id="crypto-table">

<div id="notif" style="z-index: 1000; border-radius: 25px; padding: 5px; padding-left: 10px; padding-right: 10px; overflow-wrap: break-word; box-shadow: 0 3px 10px 0 #00000030; visibility: hidden; background-color: #FFF; color: #449f33; position: fixed; transform: translateX(-50%); left: 50%; top: 10%; animation: fadein 0.5s, fadeout 0.5s 1s;">Copied to clipboard</div>

{{ trans(key='name', lang=lang) }} | {{ trans(key='token', lang=lang) }} | {{ trans(key='address', lang=lang) }}
:-------------|:-----|:----------------------------------------------------------
Bitcoin       | BTC  | <button onClick="copyToClipboard(this)">copy</button> [{{ config.extra.btc }}](bitcoin:{{ config.extra.btc }}?message=Donation)
Ethereum      | ETH  | <button onClick="copyToClipboard(this)">copy</button> [{{ config.extra.eth }}](ethereum:{{ config.extra.eth }})
Tether/ERC20  | USDT | <button onClick="copyToClipboard(this)">copy</button> {{ config.extra.eth }}
Tron          | TRX  | <button onClick="copyToClipboard(this)">copy</button> [{{ config.extra.trx }}](tron:{{ config.extra.trx }})
Tether/TRC20  | USDT | <button onClick="copyToClipboard(this)">copy</button> {{ config.extra.trx }}
Litecoin      | LTC  | <button onClick="copyToClipboard(this)">copy</button> [{{ config.extra.ltc }}](litecoin:{{ config.extra.ltc }})
Bitcoin Cash  | BCH  | <button onClick="copyToClipboard(this)">copy</button> [{{ config.extra.bch }}](bitcoincash:{{ config.extra.bch }})
Telegram      | TON  | <button onClick="copyToClipboard(this)">copy</button> [{{ config.extra.ton }}](ton://transfer/{{ config.extra.ton }})
Lighting (Satoshi)| SAT | <button onClick="copyToClipboard(this)">copy</button> [{{ config.extra.lnurl }}](lightning:{{ config.extra.lnurl }})
Binance Coin  | BNB  | <button onClick="copyToClipboard(this)">copy</button> [{{ config.extra.bnb }}](bnb:{{ config.extra.bnb }})
Algorand      | ALGO | <button onClick="copyToClipboard(this)">copy</button> [{{ config.extra.algo }}](algorand://{{ config.extra.algo }})
Cardano       | ADA  | <button onClick="copyToClipboard(this)">copy</button> [{{ config.extra.ada }}](cardano:{{ config.extra.ada }})
XRP           | XRP  | <button onClick="copyToClipboard(this)">copy</button> [{{ config.extra.xrp }}](ripple:{{ config.extra.xrp }})
Solana        | SOL  | <button onClick="copyToClipboard(this)">copy</button> {{ config.extra.sol }}
ShibaINU/ERC20| SHIB | <button onClick="copyToClipboard(this)">copy</button> {{ config.extra.eth }}
Dogecoin      | DOGE | <button onClick="copyToClipboard(this)">copy</button> [{{ config.extra.doge }}](dogecoin:{{ config.extra.doge }})
Monero        | XMR  | <button onClick="copyToClipboard(this)">copy</button> [{{ config.extra.xmr }}](monero:{{ config.extra.xmr }})
ZCash         | ZEC  | <button onClick="copyToClipboard(this)">copy</button> [{{ config.extra.zec }}](zcash:{{ config.extra.zec }})
Nano (XNO)    | NANO | <button onClick="copyToClipboard(this)">copy</button> [{{ config.extra.nano }}](nano:{{ config.extra.nano }})
Polkadot      | DOT  | <button onClick="copyToClipboard(this)">copy</button> [{{ config.extra.dot }}](polkadot:{{ config.extra.dot }})

<script>
  function copyToClipboard(button) {
    var text = null;
    var previousElement = button.previousElementSibling;
    if (previousElement) {
      text = previousElement.innerText;
    }
    if (!text) {
      text = button.previousSibling.textContent;
    }
    var notif = document.getElementById("notif");
      notif.innerText = "Copied " + text + " to clipboard";
      notif.style.visibility = "visible";
      setTimeout(function(){ notif.style.visibility = "hidden";
    }, 1500);
    navigator.clipboard.writeText(text);
  }
</script>

</p>

</div>
</details>
{%- endcomponent crypto_table %}
