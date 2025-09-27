import matplotlib
matplotlib.use("Agg")  # backend sin interfaz gráfica
import matplotlib.pyplot as plt
import numpy as np

# Pendiente y ordenada al origen
m = 2
b = 1

# Generar datos
x_vals = np.linspace(-10, 10, 200)
y_vals = m * x_vals + b

# Graficar
plt.figure(figsize=(6,4))
plt.plot(x_vals, y_vals, label=f"y = {m}x + {b}", color="blue")
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Recta")
plt.legend()
plt.grid(True)

# Guardar imagen
plt.savefig("recta.png")

# Señal para la API de que todo salió bien
resultado = "recta.png"
