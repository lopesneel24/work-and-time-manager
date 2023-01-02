from django import forms
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.models import User, auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
# from .forms import ContactForm



def register(request) :
   
   if request.method == 'POST':
       fname = request.POST['fname']
       email = request.POST['email']
       age = request.POST['password']
       pwd = request.POST['confirm_password']
       
      
       if age != pwd:
           messages.error(request, '*passwords dont match')
          
             
      
      
       elif age == pwd:
             if   User.objects.filter(email=email).exists():
                   messages.error(request,'credential email already exists')
                  
               
           
       else :
       
            user = User.objects.create_user(name=fname,password=pwd,email=email)
            user.save();
            messages.success(request,'registered successfully')
       
       return redirect('/')
  
   else :
         
   
   
        return redirect(request,'register.html')
     