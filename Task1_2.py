'''cook_book = {
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
  }'''

with open('recipes.txt', 'r', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dish_name = line.strip()
        ingredients_count = int(file.readline())
        ingredients = []
        for _ in range(ingredients_count):
            ing = file.readline().strip().split(' | ')
            ingredient_name, quantity, measure = ing
            ingredients.append({'ingredient_name': ingredient_name,
                                'quantity': quantity,
                                'measure': measure})
        cook_book[dish_name]=ingredients
        file.readline()


with open('dishes.txt', 'wt') as file1:
    for key, val in cook_book.items():
        file1.write('{}:{}\n'.format(key, val))

'''get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
Должен быть следующий результат:
{
  'Картофель': {'measure': 'кг', 'quantity': 2},
  'Молоко': {'measure': 'мл', 'quantity': 200},
  'Помидор': {'measure': 'шт', 'quantity': 4},
  'Сыр гауда': {'measure': 'г', 'quantity': 200},
  'Яйцо': {'measure': 'шт', 'quantity': 4},
  'Чеснок': {'measure': 'зубч', 'quantity': 6}
}'''

def get_shop_list_by_dishes(dishes, person_count):
    res={}
    for dis in dishes:
        for ing in cook_book[dis]:
            res[ing['ingredient_name']]={'measure':ing['measure'],'quantity':int(ing['quantity'])*person_count}
    print(res)

get_shop_list_by_dishes(['Запеченный картофель', 'Утка по-пекински'], 4)
get_shop_list_by_dishes(['Омлет', 'Утка по-пекински'], 1)