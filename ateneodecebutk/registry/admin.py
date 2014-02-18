from django.contrib import admin
from .models import Teacher
from .models import Section
from .models import Subject
from .models import Course

admin.site.register(Teacher)
admin.site.register(Section)
admin.site.register(Subject)
admin.site.register(Course)
