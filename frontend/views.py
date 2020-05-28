from pathlib import Path

from django.views.generic import TemplateView

from backend.settings import BASE_DIR


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
    about_project = 'Данный проект разрабатывался в свободное время с целью повышения квалификации и представляет ' \
                    'собой сборник небольших демонстрационных задач, которые были поставлены и исполнены для того ' \
                    'чтобы: освоить Django и улучшить навыки работы с Python, попробовать себя во фронтенде и ' \
                    'научиться создавать шаблоны с адаптивной версткой, Освоить Bootstrap 4, а также SCSS, MVC, jQuery'

    about_author = 'Меня зовут Магритов Николай и я занимаюсь архитектурой и разработкой серверного ПО уже более ' \
                   '3х лет. В 2016 году в результате окончания обучения в СФ МЭИ по специальности "Информатика и ' \
                   'вычислительная техника, Вычислительные машины, комплексы, системы и сети" мне была присвоена ' \
                   'степень бакалавра. В 2018 году мне была присвоена степень магистра в области "Информатика и ' \
                   'вычислительная техника" по специальности "Информатика и вычислительная техника, Информационное и ' \
                   'программное обеспечение автоматизированных систем" в результате успешной защиты выпускной ' \
                   'квалификационной работы на тему "Способ и нечеткая модель оценки опасных газов на основе ' \
                   'колориметрического анализа динамики химических реакций". Долгое время я занимался низкоуровневым' \
                   ' программированием устройств, в результате чего устроился на работу инженером в ФГУП СПО ' \
                   '"Аналитприбор", но потом я решил попробовать себя в чем-то новом и сменил место работы, а также и ' \
                   'профиль работы, так я начал углубляться архитектуру и web-разработку.'
    requirements = []

    def get_context_data(self, **kwargs):
        if not self.requirements:
            req_path = Path(BASE_DIR, 'requirements.txt')
            with open(req_path, 'r') as f:
                self.requirements = f.read().split('\n')
            self.requirements = [item.split('==') for item in self.requirements]
        context = super(AboutView, self).get_context_data(**kwargs)
        context.update({
            'nbar': self.nav,
            'requirements': self.requirements,
            'about_project': self.about_project,
            'about_author': self.about_author,
        })
        return context
