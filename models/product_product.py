# -*- coding: utf-8 -*-
from openerp import models, api, fields


class ProductProduct(models.Model):

    _inherit = 'product.product'

    property_account_income_internal = fields.Many2one(
        "account.account",
        "Internal Income Account",
        company_dependent=True,
    )

    property_account_expense_internal = fields.Many2one(
        "account.account",
        "Internal Expense Account",
        company_dependent=True,
    )
