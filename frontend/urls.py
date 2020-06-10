from django.conf.urls import url
from django.urls import path

from frontend.views import HomeView, AboutView, JokeView, QuoteView, WeatherView

urlpatterns = [
    url(r"^$", HomeView.as_view()),
    url(r"about", AboutView.as_view()),
    url(r"joke", JokeView.as_view()),
    path(r"joke", JokeView.as_view(), name='add_joke'),
    url(r"quote", QuoteView.as_view()),
    path(r"quote", QuoteView.as_view(), name='quote'),
    url(r"weather", WeatherView.as_view()),
    path(r"weather", WeatherView.as_view(), name='weather'),
]
