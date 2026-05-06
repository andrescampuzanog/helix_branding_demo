app_name = "helix_branding"
app_title = "Helix"
app_publisher = "Helix"
app_description = "Whitelabel layer that turns ERPNext into Helix"
app_email = "demo@helix.mx"
app_license = "mit"

app_logo_url = "/assets/helix_branding/images/helix-logo.svg"

app_include_css = "/assets/helix_branding/css/helix_brand.css"
app_include_js = "/assets/helix_branding/js/helix_whitelabel.js"

web_include_css = "/assets/helix_branding/css/helix_brand.css"
web_include_js = "/assets/helix_branding/js/helix_whitelabel.js"

# Strip "Built on Frappe" comment + "Powered by" link from public pages.
website_context = {
	"favicon": "/assets/helix_branding/images/helix-favicon.svg",
	"splash_image": "/assets/helix_branding/images/helix-logo.svg",
	"brand_html": "Helix",
	"copyright": "© 2026 Helix",
}

after_install = "helix_branding.install.after_install"
