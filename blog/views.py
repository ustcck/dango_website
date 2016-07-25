import datetime
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader, Context

from blog.models import Student, Teacher


class Person(object):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def say(self):
        return 'my name is ' + self.name


def index(request):
    t = loader.get_template('index.html')
    user = {'name': 'tom', 'age': '23', 'sex': 'male'}

    person = Person('jack', 12, 'female')

    booklist = ['python', 'ruby', 'java', 'c']

    c = Context({'title': 'django', 'user': user, 'book_list': booklist, 'today': datetime.datetime.now()})

    return HttpResponse(t.render(c))


def time(request):
    t = loader.get_template('time.html')
    id = request.GET.get('id')
    c = Context({'title': 'time', 'today': datetime.datetime.now(), 'id': id})
    return HttpResponse(t.render(c))


def foo(request, p1, p2):
    t = loader.get_template('time.html')
    c = Context({'title': 'foo', 'today': datetime.datetime.now(), 'id': p1, 'name': p2})

    return HttpResponse(t.render(c))


def bar(request, id, name):
    t = loader.get_template('time.html')
    c = Context({'title': 'bar', 'today': datetime.datetime.now(), 'id': id, 'name': name})

    return HttpResponse(t.render(c))


def student_list(request):
    # t = loader.get_template('student.html')
    # studentList = Student.objects.all().order_by('name')
    # studentList = Student.objects.all().filter(age=34)
    # studentList = Student.objects.all().filter(age__gt=18)
    # studentList = Student.objects.all().filter(age__gte=34)
    # studentList = Student.objects.all().filter(name__contains='si')

    # student = Student.objects.all().get(id=2)
    # student.name = 'zhaoliu'
    # student.age = 30
    # student.save()

    # student = Student.objects.all().filter(age__lt=34).update(name='xyz')

    # newstudent = Student(name='abc', age=10, intime='2013-09-03',sex=0)
    # newstudent.save()

    # student = Student.objects.all().get(id=2)
    # student.delete()
    #
    #
    #
    # c = Context({'title': 'student', 'student': student})




    t = loader.get_template('student_teacher.html')
    # studentList =Student.objects.all()
    teacher = Teacher.objects.get(id=1)
    studentList = teacher.student_teacher.all()
    # teacher =student.teacher.name
    c = Context({'title': 'student_teacher', 'studentList': studentList})

    return HttpResponse(t.render(c))
