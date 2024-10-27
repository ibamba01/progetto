import timeit # per misurare i tempi di esecuzione
import random # per generare numeri casuali
import matplotlib.pyplot as plt # per i grafici
import pandas as pd # per i dataframe
import os # per gestire i file

# Importo le classi degli alberi
from ABR import Abr
from AlberiRossoNeri import Arn
from AlberiAVL import Avl

n = 5006 # 5006
step = 50 #
test_per_iteration = 5 # 30

# funzione per creare un array random
def random_array(num):
    array = []
    for j in range(0, num):
        array.append(j)
    random.shuffle(array)
    return array

# test per la misurazione dei tempi di inserimento
def test_insert_mesure(insert_fun, array):
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


# test per la misurazione dei tempi di ricerca del k-esimo elemento più piccolo
def test_os_mesure(os_function, length):
    k = length // 2  # in questo modo k è un elemento non troppo piccolo e non troppo grande
    t = timeit.timeit(stmt=lambda: os_function(k), number=test_per_iteration)
    return (t / test_per_iteration) * 1000  # tempo in ms


# test per la misurazione dei tempi di ricerca del rank di un elemento
def test_rank_mesure(rank_function, ric):
    return timeit.timeit(stmt=lambda: rank_function(ric),
                            number=test_per_iteration) / test_per_iteration * 1000  # tempo in ms)

def test(abr_insert,abr_kesimo,arn_insert,arn_kesimo,avl_insert,avl_kesimo, num, stepp):
    # creo le strutture dati
    abr = Abr()
    arn = Arn()
    avl = Avl()

    # test
    for i in range(5, num, stepp):

        arr = random_array(i)

        # test per la misurazione dei tempi di inserimento
        abr_insert.append(test_insert_mesure(abr.insert, arr))
        arn_insert.append(test_insert_mesure(arn.insert, arr))
        avl_insert.append(test_insert_mesure(avl.insert, arr))

        # test per la misurazione dei tempi di ricerca del k-esimo elemento più piccolo
        abr_kesimo.append(test_os_mesure(abr.kesimo, i)) # risolto
        arn_kesimo.append(test_os_mesure(arn.kesimo, i)) # risolto
        avl_kesimo.append(test_os_mesure(avl.kesimo, i)) # risolto

    abr = Abr()
    arn = Arn()
    avl = Avl()

    return abr_insert, abr_kesimo, arn_insert, arn_kesimo, avl_insert, avl_kesimo

