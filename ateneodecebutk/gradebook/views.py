from django.shortcuts import render

import gradebook
import glob
import os
import json

from ateneodecebutk.settings.base import BASE_DIR

# Create your views here.
def index(request):
    grade_levels = range(1,7)

    subject_array = []

    for grade_level in range(1,7):
        subject_array.append(gradebook.get_subjects(grade_level))

    gradebook_data = []

    for level in grade_levels:
        glob_dir = os.path.join(BASE_DIR, 'data/assessments/levels/' + str(level))
        for f in glob.glob(glob_dir + '/*.json'):
            json_file = open(f)
            json_data = json.load(json_file)
            gradebook_data.append(json_data)

    context = {
        'grade_levels': grade_levels,
        'sections': gradebook.SECTIONS,
        'subject_array': subject_array,
        'gradebook_data': gradebook_data
    }
    return render(request, 'gradebook/index.html', context)
