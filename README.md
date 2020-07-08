# db-hack
 
С данным кодом вы сможете изменять базу данных [электронного дневника](https://github.com/devmanorg/e-diary/tree/master).

## Настройка кода

Переложите файл scripts.py в репозиторий рядом с manage.py.

## Запуск python shell

Запустите python shell командой:
```bash
python manage.py shell
```
Используйте python3, если есть конфликт с Python2.

## Модуль scripts

Правила ввода:
- ФИО с большой буквы, в Именительном падеже, через пробел в виде "Фамилия Имя", либо "Фамилия Имя Отчество". 
- Школьные предметы: первое слово - с большой буквы; в Именительном падеже.

Либо смотрите примеры написания в базе данных [электронного дневника](https://github.com/devmanorg/e-diary/tree/master).

### scripts.get_schoolkid()

```python
>>> import scripts
>>> scripts.get_schoolkid("Иванов Иван Иванович")
# <Schoolkid: Иванов Иван Иванович 1А>
```
Выдаёт карточку ученика Иванова Ивана Ивановича.

### scripts.fix_marks()

```python
>>> import scripts
>>> scripts.fix_marks("Иванов Иван Иванович")
```
Все отрицательные оценки (2, 3) ученика Иванова Ивана Ивановича исправятся на 5.

### scripts.remove_chastisements()

```python
>>> import scripts
>>> scripts.remove_chastisements("Иванов Иван Иванович")
```
Все замечания ученика Иванова Ивана Ивановича удалятся.

### scripts.create_commendation()

```python
>>> import scripts
>>> scripts.create_commendation("Иванов Иван Иванович", "Математика")
```
Создаёт "похвалу" по математике Иванову Ивану Ивановичу, со словами "Хвалю!".

```python
>>> import scripts
>>> scripts.create_commendation("Иванов Иван Иванович", "Математика", "Молодец!")
```
Создаёт "похвалу" по математике Иванову Ивану Ивановичу, со словами "Молодец!".

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
