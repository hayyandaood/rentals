// Copyright (c) 2025, Hayyan and contributors
// For license information, please see license.txt

frappe.ui.form.on("Ride Booking", {
	refresh(frm) {
        frm.add_custom_button( ('Change Rate'), () => {
            frm.set_value({
                'rate': 60,
                'total_amount' : 100
            })
            frm.save()
        },('Actions'))
	},
    rate(frm) {
        frm.trigger("update_total_amount")
    },
    update_total_amount(frm){
        let total_d = 0;
        for (let item of frm.doc.items){ //practice
            total_d += item.distance
        }
        frm.set_value(
          "total_amount", total_d * frm.doc.rate,
        )
    }
});

frappe.ui.form.on('Ride Booking Item', {
	refresh(frm) {
		// your code here
	},
    distance(frm, cdt, cdn){
        //console.log(cdt, cdn)
        //my_child = frappe.get_doc(cdt, cdn);
        //frappe.model.set_value(cdt,cdn,"source", "Updated Source")
        frm.trigger("update_total_amount")

        // let row = locals[cdt][cdn]
        // console.log(row.source)
    },
    items_remove(frm){
        frm.trigger("update_total_amount")
    }
})