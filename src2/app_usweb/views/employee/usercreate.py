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
from ...forms import (LoginForm, UserCreateForm)
from ...forms import SearchForm
from django.db.models import Q
###############################

class UserCreate(generic.CreateView):
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