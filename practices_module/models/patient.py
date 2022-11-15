from odoo import api,fields,models,_
from datetime import date

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ["mail.thread"]
    _description = "Hospital patient"

    name = fields.Char(string="Patient Name")
    age = fields.Integer(string="Patient Age",compute='_compute_age')
    gender = fields.Selection([
        ('male','Male'),('female','Female'),('other','Other')
    ],string="gender",default = 'male')
    date_of_birth=fields.Date(string="Date of birth")



    def _compute_age(self):
        for rec in self:
            today=date.today()
            if rec.date_of_birth:
                rec.age=today.year-rec.date_of_birth.year
            else:
                rec.age=1
