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
            return "child"
        elif edad <= 19:
            return "teen"
        elif edad <= 39:
            return "young adult"
        elif edad <= 59:
            return "adult"
        else:
            return "older adult"

    if "age" in df.columns:
        # Crea la nueva columna 'age category' sin insertarla aún
        df["age category"] = df["age"].apply(categorizar_edad)
    
        # Encuentra el índice de la columna 'age'
        age_index = df.columns.get_loc("age")

        # Inserta la nueva columna después de 'age'
        df.insert(age_index + 1, 'age category', df.pop('age category'))

        # Guardar el DataFrame resultante en un archivo CSV
        df.to_csv(nombre_nuevo, index=False)

# Usamos la función
procesar_dataframe("heart_faliure_text.csv", "heart_faliure_limpio.csv")