from datetime import date,timedelta
from django.db.models import Q
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.utils.dateparse import parse_date

from .forms import PageForm,User,Message,Codeform,UpdateDonate,UpdateLoc
from django.contrib import messages
from twilio.rest import Client

from .models import Register,search


def home (request):
    return render (request,'userr/dashboard.html')

def register(request):
    phone_number = request.session['phone_number']

    form = PageForm(request.POST or None)

    if form.is_valid() and request.POST.get('phone')==phone_number:
        #d1=date.today()
        #d2=request.POST.get('last_blood_donated_date')
        #d3:date=parse_date(d2)
        #print(d1)
        #print(d3)
        #print((d1-d3).days)

        form.save()

        request.session['phone_number'] = None
        form = PageForm

        messages.success(request,"Registered Successfully")
    else:
        form = PageForm(initial={'phone':phone_number})

    return render(request, "userr/register.html", {"form": form})


def otp(request):
    message=''
    if request.method=="POST":

        otpForm=Codeform(request.POST or None)

        if otpForm.is_valid():


            account_sid = 'AC4749e4f65c31c531046affb434fedaec'
            auth_token = '9c16f8a72ecd32088821dd0870b3049d'
            client = Client(account_sid, auth_token)
            otp = request.POST.get('otp')
            phone_number = request.POST.get('mobile')
            request.session['phone_number'] = phone_number
            print(phone_number)
            print(otp)
            if otp:
                verification_check = client.verify \
                    .services('VA925a3c834a4b3155c470b13671ecf275') \
                    .verification_checks \
                    .create(to=phone_number, code=otp)
                # approved
                message=verification_check.status
                print(message)
            else:
                verification = client.verify \
                    .services('VA925a3c834a4b3155c470b13671ecf275') \
                    .verifications \
                    .create(to=phone_number, channel='sms')
                message="OTP Sent"
            if message=="approved":

                return redirect('http://127.0.0.1:8000/register/reg/')

    else:

        otpForm=Codeform()
    return render(request,"userr/otp.html",{'otpForm':otpForm,'message':message})

def searches(request):
    if request.method=="POST":
        form = User(request.POST or None)
        if form.is_valid():
            form.save()
            d2= timedelta(days=90)
            d1 = date.today()
            d3=d1-d2
            print(d3)

            bg=request.POST.get('required_blood_group')
            pin=request.POST.get('pincode')
            qs1=Q(last_blood_donated_date__isnull=True)
            qs2 =Q(last_blood_donated_date__lte=d3)
            qs3=Q(blood_group=bg)
            qs4=Q(pincode=pin)
            query=Register.objects.filter(((qs1 | qs2) & qs3) &qs4)

            return render(request,'userr/list.html',{'registers':query})




    else:

        form=User()
    return render(request,"userr/search.html",{"form":form})

def update(request):
    return render(request, 'userr/update.html')

def updatedonate(request):
    message=""
    if request.method=="POST":
        uform = UpdateDonate(request.POST or None)
        if uform.is_valid():
            name1=request.POST.get('name')
            an=request.POST.get('aadhar_no')
            try:
                t=Register.objects.get(name=name1,aadhar_no=an)
                t.last_blood_donated_date=request.POST.get('new_donated_date')
                t.save()
                messages.success(request,"updated Successfully")
                message="Updated successfully"

            except Register.DoesNotExist:
                t=None
                message="Invalid name or aadhar number"



    else:
        uform = UpdateDonate()
    return render(request, "userr/updatedonate.html", {"uform":uform,"message":message})


def updateloc(request):
    message=""
    if request.method=="POST":
        locform = UpdateLoc(request.POST or None)
        if locform.is_valid():
            name1=request.POST.get('name')
            an=request.POST.get('aadhar_no')
            try:
                t = Register.objects.get(name=name1, aadhar_no=an)
                t.area = request.POST.get('updated_area')
                t.city = request.POST.get('updated_city')
                t.pincode = request.POST.get('updated_pincode')
                t.save()
                messages.success(request, "updated Successfully")
                message = "Updated successfully"

            except Register.DoesNotExist:
                t = None
                message="Invalid name or aadhar number"


    else:
        locform = UpdateLoc()
    return render(request, "userr/updateloc.html", {"locform": locform,"message":message})

def contact(request):
        if request.method == "POST":
            form = Message(request.POST or None)
            if form.is_valid():
                form.save()
                form = Message
                #messages.success(request, "Registered Successfully")


        else:

            form = Message()
        return render(request, "userr/contact.html", {"form": form})


def about(request):
    return render (request,'userr/about.html')



