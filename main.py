import timeit # per misurare i tempi di esecuzione
import random # per generare numeri casuali
import matplotlib.pyplot as plt # per i grafici
import pandas as pd # per i dataframe
import os # per gestire i file

# Importo le classi degli alberi
from ABR import Abr
from AlberiRossoNeri import Arn
from AlberiAVL import Avl

n = 8005
step = 50
test_iteration = 5

# funzione per creare un array random
def random_array(num):
    array = []
    for j in range(0, num):
        array.append(j)
    random.shuffle(array)
    return array
def arraylist(num):
    return list(range(num))

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
    t = timeit.timeit(stmt=lambda: os_function(k), number=test_iteration)
    return (t / test_iteration) * 1000  # tempo in ms

def test_search_mesure(search_fun, length):
    k = random.randint(0, length - 1)
    t = timeit.timeit(stmt=lambda: search_fun(k), number=test_iteration)
    return (t / test_iteration) * 1000

def test(num, stepp):
    abr_insert = []
    avl_insert = []
    arn_insert = []

    arn_kesimo = []
    abr_kesimo = []
    avl_kesimo = []

    abr_search = []
    arn_search = []
    avl_search = []
    # inizializzo gli alberi
    abr = Abr()
    arn = Arn()
    avl = Avl()

    # test
    for i in range(5, num, stepp):
        print("test con array di dim:", i)
        # i è il numero di elementi presenti nell'array
        arr = random_array(i)

        # test per la misurazione dei tempi di inserimento
        abr_insert.append(test_insert_mesure(abr.insert, arr))
        arn_insert.append(test_insert_mesure(arn.insert, arr))
        avl_insert.append(test_insert_mesure(avl.insert, arr))

        # test per la misurazione dei tempi di ricerca del k-esimo elemento più piccolo
        abr_kesimo.append(test_os_mesure(abr.kesimo, i)) # risolto
        arn_kesimo.append(test_os_mesure(arn.kesimo, i)) # risolto
        avl_kesimo.append(test_os_mesure(avl.kesimo, i)) # risolto

        abr_search.append(test_search_mesure(abr.search, i))
        arn_search.append(test_search_mesure(arn.search, i))
        avl_search.append(test_search_mesure(avl.search, i))

    return abr_insert, abr_kesimo, arn_insert, arn_kesimo, avl_insert, avl_kesimo, abr_search, arn_search, avl_search

# Funzione per svuotare una cartella

