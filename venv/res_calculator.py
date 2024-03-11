"""модуль для рассчета количества ресурсов для крафта осадных орудий"""

cost_v30 = 1048
cost_v40 = 1492
cost_v50 = 1642

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


def opora(n: int):
    nail = n * 8
    rod = n * 5
    ingot = nail * 2 + rod * 4
    dren_alloy = rod * 2
    sum_ignot = n * 65
    sum_ignot1 = sum_ignot // 10 + 1
    sum_ignot2 = sum_ignot1 * 12
    print('Опора:')
    print('нужно ', nail, 'гвоздей и ', rod, 'стержней')
    print('это ', ingot, ' слитков', ingot, ' атрацита и ', dren_alloy, ' дрен сплава')
    print('себ слит: ', ingot*(631+1747))
    print('или: ', ingot*(631+1747)*12/10)
    print('всего слитков надо: ', sum_ignot, ' или ', sum_ignot1, 'пакетов, если фастом(',  sum_ignot2, ')')


def kozhuh(n: int):
    little_plate = n * 4
    medium_plate = n * 4
    big_plate = n * 3
    dren_alloy = little_plate + medium_plate * 2 + big_plate * 2
    ingot = little_plate * 2 + medium_plate * 3 + big_plate * 3
    print('Кожух:')
    print('нужно ', little_plate, 'малых и больших пластин и ', big_plate, ' больших пластин')
    print('это ', ingot, ' слитков', ingot, ' атрацита и ', dren_alloy, ' дрен сплава')

def truba(n: int):
    kl_nosf_nit = n * 10
    kach_kozh = n * 8
    print('Труба:')
    print('Нужно: ', kl_nosf_nit, 'клубков носф нити и ', kach_kozh, ' кач кожи')
    print('это ', kl_nosf_nit * 2, ' стеблей носфе и ', kach_kozh * 2, 'кач недуб кожи')

def org_sub(n: int):
    wis_stone = n * 4
    mag_krist = n * 5
    el_water = wis_stone * 20
    el_powder = mag_krist * 4
    elit_stih = wis_stone * 4 + mag_krist * 2
    print('Орг субстанция:')
    print('Нужно: ', wis_stone, ' камней мудрости и ', mag_krist, ' магических кристаллов')
    print('это ', elit_stih, ' элитных стих камней', el_water, ' воды и ', el_powder, ' порошка' )

def core(n: int):
    gems = n * 3
    el_polirol = 13900
    core_seb = 0
    print('Ядро:')
    print('Нужно: ', gems, ' каждого камня')
    print('это ', gems * 3, ' полир порошка или ', gems * 3 * el_polirol, ' кинар + ', n*12, ' эфира')

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

    return  fuel_seb

def art_stone(n: int):
    'функция расчета количества камней акт арт из стих камней'
    res = n // 22
    mag_kr = res * 3
    wis_stone = res * 5
    kat = 11 + mag_kr + wis_stone
    vortex = res * 16
    print("Всего получится ", res, 'камней акт арт. Остается стих камней: ', res % 22)
    print('маг кристаллов: ', mag_kr)
    print('кам мудрости: ', wis_stone)
    print('катализаторов: ', kat)
    print('эфира: ', vortex)

def ore(n: int):
    'функция расчета количества итемов, которые можно произвести из n слитков дрен руды'
    kol_op = n // 36
    kol_kozh = n // 29
    kol_sum = n // 65
    print('Можно сделать ', kol_op, ' опор или ', kol_kozh, ' кожухов')
    print('Или ', kol_sum, ' кожухов и опор')

# opora(1)
# kozhuh(1)
ore(1080)
# calculate(12)
# art_stone(210)