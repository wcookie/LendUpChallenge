
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML, Button,  Field
from crispy_forms.bootstrap import FormActions

class InputForm(forms.Form):
	number=forms.CharField()
	delay =forms.CharField(
		help_text="(Delay is in Seconds)",
		required=False
		)
	helper=FormHelper()
	helper.layout=Layout(
		Field('number', css='input-xlarge'),
		Field('delay', css='input-xlarge'),
		FormActions(Submit('save_changes', 'Make Phone Call', css_class="btn-primary"),)
	)
