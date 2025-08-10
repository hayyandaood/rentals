// Copyright (c) 2025, Hayyan and contributors
// For license information, please see license.txt

frappe.ui.form.on("Ride Order", {
  onload(frm) {
    console.log("running load...");
  },
  setup(frm) {
    console.log("setup load...");
  },
  refresh(frm) {
    console.log("on refresh...");
    if (frm.doc.status !== "New") {
      frm.add_custom_button(__("Accept"), () => {
        //status = accepted
        frm.set_value({
          status: "Accepted",
        });
        //save th form
        frm.save();
      },"Actions");
      
      frm.add_custom_button(__("Reject"), () => {
        //status = accepted
        frm.set_value({
          status: "Rejected",
        });
        //save th form
        frm.save();
      },"Actions");
    }
  },
  
  status(frm) {
    frappe.show_alert({
        message: "Status Changed",
        indicator: "info"
    });
  }
});