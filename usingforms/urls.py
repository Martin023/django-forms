
from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name="contacts"),
    path('snippet/', views.snippet , name="snippet"),
]
