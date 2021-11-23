from django.shortcuts import render
from django.views import View

class LandingPage(View):
    def get(self,request):
        return render(request, 'sharing_tool/index.html')


class AddDonation(View):
    def get(self, request):
        return render(request, 'sharing_tool/form.html')


class Login(View):
    def get(self, request):
        return render(request, 'sharing_tool/login.html')


class Register(View):
    def get(self, request):
        return render(request, 'sharing_tool/register.html')


