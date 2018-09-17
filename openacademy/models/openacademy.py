from odoo import api, fields, models

class Course(models.Model):

    _name = 'openacademy.course'

    label = fields.Char()
    level = fields.Integer()
    sessions = fields.One2many('openacademy.session', 'course')

class Session(models.Model):

    _name = 'openacademy.session'
    
    date = fields.Date()
    active = fields.Boolean()
    archive = fields.Boolean()
    maester = fields.Many2one('openacademy.maester')
    attendees = fields.Many2many('openacademy.attendee')
    course = fields.Many2one('openacademy.course')
    
class Attendee(models.Model):

    _name = 'openacademy.attendee'
    
    name = fields.Char()
    sessions = fields.Many2many('openacademy.session')
    
class Maester(models.Model):

    _name = 'openacademy.maester'
    
    name = fields.Char()
    sessions = fields.One2many('openacademy.session', 'maester')
