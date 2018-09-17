from odoo import fields, models

class Course(models.Model)

    _name = 'openacademy.course'

    label = fields.Char()
    level = fields.Integer()
    sessions = fields.Many2one('openacademy.session')

class Session(models.Model)

    _name = 'openacademy.session'
    
    date = fields.Date()
    maester = fields.One2many('')
    attendees = fields.Many2many('')
    active = fields.Boolean()
    archive = fields.Boolean()
    
class Attendee(models.Model)

    _name = 'openacademy.attendee'
    
    name = fields.Char()
    
class Maester(models.Model)

    _name = 'openacademy.'
    
    name = fields.Char()