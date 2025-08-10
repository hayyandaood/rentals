# Copyright (c) 2025, Hayyan and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
    columns = [
        {"fieldname": "make", "label": "Make", "field_type": "data", "width": 200},
        {
            "fieldname": "total_revenue",
            "label": "Total Revenue",
            "field_type": "Currency",
            "options":"SYP"
        },
    ]
    makes = []
    revenues = []
    data = frappe.get_all(
        "Ride Booking",
        fields=["SUM(total_amount) AS total_revenue", "vehicle.make"],
        filters={"docstatus": 1, "vehicle": ("is", "set")},
        group_by="make",
    )
    
    for d in data:
        makes.append(d.make)
        revenues.append(d.total_revenue)
    chart = {
        "data":{
            "labels": makes,  #or [x.make from x in data]
            "datasets": [
                {
                    "values": revenues, # or [x.total_revenue for x in data]
                }
            ],
        },
        "type":"pie",
        "height":300, 
    }
    
    return columns, data, "Message Summary", chart
