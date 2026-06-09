import frappe

def execute():


    frappe.db.sql("""INSERT INTO `tabCourse` (name, course_name, course_fee)
        VALUES
        ('COURSE001', 'Software Engineering', 16000),
        ('COURSE002', 'Compiler Design', 13000),
        ('COURSE003', 'Data Structures', 20000),
        ('COURSE004', 'Blockchain', 40000),
        ('COURSE005', 'Full Stack Web Development', 25000)
    """)

frappe.db.commit()