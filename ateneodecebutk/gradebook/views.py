from django.shortcuts import render
from django.shortcuts import redirect
from django.http import Http404
from django.contrib import messages

# from django.http import HttpResponseRedirect
from .forms import UploadFileForm

from .gradebook import SECTION_CODES
from .gradebook import get_subject_status
from .gradebook import get_json_from_class_code
from .gradebook import save_ecr_file

def index(request, grading_period = None):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            save_ecr_file(request.FILES['file'], request.FILES['file'].name)
            messages.success(request,
                '<strong>Success!</strong> File successfully uploaded.')
            return redirect(request.path)
        else:
            raise Http404
    else:
        if grading_period is None:
            return redirect('/gradebook/4')

        form = UploadFileForm()

        class_table = []

        for i in range(6):
            class_table.append({
                'grade_level': i + 1,
                'sections': SECTION_CODES[i],
                'subjects': get_subject_status(grading_period, i + 1)
            })

        context = {
            'grading_period': grading_period,
            'class_table': class_table,
            'form': form
        }

        return render(request, 'gradebook/index.html', context)

def detail(request, grading_period, class_code):

    level = class_code[1]

    json_data = get_json_from_class_code(grading_period, level, class_code)

    if json_data is None:
        raise Http404

    context = {
        'json_data': json_data
    }

    return render(request, 'gradebook/detail.html', context)
