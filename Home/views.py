from django.shortcuts import render

from course.models import course


# Create your views here.
def test(request):
    courses = course.objects.all()
    coursess = []
    count = 0
    for corse in courses.reverse():
        coursess.append(corse)
        count += 1
        if count == 2:
            break
    return render(request,'Home/home.html',{'courses':coursess})

def Rep(request):
    return render(request,'Class/msg.html')

