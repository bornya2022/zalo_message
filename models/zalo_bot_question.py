
from odoo import models, fields, api


class ZaloBotQuestion(models.Model):
    _name = 'zalo.bot.question'

    name = fields.Char('Name')
