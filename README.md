# Sistema de Detección de Estacionamiento con YOLO

Este proyecto es una aplicación de detección de estacionamiento que utiliza un modelo de detección YOLO (You Only Look Once) para identificar vehículos en un video proporcionado por el usuario. La aplicación detecta automáticamente si los autos están estacionados en los espacios de estacionamiento al comparar las cajas de colisión con las coordenadas de los puntos de estacionamiento. Además, cuenta con un contador integrado que muestra el número de espacios de estacionamiento ocupados en tiempo real.

## Funcionalidades Principales

- **Detección de Vehículos:** Utiliza un modelo de detección YOLO pre-entrenado para identificar vehículos en un video.
- **Comparación de Coordenadas:** Compara las cajas de colisión de los vehículos detectados con las coordenadas de los puntos de estacionamiento para determinar si están estacionados.
- **Contador de Espacios Ocupados:** Muestra en tiempo real el número de espacios de estacionamiento ocupados.

## Tecnologías Utilizadas

- **Lenguaje de Programación:** Python
- **Modelo de Detección:** YOLO (You Only Look Once)
- **Librerías:** OpenCV, TensorFlow

## Cómo Usar la Aplicación

1. **Instalación de Dependencias:**

pip install -r requirements.txt

2. **Ejecución de la Aplicación:**

python main.py --video video.avi --config yolov3.cfg --weights yolov3.weights --classes yolov3.names --parking-coords parking_coordinates.json

- `video.avi`: Ruta al video de entrada.
- `yolov3.cfg`: Configuración del modelo YOLO.
- `yolov3.weights`: Pesos pre-entrenados del modelo YOLO.
- `yolov3.names`: Archivo con los nombres de las clases.
- `parking_coordinates.json`: Archivo JSON con las coordenadas de los puntos de estacionamiento.

## Estructura del Proyecto

|-- detector/
| |-- yolo.py # Implementación de la detección YOLO
|
|-- main.py # Script principal de la aplicación
|-- requirements.txt # Archivo de requerimientos para la instalación
|-- video.avi # Ejemplo de video de entrada
|-- yolov3.cfg # Configuración del modelo YOLO
|-- yolov3.weights # Pesos pre-entrenados del modelo YOLO
|-- yolov3.names # Archivo con los nombres de las clases
|-- parking_coordinates.json # Archivo JSON con las coordenadas de los puntos de estacionamiento

## Autor

Este proyecto fue desarrollado por **Rivera Luca** - Contacto: [lucamartinrivera@gmail.com](mailto:lucamartinrivera@gmail.com)

