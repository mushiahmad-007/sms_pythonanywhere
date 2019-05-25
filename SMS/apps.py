from django.apps import AppConfig

from django.contrib.admin.apps import AdminConfig

class SmsConfig(AppConfig):
    name = 'SMS'

class MyAdminConfig(AdminConfig):
    default_site = 'SMS.apps.MyAdminSite'