import pandas as pd
import numpy as np
import datetime
from knapsack import knapsack

def data_p01():
    item_size = 10
    item_capacity = 165
    item_w = [23, 31, 29, 44, 53, 38, 63, 85, 89, 82]
    item_p = [92, 57, 49, 68, 60, 43, 67, 84, 87, 72]
    true_y = [1, 1, 1, 1, 0, 1, 0, 0, 0, 0]
    return item_size, item_capacity, item_w, item_p, true_y

def data_p02():
    item_size = 5
    item_capacity = 26
    item_w = [12, 7, 11, 8, 9]
    item_p = [24, 13, 23, 15, 16]
    true_y = [0, 1, 1, 1, 0]
    return item_size, item_capacity, item_w, item_p, true_y

def data_p03():
    item_size = 6
    item_capacity = 190
    item_w = [56, 59, 80, 64, 75, 17]
    item_p = [50, 50, 64, 46, 50, 5]
    true_y = [1, 1, 0, 0, 1, 0]
    return item_size, item_capacity, item_w, item_p, true_y

def data_p04():
    item_size = 7
    item_capacity = 50
    item_w = [31, 10, 20, 19, 4, 3, 6]
    item_p = [70, 20, 39, 37, 7, 5, 10]
    true_y = [1, 0, 0, 1, 0, 0, 0]
    return item_size, item_capacity, item_w, item_p, true_y

def data_p05():
    item_size = 8
    item_capacity = 104
    item_w = [25, 35, 45, 5, 25, 3, 2, 2]
    item_p = [350, 400, 450, 20, 70, 8, 5, 5]
    true_y = [1, 0, 1, 1, 1, 0, 1, 1]
    return item_size, item_capacity, item_w, item_p, true_y

def data_p06():
    # optimal weight : 169
    item_size = 7
    item_capacity = 170
    item_w = [41, 50, 49, 59, 55, 57, 60]
    item_p = [442, 525, 511, 593, 546, 564, 617]
    true_y = [0, 1, 0, 1, 0, 0, 1]
    return item_size, item_capacity, item_w, item_p, true_y

def data_p07():
    # optimal profit : 1458
    item_size = 15
    item_capacity = 750
    item_w = [70, 73, 77, 80, 82, 87, 90, 94, 98, 106, 110, 113, 115, 118, 120]
    item_p = [135, 139, 149, 150, 156, 163, 173, 184, 192, 201, 210, 214, 221, 229, 240]
    true_y = [1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1]
    return item_size, item_capacity, item_w, item_p, true_y

def data_p08():
    # optimal profit : 13549094
    item_size = 24
    item_capacity = 6404180
    item_w = [382745, 799601, 909247, 729069, 467902,
              44328, 34610, 698150, 823460, 903959,
              853665, 551830, 610856, 670702, 488960,
              951111, 323046, 446298, 931161, 31385,
              496951, 264724, 224916, 169684]
    item_p = [825594, 1677009, 1676628, 1523970, 943972,
              97426, 69666, 1296457, 1679693, 1902996,
              1844992, 1049289, 1252836, 1319836, 953277,
              2067538, 675367, 853655, 1826027, 65731,
              901489, 577243, 466257, 369261]
    true_y = [1, 1, 0, 1, 1, 1, 0, 0, 0, 1,
              1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
              0, 1, 1, 1]
    return item_size, item_capacity, item_w, item_p, true_y

item_size, item_capacity, item_w, item_p, true_y = data_p01()
knapsack_01 = knapsack(cross_over="one_point", mutation=0.5, population=100,
                        gene_method="general", next_parent=5,
                        selection="tournament", min_generation=200)
opcode, best_gene = knapsack_01.train(capacity=item_capacity, weight=item_w, price=item_p)
print(">> Best Gene : " + str(best_gene))
print(">> Optimal Answer : " + str(true_y))
print(">> Start Gene :" + str(knapsack_01.getStartGene()))
print(">> End Gene : " + str(knapsack_01.getEndGene()))