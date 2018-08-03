from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('result/', views.runCrawl, name='runCrawl'),
    path('masterCrawl/', views.master, name='master'),
    path('rulePort/', views.getRules, name='getRules'),
    path('getReference/', views.getRef, name='getRef'),
    path('xedEx/', views.xedExtension, name='xedExtension')
    # ex: /polls/5/

]
