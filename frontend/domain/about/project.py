from pathlib import Path

from backend.settings import BASE_DIR
from frontend.domain.about.package import Package
from frontend.domain.about.service import Service


class Project:
    header = 'О проекте'
    info = 'Данный проект разрабатывался в свободное время с целью повышения квалификации и представляет ' \
           'собой сборник небольших демонстрационных задач, которые были поставлены и исполнены для того ' \
           'чтобы: освоить Django и улучшить навыки работы с Python, попробовать себя во фронтенде и ' \
           'научиться создавать шаблоны с адаптивной версткой, а также освоить Bootstrap 4, а также SCSS, ' \
           'MVC, jQuery \n\n ' \
           'Почему именно "Cтартапик"? - потому что на полноценный проект данная работа никак не тянет. ' \
           'Это скорее мой sandbox, в котором я в свободное время экспериментировал: имплементировал все ' \
           'что хотел попробовать и все что было интересно. Для меня это было своеобразной игрой в которой '\
           'я постоянно усложнял себе задачу, например, смогу ли я добавлять и удалять эти элементы ' \
           'реактивно, без перезагрузки страницы? ' \
           '\n\n Почему именно "Абстракцио"? - не знаю, просто захотелось.'
    technologies = ['Python 3', 'Django 3', 'Bootstrap 4', 'MVC', 'JavaScript', 'Ajax']
    requirements_header = 'Установленные пакеты Python 3.7'
    requirements = []
    services_header = 'Дополнительные сервисы'
    services = [
        Service(
            name='РжуНеМогу.RU',
            info='Отсюда я беру GET запросом случайные анекдоты, цитаты и афоризмы',
            ref='http://rzhunemogu.ru/'
        ),
        Service(
            name='openweathermap.org',
            info='Отсюда берется информация для виджета погоды и иконочки',
            ref='https://openweathermap.org/'
        ),
    ]

    def __init__(self):
        req_path = Path(BASE_DIR, 'requirements.txt')
        with open(req_path, 'r') as f:
            requirements = f.read().split('\n')
        for package in requirements:
            name, version = package.split('==')
            self.requirements.append(Package(name=name, version=version))
