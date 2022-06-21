from django.urls import path

from .views import *

urlpatterns = [
    path('', IndexPage.as_view(), name='index'),
    path('list/novosty/', NovostyListView.as_view(), name='news_list'),
]