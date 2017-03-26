from django.shortcuts import render
from asset_db.models import Task
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def user_task(request):
    """ Renders data from teh task status DB and filters it by Username"""
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


@login_required(login_url='login')
def user_task_update(request):
    """ Provides the data Jquery .load() uses to update the user_task page."""

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