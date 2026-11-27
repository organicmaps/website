{% component crypto_table(lang, config, title) -%}
<details id="crypto" class="donate-method-details">
<summary>{{ title }}</summary>
<div id="crypto-table" class="donate-table-scroll" tabindex="0" role="region" aria-label="{{ title }}">

<div id="crypto-copy-status" role="status" data-copied="Copied {address} to clipboard" data-copy-failed="Select the address and copy it manually."></div>

{{ trans(key='name', lang=lang) }} | {{ trans(key='token', lang=lang) }} | {{ trans(key='address', lang=lang) }}
:-------------|:-----|:----------------------------------------------------------
Bitcoin       | BTC  | <button type="button" data-address="{{ config.extra.btc }}">copy</button> [{{ config.extra.btc }}](bitcoin:{{ config.extra.btc }}?message=Donation)
Ethereum      | ETH  | <button type="button" data-address="{{ config.extra.eth }}">copy</button> [{{ config.extra.eth }}](ethereum:{{ config.extra.eth }})
Tether/ERC20  | USDT | <button type="button" data-address="{{ config.extra.eth }}">copy</button> {{ config.extra.eth }}
Tron          | TRX  | <button type="button" data-address="{{ config.extra.trx }}">copy</button> [{{ config.extra.trx }}](tron:{{ config.extra.trx }})
Tether/TRC20  | USDT | <button type="button" data-address="{{ config.extra.trx }}">copy</button> {{ config.extra.trx }}
Litecoin      | LTC  | <button type="button" data-address="{{ config.extra.ltc }}">copy</button> [{{ config.extra.ltc }}](litecoin:{{ config.extra.ltc }})
Bitcoin Cash  | BCH  | <button type="button" data-address="{{ config.extra.bch }}">copy</button> [{{ config.extra.bch }}](bitcoincash:{{ config.extra.bch }})
Telegram      | TON  | <button type="button" data-address="{{ config.extra.ton }}">copy</button> [{{ config.extra.ton }}](ton://transfer/{{ config.extra.ton }})
Lightning (Satoshi)| SAT | <button type="button" data-address="{{ config.extra.lnurl }}">copy</button> [{{ config.extra.lnurl }}](lightning:{{ config.extra.lnurl }})
Binance Coin  | BNB  | <button type="button" data-address="{{ config.extra.bnb }}">copy</button> [{{ config.extra.bnb }}](bnb:{{ config.extra.bnb }})
Algorand      | ALGO | <button type="button" data-address="{{ config.extra.algo }}">copy</button> [{{ config.extra.algo }}](algorand://{{ config.extra.algo }})
Cardano       | ADA  | <button type="button" data-address="{{ config.extra.ada }}">copy</button> [{{ config.extra.ada }}](cardano:{{ config.extra.ada }})
XRP           | XRP  | <button type="button" data-address="{{ config.extra.xrp }}">copy</button> [{{ config.extra.xrp }}](ripple:{{ config.extra.xrp }})
Solana        | SOL  | <button type="button" data-address="{{ config.extra.sol }}">copy</button> {{ config.extra.sol }}
ShibaINU/ERC20| SHIB | <button type="button" data-address="{{ config.extra.eth }}">copy</button> {{ config.extra.eth }}
Dogecoin      | DOGE | <button type="button" data-address="{{ config.extra.doge }}">copy</button> [{{ config.extra.doge }}](dogecoin:{{ config.extra.doge }})
Monero        | XMR  | <button type="button" data-address="{{ config.extra.xmr }}">copy</button> [{{ config.extra.xmr }}](monero:{{ config.extra.xmr }})
ZCash         | ZEC  | <button type="button" data-address="{{ config.extra.zec }}">copy</button> [{{ config.extra.zec }}](zcash:{{ config.extra.zec }})
Nano (XNO)    | NANO | <button type="button" data-address="{{ config.extra.nano }}">copy</button> [{{ config.extra.nano }}](nano:{{ config.extra.nano }})
Polkadot      | DOT  | <button type="button" data-address="{{ config.extra.dot }}">copy</button> [{{ config.extra.dot }}](polkadot:{{ config.extra.dot }})

<script>
  (() => {
    const status = document.getElementById('crypto-copy-status');
    let timeout;
    document.getElementById('crypto').addEventListener('click', async event => {
      const address = event.target.dataset.address;
      if (!address) return;
      try {
        await navigator.clipboard.writeText(address);
        status.textContent = status.dataset.copied.replace('{address}', address);
      } catch {
        status.textContent = status.dataset.copyFailed;
      }
      clearTimeout(timeout);
      timeout = setTimeout(() => { status.textContent = ''; }, 3000);
    });
  })();
</script>

</div>
</details>
{%- endcomponent crypto_table %}
