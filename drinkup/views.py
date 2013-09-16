from django.template import loader, Context
from django.shortcuts import render
from django.http import HttpResponse

def base(request):
  posts = Post.objects.all()
  t = loader.get_template("base.html")
  c = Context ({ 'posts': posts })
  return HttpResponse(t.render(c))

def view_base(request):
  return render(request, 'base.html')

def view_about(request):
  return render(request, 'about.html')

def view_past(request):
  return render(request, 'past.html')