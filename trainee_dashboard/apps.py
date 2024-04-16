from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    name = 'trainee_dashboard'
    admin_site_name = 'traineesubject_admin'
