"рассчет себестоимости еды"

cost_v50 = 1340
cost_v50_green = 3850
drag_meat = 21000
jelly = 2550
cook_ing = 117

res = round((cost_v50 * 20 + jelly) / 60, 1)
res_green = round((cost_v50_green * 20 + jelly) / 60, 1)


print(res)
print(res_green)

def gold_food(n: int, ing1: int, ing2: int, ing3: int) -> float:
    'функция рассчета стоимости голд еды'
    food_cost =  ing1 + ing2 + ing3 + cook_ing * 16
    print('себестоимость 1 еды: ', food_cost / 2)
    print('себестоимость всей еды: ', food_cost * n)

    return food_cost * n

def drag_food_salad(n: int) -> float:
    'функция рассчета драконик еды'
    food_cost = drag_meat + res_green * 1.33 + cook_ing * 16 + cost_v50
    print('себестоимость 1 салата: ', food_cost / 2)
    print('себестоимость всей еды: ', food_cost * n)

def drag_food_ragout(n: int) -> float:
    'функция рассчета драконик еды'
    food_cost = drag_meat + res_green + res + cook_ing * 16 + cost_v50
    print('себестоимость 1 рагу: ', food_cost / 2)
    print('себестоимость всей еды: ', food_cost * n)

def cocktail(n:int):
    'функция рассчитывает себестоимость коктейлся'
    food_cost = res * 2 + cook_ing * 12
    print('себестоимость 1 коктейля: ', food_cost / 2)
    print('себестоимость всех коктейлей: ', food_cost * n)

# gold_food(60, 1800, 1523, 2087)
# gold_food(60, res, res, res_green)
# drag_food_salad(20)
# drag_food_ragout(20)
cocktail(480)
