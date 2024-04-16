from edc_navbar import NavbarViewMixin
from edc_base.view_mixins import EdcBaseViewMixin
from edc_dashboard.view_mixins import ListboardFilterViewMixin, SearchFormViewMixin
from edc_dashboard.views import ListboardView as BaseListBoardView
from ....model_wrappers import SubjectConsentModelWrapper
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



class ListboardView(EdcBaseViewMixin, NavbarViewMixin,
                    ListboardFilterViewMixin, SearchFormViewMixin,
                    BaseListBoardView):

    listboard_template = 'subject_listboard_template'
    listboard_url = 'subject_listboard_url'
    listboard_panel_style = 'success'
    listboard_fa_icon = "far fa-user-circle"


    model = 'traineesubject.subjectconsent'
    model_wrapper_cls = SubjectConsentModelWrapper
    app_config_name = 'trainee_dashboard'
    navbar_name = 'trainee_dashboard'
    navbar_selected_item = 'consented_subject'
    search_form_url = 'subject_listboard_url'
   

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    


