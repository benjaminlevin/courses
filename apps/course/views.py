from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import Course, Comment, Description

def index(request):
    context = {
        "course" : Course.objects.all(),
        #"description" : Description.objects.all()
		#runs: select * from Course
    }
    return render(request, "course/index.html", context)

def add(request):
    course = Course.objects.create(name=request.POST['name'])
    Description.objects.create(description=request.POST['description'], course = course)
    return redirect('/')

def addDescription(request, description):
    description=request.POST['description']
    return redirect('/')


def comment(request, id):
    context = {
        "course" : Course.objects.get(id=id),
        "comment" : Comment.objects.filter(course=id)

    }
    return render(request, "course/comment.html", context)

def addComment(request, id):
    course = Course.objects.get(id=id)
    Comment.objects.create(comment=request.POST['comment'], course=course)
    return redirect('/courses/comment/'+id)   

def remove(request, id):
    context = {
        "course" : Course.objects.get(id=id),
    }
    return render(request, "course/destroy.html", context)
    
def delete(request, id):
    Course.objects.filter(id=id).delete()
    return redirect('/')