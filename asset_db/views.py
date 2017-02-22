from .models import AssetMetadata, Task
from django.views.generic import DetailView
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required(login_url='login'), name='dispatch')
class AssetView(DetailView):
    model = AssetMetadata


@login_required(login_url='login')
def task_status(request):

    task_list = Task.objects.order_by('-id').all()
    page = request.GET.get('page', 1)
    paginator = Paginator(task_list, 50)

    try:
        task = paginator.page(page)
    except PageNotAnInteger:
        task = paginator.page(1)
    except EmptyPage:
        task = paginator.page(paginator.num_pages)
    return render(request, 'assets_db/task.html', {'task_status': task})


@login_required(login_url='login')
def assets_in_repo(request):

    asset_list = AssetMetadata.objects.order_by('id').all()
    page = request.GET.get('page', 1)
    paginator = Paginator(asset_list, 50)

    try:
        assets = paginator.page(page)
    except PageNotAnInteger:
        assets = paginator.page(1)
    except EmptyPage:
        assets = paginator.page(paginator.num_pages)

    return render(request, 'assets_db/assets.html', {'assets': assets})
