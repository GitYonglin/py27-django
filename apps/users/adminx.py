# _*_ coding: utf-8 _*_
__data__ = '2017/2/22 15:14'

import  xadmin #引用库
from xadmin import views #主题依赖

from .models import UserProfile,EmailVerifyRecord, Banner #引用models


#使用主题
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


#修改title与footer,左侧菜单风格
class GlobalSettings(object):
    site_title = u"慕学网"
    site_footer = u"慕学在线"
    menu_style = "accordion"

# 用户数据现在还不知道怎么显示
class UserProfileAdmin(object):
    # list_display  models显示字段
    list_display = ['username', 'email', 'phone', 'send_time']
    # search_fields 显示搜索框 搜索字段
    search_fields = ['username', 'email', 'phone', 'send_time']
    # list_filter 过滤器搜索
    list_filter = ['username', 'email', 'phone', 'send_time']


class EmailVerifyRecordAdmin(object): #class名字  model class name + Admin
    #list_display  models显示字段
    list_display = ['code', 'email', 'send_type', 'send_time']
    #search_fields 显示搜索框 搜索字段
    search_fields = ['code', 'email', 'send_type']
    #list_filter 过滤器搜索
    list_filter  = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    # list_display  models显示字段
    list_display = ['image', 'title', 'index', 'add_time']
    # search_fields 显示搜索框 搜索字段
    search_fields = ['title', 'index']
    # list_filter 过滤器搜索
    list_filter = ['title', 'index', 'add_time']


# 注册数据到xadmin
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)

xadmin.site.register(UserProfile,UserProfileAdmin)
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)





















