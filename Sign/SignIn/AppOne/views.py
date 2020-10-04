from django.shortcuts import render
from AppOne.models import UserProfile
from AppOne.forms import UserForm,Usr_Profile_Form
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect , HttpResponse
from django.urls import reverse_lazy, reverse

# Create your views here.
def index(request):
    return render(request,'AppOne/Index.html')


def register(request):
    #pass
    registered=False
    if request.method =='POST':
        reg=UserForm(request.POST)
        profile_form=Usr_Profile_Form(data=request.POST)

        if reg.is_valid() and profile_form.is_valid():
            user=reg.save()
            user.set_password(user.password)
            user.save()

            profile=profile_form.save(commit=False)
            profile.user=user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
        else:
            print(reg.errors,profile_form.errors)
    else:
        reg=UserForm()
        profile_form=Usr_Profile_Form()
    return render(request,'AppOne/Register.html', context={'reg':reg,'profile_form':profile_form,'registered':registered})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def special(request):
    #return HttpResponse('You logged in')
    return render(request,'AppOne/profile.html',{})

def user_login(request):

    #pass
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('special'))
            else:
                HttpResponse('Accoount not Active')

        else:
            print('some Failled in log in')
            print('username: {} and password: {}'.format(username,password))
            return HttpResponse('invalid')
    else:
        return render (request,'AppOne/Login.html',{})

