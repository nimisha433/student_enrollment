// Copyright (c) 2026, Nimisha Verma and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Student", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on('Student', {
    refresh: function (frm) {

        frm.add_custom_button('Get Assignment Details', function () {

            frappe.call({
                method: "frappe.client.get_list",
                args: {
                    doctype: "Assignment",
                    filters: {
                        student: frm.doc.name
                    },
                    fields: ["assignment_details"],
                    order_by: "creation desc",
                    limit_page_length: 1
                },

                callback: function (r) {

                    if (r.message && r.message.length > 0) {
                        let data = r.message[0];

                        let dialog = new frappe.ui.Dialog({
                            title: 'Latest Assignment',
                            fields: [
                                {
                                    fieldname: 'assignment_details',
                                    fieldtype: 'Small Text',
                                    label: 'Assignment',
                                    default: data.assignment_details,
                                    read_only: 1
                                }
                            ]
                        });

                        dialog.show();

                    } else {
                        frappe.msgprint("No assignment found for this student.");
                    }
                }
            });

        });
    }
});