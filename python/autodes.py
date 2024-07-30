import subprocess
import schedule
import time
import os

# Ruta correcta de IDM en tu sistema
idm_path = r"C:\Program Files (x86)\Internet Download Manager\IDMan.exe"

# URL del archivo a descargar
url = "https://fs.datosabiertos.mef.gob.pe/datastorefiles/2024-Gasto-Diario.csv"

# Ruta del archivo CSV local después de la descarga
csv_file = r"D:\prueba\2024-Gasto-Diario.csv"

def download_with_idm():
    # Comando para iniciar la descarga con IDM
    command = [idm_path, "/d", url, "/p", os.path.dirname(csv_file), "/f", os.path.basename(csv_file), "/n", "/s"]
    
    try:
        subprocess.run(command, check=True)
        print(f"Descarga iniciada correctamente con IDM. Archivo guardado como {csv_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error al iniciar la descarga con IDM: {e}")

def execute_sql_command():
    # Comando SQL para cargar datos desde el archivo CSV
    sql_command = f"""
    USE DBSalud;
    BULK INSERT GastoDiario
    FROM '{csv_file}'
    WITH (
        FIELDTERMINATOR = '","',  -- Delimitador de campo adecuado para tu archivo CSV
        ROWTERMINATOR = '\\n',     -- Delimitador de fila adecuado para tu archivo CSV
        FIRSTROW = 2,              -- Omitir la primera fila (encabezado)
        CODEPAGE = '65001',        -- Codificación UTF-8
        DATAFILETYPE = 'char'      -- Tipo de datos de archivo
    );
    """

    # Comando para ejecutar en SQL Server
    command = ["sqlcmd", "-S", "localhost", "-U", "angel", "-P", "Starwar1", "-Q", sql_command]


    try:
        subprocess.run(command, check=True)
        print("Comando SQL ejecutado correctamente.")
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el comando SQL: {e}")


# Programar la descarga todos los días a las 23:30 hora local de Lima
schedule.every().day.at("23:43").do(download_with_idm)
print("Descarga programada para las 23:43 hora local de Lima.")

# Programar la ejecución del comando SQL todos los días a las 23:33 hora local de Lima
schedule.every().day.at("23:59:50").do(execute_sql_command)
print("Comando SQL programado para las 23:48 hora local de Lima.")

# Bucle principal para mantener el script en ejecución
while True:
    schedule.run_pending()  # Ejecuta las tareas programadas pendientes
    time.sleep(1)  # Espera 1 segundo antes de volver a verificar las tareas programadas