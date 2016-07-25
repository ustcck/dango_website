from django.db import models


# Create your models here.

class Teacher(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'teacher'

    def __unicode__(self):
        return self.name


class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    intime = models.DateField()
    sex = models.IntegerField()
    teacher = models.ForeignKey(Teacher, related_name='student_teacher')

    class Meta:
        db_table = 'student'

    def __unicode__(self):
        return self.name
