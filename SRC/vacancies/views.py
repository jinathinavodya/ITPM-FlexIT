from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import vacancyform
from .models import *

# Create your views here.

#def cvacancy(request):
    #return render(request, 'vacancies/cvacancy.html')

def jrecuriting(request):

    vacan = vacancy.objects.all()

    return render(request, 'vacancies/jrecuriting.html', {'vacan':vacan})
    # return render(request, 'vacancies/jrecuriting.html')

def uvacancy(request):
    return render(request, 'vacancies/uvacancy.html')

def deletecon(request):
    return render(request, 'vacancies/deletecom.html')



def cvacancy(request):

    form = vacancyform()
    if request.method == 'POST':
        #print('printing POST:', request.POST)
        form = vacancyform(request.POST)
        if form.is_valid():
                form.save()
                return redirect('jrecruiting')
        


    context = {'form':form}

    return render(request, 'vacancies/cvacancy.html',context)


def updateComVa(request, pk):

    vacan = vacancy.objects.get(id=pk)
    form = vacancyform(instance=vacan)

    if request.method == 'POST':
        #print('printing POST:', request.POST)
        form = vacancyform(request.POST, instance=vacan)
        if form.is_valid():
                form.save()
                return redirect('jrecruiting')

    context = {'form':form}
    return render(request, 'vacancies/cvacancy.html',context)


def deleteComVa(request, pk):
    vacan = vacancy.objects.get(id=pk)
    if request.method == "POST":
        vacan.delete()
        return redirect('jrecruiting')

    context = {'item':vacan}
    return render(request, 'vacancies/deletecom.html', context)


