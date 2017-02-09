from django.shortcuts import render
from asset_db.models import Profiles


def submit(request):
    profiles = Profiles.objects.order_by('-id')
    context = {'profiles': profiles}
    return render(request, 'submit/submit.html', context)


def success(request):
    profiles = Profiles.objects.order_by('-id')
    matid = request.POST['material_id']
    workflow = request.POST['workflow']
    start_date = request.POST['start_date']
    end_date = request.POST['end_date']
    context = {'profiles': profiles,
               'matid': matid,
               'workflow': workflow,
               'start_date': start_date,
               'end_date': end_date}
    return render(request, 'submit/success.html', context)
