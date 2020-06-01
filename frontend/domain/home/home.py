from frontend.domain.home.carousel_item import CarouselItem


class Home:
    header = "Заголовок"
    description = "Описалово"
    carousel = [
        CarouselItem(image='carousel/home.png'),
        CarouselItem(image='carousel/about.png', ref="about"),
    ]
    info_header = "Информация"
    infos = []
