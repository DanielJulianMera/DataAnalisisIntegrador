import pandas as pd
import numpy as np
from datasets import load_dataset

"""
dataset = load_dataset("mstz/heart_failure")

# Se convierte en un DataFrame
data = pd.DataFrame(dataset["train"])
# Se convierte a CSV
data.to_csv("heart_failure.csv", index=False)
"""

# Se lee el DataFrame desde el archivo CSV
data = pd.read_csv("heart_failure.csv")

# DataFrame con personas Vivas
data_a = data[data["is_dead"] == 0]
# DataFrame con personas Muertas
data_b = data[data["is_dead"] == 1]

# Calculamos la edad promedio de cada DataFrame
data_a_edad = data_a["age"].mean()
data_b_edad = data_b["age"].mean()

# Verificamos el tipo de dato en cada columna e imprimimos
tipos = data.dtypes
print(f"los tipos de datos son:\n{tipos}\n")

# Cantidad de hombres y mujeres fumadores
fumadores = data[data["is_smoker"] == True]
cantidad_sexo = fumadores.groupby("is_male").size()
cantidad_sexo.index = ["Mujeres:", "Hombres:"]
print(f"La cantidad de fumadores por sexo es:\n{cantidad_sexo}")