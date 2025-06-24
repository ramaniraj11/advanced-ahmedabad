from odoo import models, fields

class IrSequence(models.Model):
    _inherit = 'ir.sequence'

    def _create_date_range_seq(self, date):
        if self._context.get('sale_order'):
            # Set date_from and date_to to the same date → daily reset
            date_from = date
            date_to = date

            return self.env['ir.sequence.date_range'].sudo().create({
                'date_from': date_from,
                'date_to': date_to,
                'sequence_id': self.id,
            })

        # Use default logic for other cases
        return super()._create_date_range_seq(date)
