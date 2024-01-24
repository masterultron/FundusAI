from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

# Create your views here.

def index(request):
    return redirect('login')


class LoginView(View):
    def get(self, request):
        return render(request, 'authentication/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        # if username and password:
        #     user = auth.authenticate(username=username, password=password)

        #     if user:
        #         if user.is_active:
        #             auth.login(request, user)
        #             messages.success(request, 'Welcome, ' +
        #                              user.username.upper()+' you are now logged in')
        #             return redirect('/')
        #         messages.error(
        #             request, 'Account is not active,please check your email')
        #         return render(request, 'authentication/login.html')
        #     messages.error(
        #         request, 'Invalid credentials,try again')
        #     return render(request, 'authentication/login.html')

        # messages.error(
        #     request, 'Please fill all fields')
        # return render(request, 'authentication/login.html')


        messages.success(request, 'Welcome, Dr. ' + username.upper()+' you are now logged in')
        return redirect('/diagnosis', {'username': username})


class LogoutView(View):
    def post(self, request):
        # auth.logout(request)
        messages.success(request, 'You have been logged out')
        return redirect('login')
