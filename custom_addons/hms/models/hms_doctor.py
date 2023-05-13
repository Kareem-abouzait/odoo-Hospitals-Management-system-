from odoo import fields, models, api
class HMS_Doctor(models.Model):
    _name = "hms.doctor"
    _description = "Doctor Record"
    _rec_name = "fname"
    fname = fields.Char(string="First Name", required=True)
    lname = fields.Char(string="Last Name", required=True)
    img=fields.Binary(string="Image")
    patient_ids = fields.One2many(
        "hms.patient", "doctor_id", string="Patients"
    )
    department_id = fields.Many2one("hms.department", string="Department")
    