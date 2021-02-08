###############################
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from ...forms import EmployeeInfoRegistForm
from ...models import employee
from django.contrib import messages
from django.urls import reverse
from django import forms

class EmployeeInfoUpdateView(generic.UpdateView, LoginRequiredMixin):

    model = employee
    template_name = 'master/EMD0101.html'
    form_class = EmployeeInfoRegistForm

    def get_success_url(self):
        return reverse('app_usweb:employee_info_update', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        ''' バリデーションを通った時 '''
        messages.info(self.request, f'更新が完了しました')
        return super().form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields['employee_cd'].widget.attrs['disabled'] = 'disabled'

        return form