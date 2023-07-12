
from django.urls import path
from .import views
urlpatterns = [
    path('', views.index, name="index"),
    path('portfolio', views.portfolio, name="portfolio"),
    path('innerpage', views.innerpage, name="innerpage"),
    path('contact', views.contact, name="contact"),
]