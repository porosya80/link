from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import LinkForm
from django.views.generic import ListView, CreateView
from .models import Link
from .models import Pic


class HomePageView(ListView):
    model = Link
    template_name = 'home.html'


class CreateLinkView(CreateView):
    model = Link
    form_class = LinkForm
    template_name = 'post.html'
    success_url = reverse_lazy('home')
