import sys
import webbrowser

from approcci_lcs import get_brute_force_lcs, get_ric_lcs, get_ric_mem_lcs, get_bottom_up_lcs
from time import time_ns
import random
import string
from matplotlib.pyplot import figure
import mpld3


sys.setrecursionlimit(999999999)


def randomword(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


def get_input_integer(text):
    while True:
        try:
            r = int(input(text))
            if r > 0:
                return r
            else:
                print("Inserisci un numero intero positivo")
        except ValueError:
            print("Inserisci un numero intero valido")


def graph_plot(y_axis, title):
    fig = figure()
    ax = fig.gca()
    ax.plot(y_axis)
    ax.set_title(title)
    ax.set_xlabel('Lunghezza in caratteri')
    ax.set_ylabel('Tempo impiegato (secondi)')
    html_str = mpld3.fig_to_html(fig)
    with open(title+'.html', 'w') as html_file:
        html_file.write(html_str)


x_brute_force_axis = []
x_recursive_axis = []
x_recursive_memoization_axis = []
x_bottom_up_axis = []
y_brute_force_axis = []
y_recursive_axis = []
y_recursive_memoization_axis = []
y_bottom_up_axis = []

auto_execution = False

response1 = input(
    "Vuoi eseguire il programma con i valori di default?[Digitare [S] se si/ altro o niente per mod. manuale]: ")
if response1 == 'S':
    auto_execution = True

if auto_execution:
    for i in range(1, 17):
        x_brute_force_axis.append(i)
        x_recursive_axis.append(i)
        x_recursive_memoization_axis.append(i)
        x_bottom_up_axis.append(i)

        random_word_s1 = randomword(i)
        random_word_s2 = randomword(i)

        t0 = time_ns() / (10 ** 9)
        get_brute_force_lcs(random_word_s1, random_word_s2)
        t1 = time_ns() / (10 ** 9)
        y_brute_force_axis.append(t1 - t0)

        t0 = time_ns() / (10 ** 9)
        get_ric_lcs(random_word_s1, random_word_s2)
        t1 = time_ns() / (10 ** 9)
        y_recursive_axis.append(t1 - t0)

        t0 = time_ns() / (10 ** 9)
        get_ric_mem_lcs(random_word_s1, random_word_s2)
        t1 = time_ns() / (10 ** 9)
        y_recursive_memoization_axis.append(t1 - t0)

        t0 = time_ns() / (10 ** 9)
        get_bottom_up_lcs(random_word_s1, random_word_s2)
        t1 = time_ns() / (10 ** 9)
        y_bottom_up_axis.append(t1 - t0)
else:
    different_nm = False
    response2 = input(
        "Vuoi mantenere le lunghezze delle stringhe uguali(m=n)?[Digitare [S] se si/altro o niente per mantenere la lunghezza minore fissa e variare la lunghezza dell'altra stringa]:")
    if response2 == 'S':
        different_nm = True

    if different_nm:
        nfb = get_input_integer(
            "Inserisci il range della lunghezza delle stringhe per l'algoritmo Forza-Bruta (è fortemente consigliato inserire un valore 9<n<21): ")
        nr = get_input_integer(
            "Inserisci il range della lunghezza delle stringhe per l'algoritmo Ricorsivo (è fortemente consigliato inserire un valore 9<n<15): ")
        nrm = get_input_integer(
            "Inserisci il range della lunghezza delle stringhe per l'algoritmo Ricorsivo con memorizzazione (è fortemente consigliato inserire un valore 50<n<500): ")
        nbu = get_input_integer(
            "Inserisci il range della lunghezza delle stringhe per l'algoritmo Bottom-Up (è fortemente consigliato inserire un valore 50<n<700): ")

        for i in range(1, nfb + 1):
            x_brute_force_axis.append(i)

            random_word_s1 = randomword(i)
            random_word_s2 = randomword(i)

            t0 = time_ns() / (10 ** 9)
            get_brute_force_lcs(random_word_s1, random_word_s2)
            t1 = time_ns() / (10 ** 9)
            y_brute_force_axis.append(t1 - t0)

        for i in range(1, nr + 1):
            x_recursive_axis.append(i)

            random_word_s1 = randomword(i)
            random_word_s2 = randomword(i)

            t0 = time_ns() / (10 ** 9)
            get_ric_lcs(random_word_s1, random_word_s2)
            t1 = time_ns() / (10 ** 9)
            y_recursive_axis.append(t1 - t0)

        for i in range(1, nrm + 1):
            x_recursive_memoization_axis.append(i)

            random_word_s1 = randomword(i)
            random_word_s2 = randomword(i)

            t0 = time_ns() / (10 ** 9)
            get_ric_mem_lcs(random_word_s1, random_word_s2)
            t1 = time_ns() / (10 ** 9)
            y_recursive_memoization_axis.append(t1 - t0)

        for i in range(1, nbu + 1):
            x_bottom_up_axis.append(i)

            random_word_s1 = randomword(i)
            random_word_s2 = randomword(i)

            t0 = time_ns() / (10 ** 9)
            get_bottom_up_lcs(random_word_s1, random_word_s2)
            t1 = time_ns() / (10 ** 9)
            y_bottom_up_axis.append(t1 - t0)
    else:
        fixed_mfb = get_input_integer(
            "Inserisci la lunghezza fissa della stringa più corta per l'algoritmo Forza-Bruta: ")
        nfb = get_input_integer(
            "Inserisci il range della lunghezza della stringa per l'algoritmo Forza-Bruta (di default/inserimento valore erraro sarà maggiore del valore precedentemente inserito): ")
        if nfb <= fixed_mfb:
            nfb = fixed_mfb + 1
        fixed_mr = get_input_integer("Inserisci la lunghezza fissa della stringa più corta per l'algoritmo Ricorsivo: ")
        nr = get_input_integer(
            "Inserisci il range della lunghezza della stringa per l'algoritmo Ricorsivo (di default/inserimento valore erraro maggiore del valore precedentemente inserito): ")
        if nr <= fixed_mr:
            nr = fixed_mr + 1
        fixed_mrm = get_input_integer(
            "Inserisci la lunghezza fissa della stringa più corta per l'algoritmo Ricorsivo con memorizzazione: ")
        nrm = get_input_integer(
            "Inserisci il range della lunghezza della stringa per l'algoritmo Ricorsivo con memorizzazione (di default/inserimento valore erraro maggiore del valore precedentemente inserito): ")
        if nrm <= fixed_mrm:
            nrm = fixed_mrm + 1
        fixed_mbu = get_input_integer(
            "Inserisci la lunghezza fissa della stringa più corta per l'algoritmo Bottom-Up: ")
        nbu = get_input_integer(
            "Inserisci il range della lunghezza della stringa per l'algoritmo Bottom-Up (di default/inserimento valore erraro maggiore del valore precedentemente inserito): ")
        if nbu <= fixed_mbu:
            nbu = fixed_mbu + 1

        fixed_random_word = randomword(fixed_mfb)
        for i in range(nfb + 1):
            x_brute_force_axis.append(i)

            random_word_s2 = randomword(i)

            t0 = time_ns() / (10 ** 9)
            get_brute_force_lcs(fixed_random_word, random_word_s2)
            t1 = time_ns() / (10 ** 9)
            y_brute_force_axis.append(t1 - t0)

        fixed_random_word = randomword(fixed_mr)
        for i in range(nr + 1):
            x_recursive_axis.append(i)

            random_word_s2 = randomword(i)

            t0 = time_ns() / (10 ** 9)
            get_ric_lcs(fixed_random_word, random_word_s2)
            t1 = time_ns() / (10 ** 9)
            y_recursive_axis.append(t1 - t0)

        fixed_random_word = randomword(fixed_mrm)
        for i in range(nrm + 1):
            x_recursive_memoization_axis.append(i)

            random_word_s2 = randomword(i)

            t0 = time_ns() / (10 ** 9)
            get_ric_mem_lcs(fixed_random_word, random_word_s2)
            t1 = time_ns() / (10 ** 9)
            y_recursive_memoization_axis.append(t1 - t0)

        fixed_random_word = randomword(fixed_mbu)
        for i in range(nbu + 1):
            x_bottom_up_axis.append(i)

            random_word_s2 = randomword(i)

            t0 = time_ns() / (10 ** 9)
            get_bottom_up_lcs(fixed_random_word, random_word_s2)
            t1 = time_ns() / (10 ** 9)
            y_bottom_up_axis.append(t1 - t0)

fig = figure()
ax = fig.gca()
ax.plot(x_brute_force_axis, y_brute_force_axis, label='Forza-Bruta')
ax.plot(x_recursive_axis, y_recursive_axis, label='Ricorsivo')
ax.plot(x_recursive_memoization_axis, y_recursive_memoization_axis, label='Ric. con memorizzazione')
ax.plot(x_bottom_up_axis, y_bottom_up_axis, label='Bottom-Up')
ax.set_title('Confronto diretto dei 4 approcci')
ax.set_xlabel('Lunghezza stringhe (caratteri)')
ax.set_ylabel('Tempo impiegato (secondi)')
ax.legend()
html_str = mpld3.fig_to_html(fig)
with open('confrontoDiretto.html', 'w') as html_file:
    html_file.write(html_str)
webbrowser.open('confrontoDiretto.html')

graph_plot(y_brute_force_axis, 'Forza Bruta')
webbrowser.open('Forza Bruta.html')
graph_plot(y_recursive_axis, 'Ricorsivo')
webbrowser.open('Ricorsivo.html')
graph_plot(y_recursive_memoization_axis, 'Ricorsivo con memorizzazione')
webbrowser.open('Ricorsivo con memorizzazione.html')
graph_plot(y_bottom_up_axis, 'Bottom Up')
webbrowser.open('Bottom Up.html')
