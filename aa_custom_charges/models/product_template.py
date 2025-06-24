
from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    hsn_code = fields.Char(string="HSN Code")
    part_number = fields.Char(string="Part Number")
    item_make = fields.Char(string="Item Make")
    model_number = fields.Char(string="Model Number")