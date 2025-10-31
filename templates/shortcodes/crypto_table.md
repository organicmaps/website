<p id="crypto-table">

<div id="notif" style="z-index: 1000; border-radius: 25px; padding: 5px; padding-left: 10px; padding-right: 10px; overflow-wrap: break-word; box-shadow: 0 3px 10px 0 #00000030; visibility: hidden; background-color: #FFF; color: #449f33; position: fixed; transform: translateX(-50%); left: 50%; top: 10%; animation: fadein 0.5s, fadeout 0.5s 1s;">Copied to clipboard</div>

{{ trans(key='name', lang=lang) }} | {{ trans(key='token', lang=lang) }} | {{ trans(key='address', lang=lang) }}
:-------------|:-----|:----------------------------------------------------------
Bitcoin       | BTC  | [{{ config.extra.btc }}](bitcoin:{{ config.extra.btc }}?message=Donation) <button onClick="copyToClipboard(this)">copy</button>
Ethereum      | ETH  | [{{ config.extra.eth }}](ethereum:{{ config.extra.eth }}) <button onClick="copyToClipboard(this)">copy</button>
Tether/ERC20  | USDT | {{ config.extra.eth }} <button onClick="copyToClipboard(this)">copy</button>
Tron          | TRX  | [{{ config.extra.trx }}](tron:{{ config.extra.trx }}) <button onClick="copyToClipboard(this)">copy</button>
Tether/TRC20  | USDT | {{ config.extra.trx }} <button onClick="copyToClipboard(this)">copy</button>
Litecoin      | LTC  | [{{ config.extra.ltc }}](litecoin:{{ config.extra.ltc }}) <button onClick="copyToClipboard(this)">copy</button>
Bitcoin Cash  | BCH  | [{{ config.extra.bch }}](bitcoincash:{{ config.extra.bch }}) <button onClick="copyToClipboard(this)">copy</button>
Telegram      | TON  | [{{ config.extra.ton }}](ton://transfer/{{ config.extra.ton }}) <button onClick="copyToClipboard(this)">copy</button>
Lighting (Satoshi)| SAT | [{{ config.extra.lnurl }}](lightning:{{ config.extra.lnurl }}) <button onClick="copyToClipboard(this)">copy</button>
Binance Coin  | BNB  | [{{ config.extra.bnb }}](bnb:{{ config.extra.bnb }}) <button onClick="copyToClipboard(this)">copy</button>
Algorand      | ALGO | [{{ config.extra.algo }}](algorand://{{ config.extra.algo }}) <button onClick="copyToClipboard(this)">copy</button>
Cardano       | ADA  | [{{ config.extra.ada }}](cardano:{{ config.extra.ada }}) <button onClick="copyToClipboard(this)">copy</button>
XRP           | XRP  | [{{ config.extra.xrp }}](ripple:{{ config.extra.xrp }}) <button onClick="copyToClipboard(this)">copy</button>
Solana        | SOL  | {{ config.extra.sol }} <button onClick="copyToClipboard(this)">copy</button>
ShibaINU/ERC20| SHIB | {{ config.extra.eth }} <button onClick="copyToClipboard(this)">copy</button>
Dogecoin      | DOGE | [{{ config.extra.doge }}](dogecoin:{{ config.extra.doge }}) <button onClick="copyToClipboard(this)">copy</button>
Monero        | XMR  | [{{ config.extra.xmr }}](monero:{{ config.extra.xmr }}) <button onClick="copyToClipboard(this)">copy</button>
ZCash         | ZEC  | [{{ config.extra.zec }}](zcash:{{ config.extra.zec }}) <button onClick="copyToClipboard(this)">copy</button>
Nano (XNO)    | NANO | [{{ config.extra.nano }}](nano:{{ config.extra.nano }}) <button onClick="copyToClipboard(this)">copy</button>
Polkadot      | DOT  | [{{ config.extra.dot }}](polkadot:{{ config.extra.dot }}) <button onClick="copyToClipboard(this)">copy</button>

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