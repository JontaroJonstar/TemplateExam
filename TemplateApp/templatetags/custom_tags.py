from django import template
from datetime import datetime
import math

register = template.Library()

@register.filter(name='calculate_datetime_to_now')
def calculate_datetime_to_now(vaule):
    join_datetime = datetime.strptime(vaule, '%Y/%m/%d')
    now_datetime = datetime.now()
    diff_datetime  = now_datetime  - join_datetime
    diff_days = diff_datetime.days
    diff_years = math.floor(diff_days / 365)
    diff_month = math.floor((diff_days - 365 * diff_years) / 30)
    return f'{diff_years}年 {diff_month}カ月 {diff_days}日'
    