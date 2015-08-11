# -*- coding: utf-8 -*-
from openerp import models, api, fields


class AccountInvoiceLine(models.Model):

    _inherit = 'account.invoice.line'

    @api.multi
    def product_id_change(self, product, uom_id, qty=0, name='',
                          type='out_invoice', partner_id=False,
                          fposition_id=False, price_unit=False,
                          currency_id=False, company_id=None):

        res = super(AccountInvoiceLine, self).product_id_change(
            product, uom_id, qty, name, type, partner_id,
            fposition_id, price_unit, currency_id, company_id
            )

        # If invoice is marked as internal
        if self.invoice_id.internal_invoice or \
                ("internal_invoice" in self._context and
                 self._context["internal_invoice"]):

            product = self.env['product.product'].browse(product)

            if type in ('out_invoice', 'out_refund'):
                account = product.property_account_income_internal
                # or product.categ_id.property_account_income_categ
            else:
                account = product.property_account_expense_internal
                # or product.categ_id.property_account_expense_categ

            fpos = self.env['account.fiscal.position'].browse(fposition_id)
            account = fpos.map_account(account)

            if account:
                res['value']['account_id'] = account.id

        return res