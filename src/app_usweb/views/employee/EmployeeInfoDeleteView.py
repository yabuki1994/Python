###############################
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from ...models import employee

class EmployeeInfoDeleteView(generic.DeleteView, LoginRequiredMixin):

    model = employee
    success_url = reverse_lazy('app_usweb:employee_info_refer')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)