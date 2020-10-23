from django.urls import path

from . import views

app_name = 'website'
urlpatterns = [
    path('', views.home, name='home'),
    path('hello', views.hello, name='hello'),
    path('performances', views.performances, name='performances'),
    path('writing', views.writing, name='writing')
]
