from django.db import models

class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    middle_initial = models.CharField(max_length=5)
    salutation = models.CharField(max_length=5)
    suffix = models.CharField(max_length=5)

class Subject(models.Model):
	code = models.CharField(max_length=3)
	name = models.CharField(max_length=20)

class Section(models.Model):
	code = models.CharField(max_length=3)
	level = models.IntegerField()
	name = models.CharField(max_length=20)
	full_name = models.CharField(max_length=40)

class Course(models.Model):
	teacher = models.ManyToManyField(Teacher)
	subject = models.ForeignKey(Subject)
	section = models.ForeignKey(Section)
	schedule = models.CharField(max_length=5)

