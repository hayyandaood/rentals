import frappe 

#@frappe.whitelist()# for only logged in users //authorized 
@frappe.whitelist(allow_guest=True) #for any one # call from bruno
def get_name():
    # your API logic here
    
    return "Hayyan"

def my_function_submits_hundred_invoices():
    #print("HAYYAN BACKGROUND JOB")
    frappe.errprint("HAYYAN BACKGROUND JOB")

