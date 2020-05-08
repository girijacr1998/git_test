from django import forms
from form1.models import Users

class NewUserForm(forms.ModelForm):
   class Meta():
    model=Users
    fields='__all__'