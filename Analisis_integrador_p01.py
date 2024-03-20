import numpy as np
from datasets import load_dataset

dataset = load_dataset("mstz/heart_failure")

data = dataset["train"]

# Estructura del Dataset
# Dataset({
#     features: [
#         'age',
#         'has_anaemia',
#         'creatinine_phosphokinase_concentration_in_blood',
#         'has_diabetes',
#         'heart_ejection_fraction',
#         'has_high_blood_pressure',
#         'platelets_concentration_in_blood',
#         'serum_creatinine_concentration_in_blood', 
#         'serum_sodium_concentration_in_blood',
#         'is_male', 'is_smoker',
#         'days_in_study',
#         'is_dead'
#     ],
#     num_rows: 299
# })

# Convertir la columna en un arreglo unidimensional
edad = np.array(data["age"])

# Arreglo de edades:
# edades = np.array([75, 55, 65, 50, 65, 90, 75, 60, 65, 80, 75, 62, 45, 50, 49, 82, 87, 45, 70, 48, 65, 65, 68, 53,
#                     75, 80, 95, 70, 58, 82, 94, 85, 50, 50, 65, 69, 90, 82, 60, 60, 70, 50, 70, 72, 60, 50, 51, 60,
#                     80, 57, 68, 53, 60, 70, 60, 95, 70, 60, 49, 72, 45, 50, 55, 45, 45, 60, 42, 72, 70, 65, 41, 58,
#                     85, 65, 69, 60, 70, 42, 75, 55, 70, 67, 60, 79, 59, 51, 55, 65, 44, 57, 70, 60, 42, 60, 58, 58,
#                     63, 70, 60, 63, 65, 75, 80, 42, 60, 72, 55, 45, 63, 45, 85, 55, 50, 70, 60, 58, 60, 85, 65, 86,
#                     60, 66, 60, 60, 60, 43, 46, 58, 61, 53, 53, 60, 46, 63, 81, 75, 65, 68, 62, 50, 80, 46, 50, 61,
#                     72, 50, 52, 64, 75, 60, 72, 62, 50, 50, 65, 60, 52, 50, 85, 59, 66, 45, 63, 50, 45, 80, 53, 59,
#                     65, 70, 51, 52, 70, 50, 65, 60, 69, 49, 63, 55, 40, 59, 65, 75, 58, 60, 50, 60, 60, 40, 80, 64,
#                     50, 73, 45, 77, 45, 65, 50, 60, 63, 45, 70, 60, 78, 50, 40, 85, 60, 49, 70, 50, 78, 48, 65, 73,
#                     70, 54, 68, 55, 73, 65, 42, 47, 58, 75, 58, 55, 65, 72, 60, 70, 40, 53, 53, 77, 75, 70, 65, 55,
#                     70, 65, 40, 73, 54, 61, 55, 64, 40, 53, 50, 55, 50, 70, 53, 52, 65, 58, 45, 53, 55, 62, 65, 68,
#                     61, 50, 55, 56, 45, 40, 44, 51, 67, 42, 60, 45, 70, 70, 50, 55, 70, 70, 42, 65, 50, 55, 60, 45,
#                     65, 90, 45, 60, 52, 63, 62, 55, 45, 45, 50])

# Imprimir la edad promedio
print("Edad Promedio:", np.mean(edad))
# output: Edad Promedio: 60.82943143812709
