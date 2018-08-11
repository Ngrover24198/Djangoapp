from django.http import HttpResponse, Http404 ,HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.db.models import Avg
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from . import models
from . import forms

# Create your views here.

@login_required
def index(request):
    context = {}
    return render(request, 'main/index.html', context)

@login_required
def restaurants(request):
    query_set = models.Restaurant.objects.all()

    query_set = query_set.annotate(average_rating = Avg('review__rating')).order_by('-average_rating')

    context = {
        "query_set": query_set,
    }
    return render(request, 'main/restaurants.html', context)

@login_required
def add_restraunt(request):
    if request.method == "GET":
        form = forms.RestaurantForm()
    else: # POST request
        form = forms.RestaurantForm(request.POST)

        if form.is_valid():
            obj = form.save()
            return HttpResponse("Form Added with id " + str(obj.pk))

    context = {
        'rest_form': form
    }
    return render(request, 'main/addRestaurant.html', context)

@login_required
def restaurant(request, id):
    rest = get_object_or_404(models.Restaurant, pk = id)

    # try:
    #     rest = models.Restaurant.objects.get(pk = id)
    # except:
    #     raise Http404()
    success = False
    
    #Handling the form
    if request.method == 'GET':
        form = forms.ReviewForm()
    else: #post request
        form = forms.ReviewForm(request.POST)
        if form.is_valid():
            obj = form.save(commit = False)
            obj.restaurant = rest
            obj.save()

            success = True
            form = forms.ReviewForm()


    context = {
      'restaurant' : rest,
      'form' : form,
      'success': success,
    }
    return render(request,'main/restaurant.html',context)

def login_view(request):
    if request.method == 'GET':
        form = forms.LoginForm()
    else:
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request,username = username, password = password)
            if user:
                login(request,user)

                try:
                    return HttpResponseRedirect(request.GET['next'])
                except:
                    return HttpResponseRedirect(reverse('index'))
    context = {
    "form": form,
    }
    return render(request,'main/login.html',context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def signup_view(request):
    if request.method == 'GET':
        form = UserCreationForm()
    else:
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
    "form":form,
    }                
    return render(request,'main/signup.html',context) 


@login_required
def review(request,id):
    obj = get_object_or_404(models.Review, pk = id)

    context = {
        'review': obj
    }
    return render(request, 'main/review.html', context)