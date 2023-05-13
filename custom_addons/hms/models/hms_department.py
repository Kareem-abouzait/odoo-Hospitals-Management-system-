from odoo import fields, models, api
class HMS_Department(models.Model):
    _name = "hms.department"
    _description = "Department Record"
    _rec_name = "name"
    name = fields.Char(string="Name", required=True)
    capacity = fields.Integer(string="Capacity")
    is_open = fields.Boolean(string="Is Open")
    patient_ids = fields.One2many(
        "hms.patient", "department_id", string="Patients"
    )
    doctor_ids = fields.Many2many("hms.doctor", string="Doctors")
    
    @api.onchange("is_open")
    def onchange_is_open(self):
        if self.is_open == False:
            self.doctor_ids = [(5, 0, 0)]
            return {
                "warning": {
                    "title": "Warning",
                    "message": "You can't choose a closed department",
                }
            }
