from django import forms
from testapp.models import employee

class EmployeeFrom(forms.ModelForm):
    class Meta:
        model=employee
        fields='__all__'