from .views import LogoutView, LoginView, index
from django.urls import path
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('', index, name="index"),
    path('login', LoginView.as_view(), name="login"),
    path('logout', LogoutView.as_view(), name="logout"),
]
