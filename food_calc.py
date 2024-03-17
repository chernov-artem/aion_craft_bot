"рассчет себестоимости еды"

cost_v50 = 1572
cost_v50_green = 4050
jelly = 2600

cook_ing = 117

res = round((cost_v50 * 20 + jelly) / 60, 1)
res_green = round((cost_v50_green * 20 + jelly) / 60, 1)


print(res)
print(res_green)

def gold_food(n: int, ing1: int, ing2: int, ing3: int) -> float:
    'функция рассчета стоимости голд еды'
    food_cost =  ing1 + ing2 + ing3 + cook_ing * 16
    print('себестоимость 1 еды: ', food_cost)
    print('себестоимость всей еды: ', food_cost * n)

    return food_cost * n

gold_food(60, 1800, 1523, 2087)
gold_food(60, res, res, res_green)

