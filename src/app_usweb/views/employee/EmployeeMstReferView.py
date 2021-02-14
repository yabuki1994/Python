###############################
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views.generic import ListView
from ...forms import EmployeeInfoRegistForm
from ...models import employee
import re


# 社員マスタ検索ビュークラス
class EmployeeMstReferView(ListView, LoginRequiredMixin):

    model = employee
    template_name = 'master/EMD0100.html'
    context_object_name = 'employee_list'
    global errFlg

    def get_context_data(self, **kwargs):
        form = EmployeeInfoRegistForm()
        form.fields['qualification1'].initial = self.request.GET.get('qualification1')
        ctx = super().get_context_data(**kwargs)
        ctx['form'] = form
        global errFlg
        if errFlg:
            ctx['err_msg'] = "対象のデータが存在しません。"
        else:
            ctx['err_msg'] = ""
        return ctx

    def get_qualification_label(self, employee_list):
        form = EmployeeInfoRegistForm()
        for employee in employee_list:
            for qualification in form.fields["qualification1"].choices:
                if str(qualification[0]) == employee.qualification1:
                    employee.qualification1 = qualification[1]
                if str(qualification[0]) == employee.qualification2:
                    employee.qualification2 = qualification[1]
                if str(qualification[0]) == employee.qualification3:
                    employee.qualification3 = qualification[1]
            test = [employee.qualification1, employee.qualification2, employee.qualification3]
            employee.qualification1 = "<br>".join([n for n in test if  n != ""])

    def get_queryset(self):
        employeeCd = self.request.GET.get('employeeCd')
        employeeName = self.request.GET.get('employeeName')
        hireDate = re.sub("\\D", "", str(self.request.GET.get('hireDate')))
        qualification1 = self.request.GET.get('qualification1')
        global errFlg
        errFlg = False
        if len(self.request.GET.keys()) != 0 :
            employee_list = employee.objects.filter(
            Q(employee_cd__icontains=employeeCd),
            Q(employee_name__icontains=employeeName),
            Q(hire_date_ym__icontains=hireDate),
            Q(qualification1__icontains=qualification1) | Q(qualification2__icontains=qualification1) | Q(qualification3__icontains=qualification1)).order_by('employee_cd')
            if len(employee_list) == 0:
                employee_list = employee.objects.all().order_by('employee_cd')
                errFlg = True

        else:
            employee_list = employee.objects.all().order_by('employee_cd')
        self.get_qualification_label(employee_list)
        return employee_list
