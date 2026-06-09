import frappe

def execute():
    frappe.db.sql("""UPDATE `tabCourse` SET course_name = 'OOps with cpp' WHERE course_name = 'cpp'""")
    frappe.db.commit()