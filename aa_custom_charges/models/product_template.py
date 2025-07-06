from odoo import fields, models, api


class ProductTemplate(models.Model):
    _inherit = "product.template"

    part_number = fields.Char(string="Part Number")
    item_make = fields.Char(string="Item Make")
    model_number = fields.Char(string="Model Number")

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        args = list(args or [])
        if not name:
            return super().name_search(name=name, args=args, operator=operator, limit=limit)

        domain = ['|', '|',
                  ('part_number', operator, name),
                  ('item_make', operator, name),
                  ('model_number', operator, name)]
        if args:
            domain = ['&'] + args + domain

        templates = self.search_fetch(domain, ['display_name'], limit=limit)
        return [(template.id, template.display_name) for template in templates]

class ProductProduct(models.Model):
        _inherit = 'product.product'

        @api.model
        def name_search(self, name='', args=None, operator='ilike', limit=100):
            args = list(args or [])
            if not name:
                return super().name_search(name=name, args=args, operator=operator, limit=limit)

            domain = ['|', '|',
                      ('part_number', operator, name),
                      ('item_make', operator, name),
                      ('model_number', operator, name)]
            if args:
                domain = ['&'] + args + domain

            products = self.search_fetch(domain, ['display_name'], limit=limit)
            return [(product.id, product.display_name) for product in products]