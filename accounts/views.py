from django.shortcuts import render
from asset_db.models import Task
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required


def user_task(request):

    user_task_status = Task.objects.filter(user=request.user.username).all().order_by('-id')
    page = request.GET.get('page', 1)
    paginator = Paginator(user_task_status, 50)
    try:
        task = paginator.page(page)
    except PageNotAnInteger:
        task = paginator.page(1)
    except EmptyPage:
        task = paginator.page(paginator.num_pages)
    return render(request, 'accounts/user_task_status.html', {'user_task_status': task,
                                                              'username': request.user.username})


def user_task_update(request):

    user_task_status = Task.objects.filter(user=request.user.username).all().order_by('-id')
    page = request.GET.get('page', 1)
    paginator = Paginator(user_task_status, 50)
    try:
        task = paginator.page(page)
    except PageNotAnInteger:
        task = paginator.page(1)
    except EmptyPage:
        task = paginator.page(paginator.num_pages)
    return render(request, 'accounts/user_task_status_update.html', {'user_task_status': task,
                                                              'username': request.user.username})