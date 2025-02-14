# Проект effective_mobile

# Тестируемый сайт https://effective-mobile.ru/#main

## Описание

**effective_mobile** - это проект, для тестирования переходов по всем блокам сайта по клику главный кнопок навигации (О нас, Контакты и пр.).

## Автор

### [Кирилл Мансуров](https://github.com/Kirill374mansurov)</br>  

## Функциональность

- Можно запустить локально в консоли тесты
- Можно создать отчет по тестам с помощью Allure
- PS почти была доработана возможность запускать тесты через докер

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Kirill374mansurov/effective_mobile.git
```

Создать виртуальное окружение, активировать его и импортировать зависимости (файл requirements.txt):

```
Python -v venv venv
```

```
venv/Scripts/activate
```

```
pip install -r requirements.txt
```

```
playwright install
```

Запуск тестов локально через браузер хром (браузер можно поменять на любой):

```
pytest --headed --browser chromium
```

Запуск тестов и создание отчета через Allure(требуется установленная программа Allure):

```
pytest -v -s --alluredir
```

```
allure server results
```

Запуск проекта в Docker (не реализовано, столкнулся с ошибкой загрузки playwright):

```
docker compose up --build
```
