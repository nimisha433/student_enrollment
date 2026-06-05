# Copyright (c) 2026, Nimisha Verma and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Enrollment(Document):
    def validate(self):
        frappe.msgprint("Validation logic executed for Enrollment")

        if not self.student_name:
            frappe.throw("Student is required")

        if not self.course:
            frappe.throw("Course is required")

        if self.registration_fee < 0:
            frappe.throw("Registration Fee cannot be negative")