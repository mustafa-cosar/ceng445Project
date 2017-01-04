from django.conf.urls import url

from toPickApp.views import BaseClass

urlpatterns = [
    url(r'^$', BaseClass.as_view()),
    url(r'^load', BaseClass.as_view()),
]
