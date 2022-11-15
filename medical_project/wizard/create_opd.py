from odoo import api, fields, models
from datetime import date

class CreateOpd(models.TransientModel):
    _name = 'create.opd'

    date = fields.Date(string="Date")
    patient_id = fields.Many2one('patient.medical', string="Patient Name")
    address = fields.Char(string="Patient Address")
    age = fields.Char(string="Patient Age", compute='_compute_total')
    dob = fields.Date(string="Patient DOB")
    dep_id = fields.Many2one('department.medical', string="Department")
    doc_id = fields.Many2one('doctor.medical', string="Doctor", domain="[('department_id', '=',dep_id)]")
    medicine_id = fields.Many2many('medicine.medical', string="Medicine")

    # @api.onchange('dep_id')
    # def onchange_dep_id(self):
    #     for rec in self:
    #         return {'domain': {'doc_id': [('department_id.id', '=', rec.dep_id.id)]}}

    def create_opd(self):
        for rec in self:
            dic = {
                'patient_id': rec.patient_id.id,
                'department_id': rec.dep_id.id,
                'doctor_id': rec.doc_id.id,
                'today_date': rec.date,
                'medicine_line': rec.medicine_id
            }

            new_opd=self.env['opd.medical'].create(dic)

            action = {
                'name': 'OPD',
                'res_id': new_opd.id,
                'res_model': 'opd.medical',
                'view_mode': 'form',
                'type': 'ir.actions.act_window',
                'target': 'current',
            }

            return action

    @api.depends("dob")
    def _compute_total(self):
        for rec in self:
            today = date.today()
            if rec.dob:
                rec.age = today.year - rec.dob.year
            else:
                rec.age = 1

    @api.onchange('patient_id')
    def onchange_name(self):
        if self.patient_id:
            if self.patient_id.patient_address:
                self.address = self.patient_id.patient_address
            if self.patient_id.patient_dob:
                self.dob = self.patient_id.patient_dob
            if self.patient_id.patient_age:
                self.age = self.patient_id.patient_age

