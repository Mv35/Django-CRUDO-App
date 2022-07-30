from django import forms
from . models import ContactFormModel
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit


class ContactForm(forms.ModelForm):

    class Meta:
        model = ContactFormModel
        fields = ('name', 'email', 'category', 'subject', 'body')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            'name',
            'email',
            'category',
            'subject',
            'body',
            Submit('submit','Submit', css_class='btn-success') 
        )