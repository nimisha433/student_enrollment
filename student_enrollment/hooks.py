app_name = "student_enrollment"
app_title = "Student Enrollment"
app_publisher = "Nimisha Verma"
app_description = "assignment"
app_email = "nimisha@idesignmylife.net"
app_license = "mit"


scheduler_events = {
    "daily": [
        "student_enrollment.attendance.update_attendance_count"
    ]
}
# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "student_enrollment",
# 		"logo": "/assets/student_enrollment/logo.png",
# 		"title": "Student Enrollment",
# 		"route": "/student_enrollment",
# 		"has_permission": "student_enrollment.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/student_enrollment/css/student_enrollment.css"
# app_include_js = "/assets/student_enrollment/js/student_enrollment.js"

# include js, css files in header of web template
# web_include_css = "/assets/student_enrollment/css/student_enrollment.css"
# web_include_js = "/assets/student_enrollment/js/student_enrollment.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "student_enrollment/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "student_enrollment/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "student_enrollment.utils.jinja_methods",
# 	"filters": "student_enrollment.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "student_enrollment.install.before_install"
# after_install = "student_enrollment.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "student_enrollment.uninstall.before_uninstall"
# after_uninstall = "student_enrollment.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "student_enrollment.utils.before_app_install"
# after_app_install = "student_enrollment.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "student_enrollment.utils.before_app_uninstall"
# after_app_uninstall = "student_enrollment.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "student_enrollment.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"student_enrollment.tasks.all"
# 	],
# 	"daily": [
# 		"student_enrollment.tasks.daily"
# 	],
# 	"hourly": [
# 		"student_enrollment.tasks.hourly"
# 	],
# 	"weekly": [
# 		"student_enrollment.tasks.weekly"
# 	],
# 	"monthly": [
# 		"student_enrollment.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "student_enrollment.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "student_enrollment.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "student_enrollment.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["student_enrollment.utils.before_request"]
# after_request = ["student_enrollment.utils.after_request"]

# Job Events
# ----------
# before_job = ["student_enrollment.utils.before_job"]
# after_job = ["student_enrollment.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"student_enrollment.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

