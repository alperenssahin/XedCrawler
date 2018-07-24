from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('result/', views.runCrawl, name='runCrawl'),
    path('masterCrawl/', views.master, name='master'),

    # ex: /polls/5/

]