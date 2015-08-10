# -*- coding: utf-8 -*-
from openerp import models, api, fields


class AccountInvoice(models.Model):

    _inherit = 'account.invoice'

    internal_invoice = fields.Boolean('Internal invoice')
    internal_invoice_shown = fields.Boolean('Internal invoice shown',
                                            default=False)

    ''' We are using the old api as it has loads of onchange-functions
    that would need to be rewritten'''
    @api.v7
    def onchange_partner_id(self, cr, uid, ids, partner_type, partner_id,
                            date_invoice=False, payment_term=False,
                            partner_bank_id=False, company_id=False):

        # Update the internal invoice field
        self.onchange_partner()

        return super(AccountInvoice, self).\
            onchange_partner_id(cr, uid, ids, type, partner_id, date_invoice,
                                payment_term, partner_bank_id, company_id)

    @api.one
    def onchange_partner(self):
        pass