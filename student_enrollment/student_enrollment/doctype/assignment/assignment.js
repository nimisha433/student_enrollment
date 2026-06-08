// Copyright (c) 2026, Nimisha Verma and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Assignment", {
// 	refresh(frm) {

// 	},
// });


frappe.ui.form.on("Assignment", {
    refresh(frm) {
        set_student_filter(frm);
    },

    course(frm) {
        set_student_filter(frm);
        frm.refresh_field("student");
    },

    semester(frm) {
        set_student_filter(frm);
        frm.refresh_field("student");
    },

    setup(frm) {
        frm.make_methods = {
            "ToDo": () => {
                frappe.model.open_mapped_doc({
                    method: "student_enrollment.student_enrollment.doctype.assignment.assignment.make_todo",
                    frm: frm
                });
            }
        };
    }
});


function set_student_filter(frm) {
    frm.set_query("student", function () {

        let filters = {};

        if (frm.doc.course) {
            filters.course = frm.doc.course;
        }

        if (frm.doc.semester) {
            filters.semester = frm.doc.semester;
        }

        return {
            query: "student_enrollment.api.get_enrolled_students",
            filters: filters
        };
    });
}