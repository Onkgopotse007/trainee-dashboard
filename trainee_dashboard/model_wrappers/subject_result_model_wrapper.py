from django.apps import apps as django_apps
from edc_senaite_interface.model_wrappers import ResultModelWrapper


class SubjectResultModelWrapper(ResultModelWrapper):

    model = 'traineesubject.subjectrequisitionresult'

    @property
    def result_model_wrapper_cls(self):
        return self

    @property
    def result_model_cls(self):
        return django_apps.get_model('traineesubject.subjectrequisitionresult')

    @property
    def dashboard_url(self):
        return 'trainee_dashboard:subject_dashboard_url'

    @property
    def results_objs(self):
        if self.object:
            return self.object.subjectresultvalue_set.all()