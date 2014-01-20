from django.shortcuts import render
from django.shortcuts import redirect

import gradebook

def index(request, grading_period = None):
    if grading_period is None:
        return redirect('/gradebook/4')
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

    context = {
        'json_data': gradebook.get_json_from_class_code(grading_period,
            grade_level, class_code)
    }
    return render(request, 'gradebook/detail.html', context)
