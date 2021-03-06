from abc import ABCMeta

from django.http import HttpResponse
from django.views.generic import TemplateView
from frontend.domain.about.about import About
from frontend.domain.home.home import Home
from frontend.domain.joke.factory import JokeFactory
import json

from frontend.domain.quote_book.quote_book import QuoteBook
from frontend.domain.weather.manager import Manager


class AbstractTemplateView(TemplateView, metaclass=ABCMeta):
    nav = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'nbar': self.nav,
        })
        return context


class HomeView(AbstractTemplateView):
    template_name = 'home.html'
    nav = 'home'
    home = Home()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'home': self.home})
        return context


class AboutView(AbstractTemplateView):
    template_name = 'about.html'
    nav = 'about'
    about = About()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'about': self.about})
        return context


class JokeView(AbstractTemplateView):
    template_name = 'joke.html'
    nav = 'joke'
    jokes = []

    def get_context_data(self, **kwargs):
        if not self.jokes:
            self.jokes.append(JokeFactory.get_online_joke())
        context = super().get_context_data(**kwargs)
        context.update({'jokes': self.jokes})
        return context

    def post(self, request, *args, **kwargs):
        joke = JokeFactory.get_online_joke()
        self.jokes.append(joke)
        json_data = json.dumps(joke.serialize())
        return HttpResponse(json_data, content_type='application/json')

    def delete(self, request, *args, **kwargs):
        data = json.loads(request.body)
        self.jokes.remove(data['id_'])
        return HttpResponse('success', content_type='application/json')


class QuoteView(AbstractTemplateView):
    template_name = 'quote.html'
    nav = 'quote'
    quotes = []

    def get_context_data(self, **kwargs):
        if not self.quotes:
            self.quotes.extend(QuoteBook().get_quotes())
        context = super().get_context_data(**kwargs)
        context.update({'quotes': self.quotes})
        return context

    def post(self, request, *args, **kwargs):
        quotes = QuoteBook().get_quotes()
        self.quotes.clear()
        self.quotes.extend(quotes)
        response = {
            'quotes': [quote.serialize() for quote in quotes]
        }
        json_data = json.dumps(response)
        return HttpResponse(json_data, content_type='application/json')


class WeatherView(AbstractTemplateView):
    template_name = 'weather.html'
    nav = 'weather'
    manager = Manager()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'cities': self.manager.cities})
        return context

    def post(self, request, *args, **kwargs):
        a = json.loads(request.body)
        print(a)
        response = {'result': True}
        json_data = json.dumps(response)
        return HttpResponse(json_data, content_type='application/json')
