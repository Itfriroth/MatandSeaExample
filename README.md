# Graphing examples with matplotlib and seaborn

import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.linspace(0, 10, 100)
y = np.sin(x)
categorias = ['A', 'B', 'C', 'D']
valores = [10, 20, 15,25]
a = np.linspace(0, 10, 25)
b = np.sin(a) + (a/2)
# 1---------------LINE SINGLE GRAPH--------------------
plt.figure(figsize=(8, 4))
plt.plot(x, y, label="sin(x)", color="blue", linestyle="--")
plt.title("Ejemplo de Gráfico de Línea")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True)
plt.show()
# ---------------LINE SINGLE GRAPH with mark--------------------
plt.figure(figsize=(8, 4))
fig, ax = plt.subplots()
ax.plot(x, y, marker = "o", markersize = 5, markerfacecolor = 'r', markeredgecolor = 'black')
plt.show()
# ---------------LINE SINGLE GRAPH with fmt--------------------
plt.figure(figsize=(8, 4))
fig, ax = plt.subplots()
ax.plot(x, y, "+g-")
plt.show()

fig, ax = plt.subplots()
ax.plot(x, y, marker = "+")
ax.plot(a, b, marker = "*")
plt.show()
# 2---------------BAR CHART-----------------------
