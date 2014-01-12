from django.shortcuts import render

import gradebook

# Create your views here.
def index(request):
    grade_levels = range(1,7)

    subject_array = []

    for grade_level in range(1,7):
        subject_array.append(gradebook.get_subjects(grade_level))

    context = {
        'grade_levels': grade_levels,
        'sections': gradebook.SECTIONS,
        'subject_array': subject_array,
    }
    return render(request, 'gradebook/index.html', context)
