from odoo import models, fields, api, _
from datetime import date


class DoctorDetail(models.Model):
    _name = 'doctor.medical'
    _rec_name = 'doctor_name'

    doctor_name = fields.Char(string="Doctor Name")
    doctor_address = fields.Char(string="Doctor Address")
    doctor_age = fields.Char(string="Doctor Age", compute='_compute_total_doctor')
    doctor_dob = fields.Date(string="Doctor DOB")
    doctor_number = fields.Char(string="Doctor Number")
    opd_count = fields.Integer(string="Opd Count", compute="total_opd_visit_count")
    department_id = fields.Many2one('department.medical', string='department')
    color = fields.Integer(string="color")
    doc_seq = fields.Char(string='Doctor seq', copy=False, index=True, default=lambda self: _('New'))
    doctor_user_id = fields.Many2one('res.users', string="user id", store=True)

    def create_user_doctor(self):
        for rec in self:
            vals = {
                'name': rec.doctor_name,
                'login': rec.doctor_name,
                'in_group_31': True,
                'in_group_1': True,
            }
            user_id = self.env['res.users'].create(vals)
            rec.doctor_user_id = user_id
            return user_id

    @api.model
    def create(self, vals):
        vals['doc_seq'] = self.env['ir.sequence'].next_by_code('doctor.medical') or _('New')
        res = super(DoctorDetail, self).create(vals)
        return res


    @api.depends("doctor_dob")
    def _compute_total_doctor(self):
        for rec in self:
            today = date.today()
            if rec.doctor_dob:
                rec.doctor_age = today.year - rec.doctor_dob.year
            else:
                rec.doctor_age = 1

    @api.depends("doctor_name")
    def total_opd_visit_count(self):
        for rec in self:
            total_opd_visit = self.env['opd.medical'].search_count([("doctor_id", "=", rec.id)])
            rec.opd_count = total_opd_visit

    def total_opds(self):
        return {
            'name': 'OPD',
            'domain': [('doctor_id', '=', self.id)],
            'res_model': 'opd.medical',
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
            'target': 'current',
        }
