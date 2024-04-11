"""модуль для рассчета количества ресурсов для крафта осадных орудий"""
mage_vortex_gold = 36000
mage_vortex_blue = 11500
dren_ore = (mage_vortex_gold * 20 + 2600) / 1080
gems_cost = (mage_vortex_blue * 40 + 2600) / 180
elit_stih_cos = 1500
nosfe = 1900
kach_skin = 1100
cost_v30 = 1100
cost_v40 = 966
cost_v50 = 1400

antracide = 1765
dren_fusion = 3531
sew_ing = 1412
grind_powder = 13860
catalyst = 1471
elit_catalyst = 10063


def calculate(n: int):
    opora(n)
    print()
    kozhuh(n)
    print()
    truba(n)
    print()
    org_sub(n)
    print()
    core(n)
    print()
    fuel(n)
    sum_seb = opora(n) + kozhuh(n) + truba(n) + org_sub(n) + core(n) + fuel(n)
    print()
    print('общ себестоимость: ',sum_seb, ' или (', sum_seb / n, ' за 1 шт)')


def opora(n: int):
    nail = n * 8
    rod = n * 5
    ingot = nail * 2 + rod * 4
    dren_alloy = rod * 2
    sum_ignot = n * 65
    sum_ignot1 = sum_ignot // 10 + 1
    sum_ignot2 = sum_ignot1 * 12
    vortex_cost = n * 9 * cost_v50
    opora_seb = round(ingot*(dren_ore + antracide) + dren_alloy * dren_fusion + n * 9 * cost_v50, 1)
    print('Опора(крафтер оптимист):')
    print('нужно ', nail, 'гвоздей и ', rod, 'стержней')
    print('это ', ingot, ' слитков', ingot, ' атрацита и ', dren_alloy, ' дрен сплава. Это ', dren_alloy * dren_fusion, ' кинар')
    print('всего слитков надо: ', sum_ignot, ' или ', sum_ignot1, 'пакетов, если фастом(',  sum_ignot2, ')')
    print('Гвоздей ', nail)
    print('Стержней ', rod, ' и дрен сплава ', rod * 2)
    print('Маг эфира: ', n * 9, ' (', vortex_cost, ' кинар)')
    print('Цена эфира и дрен сплава: ', rod * 2 * dren_fusion + vortex_cost, ' только дрен сплав: ', rod * 2 * dren_fusion)
    print('себ слит: ', ingot*(dren_ore + antracide))
    print('или фастом: ', ingot * (dren_ore + antracide) * 12 / 10)
    print('себестоимость ', n, ' опор = ', opora_seb, ' (или ', round(opora_seb / n, 1), ' за 1 шт)')

    return opora_seb


def kozhuh(n: int):
    little_plate = n * 4
    medium_plate = n * 4
    big_plate = n * 3
    dren_alloy = little_plate + medium_plate * 2 + big_plate * 2
    dren_alloy_cost = dren_alloy * dren_fusion
    ingot = little_plate * 2 + medium_plate * 3 + big_plate * 4
    kozhuh_seb = ingot * antracide + dren_alloy * dren_fusion + n * 12 * cost_v50
    vortex_cost = n * 12 * cost_v50
    print('Кожух(крафтер девочка):')
    print('нужно ', little_plate, 'малых и больших пластин и ', big_plate, ' больших пластин')
    print('это ', ingot, ' слитков', ingot, ' атрацита и ', dren_alloy, ' дрен сплава. Это ', dren_alloy_cost, ' кинар')
    print('Малая пластина ', little_plate, ' днер сплава ', little_plate)
    print('Средняя пластина ', medium_plate,' днер сплава ', medium_plate * 2)
    print('Большая пластина ', big_plate, ' днер сплава ', big_plate * 2)
    print('Маг эфира: ', n * 12, ' (', vortex_cost, ' кинар)')
    print('Дрен сплава: ', dren_alloy, ' (', dren_alloy_cost, ' кинар)')
    print('Цена эфира и дрен сплава: ', dren_alloy_cost + vortex_cost)
    print('себестоимость ', n, ' кожухов = ', kozhuh_seb, ' (или ', round(kozhuh_seb / n, 1), ' за 1 шт)')

    return kozhuh_seb

def truba(n: int):
    kl_nosf_nit = n * 10
    kach_kozh = n * 8
    truba_seb = kl_nosf_nit * nosfe * 2 + sew_ing * 10 + kach_kozh * kach_skin * 4 + sew_ing * 8 * 2 + n * 12 * cost_v50
    print('Труба:')
    print('Нужно: ', kl_nosf_nit, 'клубков носф нити и ', kach_kozh, ' кач кожи')
    print('это ', kl_nosf_nit * 2, ' стеблей носфе и ', kach_kozh * 2, 'кач недуб кожи')
    print('Маг эфира: ', n * 12, ' (', n * 12 * cost_v50, ' кинар)')
    print('себестоимость ', n, ' труб = ', truba_seb, ' (или ', round(truba_seb / n, 1), ' за 1 шт)')
    print('ka4 skin = ', (kach_kozh * kach_skin * 4 + sew_ing * 8 * 2)/n)
    return truba_seb

