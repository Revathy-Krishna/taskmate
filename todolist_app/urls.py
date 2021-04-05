from .import views
from django.urls import path

app_name = 'todolist_app'

urlpatterns = [
    path('', views.todolist, name='todolist'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),

]
