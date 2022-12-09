from django.shortcuts import render
from Blog.models import Blogp

# Create your views here.

def Blog(request):
    blogs = Blogp.objects.all()
    return render(request,'Blog/index.html',{'blogs':blogs})

def post(request,inum):
    bpost = Blogp.objects.get(id=inum)
    return render(request,'Blog/post.html',{'bpost':bpost})
