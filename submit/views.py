from asset_db.models import Task, FileRepo, AssetMetadata
from django.shortcuts import render
from .functions import timestamp, create_core_xml

from .forms import SubmitJob


def job(request):

    filerepo = FileRepo.objects.values_list('filename', flat=True)

    if request.method == 'POST':
        if request.POST['material_id'] in filerepo:
            print('true')
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
                print(request.POST['start_datepicker'])
                print(request.POST['end_datepicker'])
                message = 'Task ' + str(task_id) + ' success.' + '\n' + request.POST[
                    'material_id'] + ' has been submitted'

                asset = AssetMetadata.objects.filter(material_id=str(request.POST['material_id'])).values().all()
                print(asset)
            else:
                message = 'fail'
            return render(request, 'submit/submit.html', {'form': SubmitJob(),
                                                          'message': message})
        else:
            print('false')
            message = request.POST['material_id'] + ' is not in the File Repository, please ingest'
            return render(request, 'submit/submit.html', {'form': SubmitJob(), 'message': message})
    else:
        return render(request, 'submit/submit.html', {'form': SubmitJob()})
