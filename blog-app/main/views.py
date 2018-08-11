from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator,EmptyPage , PageNotAnInteger

from . import models
from . import forms

@login_required
def Index(request):
    context = {}
    return render(request,'main/Index.html',context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('Index'))

def login_view(request):
    if request.method == "GET":
        form = forms.LoginForm()
    else:
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # authenticate checks whether the entered credentials are correct or not or are of existing user or not
            user = authenticate(request,username = username ,password = password)

            if user is not None:
                login(request,user) # sending the request and credentials to the login funtion

                try:
                    return HttpResponseRedirect(request.GET['next'])
                except:
                    return HttpResponseRedirect(reverse('Index'))

    context = {
        "form" : form
    }    
     
    return render(request,'main/login.html',context)
    
def signup_view(request):
    if request.method == 'GET':
        form = UserCreationForm()
    else: #post method
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(request,username = username, password = password)
            if user is not None:
                login(request,user)

                try:
                    return HttpResponseRedirect(request.GET['next'])
                except:
                    return HttpResponseRedirect(reverse('login'))
    context = {
        "form":form
    }
    return render(request,'main/signup.html',context)

@login_required
def Readblog(request):
    query_set = models.Blog.objects.all()
    paginator = Paginator(query_set,10)

    page = request.GET.get('page',1)

    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    context = {
        "query_set":query_set,
        "users":users,
    }
    return render(request,'main/readblog.html',context)

@login_required
def Addblog(request):
    if request.method == "GET":
        form = forms.BlogForm()
    else: # POST request
        form = forms.BlogForm(request.POST)

        if form.is_valid():
            obj = form.save()
            #return HttpResponseRedirect(reverse('Index'))
            context={
                "obj" : obj,
            }
            return render(request, 'main/success.html',context)
            #return HttpResponse('Form added with id' + str(obj.pk))

    context = {
        'form': form
    }
    return render(request, 'main/addblog.html', context)

@login_required
def art(request,id):
    rest = get_object_or_404(models.Blog,pk=id)
  
    context={
        'blog':rest
    }
    return render(request,'main/art.html',context)






