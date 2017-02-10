from asset_db.models import Task
from django.shortcuts import render
from .functions import timestamp

from .forms import SubmitJob


def job(request):
    if request.method == 'POST':
        form = SubmitJob(request.POST)
        if form.is_valid():
            insert = Task()
            insert.material_id = str(request.POST['material_id'])
            insert.workflow = str(request.POST['workflow'])
            insert.status = 'Submitted'
            insert.job_start_time = timestamp()
            insert.save()
            task_id = insert.id
            print(request.POST['material_id'])
            print(request.POST['workflow'])
            message = 'Task ' + str(task_id) + ' success.' + '\n' + request.POST['material_id'] + ' has been submitted'
        else:
            message = 'fail'
        return render(request, 'submit/submit.html', {'form': SubmitJob(),
                                                      'message': message})
    else:
        return render(request, 'submit/submit.html', {'form': SubmitJob()})

