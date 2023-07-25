from django.urls import path
from . import views

urlpatterns = [
    path('addTask/',views.addTask, name = 'addTask'),
    path('mark_as_done/<int:pk>/', views.mark_as_done, name='mark_as_done'), # we need to pass the pk, then only we will be able to fetch the data from the database using the primary key
    path('mark_as_not_done/<int:pk>/', views.mark_as_not_done, name='mark_as_not_done'),
    path('edit_task/<int:pk>/', views.edit_task, name='edit_task'),
    path('delete_task/<int:pk>/', views.delete_task, name='delete_task'),
]