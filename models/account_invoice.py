# -*- coding: utf-8 -*-
from openerp import models, api, fields


class AccountInvoice(models.Model):

    _inherit = 'account.invoice'

    internal_invoice = \
        fields.Boolean(
            'Internal invoice',
            default=False,
            help="Invoice within the company group. These invoices will be handled differently in the accounting."
        )
    internal_invoice_shown = \
        fields.Boolean(
            'Internal invoice shown',
            default=False,
        )

    ''' We are using the old api as it has loads of onchange-functions
    that would need to be rewritten otherwise.

    TODO: This functionality WILL STOP WORKING when the account form 
    partner_id onchange will be upgraded '''
    @api.v7
    def onchange_partner_id(self, cr, uid, ids, partner_type, partner_id,
                            date_invoice=False, payment_term=False,
                            partner_bank_id=False, company_id=False):

        res = super(AccountInvoice, self).\
            onchange_partner_id(cr, uid, ids, type, partner_id, date_invoice,
                                payment_term, partner_bank_id, company_id)

        # Update internal invoice fields
        vals = self.onchange_partner(cr, uid, ids, partner_id)
        if vals:
            res['value'].update(
                vals[0]['value']
            )

        return res

    @api.one
    def onchange_partner(self, partner_id):
        partners = self.get_internal_partners()[0]

        if partner_id in partners:
            self.internal_invoice_shown = True
            self.internal_invoice = True

        else:
            self.internal_invoice_shown = False
            self.internal_invoice = False

        # Supporting the old API
        res = {'value': {}}
        res['value']['internal_invoice_shown'] = self.internal_invoice_shown
        res['value']['internal_invoice'] = self.internal_invoice

        return res

    @api.one
    def get_internal_partners(self):
        companies = self.env['res.company'].search([])

        partners = []
        for company in companies:
            partners.append(company.partner_id.id)

        return partners
