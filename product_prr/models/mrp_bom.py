from odoo import fields, models

class MrpBom(models.Model):
    _inherit = 'mrp.bom'

    name = fields.Char(
        string='Name'
    )
    default = fields.Boolean(
        strong='Default',
        default=False,
    )
