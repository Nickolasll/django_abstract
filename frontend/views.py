from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'
    nav = 'home'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context.update({
            'nbar': self.nav,
        })
        return context


class AboutView(TemplateView):
    template_name = 'about.html'
    nav = 'about'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context.update({
            'nbar': self.nav,
        })
        return context


def home(request):
    return render(request, 'home.html', {})
