import frappe

@frappe.whitelist()
def get_enrolled_students(doctype, txt, searchfield, start, page_len, filters):

	conditions = {}

	if filters.get("course"):
		conditions["course"] = filters.get("course")

	if filters.get("semester"):
		conditions["semester"] = filters.get("semester")

	enrollments = frappe.get_all(
		"Enrollment",
		filters=conditions,
		fields=["student"]
	)

	students = [d.student for d in enrollments]

	if not students:
		return []

	return frappe.db.sql("""
		SELECT
			name, student_name
		FROM tabStudent
		WHERE name IN %(students)s
		AND ({key} LIKE %(txt)s
			OR student_name LIKE %(txt)s)
		LIMIT %(start)s, %(page_len)s
	""".format(key=searchfield), {
		"students": tuple(students),
		"txt": f"%{txt}%",
		"start": start,
		"page_len": page_len
	})