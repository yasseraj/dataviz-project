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
    url(r'^1data_follow', PaginaFolloIngErDataCtrl1, name='following_er_data1'),
    url(r'^2data_follow', PaginaFolloIngErDataCtrl2, name='following_er_data2'),
    url(r'^burbuja', BurbujaCtrl, name='burbuja'),
    url(r'^data_burbuja', BurbujaDataCtrl, name='burbuja_data'),
    url(r'^lineas', LineasCtrl, name='lineas'),
    url(r'^data_lineas', LineasDataCtrl, name='lineas_data'),
    url(r'^1data_lineas', LineasDataCtrl1, name='1lineas_data'),
]
