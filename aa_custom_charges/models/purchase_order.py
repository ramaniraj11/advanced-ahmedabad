from email.policy import default

from odoo import fields, models, api,_


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    company_name = fields.Selection([
        ("ats", "ATS"),
        ("acr", "ACR")],
        string="Company Name",
        required=True,
        default='ats')

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            # Determine the date to use for the sequence
            seq_date = fields.Datetime.context_timestamp(
                self, fields.Datetime.to_datetime(vals['date_order'])
            ) if 'date_order' in vals else fields.Datetime.context_timestamp(self, fields.Datetime.now())

            # Select the appropriate sequence code based on the company_name selection
            company_name = vals.get('company_name', 'ats')  # Default to 'ats' if missing
            sequence_code = f"purchase.order.{company_name}"

            # Generate the name using the correct sequence
            vals['name'] = self.env['ir.sequence'].with_context(sale_order=True).next_by_code(
                sequence_code, sequence_date=seq_date) or _("New")

        return super(PurchaseOrder, self).create(vals_list)

    def write(self, vals):
        if 'company_name' in vals:
            for order in self:
                # Use updated company_name if present, otherwise fallback to existing
                new_company_name = vals['company_name']
                sequence_code = f"purchase.order.{new_company_name}"

                # Use date_order for the sequence date or now if not set
                seq_date = order.date_order or fields.Datetime.now()
                seq_date = fields.Datetime.context_timestamp(self, fields.Datetime.to_datetime(seq_date))

                # Generate new name using the updated company_name
                new_name = self.env['ir.sequence'].with_context(sale_order=True).next_by_code(sequence_code, sequence_date=seq_date) or _("New")
                order.name = new_name

        return super(PurchaseOrder, self).write(vals)

class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    sequence = fields.Integer(string='Sequence', default=1)