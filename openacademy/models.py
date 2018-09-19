# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Courses(models.Model):
    _name = 'openacademy.course'

    name = fields.Char()
    user_id = fields.Many2one('res.users', string="Responsible")


class Sessions(models.Model):
    _name = 'openacademy.session'

    course_id = fields.Many2one('openacademy.course', string="Course")
    user_id = fields.Many2one('res.users', string="Instructor")
    start_date = fields.Date()
    seats = fields.Integer('Room Capacity')
    attendee_ids = fields.Many2many('res.partner', string="Attendees")
    attendee_count = fields.Integer(compute='_compute_total_attendee')
    
    @api.depends('attendee_ids')
    def _compute_total_attendee(self):
        for record in self:
            record.attendee_count = len(record.attendee_ids)

    @api.constrains('attendee_ids', 'seats')
    def _check_total_attendee(self):
        for record in self:
            if record.attendee_count  > record.seats:
                raise ValidationError("Too many attendees")