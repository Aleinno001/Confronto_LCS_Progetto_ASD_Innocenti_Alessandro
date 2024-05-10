from approcci_lcs import ForzaBruta, Ricorsivo, RicorsivoConMemorizzazione, BottomUp
from time import time
import random
import string
import matplotlib.pyplot as plt


def randomword(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


x_number_axis = []
y_brute_force_axis = []
y_recursive_axis = []
y_recursive_memoization_axis = []
y_bottom_up_axis = []

for i in range(2,16):
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

plt.plot(x_number_axis, y_brute_force_axis)
plt.title('Forza Bruta')
plt.xlabel('Lunghezza stringhe (caratteri)')
plt.ylabel('Tempo impiegato (secondi)')
plt.show()

plt.plot(x_number_axis, y_recursive_axis)
plt.title('Ricorsivo')
plt.xlabel('Lunghezza stringhe (caratteri)')
plt.ylabel('Tempo impiegato (secondi)')
plt.show()

