from odoo import api, fields, models
from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning
import re

class CustomerWizard(models.TransientModel):
    _name = "customer.wizard"
    _description = "Customer Wizard"

    update_phone = fields.Integer('Update Phone')
    update_phone1 = fields.Char('Update Phone')

    def phone_update(self):
        active_id = self.env.context.get('active_id')
        customer_info_rec = self.env['res.partner']
        customer_change_id = customer_info_rec.search([('id', '=', active_id)])
        print("active_id>>>>", active_id)
        print('customer_info>>', customer_info_rec)
        print('customer_change_id>>>', customer_change_id)
        # customer_change_id.phone = self.update_phone1

        Pattern = re.compile("^(0|91)?[6-9][0-9]{9}")
        if Pattern.match(str(self.update_phone1)) and (len(self.update_phone1) <= 12):
            customer_change_id.phone = self.update_phone1
        else:
            raise UserError("Invalid phone number")
        return 1

