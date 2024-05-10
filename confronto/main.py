import sys

from approcci_lcs import ForzaBruta, Ricorsivo, RicorsivoConMemorizzazione, BottomUp
from time import time
import random
import string
import matplotlib.pyplot as plt

sys.setrecursionlimit(999999999)

def randomword(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


x_number_axis = []
y_brute_force_axis = []
y_recursive_axis = []
y_recursive_memoization_axis = []
y_bottom_up_axis = []

auto_execution = True

response = input(
    "Vuoi eseguire il programma con i valori di default o proseguire con la modalità manuale?[M per mod. manuale/niente o altro per default]: ")
if response == 'M':
    auto_execution = False

if auto_execution:
    for i in range(1, 16):
        x_number_axis.append(i)

        random_word_s1 = randomword(i)
        random_word_s2 = randomword(i)

        t0 = time()
        ForzaBruta.get_lcs(random_word_s1, random_word_s2)
        t1 = time()
        y_brute_force_axis.append(t1 - t0)

        t0 = time()
        Ricorsivo.get_lcs(random_word_s1, random_word_s2)
        t1 = time()
        y_recursive_axis.append(t1 - t0)

        t0 = time()
        RicorsivoConMemorizzazione.get_lcs(random_word_s1, random_word_s2)
        t1 = time()
        y_recursive_memoization_axis.append(t1 - t0)

        t0 = time()
        BottomUp.get_lcs(random_word_s1, random_word_s2)
        t1 = time()
        y_bottom_up_axis.append(t1 - t0)
else:
    different_nm = False
    response = input(
        "Vuoi che le due stringhe su cui eseguire LCS siano della stessa lunghezza?[Digitare N per lunghezze diverse/niente o altro per stessa lunghezza]: ")
    if response == 'N':
        different_nm = True

    if different_nm:
        n = int(input("Inserisci la lunghezza delle stringhe: "))
        m = int(input("Inserisci la lunghezza delle stringhe: "))
    else:
        nfb = int(input(
            "Inserisci la lunghezza delle stringhe per l'algoritmo Forza-Bruta (è fortemente consigliato inserire un valore 0<n<21): "))
        nr = int(input(
            "Inserisci la lunghezza delle stringhe per l'algoritmo Ricorsivo (è fortemente consigliato inserire un valore 0<n<15): "))
        nrm = int(input(
            "Inserisci la lunghezza delle stringhe per l'algoritmo Ricorsivo con memorizzazione (è fortemente consigliato inserire un valore 100<n<500): "))
        nbu = int(input(
            "Inserisci la lunghezza delle stringhe per l'algoritmo Bottom-Up (è fortemente consigliato inserire un valore 100<n<700): "))

        for i in range(1, nfb + 1):
            x_number_axis.append(i)

            random_word_s1 = randomword(i)
            random_word_s2 = randomword(i)

            t0 = time()
            ForzaBruta.get_lcs(random_word_s1, random_word_s2)
            t1 = time()
            y_brute_force_axis.append(t1 - t0)

        for i in range(1, nr + 1):
            x_number_axis.append(i)

            random_word_s1 = randomword(i)
            random_word_s2 = randomword(i)

            t0 = time()
            Ricorsivo.get_lcs(random_word_s1, random_word_s2)
            t1 = time()
            y_recursive_axis.append(t1 - t0)

        for i in range(1, nrm + 1):
            x_number_axis.append(i)

            random_word_s1 = randomword(i)
            random_word_s2 = randomword(i)

            t0 = time()
            RicorsivoConMemorizzazione.get_lcs(random_word_s1, random_word_s2)
            t1 = time()
            y_recursive_memoization_axis.append(t1 - t0)

        for i in range(1, nbu + 1):
            x_number_axis.append(i)

            random_word_s1 = randomword(i)
            random_word_s2 = randomword(i)

            t0 = time()
            BottomUp.get_lcs(random_word_s1, random_word_s2)
            t1 = time()
            y_bottom_up_axis.append(t1 - t0)

plt.plot(y_brute_force_axis)
plt.title('Forza Bruta')
plt.xlabel('Lunghezza stringhe (caratteri)')
plt.ylabel('Tempo impiegato (secondi)')
plt.show()

plt.plot(y_recursive_axis)
plt.title('Ricorsivo')
plt.xlabel('Lunghezza stringhe (caratteri)')
plt.ylabel('Tempo impiegato (secondi)')
plt.show()

plt.plot(y_recursive_memoization_axis)
plt.title('Ricorsivo con memorizzazione')
plt.xlabel('Lunghezza stringhe (caratteri)')
plt.ylabel('Tempo impiegato (secondi)')
plt.show()

plt.plot(y_bottom_up_axis)
plt.title('Bottom Up')
plt.xlabel('Lunghezza stringhe (caratteri)')
plt.ylabel('Tempo impiegato (secondi)')
plt.show()
