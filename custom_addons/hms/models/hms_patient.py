from odoo import fields, models, api


class HMS_Patient(models.Model):
    _name = "hms.patient"
    _description = "Patient Record"
    _rec_name = "fname"

    fname = fields.Char(string="First Name", required=True)
    lname = fields.Char(string="Last Name", required=True)
    birthdate = fields.Date(string="Birth Date")
    age = fields.Integer(string="Age")
    history = fields.Html(string="Medical History")
    cr_ratio = fields.Float(string="CR Ratio")
    image = fields.Binary(string="Image")
    blood_type = fields.Selection(
        [
            ("A+", "A+ve"),
            ("A-", "A-ve"),
            ("B+", "B+ve"),
            ("B-", "B-ve"),
            ("AB+", "AB+ve"),
            ("AB-", "AB-ve"),
            ("O+", "O+ve"),
            ("O-", "O-ve"),
        ],
        string="Blood Type",
    )

    pcr = fields.Boolean(string="PCR", default=False)
    address = fields.Text(string="Address")
    department_id = fields.Many2one("hms.department", string="Department")
    doctor_id = fields.Many2one("hms.doctor", string="Doctor")
    related_capacity = fields.Integer(
        string="Related Capacity", related="department_id.capacity"
    )

    state = fields.Selection(
        [
            ("undetermined", "Undetermined"),
            ("good", "Good"),
            ("fair", "Fair"),
            ("serious", "Serious"),
        ],
        string="State",
        default="undetermined",
    )

    @api.constrains("pcr", "cr_ratio")
    def _check_pcr_cr_ratio(self):
        for record in self:
            if record.pcr and not record.cr_ratio:
                raise models.ValidationError(
                    "You must enter a CR Ratio if PCR is checked"
                )

    @api.onchange("age")
    def onchange_age(self):
        if self.age < 50:
            self.history = False
        if self.age < 30 and self.age != 0:
            self.pcr = True
            return {
                "warning": {
                    "title": "Warning",
                    "message": " PCR is checked",
                }
            }

    # @api.onchange("department_id.capacity")
    # def onchange_department_id_capacity(self):
    #     if self.department_id.capacity == 0:
    #         return {
    #             "warning": {
    #                 "title": "Warning",
    #                 "message": "You can't choose a closed department",
    #             }
    #         }
