from django.urls import path

from .views import HomePageView, CreateLinkView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('link/', CreateLinkView.as_view(), name='add_post')
]
