# Copyright (c) 2026, Nimisha Verma and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc

class Assignment(Document):
    def validate(self):

        enrolled = frappe.db.exists(
            "Enrollment",
            {
                "student": self.student,
                "course": self.course,
                "semester": self.semester
            }
        )

        if not enrolled:
            frappe.throw(
                f"Student {self.student} is not enrolled in {self.course} for {self.semester}"
            )




@frappe.whitelist()
def make_todo(source_name, target_doc=None):

    def set_values(source, target):
        target.reference_type = "Assignment"
        target.description = f"Assignment for {source.student}"
        target.assigned_by = "Suryansh Chaudhary"
        target.allocated_to = source.student


    return get_mapped_doc(
        "Assignment",
        source_name,
        {
            "Assignment": {
                "doctype": "ToDo",
                "field_map": {
                    "name": "reference_name"
                }
            }
        },
        target_doc,
        set_values
    )