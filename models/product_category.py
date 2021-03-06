# -*- coding: utf-8 -*-
from openerp import models, fields


class ProductCategory(models.Model):

    _inherit = 'product.category'

    property_account_income_internal_categ = fields.Many2one(
        "account.account",
        "Internal Income Account",
        company_dependent=True,
        domain=[("type", '=', "other")],
    )

    property_account_expense_internal_categ = fields.Many2one(
        "account.account",
        "Internal Expense Account",
        company_dependent=True,
        domain=[("type", '=', "other")],
    )
