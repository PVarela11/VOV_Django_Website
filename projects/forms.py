from django.forms import ModelForm
from .models import Project

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.urls import reverse

class EditProjectForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        #self.helper.form_action = 'submit_survey'

        self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
        #self.form.helper.form_action = reverse('')

    class Meta:
        model = Project
        fields = '__all__'