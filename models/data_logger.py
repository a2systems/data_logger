from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.tools.float_utils import float_compare, float_round
from datetime import datetime
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError, ValidationError

class DataLogger(models.Model):
    _name = 'data.logger'
    _description = 'data.logger'

    event = fields.Char('Event',index=True)
    table_name = fields.Char('Table')
    model_id = fields.Many2one('ir.model','Model')
    res_id = fields.Integer('Res ID')
    old_content = fields.Text('Old Content')
    new_content = fields.Text('New Content')
    tx_id = fields.Integer('Integer',index=True)

