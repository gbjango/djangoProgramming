from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from .forms import RegisterForm, LoginForm
from .models import Dsuser
from django.contrib.auth.hashers import check_password, make_password

# Create your views here.

def index(request):
    return render(request, 'index.html', { 'username': request.session.get('user')})


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/'

    def form_valid(self, form):
        dsuser = Dsuser(
            username = form.data.get('username'),
            email=form.data.get('email'),
            password=make_password(form.data.get('password'))
        )
        dsuser.save()

        return super().form_valid(form)

class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        self.request.session['user'] = form.username
        return super().form_valid(form)

def logout(request):
    if 'user' in request.session:
        del(request.session['user'])

    return redirect('/')