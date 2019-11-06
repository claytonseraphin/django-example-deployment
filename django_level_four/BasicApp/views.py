from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from forms import UserForm, UserProfileInfoForm

#

from django.contrib.auth import  authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'basic_app/index.html')
@login_required
def special(request):
    return HttpResponse("You are logged in!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def base(request):
    return render(request, 'basic_app/base.html')

def other(request):
    return render(request, 'basic_app/other.html')

def relative(request):
    return render(request, 'basic_app/relative_urls_templates.html')

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        userProfile_infoForm = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and userProfile_infoForm.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = userProfile_infoForm.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                print('Found It !')
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True
        else:
            print(user_form.errors, userProfile_infoForm.errors)

    else:
        user_form = UserForm()
        userProfile_infoForm = UserProfileInfoForm()

    return render(request, 'basic_app/register.html',
                {'user_form': user_form,
                'profile_form': userProfile_infoForm,
                'registered':registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Someone tried to login and failed!")
            print("Username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login details suppplied!")
    else:
        return render(request, 'basic_app/login.html',{})
