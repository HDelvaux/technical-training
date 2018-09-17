from odoo import api, models, fields

class Book(models.Model):

    _name = 'library.book'
    
    authors = fields.Many2many('library.author')
    editors = fields.Many2many('library.editors')
    customers = fields.Many2many('library.customer')
    edition_year = fields.Integer()
    ISBN = fields.Integer()


class Author(models.Model):

    _name = 'library.author'

    name = fields.Char()
    books = fields.Many2many('library.book')
    
class Editor(models.Model):

    _name = 'library.editor'

    name = fields.Char()
    books = fields.Many2many('library.book')
    
class Customer(models.Model):

    _name = 'library.customer'

    name = fields.Char()
    address = fields.Char()
    emails = fields.Char()
    books  = fileds.Many2many('library.book')
