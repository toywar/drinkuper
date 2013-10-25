# -*- coding: utf-8 -*-
from django.template import loader, Context
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from drinkup.models import PassedDrinkup, RequestForm

def past_passed_view(request):
    posts = PassedDrinkup.objects.all()
    t = loader.get_template("past.html")
    c = Context({ 'posts': posts })
    return HttpResponse(t.render(c))

def base_page(request):
    all_ok = ''
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            all_ok = u'Your request have been send!'
            form = RequestForm()
    else:
        form = RequestForm()
    return render(request, 'base.html', {
            'form': form,
            'all_ok': all_ok,
        })

#def base_request_drinkup(request):
#    reqs = RequestDrinkup.objects.all()
#    f = loader.get_template("base.html")
#    g = Context({ 'reqs': reqs })
#    return HttpResponse(f.render(g))

def view_about(request):
  return render(request, 'about.html')

#def view_temp(request):
#    all_ok = ''
#    if request.method == 'POST':
#        form = RequestForm(request.POST)
#        if form.is_valid():
#            form.save()
#            all_ok = u'Your request have been send!'
#            form = RequestForm()
#    else:
#        form = RequestForm()
#    return render(request, 'base.html', {
#        'form': form,
#        'all_ok': all_ok,
#    })