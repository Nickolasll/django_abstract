from abc import ABCMeta

from django.http import HttpResponse
from django.views.generic import TemplateView
from frontend.domain.about.about import About
from frontend.domain.home.home import Home
from frontend.domain.joke.factory import JokeFactory
import json

from frontend.domain.quote_book.quote_book import QuoteBook


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

    def get_context_data(self, **kwargs):
        quotes = []
        for _ in range(3):
            quotes.append(QuoteBook.get_quote())
        context = super().get_context_data(**kwargs)
        context.update({'quotes': quotes})
        return context

    # def post(self, request, *args, **kwargs):
    #     joke = JokeFactory.get_online_joke()
    #     self.jokes.append(joke)
    #     json_data = json.dumps(joke.serialize())
    #     return HttpResponse(json_data, content_type='application/json')
    #
    # def delete(self, request, *args, **kwargs):
    #     data = json.loads(request.body)
    #     self.jokes.remove(data['id_'])
    #     return HttpResponse('success', content_type='application/json')
