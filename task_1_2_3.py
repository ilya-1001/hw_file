import os

with open('recipe.txt') as f:
    cook_book = {}
    for el in f:
        dish_name = el.strip()
        _list = []
        count_ingredients = f.readline()
        # print(count_ingredients)
        for i in range(int(count_ingredients)):
            ingredients = f.readline()
            ingredient_name, quantity, measure = ingredients.strip().split(' | ')
            _list.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
            dep = {dish_name: _list}
        blank_line = f.readline()
        cook_book.update(dep)
print(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    result = {}
    for n in cook_book.keys():
        if n in dishes:
            for m in cook_book.get(n):
                _dict = {m['ingredient_name']: {'measure': m['measure'],
                                                'quantity': int(m['quantity']) * person_count}}
                result.update(_dict)
    return result


print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

x_files = [x for x in os.listdir() if x == '1.txt' or x == '2.txt' or x == '3.txt']
x_files = list(reversed(x_files))
with open('result.txt', 'a+') as file:
    count = []
    for x in x_files:
        f = open(x).readlines()
        count = (len(f))
        file.write(x)
        file.write('\n')
        file.write(str(count))
        file.write('\n')
        res = open(x).read()
        file.write(res)
