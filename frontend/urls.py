from django.conf.urls import url
from frontend.views import home


urlpatterns = [
    url(r"^$", home, name="home"),
]
