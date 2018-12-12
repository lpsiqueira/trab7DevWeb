from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from projeto import settings
from django.shortcuts import redirect

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.login_url = getattr(settings, 'LOGIN_URL')

    def __call__(self, request):
        if request.path != self.login_url and not request.user.is_authenticated:
            return HttpResponseRedirect(self.login_url)
        else:            
            return self.get_response(request)
        