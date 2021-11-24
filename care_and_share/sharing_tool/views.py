from django.shortcuts import render
from django.views import View

from sharing_tool.models import Institution, Donation


class LandingPage(View):
    def get(self,request):
        donations = Donation.objects.all()
        bags_count = 0
        for donation in donations:
            bags_count += donation.quantity
        organizations_count = Institution.objects.count()
        foundations = Institution.objects.filter(type=0)
        ngos = Institution.objects.filter(type=1)
        foundraisings = Institution.objects.filter(type=2)
        context = {'bags_count':bags_count,
                   'organizations_count':organizations_count,
                   'foundations':foundations,
                   'ngos':ngos,
                   'foundraisings':foundraisings,
                   }
        return render(request, 'sharing_tool/index.html', context)


class AddDonation(View):
    def get(self, request):
        return render(request, 'sharing_tool/form.html')


class Login(View):
    def get(self, request):
        return render(request, 'sharing_tool/login.html')


class Register(View):
    def get(self, request):
        return render(request, 'sharing_tool/register.html')


