from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Reports, Recommendation

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class ReportForm(forms.ModelForm):
    
    class Meta:
        model = Reports
        exclude = ['created_at']
        fields = ('institution_name', 'dept', 'location', 'institution_category', 'outstanding', 'desc')


class RecommendationsForm(forms.ModelForm):
    
    class Meta:
        model = Recommendation
        exclude = ['created_at']
        fields = ('institution_name', 'dept', 'location', 'institution_category', 'outstanding', 'desc')