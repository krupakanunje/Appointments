from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from doctorApp.models import family_doc,pd_doc,Contact,booking,p_name,f_name
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from datetime import datetime


# Create your views here.
def index(request):
    return render(request,'start.html')
    #return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    if request.method== "POST":
        name=request.POST.get('name')
        print(name)
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        #date=request.POST.get('date')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,dates=datetime.today())
        contact.save()
        messages.success(request, 'message sent succefully!')

    return render(request,'contact.html')
def loginInd(request):
    if request.user.is_anonymous:
        return render(request,'loginInd.html')
    return redirect("/loginIN")
    
#from django.contrib.auth import authenticate
    
def loginIN(request):
    if request.method == "POST":
       username=request.POST.get('username')
       password = request.POST.get('password') 
       user = authenticate(request,username=username, password= password)
       if user is not None:
           if username=="admin" and password=="admin":
                  return redirect("/admin")
           else:
                login(request, user)
                return redirect("/index")
        # A backend authenticated the credentials
       else:
         # No backend authenticated the credentials
           return  render(request,'login.html')
    return  render(request,'login.html')
def logOut(request):
    logout(request)
    return render(request,'login.html')        
def regist(request):
    return render(request,'register.html')
def newUser(request):
    if request.method=="POST":
      username=request.POST.get('username')
      password = request.POST.get('password') 
      user= User.objects.create_user(username= username, password= password)
      return redirect("/")
    return render(request,'register.html')
def fd_avl(request):
     fd=f_name.objects.all()
     return render(request,'select_fd.html',{'fd':fd})
def fd_get(request):
        if request.method=="POST":
            dc= request.POST.get('dc_name')
            print(dc)
            fd=family_doc.objects.filter(dc_name=dc)
            funq=family_doc.objects.values('dc_name').distinct()
            #print(fd.aval_timing)
            return render(request,'getsz.html',{'fd':fd,'funq':funq})
def pd_avl(request):
    cd = p_name.objects.all()
    return render(request,'select_cd.html',{'cd':cd})
def pd_get(request): 
    if request.method=="POST":
            dc= request.POST.get('dc_name')
            print(dc)
            cd=pd_doc.objects.filter(dc_name=dc)
            print(cd)
            funq=pd_doc.objects.values('dc_name').distinct()
            return render(request,'getpd.html',{'cd':cd,'funq':funq})

def dignos(request):
    return render(request,'vRegular.html')
def counsult(request):
    return render(request,'vSquare.html')
def admit(request):
    return render(request,'vRegSml.html')
def nicu(request):
    return render(request,'cRegular.html')

     
 
def Appointment(request):
    #pz_name='plain cheese'
    if request.method== "POST":
        
        aval_timing=request.POST.get('aval_timing')
        Patient_name=request.POST.get('Patient_name')
        contact_no=request.POST.get('contact_no')
        dc_name1=request.POST.get('dc_name1')
        #dc_name1=request.POST.get('dc_name1')
        print(aval_timing)
        #date_object = datetime.strptime(aval_timing, "MMM. MM,yyyy, ZZZ a")
        #print(date_object)
        book=booking(dc=dc_name1,aval_timing=aval_timing,Patient_name=Patient_name,contact_no=contact_no)
        book.save()
        return render(request,'booked.html',messages.success(request, 'Appointment booked succefully!'))
        #messages.success(request, 'Appointment booked succefully!')
       

    return render(request,'getsz.html') 

def csAppointment(request):
    #pz_name='plain cheese'
    if request.method== "POST":
        
        aval_timing=request.POST.get('aval_timing')
        Patient_name=request.POST.get('Patient_name')
        contact_no=request.POST.get('contact_no')
        dc_name1=request.POST.get('dc_name1')
        #dc_name1=request.POST.get('dc_name1')
        print(dc_name1)
        book=booking(dc=dc_name1,aval_timing=aval_timing,Patient_name=Patient_name,contact_no=contact_no)
        book.save()
        return render(request,'booked.html',messages.success(request, 'Appointment booked succefully!'))
       

    return render(request,'getsz1.html')     
    
    