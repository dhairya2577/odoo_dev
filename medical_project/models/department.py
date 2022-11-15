from odoo import models, fields, api, _

class DoctorDetail(models.Model):
    _name = 'department.medical'
    _rec_name = 'department'

    department = fields.Char(string="Department")
    department_seq = fields.Char(string='Doctor seq', copy=False, index=True, default=lambda self: _('New'))

    @api.model
    def create(self, vals):
        vals['department_seq'] = self.env['ir.sequence'].next_by_code('department.medical') or _('New')
        res = super(DoctorDetail, self).create(vals)
        return res

