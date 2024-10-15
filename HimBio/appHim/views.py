from django.shortcuts import render 
from django.views import View

def index(request):
    return render(request, 'index/index.html')

def about(request):
    return render(request, 'index/about.html')

def faq(request):
    return render(request, 'index/faq.html')

def results(request):
    return render(request, 'index/results.html')

class LessonView(View):
    def get(self, request):
        context = {}
        return render(request, 'lesson.html', context)