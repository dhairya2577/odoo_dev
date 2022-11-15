from odoo import models, fields, api, _
from datetime import date

class PatientDetail(models.Model):
    _name = 'patient.medical'
    _rec_name = 'patient_name'

    patient_name = fields.Char(string="Patient Name", required=True)
    patient_address = fields.Char(string="Patient Address")
    patient_age = fields.Char(string="Patient Age", compute='_compute_total')
    patient_dob = fields.Date(string="Patient DOB")
    patient_number = fields.Char(string="Patient Number")
    total_opd = fields.Integer(string="OPD Count", compute='total_opd_count')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
    ], string='Status', readonly=True, copy=False, index=True, tracking=3, default='draft')
    color = fields.Integer(string="color")
    patient_seq = fields.Char(string='Doctor seq', copy=False, index=True, default=lambda self: _('New'))
    user_id = fields.Many2one('res.users', string="user id", store=True)

    def create_user_patient(self):
        for rec in self:
            vals = {
                'name': rec.patient_name,
                'login': rec.patient_name,
                'in_group_33': True,
                'in_group_1': True,
            }
            create_user = self.env['res.users'].create(vals)
            rec.user_id = create_user
            return create_user


    @api.model
    def create(self, vals):
        vals['patient_seq'] = self.env['ir.sequence'].next_by_code('patient.medical') or _('New')
        res = super(PatientDetail, self).create(vals)
        return res


    @api.depends("patient_dob")
    def _compute_total(self):
        for rec in self:
            today = date.today()
            if rec.patient_dob:
                rec.patient_age = today.year - rec.patient_dob.year
            else:
                rec.patient_age = 1

    @api.depends("patient_name")
    def total_opd_count(self):
        for rec in self:
            total_count = self.env['opd.medical'].search_count([("patient_id", "=", rec.id)])
            rec.total_opd = total_count


    def total_count(self):
        return {
            'name': 'OPD',
            'domain': [('patient_id', '=', self.id)],
            'res_model': 'opd.medical',
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
            'target': 'current',
        }


    def action_confirm(self):
        self.write({'state': 'confirm'})
        return True

    def action_cancel(self):
        self.write({'state': 'cancel'})
        return True

    def action_done(self):
        self.write({'state': 'done'})
        return True

    def action_draft(self):
        self.write({'state': 'draft'})
        return True
