from django.shortcuts import render, redirect
from django.http import HttpResponse
from toPickApp.forms import LoadForm
import ceng445

# Create your views here.


def index(request):
    session = request.session
    app = ceng445.Application()

    context = {}
    context['availableComponentsForm'] = LoadForm(choices=[(i, i) for i in app.available()])
    return render(request, 'index.html', context)

def load(request):
    print('############3 GET ', request.GET)
    return redirect('/')

def like(request):
    ...

def dislike(request):
    ...
