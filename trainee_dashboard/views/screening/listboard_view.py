from trainee_dashboard.model_wrappers.subject_screening_model_wrapper import SubjectScreeningModelWrapper
from edc_navbar import NavbarViewMixin
from edc_base.view_mixins import EdcBaseViewMixin
from edc_dashboard.view_mixins import ListboardFilterViewMixin, SearchFormViewMixin
from edc_dashboard.views import ListboardView
from trainee_dashboard.views.screening.filters import ListboardViewFilters
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class ListBoardView(NavbarViewMixin, EdcBaseViewMixin,
                    ListboardFilterViewMixin, SearchFormViewMixin, ListboardView):
    listboard_template = 'screening_listboard_template'
    listboard_url = 'screening_listboard_url'
    
    listboard_panel_style = 'info'
    listboard_fa_icon = "fa-user-plus"

    listboard_view_filters = ListboardViewFilters()
    model = 'traineesubject.subjectscreening'
    model_wrapper_cls = SubjectScreeningModelWrapper
    navbar_name = 'trainee_dashboard'
    navbar_selected_item = 'eligible_subject'
    search_form_url = 'screening_listboard_url'


    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            subject_screening_add_url=self.model_cls().get_absolute_url(),
        )
        return context
    
    def get_queryset_filter_options(self, request, *args, **kwargs):
        options = super().get_queryset_filter_options(request, *args, **kwargs)
        if kwargs.get('screening_identifier'):
            options.update(
                {'screening_identifier': kwargs.get('screening_identifier')}, )
        return options