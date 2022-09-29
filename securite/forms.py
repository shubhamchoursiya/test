from django import forms
from .models import Employee,EmployeeFace

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('emp_id','emp_name','designation','email','phone','department','gender')

class EmployeefaceForm(forms.ModelForm):
	class Meta:
		model= EmployeeFace
		fields = ('image',)
