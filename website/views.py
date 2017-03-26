from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from system_blog.models import SystemBlog
from asset_db.models import Task


@login_required(login_url='login')
def index(request):
    """ 
        index creates the Home page, rendering data from the system blog,
        it also renders the most recent 20 submitted jobs.
    """
    blog_v = SystemBlog.objects.all().order_by('-id')[:5]
    task_list = Task.objects.order_by('-id')[:20].all()
    return render(request, 'website/home.html', {'user': request.user.username,
                                                 'blog': blog_v,
                                                 'task_list': task_list})


@login_required(login_url='login')
def index_update(request):
    """
        index_update creates the task data which the Home page template poll's using Jquery .load(). 
    """
    task_list = Task.objects.order_by('-id')[:20].all()
    return render(request, 'website/home_update.html', {'user': request.user.username, 'task_list': task_list})
