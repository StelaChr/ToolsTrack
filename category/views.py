from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.shortcuts import render, redirect

from tools.models import Tool
from .forms import CategoryForm
from .models import Category

@login_required
def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)   # ⛔ Don't save yet
            category.owner = request.user        # ✅ Assign the logged-in user
            category.save()                      # ✅ Now save to DB
            return redirect('create-tool')
    else:
        form = CategoryForm()

    return render(request, 'create-category.html', {'form': form})


@login_required
def category_tools_view(request, category_id):
    category = get_object_or_404(Category, id=category_id)

    # Check if the current user is allowed to view this category
    if not category.tools.filter(owner=request.user).exists() and not (request.user.is_staff or request.user.is_superuser):
        raise PermissionDenied  # Return a 403 page

    tools = Tool.objects.filter(owner=request.user, category=category)
    search_query = request.GET.get('q', '')

    return render(request, 'category-tools.html', {
        'category': category,
        'tools': tools,
        'search_query': search_query
    })