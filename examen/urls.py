from . import views
from django.conf.urls import url
from django.urls import path

urlpatterns = [
    url(r'^cliente/$', views.lista_alquileres, name='lista_alquileres'),
    path(
            'cliente/<slug:slug>/',
            views.show_cliente,
            name='detail'
        ),
]