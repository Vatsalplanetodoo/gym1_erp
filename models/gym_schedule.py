import re
from odoo import api, fields, models
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError
class Member(models.Model):
    _inherit = 'res.partner'
    joining_date = fields.Date('Joining date')
    workout_ids = fields.One2many(comodel_name='workout.plan', inverse_name='exercise_plan_id')
    total_price = fields.Integer('TotalPrice', compute='_total', readonly=True)
    born = fields.Date('Date of birth')
    # age = fields.Integer('Age',compute='_calculate_age',store=1)
    age1 = fields.Char('Age')

    @api.depends('workout_ids')
    def _total(self):
        total = 0
        for record in self.workout_ids:
            print(self.workout_ids)
            total += record.price
        self.total_price = total

    # @api.onchange('born')
    # def _calculate_age(self):
    #     today = date.today()
    #     self.age1= today.year - self.born.year - ((today.month, today.day) < (self.born.month, self.born.day))
    #     return 0

    @api.onchange('email')
    def validate_mail(self):
        if self.email:
            match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+([a-z0-9-]+)*(\.[a-z]{2,4})$', self.email)
            if match == None:
                raise ValidationError('Not a valid E-mail ID')

class WorkoutPlan(models.Model):
    _name = 'workout.plan'
    name = fields.Char('Name of member')
    exercise_plan_id = fields.Many2one('res.partner')
    in_time = fields.Datetime('In time')
    out_time = fields.Datetime('Out time')
    massage = fields.Boolean('Free Massage')
    supplement = fields.Boolean('Supplement')
    # total_price = fields.Integer('TotalPrice',compute='_total',readonly = True)
    price = fields.Integer('Price',compute='_gymcondi',readonly = True)
    exercise_plan_id1 = fields.Many2one('new.form','Exercise name')
    # exercise_ids = fields.One2many(comodel_name='new.form', inverse_name='exercise_name',string='Exercise plan')

    @api.depends('massage','supplement')
    def _gymcondi(self):
        mprice = 500
        sprice = 100
        if self.massage == True and self.supplement == True:
            self.price = mprice + sprice
        elif self.massage:
            self.price = mprice
        elif self.supplement:
            self.price = sprice
        else:
            self.price = 0


class newform(models.Model):
    _name = 'new.form'
    _rec_name = 'exercise_name'
    # exercise1_id = fields.Many2one('workout.plan')
    exercise_name = fields.Char('Exercise Name')
    sets = fields.Integer('No of Sets')
    reps = fields.Integer('No of Reps')

