from django.conf.urls import url

from toPickApp.views import BaseClass, AjaxHandler, home,register,login,logout

urlpatterns = [
    url(r'^$', home),
    url(r'^ajax/(?P<componentName>\w+)/(?P<instanceID>\S+)$', AjaxHandler.as_view()),
    url(r'^home$', BaseClass.as_view()),
    url(r'^load$', BaseClass.as_view()),
    url(r'^login$', login),
    url(r'^logout$', logout),
    url(r'^register$', register),
    url(r'^loadComponent$', BaseClass.as_view(name='loadComponent')),
    url(r'^addInstance$', BaseClass.as_view(name='addInstance')),
    url(r'^removeInstance$', BaseClass.as_view(name='removeInstance')),
    url(r'^execute$', BaseClass.as_view(name='execute')),
    url(r'^callMethod/(?P<instanceID>\S*)$', BaseClass.as_view(name='callMethod')),
    url(r'^saveDesign$', BaseClass.as_view(name='saveDesign')),
    url(r'^loadDesign$', BaseClass.as_view(name='loadDesign')),
]
