import random
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    num = None
    some_list = [random.randint(0,100000),
                 random.randint(0,100000),
                 random.randint(0,100000)
                 ]
    condition_bool_item = True
    if condition_bool_item:
        num = random.randint(0,100000)
    context = {"num": num,
               "some_list" : some_list}
    return render(request,'home.html',context)#response


def tables(request):
    context = {

    }
    return render(request,'tables.html',context)#response


def queries(request):
    context = {

        }
    return render(request,'queries.html', context)#response


def forms(request):
    context = {

        }
    return render(request,'forms.html', context)#response

def reports(request):
    context = {

        }
    return render(request,'reports.html', context)#response