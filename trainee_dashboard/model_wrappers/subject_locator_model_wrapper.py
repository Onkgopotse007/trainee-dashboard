from django.conf import settings

from edc_model_wrapper import ModelWrapper

class SubjectLocatorModelWrapper(ModelWrapper):
    model = 'traineesubject.subjectlocator'
    querystring_attrs = ['screening_identifier', 'subject_identifier', 'first_name', 'last_name']
    next_url_attrs = ['screening_identifier', 'subject_identifier']
    next_url_name = settings.DASHBOARD_URL_NAMES.get('screening_listboard_url')