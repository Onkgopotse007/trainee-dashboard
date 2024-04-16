from edc_visit_schedule.model_wrappers import RequisitionModelWrapper


class SubjectRequisitionModelWrapper(RequisitionModelWrapper):

    visit_model_attr = 'subject_visit'

    querystring_attrs = [visit_model_attr, 'panel']

    @property
    def subject_visit(self):
        return str(getattr(self.object, self.visit_model_attr).id)