# _*_ coding: utf-8 _*_
__data__ = '2017/2/22 15:14'

import  xadmin
from .models import EmailVerifyRecord

class EmailVerifyRecordAdmin(object):
    #list_diaplat  显示字段
    list_display = ['code', 'email', 'send_type', 'send_time']
    #search_fields 显示搜索框 搜索字段
    search_fields = ['code', 'email', 'send_type']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)





















