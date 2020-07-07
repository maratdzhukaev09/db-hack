# db-hack
 
С данным кодом вы сможете изменять базу данных [электронного дневника](https://github.com/devmanorg/e-diary/tree/master).

## Настройка кода

Переложите файл scripts.py в репозиторий рядом с manage.py.

## Запуск python shell

Запустите python shell командой:
```commandline
python manage.py shell
```
Используйте python3, если есть конфликт с Python2.

## Модуль scripts

### scripts.get_schoolkid()

```pydocstring
>>> import scripts
>>> scripts.get_schoolkid("Иванов Иван Иванович")
# <Schoolkid: Иванов Иван Иванович 1А>
```
Выдаёт карточку ученика Иванова Ивана Ивановича.

### scripts.fix_marks()

```pydocstring
>>> import scripts
>>> scripts.fix_marks("Иванов Иван Иванович")
```
Все отрицательные оценки (2, 3) ученика Иванова Ивана Ивановича исправятся на 5.

### scripts.remove_chastisements()

```pydocstring
>>> import scripts
>>> scripts.remove_chastisements("Иванов Иван Иванович")
```
Все замечания ученика Иванова Ивана Ивановича удалятся.

### scripts.create_commendation()

```pydocstring
>>> import scripts
>>> scripts.create_commendation("Иванов Иван Иванович", "Математика")
```
Создаёт "похвалу" по математике Иванову Ивану Ивановичу, со словами "Хвалю!".

```pydocstring
>>> import scripts
>>> scripts.create_commendation("Иванов Иван Иванович", "Математика", "Молодец!")
```
Создаёт "похвалу" по математике Иванову Ивану Ивановичу, со словами "Молодец!".

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
