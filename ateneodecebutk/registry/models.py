from django.db import models

class Teacher(models.Model):
    salutation = models.CharField(max_length=5)
    first_name = models.CharField(max_length=30)
    middle_initial = models.CharField(max_length=5, blank=True)
    last_name = models.CharField(max_length=30)
    suffix = models.CharField(max_length=5, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __unicode__(self):
        return self.last_name + ', ' + self.first_name

    class Meta:
        ordering = ['last_name']

class Subject(models.Model):
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Section(models.Model):
    code = models.CharField(max_length=3)
    level = models.IntegerField()
    name = models.CharField(max_length=20)
    full_name = models.CharField(max_length=40)

    def __unicode__(self):
        return str(self.level) + '-' + self.name

    class Meta:
        ordering = ['code']

class Course(models.Model):
    section = models.ForeignKey(Section)
    subject = models.ForeignKey(Subject)
    teacher = models.ForeignKey(Teacher, null=True)
    schedule = models.CharField(max_length=5, blank=True)

    def __unicode__(self):
        return str(self.section) + ' | ' + str(self.subject)

    class Meta:
        ordering = ['section', 'subject']
