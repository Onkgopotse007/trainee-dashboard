from edc_senaite_interface.views import ListboardView

from ....model_wrappers import SubjectResultModelWrapper
from ...view_mixin import ResultRefreshViewMixin


class ResultListboardView(ResultRefreshViewMixin, ListboardView):

    model = 'traineesubject.subjectrequisitionresult'
    model_wrapper_cls = SubjectResultModelWrapper

    def get(self, request, *args, **kwargs):
        refresh_table = self.request.GET.get('refresh', False)
        if refresh_table:
            self.refresh_context_data(app_label='traineesubject')
        return super().get(request, *args, **kwargs)