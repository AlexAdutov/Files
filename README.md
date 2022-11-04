# Домашнее задание к лекции «Открытие и чтение файла, запись в файл»

### Задача №1

#### Должен получится следующий словарь

```
cook_book = {
  'Омлет': [
    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
  'Утка по-пекински': [
    {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
    {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
    {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
    {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
  'Запеченный картофель': [
    {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
    {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
    {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ]
  }
  ```

### Задача №2

#### Нужно написать функцию, которая на вход принимает список блюд из cook_book и количество персон для кого мы будем готовить
```
get_shop_list_by_dishes(dishes, person_count)
```

### Задача №3

#### В папке лежит некоторое количество файлов. Считайте, что их количество и имена вам заранее известны

#### Необходимо объединить их в один по следующим правилам:

#### Содержимое исходных файлов в результирующем файле должно быть отсортировано по количеству строк в них (то есть первым нужно записать файл с наименьшим количеством строк, а последним - с наибольшим)
#### Содержимое файла должно предваряться служебной информацией на 2-х строках: имя файла и количество строк в нем
