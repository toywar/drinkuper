from django.template import loader, Context
from django.shortcuts import render
from django.http import HttpResponse
from drinkup.models import PassedDrinkup, RequestDrinkup

def past_passed_view(request):
    posts = PassedDrinkup.objects.all()
    t = loader.get_template("past.html")
    c = Context({ 'posts': posts })
    return HttpResponse(t.render(c))

def base_passed_view(request):
    drinks = PassedDrinkup.objects.all()
    b = loader.get_template("base.html")
    a = Context({ 'drinks': drinks })
    return HttpResponse(b.render(a))

def base_request_drinkup(request):
    reqs = RequestDrinkup.objects.all()
    f = loader.get_template("base.html")
    g = Context({ 'reqs': reqs })
    return HttpResponse(f.render(g))

def view_about(request):
  return render(request, 'about.html')