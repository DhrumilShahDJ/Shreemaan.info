from django.http import HttpResponse
from django.views import View
from django.shortcuts import render

# Create your views here.

class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        return HttpResponse('post')
    
def about_us(request):
    return render(request, 'about_us.html')