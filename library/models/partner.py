# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _

class Partner(models.Model):
    _inherit = 'res.partner'

    author =  fields.Boolean('is an Author', default=False)
    publisher =  fields.Boolean('is a Publisher', default=False)
    rental_ids = fields.One2many(
        'library.rental',
        'customer_id',
        string='Rentals')
    book_ids = fields.Many2many(
        comodel_name="product.product",
        string="Books",
        domain=[('book','=',True), ],
    )
    nationality_id = fields.Many2one(
        'res.country',
        'Nationality',
    )
    birthdate =  fields.Date('Birthdate',)

    owing = fields.Integer(compute='_compute_owing', string='Owing', store=True)

    @api.depends('rental_ids.rental_cost', 'rental_ids.rental_fine')
    def _compute_owing(self):
        for partner in self:
            owing = 0
            for rental in partner.rental_ids:
                owing += rental.rental_cost + rental.rental_fine
            partner.owing = owing
