from django.shortcuts import render

from gradebook import SUBJECTS
from gradebook import SECTIONS

# Create your views here.
def index(request):
    grade_levels = range(1,7)
    context = {
        'grade_levels': grade_levels,
        'sections': SECTIONS,
        'subjects': SUBJECTS
    }
    return render(request, 'gradebook/index.html', context)