def svuota_cartella(cartella):
    for root, dirs, files in os.walk(cartella):
        for file in files:
            file_path = os.path.join(root, file)
            os.remove(file_path)  # Elimina il file
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Set up")
    # set up dei grafici
    arrx = [] # indica la lunghezza dell'array, sarà la lunghezza delle ascisse e orsinate

    for i in range(5, n, step):
        arrx.append(i)
    # inizializzo gli array dei risultati a tipi float
    abr_insert_times = [0.0] * len(arrx)
    arn_insert_times = [0.0] * len(arrx)
    avl_insert_times = [0.0] * len(arrx)
    abr_order_statistic_times = [0.0] * len(arrx)
    arn_order_statistic_times = [0.0] * len(arrx)
    avl_order_statistic_times = [0.0] * len(arrx)
    abr_search_times = [0.0] * len(arrx)
    arn_search_times = [0.0] * len(arrx)
    avl_search_times = [0.0] * len(arrx)

    print("Inizio i test")

    for j in range(test_iteration):
        print("Test numero: ", (j+1), " di ", test_iteration)

        abr_temp_insert, abr_temp_os, arn_temp_insert, arn_temp_os, avl_temp_insert, avl_temp_os, abr_temp_search, arn_temp_search, avl_temp_search = test(n, step)

        for k in range(len(arrx)):
            print("riempio gli array ","[",(k+1), " di ", len(abr_temp_insert),"]")
            # Inserimento
            abr_insert_times[k] += abr_temp_insert[k]
            arn_insert_times[k] += arn_temp_insert[k]
            avl_insert_times[k] += avl_temp_insert[k]

            # Statistica D'Ordine
            abr_order_statistic_times[k] += abr_temp_os[k]
            arn_order_statistic_times[k] += arn_temp_os[k]
            avl_order_statistic_times[k] += avl_temp_os[k]

            abr_search_times[k] += abr_temp_search[k]
            arn_search_times[k] += arn_temp_search[k]
            avl_search_times[k] += avl_temp_search[k]

    print("faccio la media")
    # Calcolo la media
    for s in range(0, len(arrx)):
        # Inserimento
        abr_insert_times[s] /=  test_iteration
        arn_insert_times[s] /=  test_iteration
        avl_insert_times[s] /=  test_iteration

        # Statistica d'ordine
        abr_order_statistic_times[s] /=  test_iteration
        arn_order_statistic_times[s] /=  test_iteration
        avl_order_statistic_times[s] /=  test_iteration

        # Ricerca
        abr_search_times[s] /= test_iteration
        arn_search_times[s] /= test_iteration
        avl_search_times[s] /= test_iteration

    # svuoto le cartelle dei grafici
    svuota_cartella("tabelle")
    svuota_cartella("immagini")

    # creo i grafici
    print("Creo i grafici")



    # Grafico inserimento albero binario
    plt.clf()
    plt.plot(arrx, abr_insert_times, color='blue', label='Inserimento albero binario di ricerca')
    plt.xlabel('Dimensione dell\'array')
    plt.ylabel('Tempo di esecuzione (ms)')
    plt.title('Tempi inserimento albero binario')
    plt.legend()
    plt.savefig('immagini/insert/abr_ins.png')
    plt.show()


    # Grafico inserimento albero rosso-nero
    plt.clf()
    plt.plot(arrx, arn_insert_times, color='red', label='Inserimento albero rosso-nero')
    plt.xlabel('Dimensione dell\'array')
    plt.ylabel('Tempo di esecuzione (ms)')
    plt.title('Tempi inserimento albero rosso-nero')
    plt.legend()
    plt.savefig('immagini/insert/rbt_ins.png')
    plt.show()

    # Grafico inserimento albero AVL
    plt.clf()
    plt.plot(arrx, avl_insert_times, color='green', label='Inserimento albero AVL')
    plt.xlabel('Dimensione dell\'array')
    plt.ylabel('Tempo di esecuzione (ms)')
    plt.title('Tempi inserimento albero AVL')
    plt.legend()
    plt.savefig('immagini/insert/avl_ins.png')
    plt.show()

    # Grafico confronto tra i tre tempi di inserimento
    plt.clf()
    plt.plot(arrx, abr_insert_times, color='blue', label='Inserimento albero binario di ricerca')
    plt.plot(arrx, avl_insert_times, color='green', label='Inserimento albero AVL')
    plt.plot(arrx, arn_insert_times, color='red', label='Inserimento albero Rosso-nero')
    plt.xlabel('Dimensione dell\'array')
    plt.ylabel('Tempo di esecuzione (ms)')
    plt.title('Confronto tempi inserimento')
    plt.legend()
    plt.savefig('immagini/insert/conf_ins.png')
    plt.show()

    # Grafico ricerca k-esimo elemento più piccolo, Albero binario
    plt.clf()
    plt.plot(arrx, abr_order_statistic_times, color='blue', label='k esimo albero binario di ricerca')
    plt.xlabel('Dimensione dell\'array')
    plt.ylabel('Tempo di esecuzione (ms)')
    plt.title('Tempi di ricerca del k-esimo elemento più piccolo, albero binario')
    plt.legend()
    plt.savefig('immagini/order/abr_k.png')
    plt.show()

    # Grafico ricerca k-esimo elemento più piccolo, Albero rosso-nero
    plt.clf()
    plt.plot(arrx, arn_order_statistic_times, color='red', label='k esimo albero rosso-nero')
    plt.xlabel('Dimensione dell\'array')
    plt.ylabel('Tempo di esecuzione (ms)')
    plt.title('Tempi di ricerca del k-esimo elemento più piccolo, albero rosso-nero')
    plt.legend()
    plt.savefig('immagini/order/rbt_k.png')
    plt.show()

    # Grafico ricerca k-esimo elemento più piccolo, albero AVL
    plt.clf()
    plt.plot(arrx, avl_order_statistic_times, color='green', label='k esimo albero AVL')
    plt.xlabel('Dimensione dell\'array')
    plt.ylabel('Tempo di esecuzione (ms)')
    plt.title('Tempi di ricerca del k-esimo elemento più piccolo, albero AVL')
    plt.legend()
    plt.savefig('immagini/order/avl_k.png')
    plt.show()

    # Grafico confronto tra i tre tempi di ricerca k-esimo elemento più piccolo,
    plt.clf()
    plt.plot(arrx, abr_order_statistic_times, color='blue', label='k-esimo albero binario di ricerca')
    plt.plot(arrx, avl_order_statistic_times, color='green', label='k-esimo albero AVL')
    plt.plot(arrx, arn_order_statistic_times, color='red', label='k-esimo albero Rosso-nero')
    plt.xlabel('Dimensione dell\'array')
    plt.ylabel('Tempo di esecuzione (ms)')
    plt.title('Confronto tempi di ricerca del k-esimo elemento più piccolo')
    plt.legend()
    plt.savefig('immagini/order/conf_k.png')
    plt.show()

    # Grafico ricerca elemento, Albero binario
    plt.clf()
    plt.plot(arrx, abr_search_times, color='blue', label='k esimo albero binario di ricerca')
    plt.xlabel('Dimensione dell\'array')
    plt.ylabel('Tempo di esecuzione (ms)')
    plt.title('Tempi di ricerca di un elemento, albero binario')
    plt.legend()
    plt.savefig('immagini/search/abr_search.png')
    plt.show()

    # Grafico ricerca elemento, Albero rosso-nero
    plt.clf()
    plt.plot(arrx, arn_search_times, color='red', label='k esimo albero rosso-nero')
    plt.xlabel('Dimensione dell\'array')
    plt.ylabel('Tempo di esecuzione (ms)')
    plt.title('Tempi di ricerca di un elemento, albero rosso-nero')
    plt.legend()
    plt.savefig('immagini/search/rbt_search.png')
    plt.show()

    # Grafico ricerca elemento, Albero AVL
    plt.clf()
    plt.plot(arrx, avl_search_times, color='green', label='k esimo albero AVL')
    plt.xlabel('Dimensione dell\'array')
    plt.ylabel('Tempo di esecuzione (ms)')
    plt.title('Tempi di ricerca di un elemento, albero AVL')
    plt.legend()
    plt.savefig('immagini/search/avl_search.png')
    plt.show()

    # Grafico confronto tra i tre tempi di ricerca k-esimo elemento più piccolo,
    plt.clf()
    plt.plot(arrx, abr_search_times, color='blue', label='k-esimo albero binario di ricerca')
    plt.plot(arrx, avl_search_times, color='green', label='k-esimo albero AVL')
    plt.plot(arrx, arn_search_times, color='red', label='k-esimo albero Rosso-nero')
    plt.xlabel('Dimensione dell\'array')
    plt.ylabel('Tempo di esecuzione (ms)')
    plt.title('Confronto tempi di ricerca di un elemento')
    plt.legend()
    plt.savefig('immagini/search/conf_search.png')
    plt.show()



    # Creazione delle tabelle

    # Creazione delle liste dei dati per inserimento, ricerca k-esima statistica d'ordine e rank
    data_inserimento = {'Dimensione dell\'array': arrx,
                        'Albero binario di ricerca': abr_insert_times,
                        'Albero Rosso-nero': arn_insert_times,
                        'Albero AVL': avl_insert_times }
    df_ins = pd.DataFrame(data_inserimento)

    data_order_statistic = {'Dimensione dell\'array': arrx,
                            'Albero binario di ricerca': abr_order_statistic_times,
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
