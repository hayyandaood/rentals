// Copyright (c) 2025, Hayyan and contributors
// For license information, please see license.txt

frappe.ui.form.on("Vehicle", {
	refresh(frm) {

	},
    get_summary(frm){
        frm.get_field("summary").$wrapper.append("<h1>Here Is your summary</h1>")
    }
    
});
