# Analizador de Rutas Largas en Sistema de Archivos

## 1. Propósito

Este script tiene como objetivo identificar **rutas de archivos o carpetas** que excedan el límite tradicional de 260 caracteres en sistemas Windows. Esto es útil en contextos donde se realizan migraciones, respaldos, organización de estructuras BIM o validaciones de compatibilidad con herramientas que no aceptan rutas extensas.

---

## 2. Instrucciones de Uso

1. Asegúrate de tener Python 3 instalado en tu sistema.
2. Guarda el script en un archivo llamado `analizador_rutas.py`.
3. Ejecuta el script desde la terminal o PowerShell con:

```bash
python analizador_rutas.py
```

4. Ingresa la ruta raíz que deseas analizar cuando se te solicite (por ejemplo: `H:\NasIndesco\Back_Up\05_25\ADMINISTRACIÓN`)
5. El programa imprimirá por pantalla la longitud de cada carpeta y archivo, y generará un archivo CSV con las rutas que superan los 260 caracteres.

---

## 3. Control de Versiones

| Versión | Fecha       | Cambios                                                                 |
|---------|-------------|-------------------------------------------------------------------------|
| 1.0     | 2025-07-28  | Versión inicial con análisis de archivos con longitud excesiva         |
| 1.1     | 2025-07-28  | Inclusión de análisis de carpetas además de archivos                   |
| 1.2     | 2025-07-28  | Exportación a CSV con tipo, longitud y ruta completa                   |
| 1.3     | 2025-07-28  | Comentarios explicativos agregados al código para documentación interna|

---

## 4. Diagrama de Secuencia

```
Usuario
  │
  ▼
Solicita ingreso de ruta ----------------┐
  │                                      │
  ▼                                      ▼
Valida existencia ruta             Error si no existe
  │
  ▼
Recorre carpetas y archivos usando os.walk()
  │
  ├─► Evalúa longitud de cada carpeta
  │      └─► Imprime por pantalla
  │      └─► Si excede, lo agrega a lista
  │
  ├─► Evalúa longitud de cada archivo
  │      └─► Imprime por pantalla
  │      └─► Si excede, lo agrega a lista
  │
  ▼
Guarda resultados en archivo CSV
  │
  ▼
Imprime resumen final al usuario
```

---

## 5. Descripción Técnica (¿Cómo lo hace?)

- El script utiliza `os.walk()` para recorrer de forma recursiva toda la estructura de carpetas desde una ruta raíz.
- Evalúa cada carpeta y archivo para medir la longitud total de su ruta absoluta.
- Si una ruta (archivo o carpeta) supera los 260 caracteres, se agrega a una lista.
- Al finalizar el recorrido, exporta los elementos largos a un archivo `rutas_largas.csv`, incluyendo:
  - Tipo (`Archivo` o `Carpeta`)
  - Longitud de la ruta
  - Ruta completa
- Además, muestra en tiempo real por consola las rutas analizadas, lo que facilita la supervisión del proceso.

---