def org_sub(n: int):
    mag_krist = n * 4
    wis_stone = n * 5
    el_water = mag_krist * 20
    el_powder = wis_stone  * 4
    elit_stih = wis_stone * 4 + mag_krist * 2
    org_sub_seb = elit_stih * elit_stih_cos + n * 9 * elit_catalyst + n * 12 * cost_v50
    vortex_cost = n * 12 * cost_v50
    catalyst_cost = (wis_stone + mag_krist) * elit_catalyst
    print('Орг субстанция(крафтер RnnS):')
    print('Нужно: ', wis_stone, ' камней мудрости и ', mag_krist, ' магических кристаллов')
    print('это ', elit_stih, ' элитных стих камней', el_water, ' воды и ', el_powder, ' порошка')
    print('или фастом: ', elit_stih * 1.2, ' элитных стих камней', el_water / 50, 'итераций воды и ', el_powder / 20, 'итераций порошка')
    print('Маг эфира: ', n * 12, ' (', vortex_cost, ' кинар)')
    print('Катализаторов ', wis_stone + mag_krist, ' это ', catalyst_cost, ' кинар. С маг эфиром: ', vortex_cost + catalyst_cost)
    print('себестоимость ', n, ' орг субст = ', org_sub_seb, ' (или ', round(org_sub_seb / n, 1), ' за 1 шт)')

    return org_sub_seb

def core(n: int):
    gems = n * 3
    core_seb = gems * 3 * grind_powder + n * 15 * cost_v50
    print('Ядро:')
    print('Нужно: ', gems, ' каждого камня')
    print('это ', gems * 3, ' полир порошка или ', gems * 3 * grind_powder, ' кинар + ', n*12, ' эфира')
    print('Маг эфира: ', n * 12, ' (', n * 12 * cost_v50, ' кинар)')
    print('Себестоимость ', n, ' ядер ', core_seb, ' (или ', core_seb / n, ' за 1 шт)')

    return core_seb

def fuel(n: int):
    vortex30 = n * 11 * 2
    vortex40 = n * 13 * 2
    vortex50 = n * 15 * 2
    cold_water = n * 100
    fuel_seb = vortex30 * cost_v30 + vortex40 * cost_v40 + vortex50 * cost_v50 + cold_water * 27
    print('Топливо:')
    print('Нужно: ', vortex30, ' оск эфира', vortex40, ' обыч эфира и ', vortex50, ' маг эфира + ', cold_water * 2, ' хол воды')
    print('это ', fuel_seb, ' кинар')
    print()

    return  fuel_seb

def vendor_res(n: int):
    "функция для подсчета количества ресурсов для заданного количества осадок"
    dren_alloy = n * 10 + n * 18
    paint_cost = sew_ing * n * 10
    elit_catalyst_cost = elit_catalyst * n * 9
    grind_powder_cost = grind_powder * n * 9
    print('всего дрен сплава:', dren_alloy, ' это ', dren_alloy * dren_fusion, ' кинар')
    print(n * 10, 'сплава  для оптимиста и', n * 9, ' эфира')
    print(n * 18, ' сплава для девочки и ', n * 12, ' эфира')
    print()
    print(n * 10, ' элитной краски + столько же эл кож усил для GoodVibes (', paint_cost * 2,' кинар) и ', n * 12, ' эфира')
    print(n * 9, ' элитных катализаторов для RnnS (', elit_catalyst_cost,' кинар) и ', n * 12, ' эфира')
    print()
    print(n * 9, ' элит. шлиф материала для Осадок (', grind_powder_cost,' кинар) и ', n * 12, ' эфира')
    print()
    print(n * 22, ' эфира 30, ', n * 26, ' эфира 40 и ', n * 30, ' эфира 50 для МелкойГальки')

    print('Всего маг эфира: ', n * 87)
    print('Всего кинар на ресурсы для ', n, ' осадок: ',
          dren_alloy * dren_fusion + paint_cost * 2 + elit_catalyst_cost + grind_powder_cost, ' кинар')




def art_stone(n: int, mk: int = 0, ws: int = 0, water: int = 0, powder: int = 0):
    'функция расчета количества камней акт арт из стих камней'
    n_pack = n // 12
    print('Посчитать фастом: введи значение: ', n_pack * 10)
    res = n // 22
    mag_kr = res * 3 + mk + water // 20
    wis_stone = res * 5 + ws + powder // 4
    kat = 11 * res + mag_kr + water // 20 + wis_stone + powder // 4
    vortex = res * 16


    print("Всего получится ", res, 'камней акт арт. Остается стих камней: ', res % 22)
    print('маг кристаллов: ', mag_kr, '(', mag_kr * 4, ' иттераций воды)')
    print('кам мудрости: ', wis_stone, '(', wis_stone * 2, ' иттераций порошка)')
    print('катализаторов: ', kat)
    print('эфира: ', vortex)



def ore(n: int):
    'функция расчета количества итемов, которые можно произвести из n слитков дрен руды'
    kol_op = n // 36
    kol_kozh = n // 32
    kol_sum = n // 68
    print('Себестоимость слитков(только атрацита) = ', n * antracide)
    print('Можно сделать ', kol_op, ' опор или ', kol_kozh, ' кожухов')
    print('Или ', kol_sum, ' кожухов и опор')
    print(kol_sum * 36, ' слитков на опоры')
    print(kol_sum * 32, ' слитков на кожухи')


# art_stone(0, 0, 0, 6720, 2240)
# ore(6021)
calculate(80)
# vendor_res(80)