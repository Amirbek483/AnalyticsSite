from django import forms
from .models import *


# create form to upload file
class AnalyticsForm(forms.ModelForm):
		class Meta:
				model = Analytics
				fields = ('file',)

