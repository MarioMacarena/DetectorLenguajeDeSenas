# DetectorLenguajeDeSenas
Reconocimiento de Lenguaje de Señas en Tiempo Real
Este proyecto implementa un sistema de reconocimiento de lenguaje de señas en tiempo real utilizando Python, MediaPipe, y OpenCV. La aplicación detecta y analiza la posición de las manos y los dedos a través de la cámara para interpretar gestos que representan letras del alfabeto.

Actualmente, el sistema ha sido probado con un conjunto de datos limitado a las letras 'A', 'B', y 'C' para demostrar su funcionalidad básica. Sin embargo, el proyecto está completamente preparado para expandir este conjunto de datos e incluir más letras y gestos.

Características
Detección en tiempo real: Utiliza la cámara web para capturar y procesar el video en tiempo real.
Reconocimiento de gestos: Interpreta las posiciones de las manos y los dedos para identificar letras del lenguaje de señas.
Escalabilidad: Permite la creación sencilla de nuevos conjuntos de datos para expandir el vocabulario de señas reconocido.

Primeros Pasos
Para poner en marcha este proyecto, sigue los siguientes pasos:

1. Preparación del Entorno
Asegúrate de tener Python instalado. Luego, instala las dependencias necesarias:

Reconocimiento de Lenguaje de Señas en Tiempo Real
Este proyecto implementa un sistema de reconocimiento de lenguaje de señas en tiempo real utilizando Python, MediaPipe, y OpenCV. La aplicación detecta y analiza la posición de las manos y los dedos a través de la cámara para interpretar gestos que representan letras del alfabeto.

Actualmente, el sistema ha sido probado con un conjunto de datos limitado a las letras 'A', 'B', y 'C' para demostrar su funcionalidad básica. Sin embargo, el proyecto está completamente preparado para expandir este conjunto de datos e incluir más letras y gestos.

Características
Detección en tiempo real: Utiliza la cámara web para capturar y procesar el video en tiempo real.
Reconocimiento de gestos: Interpreta las posiciones de las manos y los dedos para identificar letras del lenguaje de señas.
Escalabilidad: Permite la creación sencilla de nuevos conjuntos de datos para expandir el vocabulario de señas reconocido.
Primeros Pasos
Para poner en marcha este proyecto, sigue los siguientes pasos:

1. Preparación del Entorno
Asegúrate de tener Python instalado. Luego, instala las dependencias necesarias
pip install mediapipe opencv-python tensorflow scikit-learn numpy

3. Creación de un Nuevo Conjunto de Datos (Opcional)
Si deseas añadir más letras o mejorar el reconocimiento de las existentes, puedes crear tu propio conjunto de datos:
Recolecta imágenes: Ejecuta RecolectarImg.py para capturar imágenes de tus gestos. Este script te guiará para tomar múltiples fotos de cada nueva letra que desees añadir.
Crea el conjunto de datos: Una vez que hayas recolectado las imágenes, ejecuta CrearDataSet.py. Este script procesará las imágenes y generará el conjunto de datos necesario para el entrenamiento.

4. Entrenamiento del Modelo
Después de tener tu conjunto de datos listo (ya sea el preexistente o uno nuevo), entrena el modelo:
Ejecuta Entrenar.py. Este script utilizará el conjunto de datos para entrenar el modelo de reconocimiento de gestos, mejorando su precisión.

5. Ejecución del Sistema de Reconocimiento
Finalmente, para iniciar el reconocimiento en tiempo real:
Abre el archivo main.py.
Modifica el class_map: Si has añadido nuevas letras, asegúrate de actualizar el diccionario class_map en main.py para incluir las nuevas correspondencias entre los índices del modelo y las letras del alfabeto.
Ejecuta main.py. Se abrirá una ventana mostrando la transmisión de tu cámara y el reconocimiento de gestos en tiempo real.
