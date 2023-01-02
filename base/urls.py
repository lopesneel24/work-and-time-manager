from unicodedata import name
from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate,TaskUpdate, DeleteView,CustomLoginView,TaskReorder,RegisterPage, chart,mylist,TaskReorder1,chart
from django.contrib.auth.views import LogoutView
from .views2 import register
from . import views


urlpatterns = [
    # path('',index, name="index"),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('login/login/',CustomLoginView.as_view(), name='login'),
   # path('login/mylist',mylist.as_view,name='mylist'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
   # path('register.html',views2.register1,name = "register1"),
   # path('register/', views2.register, name='register'),

    path('', TaskList.as_view(), name='tasks'),
    path('tasks-mylist/', mylist.as_view,name='tasks1'),
  # path('tasks-mylist/',mylist.as_view,name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', DeleteView.as_view(), name='task-delete'),
    path('task-reorder/', TaskReorder.as_view(), name='task-reorder'),
    path('task-reorder1/', TaskReorder1.as_view(), name='task-reorder1'),
    path('login/register',register),
    path('tasks-chart/',chart, name = 'chart'),
    
]
