###############################
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from ...forms import EmployeeInfoRegistForm
from ...models import employee
from django.contrib import messages
from django.urls import reverse_lazy

class EmployeeInfoRegistView(generic.CreateView, LoginRequiredMixin):

    model = employee
    template_name = 'master/EMD0101.html'
    form_class = EmployeeInfoRegistForm
    success_url = reverse_lazy('app_usweb:employee_info_regist')
    #Fields = ['employeeCd', 'employeeName', 'employeeNameKana', 'hireDateYm', 'hobby', 'qualification1', 'qualification2', 'qualification3']

    def form_valid(self, form):
        ''' バリデーションを通った時 '''
        messages.info(self.request, f'登録が完了しました')
        return super().form_valid(form)
