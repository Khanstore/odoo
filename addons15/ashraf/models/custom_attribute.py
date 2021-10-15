# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
# from odoo.osv import expression
# from odoo.exceptions import ValidationError

class ProductTemplate(models.Model):
    _inherit = "product.template"
    custom_attribute_line_ids = fields.One2many('custom.product.template.attribute.line', 'product_tmpl_id', 'Product Attributes', copy=True)

class customProductAttribute(models.Model):
    _name = "custom.product.attribute"
    _description = "Product Attribute"
    # if you change this _order, keep it in sync with the method
    # `_sort_key_attribute_value` in `product.template`
    _order = 'sequence, id'

    name = fields.Char('Attribute', required=True, translate=True)
    value_ids = fields.One2many('custom.product.attribute.value', 'attribute_id', 'Values', copy=True)
    sequence = fields.Integer('Sequence', help="Determine the display order", index=True)


class CustomProductAttributeValue(models.Model):
    _name = "custom.product.attribute.value"
    # if you change this _order, keep it in sync with the method
    # `_sort_key_variant` in `product.template'
    _order = 'attribute_id, sequence, id'
    _description = 'Attribute Value'

    name = fields.Char(string='Value', required=True, translate=True)
    sequence = fields.Integer(string='Sequence', help="Determine the display order", index=True)
    attribute_id = fields.Many2one('custom.product.attribute', string="Attribute", ondelete='cascade', required=True, index=True,
        help="The attribute cannot be changed once the value is used on at least one product.")

    is_custom = fields.Boolean('Is custom value', help="Allow users to input custom values for this attribute value")
    html_color = fields.Char(
        string='Color',
        help="Here you can set a specific HTML color index (e.g. #ff0000) to display the color if the attribute type is 'Color'.")
    _sql_constraints = [
        ('value_company_uniq', 'unique (name, attribute_id)', "You cannot create two values with the same name for the same attribute.")
    ]

class customProductTemplateAttributeLine(models.Model):
    """Attributes available on product.template with their selected values in a m2m.
    Used as a configuration model to generate the appropriate product.template.attribute.value"""

    _name = "custom.product.template.attribute.line"
    _rec_name = 'attribute_id'
    _description = 'Product Template custom Attribute Line'
    _order = 'attribute_id, id'

    active = fields.Boolean(default=True)
    product_tmpl_id = fields.Many2one('product.template', string="Product Template", ondelete='cascade', required=True, index=True)
    attribute_id = fields.Many2one('custom.product.attribute', string="Attribute", ondelete='restrict', required=True, index=True)
    value_ids = fields.Many2many('custom.product.attribute.value', string="Values", domain="[('attribute_id', '=', attribute_id)]",
        relation='custom_prd_attribute_value_prd_template_attribute_line_rel', ondelete='restrict')
#     product_template_value_ids = fields.One2many('custom.product.template.attribute.value', 'attribute_line_id', string="Product Attribute Values")








class resPartner(models.Model):
    _inherit = "res.partner"
    custom_attribute_line_ids = fields.One2many('custom.partner.attribute.line', 'partner_id', 'Custom Attributes', copy=True)

class customPartnerAttribute(models.Model):
    _name = "custom.partner.attribute"
    _description = "Partner Attribute"
    # if you change this _order, keep it in sync with the method
    # `_sort_key_attribute_value` in `product.template`
    _order = 'sequence, id'

    name = fields.Char('Attribute', required=True, translate=True)
    value_ids = fields.One2many('custom.partner.attribute.value', 'attribute_id', 'Values', copy=True)
    sequence = fields.Integer('Sequence', help="Determine the display order", index=True)


class CustomPartnerAttributeValue(models.Model):
    _name = "custom.partner.attribute.value"
    # if you change this _order, keep it in sync with the method
    # `_sort_key_variant` in `product.template'
    _order = 'attribute_id, sequence, id'
    _description = 'Attribute Value'

    name = fields.Char(string='Value', required=True, translate=True)
    sequence = fields.Integer(string='Sequence', help="Determine the display order", index=True)
    attribute_id = fields.Many2one('custom.partner.attribute', string="Attribute", ondelete='cascade', required=True, index=True,
        help="The attribute cannot be changed once the value is used on at least one partner.")

    is_custom = fields.Boolean('Is custom value', help="Allow users to input custom values for this attribute value")
    html_color = fields.Char(
        string='Color',
        help="Here you can set a specific HTML color index (e.g. #ff0000) to display the color if the attribute type is 'Color'.")
    _sql_constraints = [
        ('value_company_uniq', 'unique (name, attribute_id)', "You cannot create two values with the same name for the same attribute.")
    ]

class customPartnerAttributeLine(models.Model):
    """Attributes available on product.template with their selected values in a m2m.
    Used as a configuration model to generate the appropriate product.template.attribute.value"""

    _name = "custom.partner.attribute.line"
    _rec_name = 'attribute_id'
    _description = 'Partner Custom Attribute Line'
    _order = 'attribute_id, id'

    active = fields.Boolean(default=True)
    partner_id = fields.Many2one('res.partner', string="Contact", ondelete='cascade', required=True, index=True)
    attribute_id = fields.Many2one('custom.partner.attribute', string="Attribute", ondelete='restrict', required=True, index=True)
    value_ids = fields.Many2many('custom.partner.attribute.value', string="Values", domain="[('attribute_id', '=', attribute_id)]",
        relation='custom_partner_attribute_value_partner_attribute_line_rel', ondelete='restrict')
#     product_template_value_ids = fields.One2many('custom.product.template.attribute.value', 'attribute_line_id', string="Product Attribute Values")
