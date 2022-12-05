from django.shortcuts import render,redirect
from  django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from .forms import SignupForm ,ProfileForm,LoginForm
from .models import Profile ,User
# Create your views here.



def Home(request):
    alldata=Profile.objects.all()
    context={'alldata':alldata}
    return render (request,'home.html',context)

def Signup(request):
   if request.user.is_authenticated:
     return redirect('home')
    
   else:
       if request.method == 'POST':
         fm=SignupForm(request.POST)
         if fm.is_valid():
            fm.save()
            return redirect('login')
       else:
        fm=SignupForm()
       context={'form':fm}
       return render(request,'signup.html',context)


def Login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
          fm= LoginForm(request=request, data=request.POST)
          if  fm.is_valid():
            username=fm.cleaned_data['username']
            password=fm.cleaned_data['password']
            user=authenticate(username=username,password=password)
            if user is not None and user.is_mistri:
                login(request,user)
                return redirect('mistriprofile')
            elif user is not None and user.is_customer:
                login(request,user)
                return redirect('home')
            elif user is not None:
                login(request,user)
                return redirect('home')
        else:
          fm=LoginForm
        context={'form':fm}
        return render (request,'login.html',context)




def Logout(request):
    logout(request)
    return redirect('login')

def MistriProfile(request):
    if request.user.is_authenticated and request.user.is_mistri:
        fm=Profile.objects.filter(user=request.user)
        context={'form':fm}
        return render(request,'mistriprofile.html',context)
    else:
        return redirect('home')

def EditProfile(request):
    if request.user.is_authenticated and request.user.is_mistri:
        if request.method =='POST':
          ed=Profile.objects.get(user=request.user)
          fm=ProfileForm(request.POST,instance=ed)
          if fm.is_valid():
            fm.save()
            return redirect('mistriprofile')
        else:
            ed=Profile.objects.get(user=request.user)
            fm=ProfileForm(instance=ed)
        context={'form':fm}
        return render(request,'editprofile.html',context)
    else:
        return redirect('home')

def DetailsProfile(request,id):
    details=Profile.objects.get(id=id)
    
    context={'details':details}
    return render(request,'detailsprofile.html',context)