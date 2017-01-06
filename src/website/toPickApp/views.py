from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from ceng445 import *
import pickle

# Create your views here.


class BaseClass(View):
    name = ''

    def get(self, request, *args, **kwargs):
        app = self._getApplication(request)

        context = self.getDeafultContext()
        self.setApplicationDataToContext(context, app)

        self._setApplication(request, app)
        return render(request, 'index.html', context)

    def post(self, request, *args, **kwargs):
        app = self._getApplication(request)

        context = self.getDeafultContext()

        if self.name == 'loadComponent':
            for comp in request.POST.getlist('component', []):
                app.load(comp)

        self.setApplicationDataToContext(context, app)
        self._setApplication(request, app)
        return render(request, 'index.html', context)

    def _getApplication(self, request):
        app = request.session.get('app', None)
        if app:
            app = pickle.loads(app)
        else:
            app = Application()
        return app

    def _setApplication(self, request, app):
        request.session['app'] = pickle.dumps(app)

    def getDeafultContext(self):
        context = {}
        return context

    def setApplicationDataToContext(self, context, app):
        self.setAvailableComponentsToContext(context, app)
        self.setLoadedComponentsToContext(context, app)
        return context

    def setAvailableComponentsToContext(self, context, app):
        context['availableComponents'] = app.available()
        return context

    def setLoadedComponentsToContext(self, context, app):
        loadedComponents = app.loaded()
        context['loadedComponents'] = [(a,loadedComponents[a]) for a in loadedComponents]
        return context

    def setInstancesToContext(self, context, app):
        instances = app.instances()
        context['instances'] = [(a, instances[a]) for a in instances]
        return context


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
