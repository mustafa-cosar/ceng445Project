from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from ceng445 import *
import pickle

# Create your views here.


class BaseClass(View):

    def get(self, request, *args, **kwargs):
        app = self._getApplication(request)



        self._setApplication(request, app)
        return render(request, 'index.html', {})

    def post(self, request, *args, **kwargs):
        return render(request, 'index.html', {})

    def _getApplication(self, request):
        app = request.session.get('app', None)
        if app:
            app = pickle.loads(app)
        else:
            app = Application()
        return app

    def _setApplication(self, request, app):
        request.session['app'] = pickle.dumps(app)

    

def index(request):
    session = request.session
    app = ceng445.Application()

    context = getContext(request, app)

    return render(request, 'index.html', context)


def loadComponent(request):
    ...

def addInstance(request):
    ...



def getContext(request):
    ...
