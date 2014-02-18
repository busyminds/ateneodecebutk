import os

from django.shortcuts import render
from django.shortcuts import redirect
from django.http import Http404
from django.contrib import messages

from .forms import UploadFileForm

from .gradebook_reader import SECTION_CODES
from .gradebook_reader import get_subject_status
from .gradebook_reader import get_json_from_class_code
from .gradebook_reader import save_ecr_file
from .gradebook_writer import write_gradebook_data

from .mail_sender import send_message

def index(request, grading_period = None):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            filepath = save_ecr_file(request.FILES['file'],
                request.FILES['file'].name)
            # try:
            class_data = write_gradebook_data(grading_period, filepath)
            send_message(request, class_data)
            message = '<strong>Success!</strong> File uploaded.'
            messages.success(request, message)
            # except:
                # os.remove(filepath)
                # err_msg = '<strong>Error!</strong> '
                # err_msg += 'Please make sure you are uploading the correct '
                # err_msg += 'file.'
                # messages.add_message(request, messages.ERROR, err_msg,
                #     'danger')

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
            'form': form,
            'debug': request.get_host()
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

def subject(request, grading_period, grade_level, subject):

    pass
