from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.home,name='home'),
    path('newprofile/',views.profile,name ='profile'),
    path('showprofile/<id>',views.display_profile,name = 'showprofile'),
    path('image/', views.add_image, name='upload_image'),
    path('comment/(<image_id>)', views.comment, name='comment'),
    path('like/(<image_id>)', views.like, name='like'),
    path('messages/', views.messages, name='messages'),
    path('explore/', views.explore, name='explore'),
    path('search/',views.search, name='search'),
    path('follow/(<user_id>)', views.follow, name='follow'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('register/',views.register, name='registration'),
]