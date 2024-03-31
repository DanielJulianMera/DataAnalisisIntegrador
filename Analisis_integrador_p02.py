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

# DataFrame con pacientes vivos
data_a = data[data["is_dead"] == 0]
#Edad promedio de pacientes vivos
age_prom_a = data_a["age"].mean()

# DataFrame con pacientes muertos
data_b = data[data["is_dead"] == 1]
#Edad promedio de pacientes vivos
age_prom_b = data_b["age"].mean()

# Calculamos la edad promedio de cada DataFrame y se imprime
print("La edad promedio de los pacientes Vivos es: ", round(age_prom_a))
print("La edad promedio de los pacientes Muertos es: ", round(age_prom_b))