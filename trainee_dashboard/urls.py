"""trainee_dashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.urls.conf import path,include
from .patterns import screening_identifier,subject_identifier,sample_result_identifier
from trainee_dashboard.views import SubjectListboardView,SubjectScreeningListboardView,SubjectDashboardView,SubjectResultListboardView



from edc_dashboard import UrlConfig

app_name ='trainee_dashboard'

screening_listboard_url_config = UrlConfig(
    url_name='screening_listboard_url',
    view_class=SubjectScreeningListboardView,
    label='screening_listboard',
    identifier_label='screening_identifier',
    identifier_pattern=screening_identifier)

subject_listboard_url_config = UrlConfig(
    url_name='subject_listboard_url',
    view_class=SubjectListboardView,
    label='subject_listboard',
    identifier_label='subject_identifier',
    identifier_pattern=subject_identifier)



subject_dashboard_url_config = UrlConfig(
    url_name='subject_dashboard_url',
    view_class=SubjectDashboardView,
    label='subject_dashboard',
    identifier_label='subject_identifier',
    identifier_pattern=subject_identifier)

subject_listboard_result_url_config = UrlConfig(
    url_name='subject_result_listboard_url',
    view_class=SubjectResultListboardView,
    label='subject_result_listboard',
    identifier_label='sample_id',
    identifier_pattern=sample_result_identifier)

urlpatterns = []
urlpatterns += subject_listboard_url_config.listboard_urls
urlpatterns += screening_listboard_url_config.listboard_urls
urlpatterns += subject_dashboard_url_config.dashboard_urls
urlpatterns += subject_listboard_result_url_config.listboard_urls


if settings.APP_NAME == 'trainee_dashboard':

    from django.views.generic.base import RedirectView

    urlpatterns += [
        path('accounts/', include('edc_base.auth.urls')),
        path('edc_data_manager/', include('edc_data_manager.urls')),
        path('edc_device/', include('edc_device.urls')),
        path('edc_protocol/', include('edc_protocol.urls')),
        path('administration/', RedirectView.as_view(url='admin/'),
             name='administration_url'),
        path(r'', RedirectView.as_view(url='admin/'), name='home_url'),


        ]

