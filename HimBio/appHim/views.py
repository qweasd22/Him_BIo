from django.shortcuts import render 
from django.views import View
from .forms import RecordForm
from django.shortcuts import redirect

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
    
from .models import Record

def home(request):
    records = Record.objects.all()
    return render(request, 'index.html', {'records': records})

def record_create(request):
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            new_record = form.save(commit=False)
            new_record.user = request.user
            new_record.save()
            return redirect('home')
    else:
        form = RecordForm()
    return render(request, 'record_form.html', {'form': form})

from django.core.mail import send_mail

def send_notification(request):
    subject = 'Новая запись пользователя'
    message = 'Пользователь {} создал новую запись'.format(request.user.username)
    recipient_list = ['koltsov-main@mail.ru']
    send_mail(subject, message, 'noreply@example.com', recipient_list)

    return redirect('home')