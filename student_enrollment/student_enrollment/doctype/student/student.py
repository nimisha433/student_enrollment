# Copyright (c) 2026, Nimisha Verma and contributors
# For license information, please see license.txt

# import frappe
import frappe
from frappe.model.document import Document


class Student(Document):

    def after_insert(self):

        user = frappe.db.get_value(
            "User",
            {"email": self.email},
            "name"
        )

        if not user:
            return

        has_student_role = frappe.db.exists(
            "Has Role",
            {
                "parent": user,
                "role": "Students"
            }
        )

        if (
            has_student_role
            and not frappe.db.exists(
                "User Permission",
                {
                    "user": user,
                    "allow": "Student",
                    "for_value": self.name
                }
            )
        ):
            frappe.get_doc({
                "doctype": "User Permission",
                "user": user,
                "allow": "Student",
                "for_value": self.name
            }).insert(ignore_permissions=True)