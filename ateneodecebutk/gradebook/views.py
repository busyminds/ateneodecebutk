from django.shortcuts import render

import gradebook
import glob
import os
import json

from ateneodecebutk.settings.base import BASE_DIR

def index(request):
    class_table = [
        {
            'grade_level': 1,
            'sections': gradebook.SECTION_CODES[0],
            'subjects': gradebook.get_subjects(1)
        },
        {
            'grade_level': 2,
            'sections': gradebook.SECTION_CODES[1],
            'subjects': gradebook.get_subjects(2)
        },
        {
            'grade_level': 3,
            'sections': gradebook.SECTION_CODES[2],
            'subjects': gradebook.get_subjects(3)
        },
        {
            'grade_level': 4,
            'sections': gradebook.SECTION_CODES[3],
            'subjects': gradebook.get_subjects(4)
        },
        {
            'grade_level': 5,
            'sections': gradebook.SECTION_CODES[4],
            'subjects': gradebook.get_subjects(5)
        },
        {
            'grade_level': 6,
            'sections': gradebook.SECTION_CODES[5],
            'subjects': gradebook.get_subjects(6)
        }
    ]

    gradebook_data = {}

    for level in class_table:
        glob_dir = os.path.join(BASE_DIR, 'data/assessments/levels/'
            + str(level['grade_level']))
        for f in glob.glob(glob_dir + '/*.json'):
            json_file = open(f)
            json_data = json.load(json_file)
            codes = os.path.basename(f).rstrip('.json').split('-')
            gradebook_data[codes[0]]={}
            gradebook_data[codes[0]][codes[1]] = json_data

    context = {
        # 'grade_levels': grade_levels,
        # 'sections': gradebook.SECTIONS,
        # 'subject_array': subject_array,
        'gradebook_data': gradebook_data,
        'class_table': class_table
    }
    return render(request, 'gradebook/index.html', context)