# Funzione per svuotare una cartella
def svuota_cartella(cartella):
    file_lista = os.listdir(cartella)
    for file in file_lista:
        file_path = os.path.join(cartella, file)
        os.remove(file_path)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # test
    result = []

    # Serve per i grafici
    for i in range(5, n, step):
        result.append(i)

    abr_insert_times = [0.0] * len(result)
    arn_insert_times = [0.0] * len(result)
    avl_insert_times = [0.0] * len(result)
    abr_order_statistic_times = [0.0] * len(result)
    arn_order_statistic_times = [0.0] * len(result)
    avl_order_statistic_times = [0.0] * len(result)

    print("Parto con l'esecuzione dei test")

    for j in range(test_per_iteration):
        print("Test numero: ", (j+1), " di ", test_per_iteration)
        abr_temp_insert = []
        arn_temp_insert = []
        avl_temp_insert = []

        abr_temp_os = []
        arn_temp_os = []
        avl_temp_os = []

        abr_temp_insert, abr_temp_os, arn_temp_insert, arn_temp_os, avl_temp_insert, avl_temp_os = test(abr_temp_insert, abr_temp_os, arn_temp_insert,
                                                                                                        arn_temp_os, avl_temp_insert, avl_temp_os, n, step)

        for k in range(len(abr_temp_insert)):
            print("Iterazione numero: ", (k+1), " di ", len(abr_temp_insert))
            # Inserimento
            abr_insert_times[k] += abr_temp_insert[k]
            arn_insert_times[k] += arn_temp_insert[k]
            avl_insert_times[k] += avl_temp_insert[k]

            # Statistica D'Ordine
            abr_order_statistic_times[k] += abr_temp_os[k]
            arn_order_statistic_times[k] += arn_temp_os[k]
            avl_order_statistic_times[k] += avl_temp_os[k]
            # Rango

    print("faccio la media")
    # Calcolo la media
    for s in range(0, len(result)):
        # Inserimento
        abr_insert_times[s] /=  test_per_iteration
        arn_insert_times[s] /=  test_per_iteration
        avl_insert_times[s] /=  test_per_iteration

        # Statistica d'ordine
        abr_order_statistic_times[s] /=  test_per_iteration
        arn_order_statistic_times[s] /=  test_per_iteration
        avl_order_statistic_times[s] /=  test_per_iteration

    # Svuota la cartella "tabelle"
    svuota_cartella("tabelle")

    # Svuota la cartella "immagini"
    svuota_cartella("immagini")

    # Grafici test inserimento
    print("Creo i grafici")



    # Grafico inserimento albero binario
    plt.clf()
    plt.plot(result, abr_insert_times, color='green', label='Inserimento albero binario di ricerca')
    plt.xlabel('Dimensione dell\'array')
    plt.ylabel('Tempo di esecuzione (ms)')
    plt.title('Tempi inserimento albero binario')
    plt.legend()
    plt.savefig('immagini/abr_ins.png')
    plt.show()


    # Grafico inserimento albero rosso-nero
    plt.clf()
    plt.plot(result, arn_insert_times, color='red', label='Inserimento albero rosso-nero')
    plt.xlabel('Dimensione dell\'array')
    plt.ylabel('Tempo di esecuzione (ms)')
    plt.title('Tempi inserimento albero rosso-nero')
    plt.legend()
    plt.savefig('immagini/rbt_ins.png')
    plt.show()

    # Grafico inserimento albero AVL
    plt.clf()
    plt.plot(result, avl_insert_times, color='green', label='Inserimento albero AVL')
    plt.xlabel('Dimensione dell\'array')
    plt.ylabel('Tempo di esecuzione (ms)')
    plt.title('Tempi inserimento albero binario')
    plt.legend()
    plt.savefig('immagini/avl_ins.png')
    plt.show()

    # Grafico confronto tra i tre tempi di inserimento
    plt.clf()
    plt.plot(result, arn_insert_times, color='blue', label='Inserimento albero binario di ricerca')
    plt.plot(result, avl_insert_times, color='green', label='Inserimento albero AVL')
    plt.plot(result, arn_insert_times, color='red', label='Inserimento albero Rosso-nero')
    plt.xlabel('Dimensione dell\'array')
    plt.ylabel('Tempo di esecuzione (ms)')
    plt.title('Confronto tempi inserimento')
    plt.legend()
    plt.savefig('immagini/conf_ins.png')
    plt.show()

    # Creazione delle tabelle

    # Creazione delle liste dei dati per inserimento, ricerca k-esima statistica d'ordine e rank
    data_inserimento = {'Dimensione dell\'array': result, 'Albero binario di ricerca': arn_insert_times,
                        'Albero Rosso-nero': arn_insert_times, 'Albero AVL': avl_insert_times}
    df_ins = pd.DataFrame(data_inserimento)
    data_order_statistic = {'Dimensione dell\'array': result, 'Albero binario di ricerca': abr_order_statistic_times,
                            'Albero Rosso-nero': arn_order_statistic_times,
                            'Albero AVL': avl_order_statistic_times}
    df_os = pd.DataFrame(data_order_statistic)


    # Approssimazione dei tempi di esecuzione
    df_ins = df_ins.round(4)
    df_os = df_os.round(4)

    plt.clf()

    # Visualizzazione delle tabelle come immagini separate
    plt.figure(figsize=(10, 6))  # Imposta la dimensione dell'immagine

    # Tabella 1: Inserimento
    plt.title("Inserimento")
    plt.axis('off')  # Rimuove gli assi
    table1 = plt.table(cellText=df_ins.values, colLabels=df_ins.columns, loc='center')
    table1.auto_set_font_size(False)
    table1.set_fontsize(10)
    plt.savefig('tabelle/tabella_inserimento.png')  # Salva l'immagine della tabella di inserimento come file PNG
    plt.show()

    # Creazione di una nuova figura per la tabella di ricerca della k-esima statistica d'ordine
    plt.clf()
    plt.figure(figsize=(10, 6))
    plt.title("Ricerca K-esima Statistica d'Ordine")
    plt.axis('off')
    table2 = plt.table(cellText=df_os.values, colLabels=df_os.columns, loc='center')
    table2.auto_set_font_size(False)
    table2.set_fontsize(10)
    plt.savefig('tabelle/tabella_kesima_statistica_ordine.png')
    plt.show()
