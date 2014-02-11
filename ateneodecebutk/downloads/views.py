from django.shortcuts import render
# from django.http import HttpResponse
import glob
import os
from ateneodecebutk.settings.production import MEDIA_ROOT

# Create your views here.
def index(request):
    ecr_files = [os.path.basename(f) for f in
        glob.glob(MEDIA_ROOT + '/downloads/gradebook/*')]
    ecr_files.sort()
    context = {
        'ecr_files': ecr_files,
        'test': 'Hello'
    }
    return render(request, 'downloads/index.html', context)
