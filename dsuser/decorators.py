from django.shortcuts import redirect
from .models import Dsuser

def login_required(function):
    def wrap(request, *args, **kwargs):
        user = request.session.get('user')
        if user is None or not user:
            return redirect('/user/login')
        return function(request, *args, **kwargs)

    return wrap