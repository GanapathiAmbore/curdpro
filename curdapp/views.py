from django.shortcuts import render
from curdapp.models import HallTicket
def home(request):
    return render(request,'home.html')

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def faqs(request):
    return render(request,'faqs.html')

def search(request):
    return render(request,'search.html')

def students(request):
    students=HallTicket.objects.all()
    return render(request,'students.html',{"students":students})
