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
                dicts = {m['ingredient_name']: {'measure': m['measure'],
                                                'quantity': int(m['quantity']) * person_count}}
                result.update(dicts)
    return result


print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

path = '/home/msi_alt_kde/text_files'
list_files = [x for x in os.listdir(path) if x.endswith('.txt') and x.startswith(('1', '2', '3'))]
new_dict = {}
for names in list_files:
    with open(names, 'r', encoding='utf-8') as f:
        count_lines = len(f.readlines())
        f.seek(0)
    with open(names, 'r', encoding='utf-8') as f:
        text = f.read()
    _dict = {names: (count_lines, text)}
    new_dict.update(_dict)
sorted_dict = dict(sorted(new_dict.items(), key=lambda item: item[1]))
with open('result.txt', 'w', encoding='utf-8') as file:
    for el in sorted_dict:
        file.write(el)
        file.write('\n')
        file.write(str(sorted_dict[el][0]))
        file.write('\n')
        file.write(sorted_dict[el][1])
        file.write('\n')
        