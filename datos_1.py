import pandas as pd
import matplotlib.pyplot as plt

# Cargar CSV
df = pd.read_csv("usuarios_limpiesa.csv")

# Nombre exacto de la columna de tiempo en tu archivo
tiempo_col = "tiempo sesión"   # 👈 cámbialo si en tu CSV se llama distinto

# Limpiar datos
df = df.dropna(subset=["edad", tiempo_col])
df["edad"] = pd.to_numeric(df["edad"], errors="coerce")
df[tiempo_col] = pd.to_numeric(df[tiempo_col], errors="coerce")
df = df.dropna(subset=["edad", tiempo_col])

# Graficar
plt.scatter(df["edad"], df[tiempo_col], alpha=0.6)
plt.title("Relación entre Edad y Tiempo de Sesión")
plt.xlabel("Edad")
plt.ylabel("Tiempo de sesión (minutos)")
plt.grid(True)
plt.show()
