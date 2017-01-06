from django.conf.urls import url

from toPickApp.views import BaseClass

urlpatterns = [
    url(r'^$', BaseClass.as_view()),
    url(r'^load$', BaseClass.as_view()),
    url(r'^loadComponent$', BaseClass.as_view(name='loadComponent')),
    url(r'^addInstance$', BaseClass.as_view()),
    url(r'^removeInstance$', BaseClass.as_view()),
    url(r'^execute$', BaseClass.as_view()),
]
