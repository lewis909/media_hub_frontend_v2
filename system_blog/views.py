from django.shortcuts import render
from .models import SystemBlog
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def blog(request):

    sys_blog = SystemBlog.objects.all().order_by('-id')
    context = {'blog': sys_blog}
    print()
    return render(request, 'system_blog/system_blog.html', context)

