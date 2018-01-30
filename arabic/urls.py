from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('verbs', views.verbs, name='verbs'),
    re_path(r'^verbs/(?P<verb>.+)/$', views.selected_verb, name='selected_verb'),
    path('nouns', views.nouns, name='nouns'),
    path('current_verb', views.studying_verb, name='studying_verb'),
    path('current_verb/conjugations', views.conjugations, name='conjugations'),
]
