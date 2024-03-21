import pandas as pd
import numpy as np
from datasets import load_dataset

dataset = load_dataset("mstz/heart_failure")

# Se convierte en un DataFrame
data = pd.DataFrame(dataset["train"])

# DataFrame con personas Vivas
data_a = data[data["is_dead"] == 0]

# DataFrame con personas Muertas
data_b = data[data["is_dead"] == 1]

# Calculamos la edad promedio de cada DataFrame y se imprime
print("La edad promedio de los pacientes Vivos es: ", data_a["age"].mean())
print("La edad promedio de los pacientes Muertos es: ", data_b["age"].mean())


