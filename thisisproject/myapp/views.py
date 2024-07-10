from django.shortcuts import render , redirect
from django.contrib.auth import login, authenticate

from .forms import BlogForm
from .forms import SignUpForm

from . models import *
from django.contrib import messages
# Create your views here.
# myapp/views.py

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world!")

def Blogs(request):
    blog_db = Blog.objects.all()
    return render(request, 'myapp/blog.html', {'blog_db' : blog_db})

def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST,request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('create_blog')
    else:
        form = BlogForm()

    return render(request,'myapp/create_blog.html',{'form' : form})


def update_blog(request, blog_id):
    update = Blog.objects.get(id=blog_id)
    if request.method == "POST":
        title = request.POST.get('title')
        subtitle = request.POST.get("subtitle")
        description = request.POST.get("description")
        image = request.FILES.get('image')

        update.title =title
        update.subtitle = subtitle
        update.description = description
        update.image = image 


        update.save()
        messages.success(request,"this blog is updated")
        return redirect('Blog')
    return render(request, 'myapp/update.html',{'update': update})
       

def delete_blog(request,blog_id):
    deleted = Blog.objects.get(id=blog_id)
    deleted.delete()
    messages.success(request,"this is deleted")
    return redirect('Blog')

# for signup
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})



# for login 
# views.py
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'login.html'





