from django.urls import path
from .views import my_login,my_signup
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path("login",csrf_exempt( my_login.as_view()),name="login"),
    path("signup",csrf_exempt( my_signup.as_view()),name="signup"),
    
]