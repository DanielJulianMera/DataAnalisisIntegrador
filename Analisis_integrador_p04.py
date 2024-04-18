import requests

def descargar_y_guardar_csv(url, nombre_archivo = 'datos.csv'):
    
    # Realiza la petición GET
    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        # Abre un archivo para escribir en modo texto
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            archivo.write(respuesta.text)
        print(f'Archivo {nombre_archivo} guardado exitosamente.')
    else:
        print(f'Error al descargar los datos: código de estado {respuesta.status_code}')


url = "https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv"
nombre = "heart_faliure_text.csv"

descargar_y_guardar_csv(url, nombre)