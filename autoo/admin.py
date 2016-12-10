from django.contrib import admin
from autoo.models import *

# class MessageAdmin(admin.ModelAdmin):
#     class Media:
#         js=(
#             '/static/js/kindeditor-4.1.7/kindeditor-min.js',
#             '/static/js/kindeditor-4.1.7/lang/zh_CN.js',
#             '/static/js/kindeditor-4.1.7/config.js',
#         )
#

# Register your models here.
admin.site.register(User)


# admin.site.register(GroupManager)
admin.site.register(Power)
admin.site.register(Role)
# admin.site.register(Notification)
# admin.site.register(Message)
# admin.site.register(UserSendMessage)
# admin.site.register(LocationServer)
# admin.site.register(Project)
# admin.site.register(Server)