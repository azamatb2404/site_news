from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.
from django.views.generic import TemplateView




class IndexPage(TemplateView):
    template_name = "index.html"
