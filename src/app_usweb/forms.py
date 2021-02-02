from django import forms
from django.core.validators import MinLengthValidator
from django.contrib.auth.forms import (AuthenticationForm, UserCreationForm, UsernameField)
from django.contrib.auth import get_user_model
from .models.employee import employee
from .models.code import code
from django.forms.models import ModelChoiceField

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
        fields = ('employee_cd', 'last_name', 'first_name', 'email',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class SearchForm(forms.Form):
    employee_cd = forms.IntegerField(
        initial='',
        label='社員番号',
        required=True,
    )


class myModelChoiceField(ModelChoiceField):

    def to_python(self, value):
        # オブジェクトに変換しないでそのまま返す.
        return value


class EmployeeInfoRegistForm(forms.ModelForm):

    class Meta:
        model = employee
        fields = ['employee_cd', 'employee_name', 'employee_name_kana', 'hire_data_ym', 'hobby', 'qualification1', 'qualification2', 'qualification3']

#    employee_cd = forms.CharField(label='社員番号', max_length=6, required=False)
#    employee_name = forms.CharField(label='氏名', max_length=15, required=False)
#    employee_name_kana = forms.CharField(label='カナ氏名', max_length=30, required=False)
#    hire_data_ym = forms.CharField(label='入社年月', max_digits=6, decimal_places=0, required=False)
#    hobby = forms.CharField(label='趣味', max_length=10, required=False)
    qualification1 = myModelChoiceField(queryset=code.objects, label='保有資格1', empty_label='', to_field_name='code', required=False)
    qualification2 = myModelChoiceField(queryset=code.objects, label='保有資格2', empty_label='', to_field_name='code', required=False)
    qualification3 = myModelChoiceField(queryset=code.objects, label='保有資格3', empty_label='', to_field_name='code', required=False)
