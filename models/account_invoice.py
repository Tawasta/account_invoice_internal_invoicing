# -*- coding: utf-8 -*-
from openerp import models, api, fields


class AccountInvoice(models.Model):

    _inherit = 'account.invoice'

    internal_invoice = \
        fields.Boolean(
            'Internal invoice',
            default=False,
            help="Invoice within the company group. These invoices will be handled differently in the accounting.",
            readonly=True,
            states={'draft': [('readonly', False)]},
        )
    internal_invoice_shown = \
        fields.Boolean(
            'Internal invoice shown',
            default=False,
            readonly=True,
            states={'draft': [('readonly', False)]},
        )

    ''' Don't change the "type" even when it's a reserved name
        Some old objects call it as a keyword.
    '''
    @api.multi
    def onchange_partner_id(
        self, type, partner_id, date_invoice=False,
        payment_term=False, partner_bank_id=False, company_id=False
    ):

        partners = self.get_internal_partners()

        if partner_id in partners:
            internal_invoice_shown = True
            internal_invoice = True
        else:
            internal_invoice_shown = False
            internal_invoice = False

        res = super(AccountInvoice, self).\
            onchange_partner_id(
                type, partner_id, date_invoice,
                payment_term, partner_bank_id, company_id
            )

        # Supporting the old API
        res['value']['internal_invoice_shown'] = internal_invoice_shown
        res['value']['internal_invoice'] = internal_invoice

        return res

    @api.onchange('internal_invoice')
    @api.depends('invoice_line')
    def onchange_internal_invoice(self):

        # Changes product line accounts
        if self.internal_invoice:
            for invoice_line in self.invoice_line:
                invoice_line.account_id = \
                    invoice_line._get_internal_account(
                        self.type, invoice_line.product_id
                    )
        else:
            for invoice_line in self.invoice_line:
                invoice_line.account_id = \
                    invoice_line._get_external_account(
                        self.type, invoice_line.product_id
                    )

    def get_internal_partners(self):
        # Gets internal partner ids
        companies = self.env['res.company'].search([])

        partners = []
        for company in companies:
            partners.append(company.partner_id.id)

        return partners
