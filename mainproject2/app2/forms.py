from django import forms
from app2.models import Employee,News,Calendar
from django.contrib.auth.models import User

class EmpForm(forms.ModelForm):
	class Meta:
		model = Employee
		fields = "__all__"

class NewsForm(forms.ModelForm):
	class Meta:
		model = News
		fields = "__all__"

class CalendarForm(forms.ModelForm):
	class Meta:
		model = Calendar
		fields ="__all__"

class SignupForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username','password','email','first_name','last_name']