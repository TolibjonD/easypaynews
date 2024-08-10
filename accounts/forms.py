from django.contrib.auth.models import User
from django import forms

class RegisterForm(forms.ModelForm):
    password = forms.CharField(label="Parolni kiriting", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Parolni takrorlang", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'password', 'password2')

    def clean_password2(self):
        data = self.cleaned_data
        if data['password'] != data['password2']:
            raise forms.ValidationError("Siz kiritgan parollar o'xshash emas.")
        return data['password2']