from django import forms
from django.contrib.auth.forms import (AuthenticationForm, UserCreationForm, UsernameField)
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginForm(AuthenticationForm):
    """ログインフォーム"""
    username = UsernameField(widget=forms.NumberInput(attrs={'autofocus': True}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label


class UserCreateForm(UserCreationForm):
    """ユーザー登録用フォーム"""

    class Meta:
        model = User
        fields = ('employee_cd', 'last_name', 'first_name', 'email', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class SearchForm(forms.Form):
    employee_cd = forms.IntegerField(
        initial='',
        label='社員番号',
        required = True,
    )