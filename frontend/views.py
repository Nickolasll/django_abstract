from abc import ABCMeta
from pathlib import Path

from django.views.generic import TemplateView

from backend.settings import BASE_DIR
from frontend.domain.about.about import About


class AbstractView(TemplateView, metaclass=ABCMeta):
    nav = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'nbar': self.nav,
        })
        return context


class HomeView(AbstractView):
    template_name = 'home.html'
    nav = 'home'


class AboutView(AbstractView):
    template_name = 'about.html'
    nav = 'about'
    about = About()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                'about': self.about,
            }
        )
        return context
