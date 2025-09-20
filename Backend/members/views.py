from django.shortcuts import render
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from .models import Member

def members(request):
    mymembers=Member.objects.all().values()
    template=loader.get_template("index.html")
    context={
        'mymembers':mymembers,
    }
    return HttpResponse(template.render(context,request))
def details(request,id):
    mymember=Member.objects.all().values()
    print(mymember)
    template=loader.get_template("details.html")
    context={
        "mymember":mymember,
    }
    return HttpResponse(template.render(context,render))
def main(request):
    template=loader.get_template('main.html')
    return HttpResponse(template.render())