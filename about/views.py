from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, View, TemplateView

class IndexView(TemplateView):
    template_name = 'about/index.html'
