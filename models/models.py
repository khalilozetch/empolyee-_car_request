# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CarRequest(models.Model):
    _name = 'car.request'  # table in database
    _rec_name = 'name'
    _description = 'Car Request'
    name = fields.Char(string="Request", required=True, )
    date_from = fields.Char(string=" Starting Date ", default=fields.datetime.now(), )
    date_to = fields.Char(string=" End Date ", required=False, )
    employee_id = fields.Many2one(comodel_name="hr.employee", string="Employee", required=True, )
    car_id = fields.Many2one(comodel_name="fleet.vehicl", string="Car", required=True, )
