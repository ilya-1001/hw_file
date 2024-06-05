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
