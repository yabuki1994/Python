###############################
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from ...models import employee


# 社員マスタ削除ビュークラス
class EmployeeMstDeleteView(DeleteView, LoginRequiredMixin):

    model = employee
    success_url = reverse_lazy('app_usweb:employee_mst_refer')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        result = super().delete(request, *args, **kwargs)
        messages.success(
            self.request, '社員番号：{} のデータを削除しました'.format(self.kwargs['pk']))
        return result
