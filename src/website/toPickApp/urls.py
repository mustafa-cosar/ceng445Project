from django.conf.urls import url

from toPickApp.views import BaseClass

urlpatterns = [
    url(r'^$', BaseClass.as_view()),
    url(r'^load$', BaseClass.as_view()),
    url(r'^loadComponent$', BaseClass.as_view(name='loadComponent')),
    url(r'^addInstance$', BaseClass.as_view(name='addInstance')),
    url(r'^removeInstance$', BaseClass.as_view(name='removeInstance')),
    url(r'^execute$', BaseClass.as_view(name='execute')),
    url(r'^callMethod/(?P<instanceID>\S*)$', BaseClass.as_view(name='callMethod')),
]
