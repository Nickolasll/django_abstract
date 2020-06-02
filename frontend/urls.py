from django.conf.urls import url
from django.urls import path

from frontend.views import HomeView, AboutView, JokeView

urlpatterns = [
    url(r"^$", HomeView.as_view()),
    url(r"about", AboutView.as_view()),
    url(r"joke", JokeView.as_view()),
    path(r"joke", JokeView.as_view(), name='add_joke'),
]
