from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    # first_name = forms.CharField(max_length=20, required=True, help_text='Enter your first name')
    # last_name = forms.CharField(max_length=30, required=True, help_text='Enter your last name')
    # email = forms.EmailField(max_length=254, required=True, help_text='Enter your e-mail address')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')


class RecoveryForm(UserForm):
    class Meta(UserForm.Meta):
        exclude = ('first_name', 'last_name', 'password')


class UserProfileForm(UserForm):
    class Meta(UserForm.Meta):
        exclude = ['password']


class UserChangePassForm(forms.ModelForm):
    old_pass = forms.PasswordInput()
    new_pass = forms.PasswordInput()
    repeat_pass = forms.PasswordInput()
    class Meta:
        fields = ('old_pass', 'new_pass', 'repeat_pass')
