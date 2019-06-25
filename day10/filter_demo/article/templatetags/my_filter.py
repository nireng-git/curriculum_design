from django import template
from datetime import datetime
register = template.Library()


@register.filter #将过滤器注册到系统中
def time_since(value):
    # 小于1分钟显示刚刚
    #小于一个小时  X分钟以前
    #小于24 小时  X小时以前
    #小于30天  X天前
    #其它时间显示 年月日
    if not isinstance(value,datetime):
        return value
    now = datetime.now()
    timestamp = (now-value).total_seconds()
    if timestamp < 60:
        return '刚刚'
    elif timestamp > 60 and timestamp < 60*60:
        minutes = int(timestamp/60)
        return "%s 分钟以前" % minutes
    elif timestamp > 60*60 and timestamp < 60*60*24:
        hours = int(timestamp/60/60)
        return "%s 小时以前" % hours
    elif timestamp > 60*60*24 and timestamp < 60*60*24*30:
        day = int(timestamp/60/60/24)
        return "%s 天以前" % day
    else:
        return value.strftime("%Y/%m/%d %H:%M")
