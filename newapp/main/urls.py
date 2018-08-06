from django.urls import path

from . import views

urlpatterns = [
    path('', views.Index ,name='Index'),
    path('login/', views.login_view, name = 'login'),
    path('logout/', views.logout_view, name = 'logout'),
    path('signup/',views.signup_view, name = 'signup'),
    path('readblog/',views.Readblog, name='readblog'),
    path('addblog/',views.Addblog, name = 'addblog'),
    path('success/',views.Addblog, name = 'success'),
    path('art/<int:id>',views.art,name = 'art'),
]
