import frappe 


def get_conext(context):
    context.my_secret_imoji = "hi"
    context.number = 1990

    context.no_cache = 1
    return context