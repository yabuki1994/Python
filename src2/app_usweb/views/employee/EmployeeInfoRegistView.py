###############################
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from ...forms import (EmployeeInfoRegistForm)
from ...models import employee
from django.contrib import messages
import json
###############################
from django.shortcuts import render
from telnetlib import theNULL

class EmployeeInfoRegistView(generic.CreateView, LoginRequiredMixin):

    model = employee
    template_name = 'master/EMD0101.html'
    form_class = EmployeeInfoRegistForm
    #Fields = ['employeeCd', 'employeeName', 'employeeNameKana', 'hireDateYm', 'hobby', 'qualification1', 'qualification2', 'qualification3']

    def form_valid(self, form):
        ''' バリデーションを通った時 '''
        print('成功')
        return super().form_valid(form)

    def form_invalid(self, form):
        ''' バリデーションに失敗した時 '''
        print('失敗')

#       test = {}
#       for key, value in form.errors.items():
#            for meta_field in employee._meta.get_fields():
#                if meta_field.attname ==  key :
#                    test[meta_field.verbose_name] = value
#                #  pass
#        form.errors.clear()
#      #  for key, value in test.items():
#        form.add_error('employee_cd', json.dumps(test))

#        return render(self.request, self.template_name, {'form': form}) #エラーメッセージを含んだフォームをセットして再表示
        return super().form_invalid(form)
