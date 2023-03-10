# Консольное приложение по управлению БД

Приложение позволяет создать простую базу данных, состоящую из следующих полей:

- Фамилия, Имя, Отчество
- Дата рождения
- Пол

Управление приложением происходит с помощью консольных комманд:

 - add - создает запись
 - delete - удаляет запись по id
 - show_all - выводит все записи (не более 100)
 - find - выполняет поиск по фамилии (выводит не более 100)
 - quit - завершает работу приложения

Проект написан на Python 3 с использованием библиотеки sqlite3.

### Примеры запросов
```
add Ivanov Ivan Sergeevich 1987-09-11 M

delete 9

find Ivanov
```
### Запуск проекта

 - Клонируйте репозиторий:
```
   git clone git@github.com:korecbtc/db-terminal.git
```
 - Перейдите в папку с проектом:
```
   cd db-terminal
```
  - Запустите программу в коммандной строке:
```
  python db-terminal.py
```
### Развитие проекта
Проект разработан как минимально жизнеспособный продукт.
Вариантов доработки множество, например:
- Валидация данных
- Расширенные возможности поиска
- Редактирование данных
- Графический интерфейс
- Тесты
- Логгирование

### Автор

Иван Корец

