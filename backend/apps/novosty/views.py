from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.
from django.views.generic import TemplateView, ListView
from .models import Category, Novosty



class IndexPage(TemplateView):
    template_name = "index.html"


class NovostyListView(ListView):
    model = Novosty
    template_name = "news_list.html"
    context_object_name = "news"