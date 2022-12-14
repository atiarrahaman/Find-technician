from django.shortcuts import render,redirect
from  django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from .forms import SignupForm ,ProfileForm,LoginForm,ProfileFormTutor
from .models import Profile ,User
from .filters import MistriFilter,toutorFilter
from django.db.models import Q

from django.core.paginator import Paginator
# Create your views here.









def Search(request):
    query=request.POST.get('search','')
    if query:
        queryset = (Q(skill__icontains=query)) | (Q(add_more_skill__icontains=query))
                       
        results=Profile.objects.filter(queryset).distinct()
    else:
        results=[]
    context={
        'results':results
    }
    return render (request,'search.html',context)
    




def Home(request):
    alldata=Profile.objects.filter(aggre=True).order_by('-id')
    q=MistriFilter(request.GET ,queryset=alldata)
    alldata=q.qs
    paginator = Paginator(alldata, 6) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)      
    
    context={'q':q ,'page_obj':page_obj }
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
            elif user is not None and user.is_tutor:
                login(request,user)
                return redirect('tutorprofile')
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
    if request.user.is_authenticated and request.user.is_mistri :
        fm=Profile.objects.filter(user=request.user)
        context={'form':fm}
        return render(request,'mistriprofile.html',context)
    else:
        return redirect('home')

def EditProfile(request):
    if request.user.is_authenticated and request.user.is_mistri:
        if request.method =='POST':
          ed=Profile.objects.get(user=request.user)
          fm=ProfileForm(request.POST,request.FILES,instance=ed)
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
   if request.user.is_authenticated:
     details=Profile.objects.get(id=id)
    
     context={'details':details}
     return render(request,'detailsprofile.html',context)
   else:
    return redirect('login')


def TutorProfile(request):
    if request.user.is_authenticated and request.user.is_tutor :
        fm=Profile.objects.filter(user=request.user)
        context={'form':fm}
        return render(request,'tutorprofile.html',context)
    else:
        return redirect('home')


def TutorProfileEdit(request):
    if request.user.is_authenticated and request.user.is_tutor:
        if request.method =='POST':
          ed=Profile.objects.get(user=request.user)
          fm=ProfileFormTutor(request.POST,request.FILES,instance=ed)
          if fm.is_valid():
            fm.save()
            return redirect('tutorprofile')
        else:
            ed=Profile.objects.get(user=request.user)
            fm=ProfileFormTutor(instance=ed)
        context={'form':fm}
        return render(request,'tutoreditprofile.html',context)
    else:
        return redirect('home')



def TutorShow(request):

    tutorshow=Profile.objects.filter(tutor=True).order_by('-id')
    
    tq=toutorFilter(request.GET ,queryset=tutorshow)
    tutorshow=tq.qs
    context={'tutorshow':tutorshow,'tq':tq}
    return render(request,'tutorshow.html',context)



def TutorDetials(request,id):
    if request.user.is_authenticated:
       tutordetails=Profile.objects.get(id=id)
       contexts={'td':tutordetails}
       return render(request,'tutordetails.html',contexts)
    else:
        return redirect('login')
  