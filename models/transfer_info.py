from odoo import api, fields, models

class Transfers(models.Model):
    _inherit = 'stock.picking'
    prod_name = fields.Char('prod name')