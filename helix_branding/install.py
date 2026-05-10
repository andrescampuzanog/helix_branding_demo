import frappe

LOGO = "/assets/helix_branding/images/helix-logo.png"
FAVICON = "/assets/helix_branding/images/favicon.png"
LOGIN_BG = "/assets/helix_branding/images/helix-login-bg.svg"
BRAND_COLOR = "#0B5394"


def after_install():
	"""Apply Helix whitelabel to all single-doctype settings.

	Each step commits independently so a partial failure (e.g. theme schema variation
	across Frappe builds) does not roll back the earlier writes.
	"""
	apply_branding()


def after_migrate():
	"""Re-apply persisted branding settings after app updates."""
	apply_branding()


def apply_branding():
	_apply_website_settings()
	frappe.db.commit()
	_apply_navbar_settings()
	frappe.db.commit()
	_apply_system_settings()
	frappe.db.commit()
	_apply_website_theme()
	frappe.db.commit()


def _apply_website_settings():
	for key, value in {
		"app_name": "Helix",
		"app_logo": LOGO,
		"favicon": FAVICON,
		"splash_image": LOGO,
		"brand_html": "<span style='font-weight:600'>Helix</span>",
		"footer_address": "Helix S&OP",
		"banner_image": LOGO,
		"home_page": "login",
		"hide_login": 0,
		"login_with_email_link": 0,
	}.items():
		try:
			frappe.db.set_single_value("Website Settings", key, value)
		except Exception:
			pass


def _apply_navbar_settings():
	for key, value in {
		"app_logo": LOGO,
		"logo": LOGO,
	}.items():
		try:
			frappe.db.set_single_value("Navbar Settings", key, value)
		except Exception:
			pass


def _apply_system_settings():
	for key, value in {
		"app_name": "Helix",
		"country": "Mexico",
		"currency": "MXN",
		"setup_complete": 1,
		"disable_signup": 1,
	}.items():
		try:
			frappe.db.set_single_value("System Settings", key, value)
		except Exception:
			pass


def _apply_website_theme():
	"""Best-effort. Brand color is also enforced via app_include_css, so non-blocking."""
	try:
		theme_name = "Helix"
		if not frappe.db.exists("Website Theme", theme_name):
			theme = frappe.get_doc(
				{
					"doctype": "Website Theme",
					"theme": theme_name,
					"name": theme_name,
					"custom_overrides": f":root {{ --primary: {BRAND_COLOR}; --primary-color: {BRAND_COLOR}; }}",
				}
			)
			theme.insert(ignore_permissions=True, ignore_mandatory=True)
		frappe.db.set_single_value("Website Settings", "website_theme", theme_name)
	except Exception as e:
		print(f"[helix_branding] could not set website theme: {e}")
