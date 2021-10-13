# Framebuffer-lib

linux framebuffer файл /dev/fb0 позволяет выводить на экран любое изображение поверх экрана.
### Видео пример запуска:
[![video](https://img.youtube.com/vi/kdESV7I0SVY/hqdefault.jpg)](https://youtu.be/kdESV7I0SVY)

Работа программы проверена на arch linux без графического окружения. \
На данный момент есть возможности для:
* Вывод на экран базовых примитивов
* Работа с мышкой
* Вывод на экран текста
* Вывод изображений
* Копирование части буффера
* Вставка части буффера
* Окружение для python

Для запуска программы требуются права администратора.\
`make` \
`sudo ./out/main`

Для работы с python кодом необходимо создать библиотеку\
`make lib`\
И запустить выбранный python файл\
`cd python`\
`sudo python3 test_mouse1.py`

[png file in terminal](https://www.youtube.com/watch?v=JM0PU0z6nyM)