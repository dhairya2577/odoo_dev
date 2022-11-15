from odoo import models, fields, api

class MedicineDetail(models.Model):
    _name = 'medicine.medical'

    medicine_id = fields.Many2one('opd.medical', string="Medicine Name")
    medicine_id2 = fields.Many2one('medicine.pharmacy', string="Medicine Name")
    quantity = fields.Integer(string="Medicine Quantity", default=1.0)
    medicine_category = fields.Selection([
        ('tablet', 'Tablet'),
        ('syrup', 'Syrup'),
        ('ointment', 'Ointment')
    ], string="medicine Category")
    currency_id = fields.Many2one('res.currency', related='medicine_id.currency_id')
    price_unit = fields.Float('Unit Price', required=True, digits='Product Price', default=0.0)
    price_subtotal = fields.Monetary(string='Subtotal', store=True, compute='compute_price_subtotal')

    tax_id = fields.Many2many('account.tax', string='Taxes', context={'active_test': False})
    price_tax = fields.Float(compute='compute_price_subtotal', string='Total Tax', store=True)

    @api.depends('price_unit', 'quantity', 'tax_id')
    def compute_price_subtotal(self):
        for rec in self:
            rec.price_subtotal = rec.price_unit * rec.quantity
            taxes = rec.tax_id.compute_all(rec.price_unit, rec.medicine_id.currency_id, rec.quantity)
            rec.price_tax = sum(t.get('amount', 0.0) for t in taxes.get('taxes', []))


    @api.onchange('medicine_id2')
    def select_price_auto(self):
        for rec in self:
            rec.price_unit = self.medicine_id2.price
            rec.quantity = self.medicine_id2.quantity




class MedicalPharmacy(models.Model):
    _name = 'medicine.pharmacy'
    _rec_name = 'medicine_name'

    medicine_name = fields.Char(string="Medicine Name")
    quantity = fields.Integer(string="Medicine Quantity", default=1.0)
    price = fields.Float('Unit Price', required=True, digits='Product Price', default=0.0)

