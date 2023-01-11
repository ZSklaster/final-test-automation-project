# final-test-automation-project

Автотесты для выполнения исследовательского тестирования страници аутентификации сайта
Ростелеком https://b2c.passport.rt.ru/auth/
Тест кейсы можно посмотреть по ссылке https://docs.google.com/spreadsheets/d/1xkKzx2Z3AwmXoZn5DcIoyzXLXYnOikGJv1e3JDzhAHw/edit?usp=sharing

После скачивания нужно отредактировать файл config.py и ввести телефон и почту своей учетной записи Ростелеком
В файле test_rostelecom.py ввести путь до файла chromedriver.exe

Для запуска тестов необходимы следующие бибилиотеки и их зависимости: 
pytest
time
selenium 
А так-же установлен webdraiver для браузера Google Crome

В консоли перейти в каталог с файлами test_rostelecom.py и config.py
Ввести команду python -m pytest test_rostelecom.py


