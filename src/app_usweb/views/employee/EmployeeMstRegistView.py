###############################
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView
from ...forms import EmployeeInfoRegistForm
from ...models import employee


# 社員マスタ登録ビュークラス
class EmployeeMstRegistView(CreateView, LoginRequiredMixin):

    model = employee
    template_name = 'master/EMD0101.html'
    form_class = EmployeeInfoRegistForm
    success_url = reverse_lazy('app_usweb:employee_mst_regist')

    def form_valid(self, form):
        ''' バリデーションを通った時 '''
        messages.info(self.request, f'登録が完了しました')
        return super().form_valid(form)
