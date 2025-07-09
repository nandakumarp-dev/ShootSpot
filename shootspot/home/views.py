from django.shortcuts import render
from django.views import View

# Create your views here.


class LandingPageView(View):

    def get(self,request,*args,**kwargs):

        return render(request,'landing_page.html')