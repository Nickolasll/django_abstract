from django.conf.urls import url
from frontend.views import HomeView, AboutView

urlpatterns = [
    url(r"^$", HomeView.as_view()),
    url(r"about", AboutView.as_view()),
]
