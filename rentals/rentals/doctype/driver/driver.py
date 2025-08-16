# Copyright (c) 2025, Hayyan and contributors
# For license information, please see license.txt
import frappe
from frappe.model.document import Document
from frappe.desk.form import assign_to

class Driver(Document):
    
    def before_save(self):
        #do it from server script
        # print("before_save")
        # if self.last_name:
        #     self.full_name = f"{self.first_name} {self.last_name}"  # 1 way
        #     #self.full_name = self.first_name + " " + self.last_name # 2 way
        # else:
        #     #self.full_name = self.first_name
        #     self.full_name = f"{self.first_name}"
        pass

    
    #from bench console(d.get_doc = "Driver" , d.send_alert)
    def send_alert(self):
        print("sending message")

    def after_insert(self):
        print("validated")
        assign_to.add({
            "assign_to": ["hayyan@developer.com","api@developer.com"],
            "doctype": self.doctype,
            "name":self.name,
            "description": "please veiw the task"
        })
        

#user : hayyan@developer.com
#API Secret: b30caa2e5623434
#API KEY: d467f65465a3a0e


#user : api@developer.com
#API Secret: 7612f2e71285a6c
#API KEY: 3ec66f9204a850b