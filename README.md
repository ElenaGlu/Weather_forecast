## _Веб-Приложение для прогноза погоды_

«Weather Forecast»: приложение, в котором по запросу города, можно узнать его текущие погодные условия и прогноз на пять дней вперед.

### Технологии:

Python3, Django

### Запуск проекта на локальной машине:

- Клонировать репозиторий:
```
https://github.com/ElenaGlu/Django-Weather.git
```
### Создайте и активируйте виртуальное окружение:

```
python -m venv venv
source venv/bin/activate     #для Linux
```
### В директории Django-Weather создайте файл `.env` и заполните данными:

```
DJANGO_KEY = 'key'
API_KEY_WEATHER = 'key'      #API key - https://openweathermap.org/
```
### Установите требуемые зависимости:

- Выполните команду в терминале: 
```
pip install -r requirements.txt
```
### Запустите проект:

```
python manage.py runserver
```

- После запуска проект будут доступен по адресу: [http://localhost/](http://localhost/)
![IMG_5541](https://github.com/ElenaGlu/Django-Weather/assets/123466535/63b8fac2-ca3b-414f-8a38-4194679d580e)
![photo_2023-10-26_19-03-36 (2)](https://github.com/ElenaGlu/Django-Weather/assets/123466535/41de0fce-0cd8-48ff-9d04-d1a0b45676fd)


