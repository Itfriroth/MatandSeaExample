# Graphing examples with matplotlib and seaborn

import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.linspace(0, 10, 100)
y = np.sin(x)
categorias = ['A', 'B', 'C', 'D']
valores = [10, 20, 15,25]
etiquetas = ["No Have", "Cars", "Motorcycle","Bicycle"]
a = np.linspace(0, 10, 25)
b = np.sin(a) + (a/2)

# 1---------------LINE SINGLE GRAPH--------------------
plt.figure(figsize=(8, 4))
plt.plot(x, y, label="sin(x)", color="blue", linestyle="--")
plt.title("Ejemplo de Gráfico de Línea")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
#grid simple
plt.grid(True)
plt.show()

# ---------------LINE SINGLE GRAPH with mark--------------------
plt.figure(figsize=(8, 4))
fig, ax = plt.subplots()
ax.plot(x, y, marker = "o", markersize = 5, markerfacecolor = 'r', markeredgecolor = 'black')
#grid for "x"
ax.grid(axis = "x")
plt.show()

# ---------------LINE SINGLE GRAPH with fmt--------------------
plt.figure(figsize=(8, 4))
fig, ax = plt.subplots()
ax.plot(x, y, "+g-")
#grid for "y"
ax.grid(axis = "y")
plt.show()

# ---------------LINE DOUBLE GRAPH --------------------
fig, ax = plt.subplots()
ax.plot(x, y, label = "Sin(x) + x/2", marker = "+")
ax.plot(a, b, label = "Cos(a) + a/2", marker = "*")
ax.legend()
#with secondary grid
ax.grid(which = "minor")
ax.minorticks_on()
plt.show()

# ---------------STEP PLOT GRAPH --------------------
plt.figure(figsize=(8, 4))
fig, ax = plt.subplots()
ax.bar(x = x, height = y)
plt.show()

# ---------------LINE GRAPH FULL-------------------- 
plt.figure(figsize=(8, 4))
fig, ax = plt.subplots()
ax.bar(x = x, height = y)
#grid with color
ax.grid(color = "red")
plt.show()

# 2---------------BAR CHART-----------------------
fig, ax = plt.subplots()
ax.bar(x = categorias, height = valores)
#grid with color and axis below
ax.grid(color = "red")
ax.set_axisbelow(True)
plt.show()

# ---------------BAR CHART WITH LABELS-----------------------

fig, ax = plt.subplots()
ax.bar(x = categorias, height = valores, tick_label = etiquetas)
#grid with color and linestyle
ax.grid(color = "green",linestyle = "dashed")
plt.show()

# ---------------BAR CHART TYPE LOG-----------------------

fig, ax = plt.subplots()
ax.bar(x = categorias, height = valores, log = True)
#grid thickness
ax.grid(which = "major", linewidth = 1)
ax.grid(which = "minor", linewidth = 0.3)
ax.minorticks_on()
plt.show()

# ---------------BARH CHART -----------------------

fig, ax = plt.subplots()
ax.barh(y = categorias, width = valores,color = "green",edgecolor = "darkseagreen")
# grid transparency
ax.grid(linewidth = 1.7, alpha = 0.35)
plt.show()




