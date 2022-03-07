from django.urls import path 
from Apped import views

app_name = 'Apped'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('signup/', views.signup, name = 'signup'),
    path('login/', views.user_login, name = 'user_login'),
    path('logout/', views.user_logout, name='user_logout'),
]