from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class TaskCreationForm(forms.Form):
    title = forms.CharField(label='título', max_length=255)
    content = forms.CharField(label='contenido', widget=forms.Textarea())
    
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email', 'age')
        
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = (
            'username',
            'email',
            'age',
        )
