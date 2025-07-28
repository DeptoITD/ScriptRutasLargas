import os
import csv

# -------------------------------------------
# CONFIGURACIÓN
# -------------------------------------------

# Definimos el límite de caracteres permitido por ruta en sistemas Windows (convención clásica)
limite_caracteres = 260

# Solicitamos al usuario la ruta raíz que se desea analizar
ruta_base = input("Ingresa la ruta que deseas analizar: ").strip()

# Verificamos que la ruta ingresada exista en el sistema de archivos
if not os.path.exists(ruta_base):
    print(f"❌ La ruta '{ruta_base}' no existe.")
    exit()  # Terminamos el script si la ruta no es válida

# Nombre del archivo CSV que se generará con las rutas que exceden el límite
archivo_csv = "rutas_largas.csv"

# Lista donde se almacenarán los elementos (archivos o carpetas) que exceden el límite
elementos_largos = []

# -------------------------------------------
# RECORRIDO DEL SISTEMA DE ARCHIVOS
# -------------------------------------------

print(f"\n📂 Recorriendo: {ruta_base}\n")

# Recorremos de forma recursiva todas las carpetas y archivos usando os.walk()
for carpeta_raiz, subcarpetas, archivos in os.walk(ruta_base):
    
    # --- Evaluación de la carpeta actual ---
    ruta_carpeta = carpeta_raiz  # Ruta absoluta de la carpeta actual
    largo_carpeta = len(ruta_carpeta)  # Cantidad de caracteres en la ruta
    print(f"[Carpeta] {largo_carpeta} caracteres | {ruta_carpeta}")
    
    # Si la ruta de la carpeta supera el límite, la guardamos
    if largo_carpeta > limite_caracteres:
        elementos_largos.append(["Carpeta", largo_carpeta, ruta_carpeta])

    # --- Evaluación de cada archivo dentro de la carpeta actual ---
    for archivo in archivos:
        ruta_archivo = os.path.join(carpeta_raiz, archivo)  # Ruta absoluta del archivo
        largo_archivo = len(ruta_archivo)  # Longitud total de la ruta
        print(f"[Archivo] {largo_archivo} caracteres | {ruta_archivo}")

        # Si la ruta del archivo supera el límite, la registramos
        if largo_archivo > limite_caracteres:
            elementos_largos.append(["Archivo", largo_archivo, ruta_archivo])

# -------------------------------------------
# EXPORTACIÓN A CSV
# -------------------------------------------

# Abrimos el archivo CSV en modo escritura y codificación UTF-8
with open(archivo_csv, mode="w", newline="", encoding="utf-8") as archivo:
    writer = csv.writer(archivo)
    
    # Escribimos la fila de encabezado
    writer.writerow(["Tipo", "Caracteres", "Ruta"])
    
    # Escribimos todas las filas correspondientes a rutas largas
    writer.writerows(elementos_largos)

# Confirmación final con resumen
print(f"\n✅ Se guardaron {len(elementos_largos)} rutas largas en: {archivo_csv}")


