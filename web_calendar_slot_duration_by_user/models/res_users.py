# Copyright 2024 Nomadi Plus Tecnologia LTDA - Italo LOPES
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class ResUsers(models.Model):
    _inherit = "res.users"

    use_custom_calendar = fields.Boolean(
        help="If checked, the user will use the custom calendar",
    )
    slot_duration = fields.Char(
        help="The slot duration for the user",
    )
