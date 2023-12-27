from django.shortcuts import render
from django.views import View

class ppolicy(View):
    def get(self, request):
        return render(request, 'privacypolicy.html')