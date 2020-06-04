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
        Faq(question='Анекдоты в 2020? Серьезно?', answer='Да, Серьезно! На самом деле здесь впервые был использован '
                                                          'механизм реактивного построения интерфейса. Анекдоты не '
                                                          'хранятся в базе данных, а лежат в оперативной памяти, '
                                                          'дожидаясь перезагрузки сервера!'),
        Faq(question='Цитаты?', answer='Насладитесь генератором цитат от знаменитого Джейсона Стетхема! Цитаты тоже '
                                       'не записываются с базу данных, да и нечего там им сейчас делать.'),
    ]
