from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView,LogoutView

app_name = 'furn'

urlpatterns = [
    path('', home, name="home"),
    path('signup', signup, name='signup'),
    path('<int:pk>/details/', arrivals_detail, name='arrival_detail',),
    path('login/', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(),name='logout')
]
 