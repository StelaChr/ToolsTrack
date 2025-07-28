from django.contrib.auth.decorators import login_required


from django.shortcuts import render
from django.views.generic import TemplateView

from category.models import Category
from tools.models import Tool
from django.db.models import Count, Q

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'


@login_required
def dashboard_view(request):
    search_query = request.GET.get('q', '')

    tools_qs = Tool.objects.filter(owner=request.user)

    if search_query:
        tools_qs = tools_qs.filter(
            Q(name__iexact=search_query) |
            Q(brand_name__iexact=search_query) |
            Q(inventory_number=search_query) |
            Q(room__iexact=search_query) |
            Q(section_number=search_query)
        )

    categories = Category.objects.filter(
        tools__in=tools_qs
    ).distinct().annotate(
        tool_count=Count('tools', filter=Q(tools__in=tools_qs))
    )

    context = {
        'categories': categories,
        'search_query': search_query,
    }

    if search_query:
        context['tools'] = tools_qs  # <- this is what your template expects

    return render(request, 'dashboard.html', context)

