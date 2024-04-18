import pandas as pd

def procesar_dataframe(nombre_archivo, nombre_nuevo = "datos.csv"):

    # Convertir el archivo en DataFrame
    df = pd.read_csv(nombre_archivo, index_col = False)

    # Verificar y eliminar valores faltantes
    if df.isnull().values.any():
        df = df.dropna()

    # Eliminar filas duplicadas
    df = df.drop_duplicates()

    # Detectar y eliminar valores atípicos utilizando el método IQR
    for columna in df.select_dtypes(include=["number"]).columns:  # Solo considerar columnas numéricas
        Q1 = df[columna].quantile(0.25)
        Q3 = df[columna].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        df = df[(df[columna] >= lower_bound) & (df[columna] <= upper_bound)]

    # Crear una columna que categorice por edades
    def categorizar_edad(edad):
        if edad <= 12:
            return "Niño"
        elif edad <= 19:
            return "Adolescente"
        elif edad <= 39:
            return "Jóvenes adulto"
        elif edad <= 59:
            return "Adulto"
        else:
            return "Adulto mayor"

    if "Edad" in df.columns:
        df["Categoría Edad"] = df["Edad"].apply(categorizar_edad)

    # Guardar el DataFrame resultante en un archivo CSV
    df.to_csv(nombre_nuevo, index=False)

# Usamos la función
procesar_dataframe("heart_faliure_text.csv", "hert_faliure_limpio.csv")