from odoo import fields, models, api, _
from odoo.exceptions import UserError


class SlideSlide(models.Model):
    _inherit = "slide.slide"

    fen = fields.Char('fen')

