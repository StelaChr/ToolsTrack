from urllib import request

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from .forms import BorrowForm, CreateToolForm, ToolEditForm
from .models import Tool, Borrow


class ToolCreateView(LoginRequiredMixin, CreateView):
    model = Tool
    form_class = CreateToolForm
    template_name = 'create-tool.html'
    success_url = reverse_lazy('dashboard')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  # ✅ Pass the user to the form
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST and self.request.POST.get('is_borrowed') == 'on':
            context['borrow_form'] = BorrowForm(self.request.POST)
        else:
            context['borrow_form'] = BorrowForm()
        return context

    def form_valid(self, form):

        tool = form.save(commit=False)
        tool.owner = self.request.user
        is_borrowed = self.request.POST.get('is_borrowed') == 'on'
        tool.save()

        if is_borrowed:
            borrow_form = BorrowForm(self.request.POST)
            if borrow_form.is_valid():
                borrow = borrow_form.save(commit=False)
                borrow.tool = tool
                borrow.save()
            else:
                tool.delete()
                context = self.get_context_data(form=form)
                context['error'] = 'Borrow form is required and has errors.'
                context['borrow_form'] = borrow_form
                return self.render_to_response(context)

        return redirect(self.success_url)


class ToolUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Tool
    form_class = ToolEditForm
    template_name = 'edit-tool.html'
    success_url = reverse_lazy('dashboard')  # Or your desired success URL

    def test_func(self):
        tool = self.get_object()
        return tool.owner == self.request.user

    def handle_no_permission(self):
        return redirect('dashboard')  # Customize if needed

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tool = self.get_object()

        # Borrow instance: last borrow related to the tool or None
        borrow_instance = tool.borrows.last()

        # Initialize borrow form with POST data if available, else with the instance
        if self.request.method == 'POST' and self.request.POST.get('is_borrowed') == 'on':
            context['borrow_form'] = BorrowForm(self.request.POST, instance=borrow_instance)
        else:
            context['borrow_form'] = BorrowForm(instance=borrow_instance) if borrow_instance else BorrowForm()

        # Pass the tool itself
        context['tool'] = tool

        # Pass mic fields list for the template to check
        context['mic_fields'] = ['category', 'name', 'brand_name']

        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        tool = form.instance
        borrow_instance = tool.borrows.last()

        if tool.is_borrowed:
            borrow_form = BorrowForm(self.request.POST, instance=borrow_instance)
            if borrow_form.is_valid():
                borrow = borrow_form.save(commit=False)
                borrow.tool = tool
                borrow.save()
            else:
                # If borrow form is invalid, re-render the form with errors
                context = self.get_context_data(form=form)
                context['borrow_form'] = borrow_form
                return self.render_to_response(context)
        else:
            if borrow_instance:
                borrow_instance.delete()

        return response

class ToolDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Tool
    template_name = 'tool-detail.html'
    context_object_name = 'tool'

    def test_func(self):
        tool = self.get_object()
        return self.request.user == tool.owner or self.request.user.is_staff or self.request.user.is_superuser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tool = self.get_object()

        # Latest borrow record based on borrowed_at
        context['borrow'] = Borrow.objects.filter(tool=tool).order_by('-borrowed_at').first()

        # All maintenance records
        context['maintenance_records'] = tool.maintenance_records.all()

        return context


class ToolDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = Tool
    template_name = 'tool-delete.html'
    success_url = reverse_lazy('dashboard')

    def test_func(self):
        tool = self.get_object()
        return self.request.user == tool.owner
