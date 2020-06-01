from frontend.domain.home.carousel_item import CarouselItem
from frontend.domain.home.faq import Faq


class Home:
    header = "Добро пожаловать в мой уютный уголок!"
    description = "Здесь в захватывающей карусели вы сможете найти все на что этот проект способен. Тогда чего " \
                  "вы ждете? Вперед!"
    carousel = [
        CarouselItem(image='carousel/home.png'),
        CarouselItem(image='carousel/about.png', ref="about"),
    ]
    faq_header = "Информация"
    faq_description = 'Здесь Вы найдете ответы на самые часто задаваемые вопросы:'
    faqs = [
        Faq(question='Что здесь происходит?', answer='Да кто его вообще знает!'),
    ]
