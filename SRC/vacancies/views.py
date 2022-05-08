from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.template import RequestContext

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



def readcvbtn(request):
    cvdata = Cvdetails.objects.all()

    return render(request, 'CVpages/dil_preBtn.html', {'cvdata': cvdata})



def ogcreatehtml(request):

    form = CvDetailsForm()
    if request.method == 'POST':
        #print('',request.POST)
        form = CvDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/button')

    context = {'form':form}
    return render(request, 'CVpages/dilcvcreate.html', context)


def updatecv(request, pk):

    cvdata = Cvdetails.objects.get(id=pk)
    form = CvDetailsForm(instance = cvdata)

    if request.method == 'POST':
        form = Cvdetails(request.POST, instance = cvdata)
        if form.is_valid():
            form.save()
            return redirect('/button')

    context = {'form':form}
    return render(request, 'CVpages/dilcvcreate.html', context)


def deleteCv(request, pk):
    cvdata = Cvdetails.objects.get(id=pk)

    if request.method == 'POST':
            cvdata.delete()
            return redirect('/button')


    context = {'form':cvdata}
    return render(request, 'CVpages/dilcvdiscard.html', context)