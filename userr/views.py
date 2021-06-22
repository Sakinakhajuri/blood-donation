# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import PageForm,User,Message,Codeform

from .models import Register,search
# Create your views here.
from django.db.models import Q
from .forms import DonorSearch
from twilio.rest import Client
from .models import SearchLogo


def home (request):
    return render (request,'userr/dashboard.html')

def register(request):

    phone_number = request.session['phone_number']

    form = PageForm(request.POST or None)

    if form.is_valid() and request.POST.get('phone')==phone_number:
        #print(form.fields['phone'])
        #form.phone = phone_number
        form.save()
        request.session['phone_number'] = None
        form = PageForm
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









def searchdisplay(request):
    search_forms = DonorSearch()
    logo_img = SearchLogo.objects.get(logo_number=1)
    if request.method == 'POST':
        search_forms = DonorSearch(request.POST)
        if search_forms.is_valid():
            blood_group = search_forms.cleaned_data['blood_group']
            location = search_forms.cleaned_data['city']
            donor_filter = Register.objects.filter(blood_group=blood_group, area__icontains=location)
            context = {
                'donor_filter' : donor_filter
            }
            return render(request, 'userr/list.html', context)



    context = {
        'forms_search' : search_forms,
        'logo_img' : logo_img
    }
    return render(request, 'userr/search.html' ,context)



def donorlistdetail(request, email):
    email = email
    detail = Register()
    detail = Register.objects.get(email=email)
    context = {
        'details' : detail
    }
    return render(request, 'userr/information.html', context)



def display(request):
    display = Register.objects.all()
    return render(request,"userr/view.html",{"display":display})


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

#def addUser(request):
    #form =Registration(request.post)

    #if form.is_valid():
      #  reg= Register(name =form.cleaned_data['name'])
     #   reg.save()
    #return redirect('home')

