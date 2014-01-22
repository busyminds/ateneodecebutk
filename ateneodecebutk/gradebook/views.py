from django.shortcuts import render
from django.shortcuts import redirect
from django.http import Http404

from .gradebook import SECTION_CODES
from .gradebook import get_subject_status
from .gradebook import get_json_from_class_code

def index(request, grading_period = None):
    if grading_period is None:
        return redirect('/gradebook/4')

    class_table = []

    for i in range(6):
        class_table.append({
            'grade_level': i + 1,
            'sections': SECTION_CODES[i],
            'subjects': get_subject_status(grading_period, i + 1)
        })

    context = {
        'grading_period': grading_period,
        'class_table': class_table
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
