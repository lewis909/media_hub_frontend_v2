from django.shortcuts import render
from .models import SystemBlog
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def blog(request):
    """
        Blog renders data from the blog DB table which is being used to provide system updates to users.
        This information is rendered on the Home page and all posts can be seen at /blog/ url.
    """

    sys_blog = SystemBlog.objects.all().order_by('-id')
    context = {'blog': sys_blog}
    print()
    return render(request, 'system_blog/system_blog.html', context)

