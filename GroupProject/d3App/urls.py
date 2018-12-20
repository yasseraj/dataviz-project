from django.conf.urls import url


from .views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^spain_portugal', SpainPortugalCtrl, name='spain_portugal'),
    url(r'^pagina_nube', PaginaNube, name='pagina_nube_palabras'),
    url(r'^nube_palabras', NubePalabrasCtrl, name='nube_palabras'),
    url(r'^followinger', PaginaFolloIngErCtrl, name='following_er'),
    url(r'^data_follow', PaginaFolloIngErDataCtrl, name='following_er_data'),
]
