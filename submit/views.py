from asset_db.models import Task, FileRepo, AssetMetadata
from django.shortcuts import render
from .functions import timestamp, create_core_xml

from .forms import SubmitJob


def job(request):

    filerepo = FileRepo.objects.values_list('filename', flat=True)

    if request.method == 'POST':
        
        mat_id_post = request.POST['material_id']
        
        if mat_id_post in filerepo:
            form = SubmitJob(request.POST)
            if form.is_valid():
                insert = Task()
                insert.material_id = str(mat_id_post)
                insert.workflow = str(request.POST['workflow'])
                insert.status = 'Submitted'
                insert.job_start_time = timestamp()
                insert.save()
                task_id = insert.id
                message = 'Task ' + str(task_id) + ' success.' + '\n' + request.POST[
                    'material_id'] + ' has been submitted'

                asset_check = AssetMetadata.objects.filter(material_id=str(mat_id_post)).values().all()
                filerepo_check = FileRepo.objects.filter(filename=str(mat_id_post)).values().all()
                core_xml_target_path = ''
                core_xml_filename = ''
                segment_start = []
                segment_dur = []
                create_core_xml(core_xml_filename,
                                core_xml_target_path,
                                asset_check.get('material_id'),
                                asset_check.get('series_id'),
                                asset_check.get('season_title'),
                                asset_check.get('season_number'),
                                asset_check.get('episode_title'),
                                asset_check.get('episode_number'),
                                asset_check.get('start_date'),
                                asset_check.get('end_date'),
                                asset_check.get('synopsis'),
                                asset_check.get('ratings'),
                                filerepo_check.get('filename'),
                                filerepo_check.get('number_of_segments'),
                                filerepo_check.get('conform_profile'),
                                filerepo_check.get('transcode_profile'),
                                filerepo_check.get('target_path'),
                                filerepo_check.get('segment_start'),
                                segment_start,
                                segment_dur
                                )
                print(asset_check[0])
                print(filerepo_check[0])
            else:
                message = 'fail'
            return render(request, 'submit/submit.html', {'form': SubmitJob(),
                                                          'message': message})
        else:
            message = mat_id_post + ' is not in the File Repository, please ingest'
            return render(request, 'submit/submit.html', {'form': SubmitJob(), 'message': message})
    else:
        return render(request, 'submit/submit.html', {'form': SubmitJob()})
