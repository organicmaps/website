{% component bank_transfer(title, labels={}) -%}
<details id="bank-transfer" class="donate-method-details">
<summary>{{ title }}</summary>
<div class="donate-table-scroll" tabindex="0" role="region" aria-label="{{ title }}">

|   |   |
|---|---|
{{ labels | get(key="account_holder", default="Account holder for all currencies") }}: | Organic Maps OÜ
{{ labels | get(key="payment_description", default="Payment description") }}: | Donation

#### {{ labels | get(key="eur", default="EUR, Euro €") }}

|   |   |
|---|---|
SWIFT/BIC:      | TRWIBEB1XXX
IBAN:           | BE39 9672 0031 0319
{{ labels | get(key="bank_name", default="Bank name") }}: | Wise
{{ labels | get(key="bank_address", default="Bank address") }}: | Rue du Trône 100, 3rd floor, Brussels, 1050, Belgium

#### {{ labels | get(key="usd", default="USD, United States Dollar $") }}

|   |   |
|---|---|
{{ labels | get(key="receiving_fee", default="Receiving fee") }}: | $4.14
{{ labels | get(key="bank_address", default="Bank Address") }}: | 30 W. 26th Street, Sixth Floor, New York NY 10010, United States
{{ labels | get(key="routing_number", default="ACH/Wire Routing number") }}: | 026073150
{{ labels | get(key="account_number", default="Account number") }}: | 8312564881
{{ labels | get(key="account_type", default="Account type") }}: | {{ labels | get(key="checking", default="Checking") }}
SWIFT/BIC:      | CMFGUS33

#### {{ labels | get(key="gbp", default="GBP, British Pound £") }}

|   |   |
|---|---|
IBAN:           | GB97 TRWI 2314 7092 7851 63
{{ labels | get(key="bank_address", default="Bank address") }}: | 56 Shoreditch High Street, London, E1 6JJ, United Kingdom
{{ labels | get(key="sort_code", default="Sort code") }}: | 23-14-70
{{ labels | get(key="account_number", default="Account number") }}: | 92785163
SWIFT/BIC:      | TRWIGB2L

#### {{ labels | get(key="try", default="Turkish lira (TL, TRY)") }}

|   |   |
|---|---|
IBAN:     | TR740010300000000047306089
{{ labels | get(key="try_account_holder", default="Ad Soyad") }}: | Organic Maps OÜ (Birleşik Ödeme Hizmetleri ve Elektronik Para A.Ş)
{{ labels | get(key="payment_description", default="Açıklama") }}: | Donation

</div>
</details>
{%- endcomponent bank_transfer %}
