from odoo import api,fields,models,_

class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ["mail.thread"]
    _description = "Hospital Appointment"

    patient_id = fields.Many2one('hospital.patient',string="Patient")
    appointment_time = fields.Datetime(string='Appointment Time',default=fields.Datetime.now)
    booking_date = fields.Date(string='Booking date',default=fields.Date.context_today)

    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_consultant', 'In Consultant'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')
    ], string='Status', index=True, tracking=3, default='draft')



