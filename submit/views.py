from django.shortcuts import render
from asset_db.models import Profiles


def submit(request):
    profiles = Profiles.objects.order_by('-id')
    context = {'profiles': profiles}
    return render(request, 'submit/submit.html', context)


def success(request):
    profiles = Profiles.objects.order_by('-id')
    context = {'profiles': profiles}
    return render(request, 'submit/success.html', context)
