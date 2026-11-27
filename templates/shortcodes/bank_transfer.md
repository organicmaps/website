{% component bank_transfer(lang, title) -%}
{% set catalog = load_data(path="templates/shortcodes/bank_transfer_labels.toml") -%}
{% set translated = catalog | get(key=lang, default={}) -%}
{% for key, _ in translated -%}
  {% if key not in catalog.default -%}
    {{ throw(message="bank_transfer: unknown " ~ lang ~ " label '" ~ key ~ "'") }}
  {%- endif -%}
{% endfor -%}
{% set labels = {...catalog.default, ...translated} -%}
<details id="bank-transfer" class="donate-method-details">
<summary>{{ title }}</summary>
<div class="donate-table-scroll" tabindex="0" role="region" aria-label="{{ title }}">

|   |   |
|---|---|
{{ labels.account_holder }}: | Organic Maps OÜ
{{ labels.payment_description }}: | Donation

#### {{ labels.eur }}

|   |   |
|---|---|
SWIFT/BIC:      | TRWIBEB1XXX
IBAN:           | BE39 9672 0031 0319
{{ labels.bank_name }}: | Wise
{{ labels.bank_address }}: | Rue du Trône 100, 3rd floor, Brussels, 1050, Belgium

#### {{ labels.usd }}

|   |   |
|---|---|
{{ labels.receiving_fee }}: | $4.14
{{ labels.bank_address }}: | 30 W. 26th Street, Sixth Floor, New York NY 10010, United States
{{ labels.routing_number }}: | 026073150
{{ labels.account_number }}: | 8312564881
{{ labels.account_type }}: | {{ labels.checking }}
SWIFT/BIC:      | CMFGUS33

#### {{ labels.gbp }}

|   |   |
|---|---|
IBAN:           | GB97 TRWI 2314 7092 7851 63
{{ labels.bank_address }}: | 56 Shoreditch High Street, London, E1 6JJ, United Kingdom
{{ labels.sort_code }}: | 23-14-70
{{ labels.account_number }}: | 92785163
SWIFT/BIC:      | TRWIGB2L

#### {{ labels.try }}

|   |   |
|---|---|
IBAN:     | TR740010300000000047306089
{{ labels.try_account_holder }}: | Organic Maps OÜ (Birleşik Ödeme Hizmetleri ve Elektronik Para A.Ş)
{{ labels.try_payment_description }}: | Donation

</div>
</details>
{%- endcomponent bank_transfer %}
