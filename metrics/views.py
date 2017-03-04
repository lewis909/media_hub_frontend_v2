from django.shortcuts import render
from asset_db.models import Task
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def task_metrics(request):
    submitted = Task.objects.filter(status='Submitted').all()
    conforming = Task.objects.filter(status='Conforming').all()
    transcoding = Task.objects.filter(status='Transcoding').all()
    complete = Task.objects.filter(status='Complete').all()
    error = Task.objects.filter(status='Error').all()
    context = {'submitted': len(list(submitted)),
               'conforming': len(list(conforming)),
               'transcoding': len(list(transcoding)),
               'complete': len(list(complete)),
               'error': len(list(error)),
               }
    return render(request, 'metrics/metrics.html', context)
