// Helix whitelabel — minimal, non-invasive.
// Sets browser tab title prefix. No DOM mutation, no observer, no boot patching.
(function () {
	"use strict";
	try {
		if (typeof frappe !== "undefined" && frappe.ui && frappe.ui.set_title_prefix) {
			frappe.ui.set_title_prefix("Helix");
		}
	} catch (e) {
		// silent: never block page rendering
	}
})();
