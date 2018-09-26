# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _
import math

class Rentals(models.Model):
    _name = 'library.rental'
    _description = 'Book rental'
    _order = "rental_date desc,return_date desc"
    _inherit = 'mail.thread'

    customer_id = fields.Many2one(
        'res.partner',
        'Customer',
        domain=[('customer','=',True), ],
        required=True,
    )
    book_id = fields.Many2one(
        'product.product',
        'Book',
        domain=[('book','=',True)],
        required=True,
    )
    rental_date =  fields.Date(string='Rental date', required=True, default=lambda self: fields.Date.today())
    return_date =  fields.Date(string='Return date', required=True, default=lambda self: fields.Date.today())
    actual_date =  fields.Date(string='Actual date', required=True)

    rental_cost = fields.Integer(compute='_compute_rental_cost')
    rental_fine = fields.Integer(compute='_compute_rental_cost')

    @api.depends('rental_date', 'return_date', 'book_id.rental_cost', 'book_id.late_fine')
    def _compute_rental_cost(self):
        for item in self:
            item.rental_cost = item.book_id.rental_cost * (fields.Date.from_string(item.return_date) - fields.Date.from_string(item.rental_date)).days
            if item.actual_date:
                item.rental_fine = item.book_id.late_fine * (fields.Date.from_string(item.actual_date) - fields.Date.from_string(item.return_date)).days
            else:
                item.rental_fine = max(item.book_id.late_fine * (fields.Date.from_string(fields.Date.today()) - fields.Date.from_string(item.return_date)).days, 0)

    @api.one
    def remind(self):
        for rental in self:
            if fields.Date.from_string(fields.Date.today()) > fields.Date.from_string(rental.return_date):
                self.env.ref('library.template_reminder').send_mail(customer_id.id)