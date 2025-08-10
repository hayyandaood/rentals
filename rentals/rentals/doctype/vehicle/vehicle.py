# Copyright (c) 2025, Hayyan and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator


class Vehicle(WebsiteGenerator):
    def before_save(self):
        self.set_title()
        #self.title = f"{self.make} {self.model}, {self.year}"  # 1 way
        #self.full_name = self.first_name + " " + self.last_name # 2 way
    
    def set_title(self):
        self.title = f"{self.make} {self.model}, {self.year}"
