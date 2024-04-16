from django.conf import settings
from edc_base.utils import get_uuid
from django.apps import apps as django_apps
from edc_model_wrapper import ModelWrapper
from django.core.exceptions import ObjectDoesNotExist
from edc_consent.model_wrappers import ConsentModelWrapperMixin
from trainee_dashboard.model_wrappers.subject_consent_model_wrapper import SubjectConsentModelWrapper
from trainee_dashboard.model_wrappers.subject_locator_model_wrapper_mixin import SubjectLocatorModelWrapperMixin


class SubjectScreeningModelWrapper(SubjectLocatorModelWrapperMixin,
                                   ConsentModelWrapperMixin,ModelWrapper):
    
    consent_model_wrapper_cls = SubjectConsentModelWrapper
    model ='traineesubject.subjectscreening'
    next_url_name = settings.DASHBOARD_URL_NAMES.get('screening_listboard_url')
    querystring_attrs = ['screening_identifier']
    next_url_attrs = ['screening_identifier']

    @property
    def consent_version(self):
        return '1'

    @property
    def subject_identifier(self):
        if self.consent_model_obj:
            return self.consent_model_obj.subject_identifier
        return None

    @property
    def consent_model_obj(self):
        """Returns a consent model instance or None.
        """
        try:
            return self.subject_consent_cls.objects.get(**self.consent_options)
        except ObjectDoesNotExist:
            return None

    @property
    def subject_consent_cls(self):
        return django_apps.get_model('traineesubject.subjectconsent')

    @property
    def create_consent_options(self):
        """Returns a dictionary of options to create a new
        unpersisted consent model instance.
        """
        options = dict(
            screening_identifier=self.screening_identifier,
            consent_identifier=get_uuid(),
            version=self.consent_version,
            #first_name=self.first_name,
            #last_name=self.last_name
            )
        return options

    @property
    def consent_options(self):
        """Returns a dictionary of options to get an existing
        consent model instance.
        """
        options = dict(
            screening_identifier=self.object.screening_identifier,
            version=self.consent_version)
        return options

    def eligible_at_enrol(self):
        return self.object.is_eligible
    
    @property
    def subject_screening(self):
        """Returns a wrapped saved or unsaved subject screening.
        """
        model_obj = self.subject_screening_model_obj or self.subject_screening_cls(
            **self.subject_screening_options)
        return self(model_obj=model_obj)
    
    @property
    def subject_screening_model_obj(self):
        """Returns a subject screening model instance or None.
        """
        try:
            return self.subject_screening_cls.objects.get(
                **self.subject_screening_options)
        except ObjectDoesNotExist:
            return None
        
    @property
    def subject_screening_options(self):
        """Returns a dictionary of options to get an existing
        verbal consent model instance.
        """
        options = dict(
            screening_identifier=self.object.screening_identifier)
        return options
    
    @property
    def subject_screening_cls(self):
        return django_apps.get_model('traineesubject.subjectscreening')


