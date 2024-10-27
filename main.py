import timeit
import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

from ABR import Abr
from AlberiRossoNeri import Arn
from AlberiAVL import Avl

n = 5006
step = 50
test_per_iteration = 30

# funzione per creare un array random
def random_array(n):
    array = []
    for i in range(0, n):
        array.append(i)
    random.shuffle(array)
    return array

def test_inser_mesure(insert_fun, array):
    # times è una lista che contiene i tempi di esecuzione di insert_fun per ogni elemento di array
    times = []
    # t è la somma dei tempi di esecuzione di insert_fun per ogni elemento di array
    t = 0
    # per ogni elemento di array calcolo il tempo di esecuzione di insert_fun
    for i in range(len(array)):
        # stmt=lambsda consente di eseguire un funzione all'interno di una funzione anonima per non avere problemi di sintaassi
        times.append(timeit.timeit(stmt=lambda: insert_fun(array[i]), number=1)) # number=1 significa che esegue la funzione una volta
        t += times[i]
    return (t / len(array)) * 1000 # è la media dei tempi di esecuzione in millisecondi

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # test
    AAA = Abr()


