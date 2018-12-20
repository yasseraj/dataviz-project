from django.conf.urls import url


from .views import *

urlpatterns = [
    url(r'^$', HomeCtrl),
    url(r'^home', HomeCtrl, name='home'),
    url(r'^spain_portugal', SpainPortugalCtrl, name='spain_portugal'),
    url(r'^pagina_nube', NubeCtrl, name='pagina_nube_palabras'),
    url(r'^nube_palabras', NubeDataCtrl, name='nube_palabras'),
    url(r'^followinger', PaginaFolloIngErCtrl, name='following_er'),
    url(r'^data_follow', PaginaFolloIngErDataCtrl, name='following_er_data'),
]
