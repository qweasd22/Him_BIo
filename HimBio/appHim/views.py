from django.shortcuts import render 
from django.views import View
from django.http import HttpResponseRedirect
from .forms import UserForm
from django.shortcuts import redirect




def index(request):
    return render(request, 'index/index.html')

def about(request):
    return render(request, 'index/about.html')

def faq(request):
    return render(request, 'index/faq.html')

def results(request):
    return render(request, 'index/results.html')

def form(request):
    userform = UserForm()
    return render(request, 'index/form.html')
def submit_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index/index.html')  # Страница с сообщением об успешной отправке
    else:
        form = UserForm()
    return render(request, 'index/index.html', {'form': form})
