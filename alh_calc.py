"рассчет себестоимости алх"

cost_v20 = 800
cost_v30 = 0
cost_v40 = 0
cost_v50 = 1350
cost_v50_green = 3850
jelly = 2600
gard_paper = 2384

pr_stih = (cost_v20 * 20 + jelly) / 40
el_stih = (cost_v50 * 20 + jelly) / 40
el_water = el_stih * 12 / 50
el_powder = el_stih * 12 / 20

gernita = (cost_v50_green * 20 + jelly) / 180
fiol_poition = (el_water * 3 + gernita * 4 + 58 * 3) / 3
manna_poition = el_water + gernita + 58
manna_sale_cost = 990
fion_poition_cost = 1600
f_krit_scroll_cost = 3669
f_krit_scroll = (cost_v50 + gard_paper * 5 + el_powder * 5) / 5


print(pr_stih)
print(el_water)
print(gernita)
print('зелье манны =', manna_poition)
print('зелье манны  маржа=', manna_sale_cost - manna_poition)
print('фиол банки', fiol_poition)
print('фиол банки маржа', fion_poition_cost - fiol_poition)
print()
print('себ свитка ф крит IV =', f_krit_scroll_cost, ' маржа ', f_krit_scroll_cost - f_krit_scroll)
