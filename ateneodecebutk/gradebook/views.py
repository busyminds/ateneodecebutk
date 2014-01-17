from django.shortcuts import render
import os

from ateneodecebutk.settings.base import BASE_DIR

import gradebook

def index(request, grading_period):
    class_table = []

    for i in range(6):
        class_table.append({
            'grade_level': i + 1,
            'sections': gradebook.SECTION_CODES[i],
            'subjects': gradebook.get_subject_status(grading_period, i + 1)
        })
    context = {
        'grading_period': grading_period,
        'class_table': class_table
    }
    return render(request, 'gradebook/index.html', context)

def detail(request, grading_period, class_code):

    grade_level = class_code[1]
    # grading_period = 4

    data_dir = os.path.join(BASE_DIR, 'files/gradebook/assessments/'
        + str(grading_period) + '/levels/' + str(grade_level) + '/')

    try:
        json_file = open(os.path.join(data_dir, class_code + '.json')).read()
    except:
        pass

    context = {
        'json_data': json_file
    }
    return render(request, 'gradebook/detail.html', context)
