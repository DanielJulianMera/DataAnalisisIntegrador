import pandas as pd
import sys
import requests

def descargar_y_guardar_csv(url, nombre_csv='datos.csv'):

    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()  # Lanza una excepción para códigos de estado 4xx/5xx
    except requests.RequestException as e:
        print(f'Error al descargar los datos: {e}')
        return

    # Guardar respuesta en archivo
    with open(nombre_csv, 'w', encoding='utf-8') as archivo:
        archivo.write(respuesta.text)
    print(f'Archivo {nombre_csv} guardado exitosamente.')

    procesar_dataframe(nombre_csv)

def procesar_dataframe(nombre_csv = "datos.csv"):
    
    # Convertir el archivo en DataFrame
    try:
        df = pd.read_csv(nombre_csv)
    except Exception as e:
        print(f"Error al leer los datos desde {nombre_csv}: {e}")
        return

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
    df.to_csv(nombre_csv, index=False)
    print(f'Archivo {nombre_csv} procesado exitosamente.')

if __name__ == '__main__':
    # Verificar al menos la presencia del segundo argumento (URL)
    if len(sys.argv) < 2:
        print("Uso: python script.py <URL> [nombre_csv]")
        sys.exit(1)

    # Capturar la URL
    url = sys.argv[1]

    # Verificar si se proporcionó el nombre del archivo como tercer argumento
    if len(sys.argv) >= 3:
        nombre_csv = sys.argv[2]
    else:
        nombre_csv = 'datos.csv'

    descargar_y_guardar_csv(url, nombre_csv)