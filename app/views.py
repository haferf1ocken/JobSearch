"""
Definition of views.
"""

from django.template.context_processors import csrf
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.template import loader
from django.contrib import auth


def home(request):
    template = loader.get_template('app/index.html')
    context = {
        'users': User.objects.all(),
        'interships': Intership.objects.all(),
        'username': auth.get_user(request).username
    }
    return HttpResponse(template.render(context, request))  # возвращает страничку, делает подгрузку бд


def getinfoUser(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/login")
    template = loader.get_template('app/user.html')
    context = {
        'users': User.objects.all()
    }
    print(context)
    if request.method == "POST":
        postinfoUser(request)
        return HttpResponseRedirect("/user")
    return HttpResponse(template.render(context, request))


def getinfoEmployer(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/login")
    template = loader.get_template('app/employer.html')
    context = {
        'employers': Employer.objects.all()
    }
    if request.method == "POST":
        postinfoEmployer(request)
        return HttpResponseRedirect("/employer")
    return HttpResponse(template.render(context, request))


def getinfoIntership(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/login")
    template = loader.get_template('app/interships.html')
    context = {
        'interships': Intership.objects.all(),
        'employers': Employer.objects.all(),
        'users': User.objects.all()
    }
    print(context)
    if request.method == "POST":
        postinfoIntership(request)
        return HttpResponseRedirect("/interships")
    return HttpResponse(template.render(context, request))


def postinfoUser(request):
    print("add new user")
    user = User()
    user.fullname = request.POST.get("user_name")
    user.education = request.POST.get("user_education")
    user.experience = request.POST.get("user_experience")
    user.summary = request.FILES["user_summary"]
    user.save()


def postinfoEmployer(request):
    print("add new employer")
    employer = Employer()
    employer.name = request.POST.get("employer_name")
    employer.address = request.POST.get("employer_address")
    employer.save()


def postinfoIntership(request):
    print("add new intersip")
    intership = Intership()
    intership.name = request.POST.get("intership_name")
    intership.experience = request.POST.get("intership_experience")
    intership.company = Employer.objects.get(name=request.POST.get("intership_employer id"))
    intership.user = User.objects.get(fullname=request.POST.get("intership_user id"))
    intership.save()


def login(request):
    template = loader.get_template('app/login.html')
    context = {}
    context.update(csrf(request))
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect("/")
        else:
            context['login_error'] = "Пользователь не найден"
            return HttpResponse(template.render(context, request))
    else:
        return HttpResponse(template.render(context, request))


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")
