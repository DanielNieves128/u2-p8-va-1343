import numpy as np
import matplotlib.pyplot as plt

diasX = ["lunes","martes","miercoles","jueves","viernes"]
califa_va_y = [5,6,3,8,10]

plt.bar(diasX,califa_va_y)
plt.title("Calificaciones 3en VA de Daniel Nieves NC = 1343")
plt.xlabel("dias de la semana abril")
plt.ylabel("calificaciones en VA")
plt.grid()
plt.show()