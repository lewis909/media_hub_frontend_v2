from asset_db.models import Profiles, Task
from django.shortcuts import render_to_response, render

from .forms import SubmitJob


def job(request):
    if request.method == 'POST':
        form = SubmitJob(request.POST)
        if form.is_valid():
            insert = Task()
            insert.material_id = str(request.POST['material_id'])
            insert.workflow = str(request.POST['workflow'])
            insert.save()
            print(request.POST['material_id'])
            print(request.POST['workflow'])
            message = 'success'

        else:
            message = 'fail'
        return render(request, 'submit/submit.html', {'message': message})
    else:
        return render(request, 'submit/submit.html', {'form': SubmitJob()})

