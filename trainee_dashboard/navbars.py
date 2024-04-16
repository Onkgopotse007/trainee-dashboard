from django.conf import settings
from edc_navbar import NavbarItem, site_navbars, Navbar


no_url_namespace = True if settings.APP_NAME == 'trainee_dashboard' else False

trainee_dashboard = Navbar(name='trainee_dashboard')

trainee_dashboard.append_item(
    NavbarItem(
        name='eligible_subject',
        title='Subject Screening',
        label='subject screening',
        fa_icon='fa fa-user-plus',
        url_name=settings.DASHBOARD_URL_NAMES[
            'screening_listboard_url'],
        no_url_namespace=no_url_namespace))

trainee_dashboard.append_item(
    NavbarItem(
        name='consented_subject',
        title='Trainee Subjects',
        label='trainee subjects',
        fa_icon='far fa-user-circle',
        url_name=settings.DASHBOARD_URL_NAMES['subject_listboard_url'],
        no_url_namespace=no_url_namespace))

site_navbars.register(trainee_dashboard)