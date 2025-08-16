# Copyright (c) 2025, Hayyan and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestDriver(FrappeTestCase):
    def test_full_name_set(self):
        test_driver = frappe.new_doc('Driver')
        test_driver.first_name = 'Modar'
        test_driver.last_name = 'Daood'
        test_driver.license_number = 'LN333999'
        test_driver.save()
    
        self.assertEqual(test_driver.full_name, "Modar Daood")
    
    def test_full_name_set_when_lastname_not_set(self):
        test_driver = frappe.new_doc('Driver')
        test_driver.first_name = 'Modar'
        test_driver.license_number = 'LN333999'
        test_driver.save()
    
        self.assertEqual(test_driver.full_name, "Modar")