from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView

from maintenance.forms import ToolMaintenanceForm
from maintenance.models import ToolMaintenance
from tools.models import Tool


# Create your views here.
class ToolMaintenanceCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = ToolMaintenance
    form_class = ToolMaintenanceForm
    template_name = 'maintenance-create.html'

    def dispatch(self, request, *args, **kwargs):
        self.tool = get_object_or_404(Tool, pk=self.kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def test_func(self):
        # Allow access if the current user is the owner of the tool or is staff/superuser
        return self.tool.owner == self.request.user or self.request.user.is_staff

    def handle_no_permission(self):
        return redirect('dashboard')  # Or show a custom permission denied page

    def form_valid(self, form):
        form.instance.tool = self.tool
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tool'] = self.tool
        return context

    def get_success_url(self):
        return reverse('tool-detail', kwargs={'pk': self.object.tool.pk}) # Or use 'tool-detail' if available


@login_required
def maintenance_records_view(request, pk):
    tool = get_object_or_404(Tool, pk=pk)
    if tool.owner != request.user and not (request.user.is_staff or request.user.is_superuser):
        raise PermissionDenied  # Return a 403 page
    maintenance_records = tool.maintenance_records.all()  # Uses related_name
    return render(request, 'maintenance-records.html', {
        'tool': tool,
        'maintenance_records': maintenance_records,
    })