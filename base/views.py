from ast import Delete
from asyncio import constants
from distutils.log import error
from ftplib import error_reply
from logging import ERROR
from msilib.schema import Error
from multiprocessing import AuthenticationError
from pyexpat import model
from time import time
from tkinter.tix import Form
from urllib import request
from django.forms import DurationField, PasswordInput
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from .forms import PositionForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User


from django.contrib.messages import constants as messages

from django.views.generic import View

# from django.http import HttpResponse 
from base.functions import handle_uploaded_file   

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
# Imports for Reordering Feature
from django.views import View
from django.shortcuts import redirect
from django.db import transaction
from requests import delete

from .models import Task
from datetime import datetime,time

MESSAGE_TAGS = {
    messages.INFO: '',
    50: 'error',
}


def index(request):
   return render(request,'index.html')

class mylist(LoginRequiredMixin, ListView):
    
    model = Task
    context_object_name = 'tasks1'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks1'] = context['tasks1'].filter(user=self.request.user)
        context['count'] = context['tasks1'].filter(complete=False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks1'] = context['tasks1'].filter(
                title__contains=search_input)

        context['search_input'] = search_input

        return context
    
  

""""
class LoginPageView(LoginView):
    template_name = 'base/login.html'
    form_class = UserCreationForm
    
    def get(self, request):
        form = self.form_class()
        message = 'username or passwords is incorrect'
        return render(request, self.template_name, context={'form': form, 'message': message})
        
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
            return redirect('login')
        message = 'Login failed!'
        return render(request, self.login, context={'UserCreationForm': form, 'username or password is incorrect': message})  
 """
 
class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            messages.error(request, 'username or password is incorrect')
            return redirect('login')
           # return redirect('login')
        
    
    def get_success_url(self):
        return reverse_lazy('tasks')
    
#333333333333333333333333333333

  
class RegisterPage(FormView):
    template_name = 'base/register.html'
    
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')
    error_message = "passwords don't match"
   # ERROR = 50
    
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            
            login(self.request, user)
        else :
             messages.error(request,'passwords dont match or does not contain recquired numeral or special character')
             messages.add_message(request,ERROR,'passwords dont match or does not contain recquired numeral or special character')
             
        
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        
      
        return super(RegisterPage, self).get(*args, **kwargs)
  
  
  
  
  
  
  
  
  
  
  
  
  
  
class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count1'] = context['tasks'].filter(complete=False).count()
        context['count2'] =context['tasks'].filter(complete=True).count()
       # context['count3'] = context['tasks'].filter(complete=False, time=tasks.end_time).count()
        

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(
                title__contains=search_input)

        context['search_input'] = search_input

        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'complete','start_time','duration','end_time','upload_file']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)
 

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'complete','start_time','duration','end_time','upload_file']
    success_url = reverse_lazy('tasks')


class DeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
    def get_queryset(self):
        owner = self.request.user
        return self.model.objects.filter(user=owner)
        



class TaskReorder(View):
    def post(self, request):
        form = PositionForm(request.POST)
        

        if form.is_valid():
            positionList = form.cleaned_data["position"].split(',')
            
            with transaction.atomic():
                self.request.user.set_task_order(positionList)
              

        return redirect(reverse_lazy('tasks'))


class TaskReorder1(View) :
    def post(self,request):
        form = PositionForm(request.POST)
        
        if form.is_valid():
           inputList = form.cleaned_data["input"].split(',')
           
           with transaction.atomic():
               self.request.user.set_task_order(inputList)
               
        return redirect(reverse_lazy('tasks'))
    
    
 
def index(request):  
    
    if request.method == 'POST':  
      form = PositionForm(request.POST, request.FILES)  
      if form.is_valid():  
            handle_uploaded_file(request.FILES['file'])  
            return HttpResponse("File uploaded successfuly")  
    else:  
         form = PositionForm() 
         return render(request,"task-create/",{'form':form})  


"""
def diff_in_time(start,end):
    startdelta=datetime.timedelta(hours=start.hour,minutes=start.minute,seconds=start.second)
    enddelta=datetime.timedelta(hours=end.hour,minutes=end.minute,seconds=end.second)
    diff_in_time(enddelta - startdelta)
    return (enddelta-startdelta).seconds/60

def get_overtime_hours(start_time, end_time) -> int:
    difference = end_time - start_time
    hours = difference.seconds/3600
    return hours






def my_leaves_view(request):
    
    model = Task
    form = PositionForm(request.POST)
    if form.is_valid():
        inst = form.save(commit=False)
        inst.duration = (Task.end_time - Task.start_time)
        inst.save()
        return redirect(reverse_lazy('tasks'))
    

"""
"""
def my_leaves_view(request):
    
    model = Task
    form = PositionForm(request.POST)
    if form.is_valid():
        inst = form.save(commit=False)
        end_time = time()
	    start_time = )
	    duration = end_time - start_time
	    print(duration.minutes)
       
        inst.duration = (Task.end_time - Task.start_time)
        inst.save()
        return redirect(reverse_lazy('tasks'))
"""

    
def chart(request):
    
      return render(
          request, 
         "base/piechart.html",
         {
            'labels': ['F', 'M'],
            'data': [52, 82],
            'colors': ["#FF4136", "#0074D9"]
            }

         )
 
	   
    



















