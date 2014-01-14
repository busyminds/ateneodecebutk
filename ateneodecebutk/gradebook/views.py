from django.shortcuts import render

import gradebook

def index(request):
    class_table = [
        {
            'grade_level': 1,
            'sections': gradebook.SECTION_CODES[0],
            'subjects': gradebook.get_subject_status(1)
        },
        {
            'grade_level': 2,
            'sections': gradebook.SECTION_CODES[1],
            'subjects': gradebook.get_subject_status(2)
        },
        {
            'grade_level': 3,
            'sections': gradebook.SECTION_CODES[2],
            'subjects': gradebook.get_subject_status(3)
        },
        {
            'grade_level': 4,
            'sections': gradebook.SECTION_CODES[3],
            'subjects': gradebook.get_subject_status(4)
        },
        {
            'grade_level': 5,
            'sections': gradebook.SECTION_CODES[4],
            'subjects': gradebook.get_subject_status(5)
        },
        {
            'grade_level': 6,
            'sections': gradebook.SECTION_CODES[5],
            'subjects': gradebook.get_subject_status(6)
        }
    ]

    class_table = []

    for i in range(6):
        class_table.append(
            {
                'grade_level': i + 1,
                'sections': gradebook.SECTION_CODES[i],
                'subjects': gradebook.get_subject_status(i + 1)
            }
        )
    context = {
        # 'grade_levels': grade_levels,
        # 'sections': gradebook.SECTIONS,
        # 'subject_array': subject_array,
        'class_table': class_table
    }
    return render(request, 'gradebook/index.html', context)
