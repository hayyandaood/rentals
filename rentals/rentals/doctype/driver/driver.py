# Copyright (c) 2025, Hayyan and contributors
# For license information, please see license.txt
import frappe
from frappe.model.document import Document


class Driver(Document):
    
    def before_save(self):
        self.full_name = f"{self.first_name} {self.last_name}"  # 1 way
        #self.full_name = self.first_name + " " + self.last_name # 2 way

    #from bench console(d.get_doc = "Driver" , d.send_alert)
    def send_alert(self):
        print("sending message")


#user : hayyan@developer.com
#API Secret: b30caa2e5623434
#API KEY: d467f65465a3a0e


#user : api@developer.com
#API Secret: 7612f2e71285a6c
#API KEY: 3ec66f9204a850b