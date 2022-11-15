from odoo import models, fields, api, _


class OpdDetail(models.Model):
    _name = 'opd.medical'
    _rec_name = 'opd_id'

    opd_id = fields.Char(string='Opd seq', copy=False, index=True, default=lambda self: _('New'))
    patient_number = fields.Char(string="Patient Number")
    patient_dob = fields.Date(string="Patient DOB")
    patient_age = fields.Char(string="Patient Age")
    department_id = fields.Many2one('department.medical', string="Department")
    doctor_id = fields.Many2one('doctor.medical', string="Doctor", domain="[('department_id','=',department_id)]")
    doctor_number = fields.Char(string="Doctor Number")
    today_date = fields.Date(string="Today Date")
    patient_id = fields.Many2one("patient.medical", string="Patient Name")
    medicine_line = fields.One2many('medicine.medical', 'medicine_id', string="Medicine")
    opd_state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
    ], string='Status Opd', readonly=True, copy=False, index=True, tracking=3, default='draft')
    color = fields.Integer(string="color")
    company_id = fields.Many2one('res.company', string='company', default=lambda self: self.env.company)
    currency_id = fields.Many2one('res.currency', related='company_id.currency_id')

    grand_total = fields.Monetary(string="Total Amount", compute='compute_total_price')
    untaxed_amount = fields.Monetary(string='Untaxed Amount', compute='compute_total_price')
    taxes = fields.Monetary(string='Taxes', compute='compute_total_price')



    @api.depends('medicine_line')
    def compute_total_price(self):
        for rec in self:
            untax_amount = tax_amount = 0
            for line in rec.medicine_line:
                if line.medicine_id2:
                    untax_amount += line.price_subtotal
                    tax_amount += line.price_tax
            rec.update({
                'untaxed_amount': untax_amount,
                'taxes': tax_amount,
                'grand_total': untax_amount + tax_amount,
            })



    @api.model
    def create(self, vals):
        vals['opd_id'] = self.env['ir.sequence'].next_by_code('opd.medical') or _('New')
        res = super(OpdDetail, self).create(vals)
        return res


    def action_opd_confirm(self):
        self.write({'opd_state': 'confirm'})
        return True

    def action_opd_cancel(self):
        self.write({'opd_state': 'cancel'})
        return True

    def action_opd_done(self):
        self.write({'opd_state': 'done'})
        return True

    def action_opd_draft(self):
        self.write({'opd_state': 'draft'})
        return True

