from asset_db.models import Task, FileRepo, AssetMetadata, Profiles, ConformProfiles
from django.shortcuts import render
from .functions import timestamp, create_core_xml
from django.contrib.auth.decorators import login_required
from .forms import SubmitJob


@login_required(login_url='login')
def job(request):
    """
        The job function renders the submit job page and handles the form POST methods generated on submit.
        It makes sure the form being submitted is valid, if this is true it will pass the relevant data to the
        create_core_xml function which creates the xml file which is used to drive the transcoders back end.
    """
    filerepo = FileRepo.objects.values_list('filename', flat=True)
    asset_mat_id = AssetMetadata.objects.all()

    if request.method == 'POST':
        
        mat_id_post = str(request.POST['material_id']).upper()
        workflow = request.POST['workflow']

        if mat_id_post in filerepo:
            form = SubmitJob(request.POST)
            if form.is_valid():
                insert = Task()
                insert.material_id = str(mat_id_post)
                insert.workflow = str(request.POST['workflow'])
                insert.status = 'Submitted'
                insert.user = str(request.user.username)
                insert.job_start_time = timestamp()
                insert.save()
                task_id = "%06d" % insert.id
                message = 'Task ' + str(task_id) + ' success.' + '\n' + mat_id_post + ' has been submitted'

                asset_check = AssetMetadata.objects.filter(material_id=str(mat_id_post)).values().all()
                filerepo_check = FileRepo.objects.filter(filename=str(mat_id_post)).values().all()

                file_aspect_ratio = filerepo_check[0].get('aspect_ratio')
                file_def = filerepo_check[0].get('definition')
                standard = ''

                if file_aspect_ratio == '12f16' and file_def == 'SD':
                    standard = 'sd169'
                elif file_aspect_ratio == '16f16' and file_def == 'SD':
                    standard = 'sd169'
                elif file_aspect_ratio == '12f12' and file_def == 'SD':
                    standard = 'sd43'
                elif file_aspect_ratio == '16f16' and file_def == 'HD':
                    standard = 'hd'

                profile_check = Profiles.objects.filter(name=str(workflow)).values().all()
                conform_check = ConformProfiles.objects.filter(name=standard).values().all()
                segment_start = []
                segment_dur = []

                for i in range(int(filerepo_check[0].get('number_of_segments'))):
                    x = i + 1
                    seg = filerepo_check[0].get('seg_%d_in' % x)
                    segment_start.append(seg)

                for i in range(int(filerepo_check[0].get('number_of_segments'))):
                    x = i + 1
                    seg = filerepo_check[0].get('seg_%d_dur' % x)
                    segment_dur.append(seg)

                core_xml_target = 'F:\\Transcoder\\staging\prep\\'
                core_xml_file_name = str(task_id) + '_' + str(profile_check[0].get('name')) + '_' + str(asset_check[0].get('material_id')) + '_'

                create_core_xml(core_xml_file_name,
                                core_xml_target,
                                task_id,
                                asset_check[0].get('material_id'),
                                asset_check[0].get('series_title'),
                                asset_check[0].get('season_title'),
                                asset_check[0].get('season_number'),
                                asset_check[0].get('episode_title'),
                                asset_check[0].get('episode_number'),
                                str(request.POST['start_datepicker']),
                                str(request.POST['end_datepicker']),
                                asset_check[0].get('synopsis'),
                                asset_check[0].get('ratings'),
                                filerepo_check[0].get('filename'),
                                filerepo_check[0].get('number_of_segments'),
                                conform_check[0].get('conform_profile'),
                                profile_check[0].get('target_profile'),
                                profile_check[0].get('target_path'),
                                file_def,
                                file_aspect_ratio,
                                profile_check[0].get('name'),
                                profile_check[0].get('package_type'),
                                segment_start,
                                segment_dur,
                                profile_check[0].get('video_naming_convention'),
                                profile_check[0].get('image_naming_convention'),
                                profile_check[0].get('package_naming_convention')
                                )
            else:
                message = 'fail'
            return render(request, 'submit/submit.html', {'form': SubmitJob(),
                                                          'message': message,
                                                          'asset_matid': asset_mat_id})
        else:
            message = mat_id_post + ' is not in the File Repository, please ingest'
            return render(request, 'submit/submit.html', {'form': SubmitJob(),
                                                          'message': message,
                                                          'asset_matid': asset_mat_id})
    else:

        return render(request, 'submit/submit.html', {'form': SubmitJob(),
                                                      'asset_matid': asset_mat_id})
