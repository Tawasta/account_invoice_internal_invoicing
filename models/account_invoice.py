# -*- coding: utf-8 -*-
from openerp import models, api, fields


class AccountInvoice(models.Model):

    _inherit = 'account.invoice'

    internal_invoice = fields.Boolean('Internal invoice')

    @api.onchange('partner_id')
    def onchange_partner(self):
        pass
