import numpy as np
import random
from collections import Counter
t0 = 100
delta = 0.9
t1 = t0*delta
opening = 8
closing = 10
tables = 4
clients = [[8, 8.5, 25],
            [8.2, 9, 20],
            [8, 8.3, 15],
            [8, 9, 40],
            [8.2, 9, 30],
            [8.5, 9.3, 60],
            [8.9, 9.4, 20],
            [9, 9.5, 20],
            [8.5, 9.3, 30],
            [9, 9.3, 10],
            [9.5, 9.9, 40],
            [8, 9.9, 50],
            [8.8, 9.4, 25],
            [9, 9.5, 20]]
time = []

for index, i in enumerate(clients):
    time.append([])
    start = (i[0]- opening)*10
    end = (i[1]- opening)*10
    for j in range(20):
        if j >= start and j<end:
            time[index].append(1)
        else:
            time[index].append(0)
time = np.array(time).reshape(14,20)



def subject(chosen,tables):
    col_table=  []
    for i in range((closing-opening)*10):
        col_sum = 0
        for j in range(len(time)):
            col_sum += time[j][i]*chosen[j]
        col_table.append(col_sum)
    if all(list(map(lambda x: True if x<=tables else False, col_table))):
        return True

def generate_chosen(tables):
    chosen = []
    while True:
        chosen =[]
        for i in range(len(clients)):
            chosen.append(bool(random.getrandbits(1)))
        if subject(chosen, tables):
            break
    return chosen

def compute_income(chosen):
    income = 0
    for index, i in enumerate(clients):
        income += i[2]*chosen[index]
    return income

def generate_tabu(tabu, last_chosen,taboos = 5, neighbours=3):
    tabu_list = [[] for i in range(taboos)]
    chosen_list = []
    for i in range(taboos):
        while True:
            tabu_list[i] = []
            for j in range(neighbours):
                r =random.choice(range(len(last_chosen)))
                tabu_list[i].append(r)

            new_chosen = last_chosen[:]
            # print(f'ostatni  {last_chosen}')
            for j in range(neighbours):
                new_chosen[tabu_list[i][j]] = not new_chosen[tabu_list[i][j]]

            duplicate = 0
            for j in tabu_list[i]:
                duplicate += tabu_list[i].count(j)
            if duplicate>3: 
                continue

            duplicate = 0
            for j in tabu:
                duplicate += tabu_list.count(j[0])
            if duplicate>0:
                continue
        
            if subject(new_chosen, tables):
                chosen_list.append(new_chosen)
                break
    return tabu_list, chosen_list


def tabu_search():
    iter = 100
    tabu_lst = 3
    tab_iter = 5
    tabu_list = []
    start = generate_chosen(tables)
    start_income = compute_income(start)
    print(f'start income is {start_income}')

    counter = 0
    for j in range(iter):
        new_tabu = generate_tabu(tabu_list, start)
        
    
        temp_value = 0
        for index, i in enumerate(new_tabu[1]):
            start = i
            inc = compute_income(i)
            if inc > start_income:
                start_income = inc
                temp_value = new_tabu[0][index]
                print(f'New highest income is: {start_income}')
        
        for index, i in enumerate(tabu_list):
            i[1]+=1

            if i[1] == tab_iter:
                del tabu_list[index]

            
        if temp_value != 0:
            tabu_list.append([temp_value])
            tabu_list[-1].append(0)
        # print(tabu_list)
        

tabu_search()