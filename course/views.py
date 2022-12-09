from django.shortcuts import redirect, render

from course.models import Join, course
from Home.views import Rep


# Create your views here.
def cls(request):
    courses = course.objects.all()
    return render(request,'Class/index.html',{'courses':courses})

def cours(request,inum):
    info = course.objects.get(id=inum)
    return render(request,'Class/section.html',{'course':info})

def join(request,inum):
    info = course.objects.get(id=inum)
    return render(request,'Class/registr.html',{'course':info})


def save(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']
        interested = request.POST['interested']

        form = Join.objects.create(name=name, email=email, contact=contact, interested=interested)
        form.save()
        return redirect('Rep')
        