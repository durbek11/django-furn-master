from django.urls import path
from django.contrib.auth.views import LoginView , LogoutView
from .views import *

app_name = "furn"

urlpatterns = [
    path('',home, name="home"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path("<int:pk>/detalis/", arrivals_detail, name="arrivals_detal"),
    path("signup/", signup, name="signup"),
    path('profile/', profile, name="profile"),
    path('submit-succses/', SuccsesView.as_view(), name="succses"),
    path("start-<int:pk>-product/", star, name="star"),
    path("rate-check/", rate_check, name="rate_check")
]
