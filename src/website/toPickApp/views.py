from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from toPickApp.forms import *
from django.contrib.auth.models import User
from ceng445 import *
import pickle
import re
import traceback

# Create your views here.


class BaseClass(View):
    name = ''

    def get(self, request, *args, **kwargs):
        app = self._getApplication(request)

        context = self.getDeafultContext(request)
        self.setApplicationDataToContext(context, app, request)

        self._setApplication(request, app)
        return render(request, 'index.html', context)

    def post(self, request, *args, **kwargs):
        app = self._getApplication(request)

        context = self.getDeafultContext(request)

        if self.name == 'loadComponent':
            for comp in request.POST.getlist('component', []):
                app.load(comp)
        elif self.name == 'addInstance':
            try:
                comp = request.POST.get('component', None)
                if comp:
                    app.addInstance(comp, int(request.POST['x']), int(request.POST['y']))
            except ValueError:
                #TODO Do something here
                ...
        elif self.name == 'removeInstance':
            instanceID = request.POST.get('instance', None)
            app.removeInstance(instanceID)
            # else:
            #     try:
            #         result.append(int(argv[i]))
            #     except:
            #         reeInstance(instanceID)
        elif self.name == 'callMethod':
            print('CALL METHOD: ', request.POST)
            instanceID = kwargs.get('instanceID', None)
            methodName =  request.POST.get('methodName-'+instanceID, None)
            try:
                args = self.parseMethodArgs(request.POST.get('args-'+instanceID, ''))
                if args:
                    callMethodResult = app.callMethod(instanceID, methodName, *args)
                else:
                    print('Calling Method with no arguments')
                    callMethodResult = redirectapp.callMethod(instanceID, methodName, None)
                    print('Result: ', callMethodResult)
            except Exception as e:
                print('An Exception occurred: ', e)
                callMethodResult = None

            if callMethodResult:
                print(str(callMethodResult))
                context['callMethodResult'] = str(callMethodResult)
        elif self.name == 'saveDesign':
            app.saveDesign(request.POST.get('filePath', None))
        elif self.name == 'loadDesign':
            print('LOAD DESIGN _______________')
            app.loadDesign(request.POST.get('filePath', None))
        elif self.name == 'execute':
            try:
                result = app.execute()
            except Exception as e:
                traceback.print_exc()
                result = None
            context['executionResult'] = result
        elif self.name == 'main':
            self.setApplicationDataToContext(context, app, request)
            self._setApplication(request, app)
            self.saveContext(request, context)
            return redirect('/')

        self.setApplicationDataToContext(context, app, request)
        self._setApplication(request, app)
        self.saveContext(request, context)
        return redirect('/')
        # return render(request, 'index.html', context)

    def _getApplication(self, request):
        app = request.session.get('app', None)
        if app:
            app = pickle.loads(app)
        else:
            app = Application()
        return app

    def _setApplication(self, request, app):
        request.session['app'] = pickle.dumps(app)

    def saveContext(self, request, context):
        request.session['context'] = context

    def parseMethodArgs(self, args):
        if args == '':
            argv = []
        else:
            argv = re.split(r'\s+', args)
        result = []
        i = 0
        while i < len(argv):
            if(argv[i] == '__Factory__'):
                result.append(Factory().createInstance(argv[i+1]))
                i += 2
                continue
            else:
                try:
                    result.append(int(argv[i]))
                except:
                    result.append(argv[i])
            i += 1
        print('---------------PARSED ARGS -------------')
        print(argv)
        if argv:
            return tuple(argv)
        else:
            return None

    def getDeafultContext(self, request):
        if request.session.get('context', None):
            context = request.session['context']
            del request.session['context']
        else:
            context = {}
        return context

    def setApplicationDataToContext(self, context, app, request):
        self.setAvailableComponentsToContext(context, app)
        self.setLoadedComponentsToContext(context, app)
        self.setInstancesToContext(context, app)
        self.setGridToContext(context, app, request)
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

    def setGridToContext(self, context, app, request):
        grid = app.makeGridHTML(request)
        print(grid)
        context['grid'] = grid
        return context

def home(request):
    context = {}
    context['userregister'] = UserRegister(request.POST)
    context['userlogin'] = UserLogin(request.POST)
    return render(request, 'register.html',context)

def register(request):
    if request.method=='POST':
        form=UserRegister(request.POST)
        for field in form:
            print(field.label)
            print(field.errors)
        if form.is_valid():
            print('form valid')
            username, email, password = form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password1']
            user = User.objects.create_user(username, email, password)
            user.is_active = True # if you want to set active
            user.save()
            return redirect('/home')
    else:
        ...
    print('register unsuccesfull')
    return redirect('/')

def login(request):
    if request.method=='POST':
        form=UserLogin(request.POST)
        for field in form:
            print(field.label)
            print(field.errors)
        if form.is_valid():
            username, password = form.cleaned_data['username'], form.cleaned_data['password']
            user = User.objects.get(username=username)
            user.is_active = True # if you want to set active
            return redirect('/home')
    else:
        ...
    print('login unsuccesfull')
    return redirect('/')

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
