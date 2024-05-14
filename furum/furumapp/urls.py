from django.urls import path

from . import views

urlpatterns = [
    path('', views.Home_View, name='home'),
    path('login/', views.sign_in, name='login'),
    path('logout/', views.sign_out, name='logout'),
    path('register/', views.sign_up, name='register'),
    path('posts/<str:topic>/', views.Posts_View, name='posts'),
    path('post/<str:post_id>/', views.Post_Details, name='postdetails')
]