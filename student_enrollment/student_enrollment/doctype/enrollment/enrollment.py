# Copyright (c) 2026, Nimisha Verma and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Enrollment(Document):

    def validate(self):

        if not self.student:
            frappe.throw("Student is required")

        if not self.course:
            frappe.throw("Course is required")

        if self.registration_fee < 0:
            frappe.throw("Registration Fee cannot be negative")

    def on_submit(self):

        course = frappe.get_doc(
            "Course",
            self.course
        )

        if course.available_seats <= 0:
            frappe.throw("No seats available for this course")

        course.available_seats -= 1

        course.save()

    def on_cancel(self):

        course = frappe.get_doc(
            "Course",
            self.course
        )

        course.available_seats += 1

        course.save()