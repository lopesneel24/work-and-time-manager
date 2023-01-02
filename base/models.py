from distutils.command.upload import upload
from enum import auto
from django.db import models
from django.contrib.auth.models import User
from numpy import True_
# Create your models here.
#from .views import get_overtime_hours

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    start_time       =     models.TimeField(default=False,blank=False,null=False)
    duration         =     models.DurationField()
    end_time         =     models.TimeField(default=False,blank=False,null=False)
    upload_file      =     models.FileField(default=False,blank=False,null=False)


    
"""
def diff_in_time(start_time,end_time):
        duration = end_time - start_time 
        return duration


{{%
from asyncio import tasks
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


print("\n")
while{{task}}:
    print("Enter  the tasks at the index :", i,)
    item = str(input())
    list.append(item)



colors=['blue', 'Red','yellow', 'green', 'orange']
labels=['personal','work','self', 'other']

{{plt.pie(number_list,labels=list, colors=colors, startangle=90, autopct='%1.1f%%')}}


plt.axis('equal')

{{plt.show()}} %}}




"""
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        


    
    
   # out = models.TimeField(null=False, help_text="When the cow went OUT")
   # _in = models.TimeField(null=False, help_text="When the cow got back IN")

   # def duration(self):
       # return self.out - self._in

    #def __str__(self):
        # return self.title 


class Meta:
       order_with_respect_to = 'user'

"""
    def duration(self):
        hours = get_overtime_hours(self.out, 
                self._in)
        return round(hours) 

#class taso(models.Model):
  
   # delete = models.BooleanField(default=False)
  
 """