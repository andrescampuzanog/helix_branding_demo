# Helix Branding

Whitelabel layer for the Helix Demand Forecasting & S&OP demo.

Replaces ERPNext / Frappe references in the desk UI with "Helix":

- App name, navbar logo, favicon, splash, login page
- Browser tab title prefix
- About dialog and help dropdown
- Tooltips and any late-rendered "ERPNext" / "Frappe Framework" strings

Install order: `helix_branding` after `erpnext`, before `helix_core`.

```
bench --site demo.helix.localhost install-app helix_branding
```
# helix_branding_demo
