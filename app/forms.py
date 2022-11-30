from flask_wtf import FlaskForm
import wtforms as ws
from app import app
from . import models
from datetime import date


class UserForm(FlaskForm):
    username = ws.StringField('Имя пользователя', validators=[ws.validators.DataRequired(),ws.validators.length(min=4,max=20) ])
    password = ws.PasswordField('Пароль', validators=[ws.validators.DataRequired(),ws.validators.length(min=8,max=24) ])


class TransactionsForm(FlaskForm):
    period = ws.StringField('Период транзакции',validators=[ws.validators.DataRequired(),])
    value = ws.IntegerField('Сумма',validators=[ws.validators.DataRequired(),])
    status = ws.StringField('Статус',validators=[ws.validators.DataRequired(),])
    unit = ws.StringField('Валюта',validators=[ws.validators.DataRequired(),])
    subject = ws.StringField('Комментариев проводки',validators=[ws.validators.DataRequired(),])

