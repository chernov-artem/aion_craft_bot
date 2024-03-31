"рассчет себестоимости алх"

cost_v20 = 800
cost_v30 = 0
cost_v40 = 0
cost_v50 = 1350
cost_v50_green = 3850
jelly = 2600

pr_stih = (cost_v20 * 20 + jelly) / 40
el_stih = (cost_v50 * 20 + jelly) / 40
el_water = el_stih * 12 / 50

gernita = (cost_v50_green * 20 + jelly) / 180
manna_poition = el_water + gernita + 58
manna_sale_cost = 990


print(pr_stih)
print(el_water)
print(gernita)
print('зелье манны =', manna_poition)
print('зелье манны  маржа=', manna_sale_cost - manna_poition)
