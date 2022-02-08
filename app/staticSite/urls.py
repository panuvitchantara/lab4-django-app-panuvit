from xml.etree.ElementInclude import include
from django.urls import path
from . import views

#URLConf
urlpatterns = [
    path("",views.index)
]