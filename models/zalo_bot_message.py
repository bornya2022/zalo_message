
from odoo import models, fields, api


class ZaloBotMessage(models.Model):
    _name = 'zalo.bot.message'

    follower_id = fields.Char('Zalo ID')
    name = fields.Char('Name')
    phone_number = fields.Char('Phone Number')
    question = fields.Char('Question')

