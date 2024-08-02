from django.shortcuts import render
from django.http import HttpResponse
from app1.models import *
# Create your views here.
def insert_Webpage(request):
    d=Topic.objects.all()
    q=Webpage.objects.all()
    l=AccessRecord.objects.all()
    v={'topic':d,'webpage':q,'accessrecord':l}
    return render(request,'h1.html',v)