"""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django_filters.views import FilterView
from django.shortcuts import render
"""
###############################
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (LoginView, LogoutView)
from django.contrib.sites.shortcuts import get_current_site
from django.core.signing import BadSignature, SignatureExpired, loads, dumps
from django.http import Http404, HttpResponseBadRequest
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.views import generic
from .forms import (LoginForm, UserCreateForm)
from .forms import SearchForm
from django.db.models import Q
###############################

User = get_user_model()

class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'app_usweb/login.html'

class Logout(LogoutView):
    """ログアウトページ"""
    template_name = 'app_usweb/top.html'

# menu.html表示
class Menu(LoginRequiredMixin, generic.TemplateView):
    template_name = 'app_usweb/menu.html'

class UserCreate(LoginRequiredMixin, generic.CreateView):
    """ユーザー登録"""
    template_name = 'app_usweb/user_create.html'
    form_class = UserCreateForm

    # データPOST時に実行される
    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = True
        user.save()
        return redirect('app_usweb:user_create_complete')

class UserCreateDone(LoginRequiredMixin, generic.TemplateView):

    template_name = 'app_usweb/user_create_done.html'


class UserCreateComplete(LoginRequiredMixin, generic.TemplateView):

    template_name = 'app_usweb/user_create_complete.html'

class Reference(LoginRequiredMixin, generic.ListView):
    paginate_by = 5
    template_name =  'app_usweb/reference.html'
    model = User
    def post(self, request, *args, **kwargs):
        form_value = [
            self.request.POST.get('employee_cd', None),
        ]
        request.session['form_value'] = form_value
        # 検索時にページネーションに関連したエラーを防ぐ
        self.request.GET = self.request.GET.copy()
        self.request.GET.clear()
        return self.get(request, *args, **kwargs)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # sessionに値がある場合、その値をセットする。（ページングしてもform値が変わらないように）
        employee_cd = ''
        if 'form_value' in self.request.session:
            form_value = self.request.session['form_value']
            employee_cd = form_value[0]
        default_data = {'employee_cd': employee_cd,  # タイトル
                        }
        test_form = SearchForm(initial=default_data) # 検索フォーム
        context['test_form'] = test_form
        return context
    def get_queryset(self):
        # sessionに値がある場合、その値でクエリ発行する。
        if 'form_value' in self.request.session:
            form_value = self.request.session['form_value']
            employee_cd = form_value[0]
            # 検索条件
            condition_employee_cd = Q()
            if len(employee_cd) != 0 and employee_cd[0]:
                condition_employee_cd = Q(employee_cd__icontains=employee_cd)
            return User.objects.select_related().filter(condition_employee_cd)
        else:
            # 何も返さない
            return User.objects.none()