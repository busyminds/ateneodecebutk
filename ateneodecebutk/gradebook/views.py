from django.shortcuts import render

import gradebook

def index(request):
    class_table = []

    for i in range(6):
        class_table.append({
            'grade_level': i + 1,
            'sections': gradebook.SECTION_CODES[i],
            'subjects': gradebook.get_subject_status(i + 1)
        })
    context = {
        'class_table': class_table
    }
    return render(request, 'gradebook/index.html', context)
