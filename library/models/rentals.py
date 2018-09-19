# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _

class Rentals(models.Model):
    _name = 'library.rental'
    _description = 'Book rental'

    customer_id = fields.Many2one('library.partner', string='Customer')
    book_id = fields.Many2one('library.book', string='Book')
    rental_date = fields.Date(string='Rental date')
    return_date = fields.Date(string='Return date')
    
    book_name = fields.Char(related='book_id.name')
    book_authors_ids = fields.Many2many(related='book_id.authors_ids')
    book_edition_date =  fields.Date(related='book_id.edition_date')
    book_isbn = fields.Char(related='book_id.isbn')
    book_publisher_id = fields.Many2one(related='book_id.publisher_id')
    #book_rental_ids = fields.Char(related='library.book.rental_ids.')
    
    customer_name = fields.Char(related='customer_id.name')
    customer_email = fields.Char(related='customer_id.email')
    customer_address = fields.Text(related='customer_id.address')
    customer_partner_type = fields.Selection(related='customer_id.partner_type')
    #customer_rental_ids = fields.Char(related='library.partner.rental_ids.')