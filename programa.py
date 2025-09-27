import matplotlib.pyplot as plt
import numpy as np

# Definir la recta: y = m*x + b
m = 2   # pendiente
b = 1   # ordenada al origen

# Crear un rango de valores de x
x = np.linspace(-10, 10, 100)

# Calcular y
y = m * x + b

# Graficar
plt.figure(figsize=(6, 4))
plt.plot(x, y, label=f"y = {m}x + {b}", color="blue")

# Ejes
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)

# Estética
plt.xlabel("x")
plt.ylabel("y")
plt.title("Gráfico de una recta")
plt.legend()
plt.grid(True)
plt.show()
