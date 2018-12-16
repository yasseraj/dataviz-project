from django.conf.urls import url


from .views import SpainPortugalCtrl, graph

urlpatterns = [
    url(r'^$', graph),
    url(r'^spain_portugal', SpainPortugalCtrl, name='spain_portugal'),
]
