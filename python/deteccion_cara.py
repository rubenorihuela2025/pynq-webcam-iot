## Detección de rostros mediante la librería OpenCV
from Adafruit_IO import Client # Importar el cliente de Adafruit IO para poder enviar datos a la plataforma IoT
import time
import cv2 # Importar OpenCV

# Configuración de Adafruit IO
ADAFRUIT_AIO_USERNAME = "rubenorihuela"
ADAFRUIT_AIO_KEY = "insertar_clave"
FEED_NAME = "adafruit"

aio = Client(ADAFRUIT_AIO_USERNAME, ADAFRUIT_AIO_KEY)

# OpenCV: Cargar Haar Cascade para detección de rostros
face_cascade = cv2.CascadeClassifier(
    "/home/xilinx/jupyter_notebooks/base/video/data/"
    "haarcascade_frontalface_default.xml"
)

# Inicializar webcam
cap = cv2.VideoCapture(0) # Abrir la webcam USB conectada a la PYNQ

if not cap.isOpened():
    raise RuntimeError("No se puede acceder a la webcam")

print("Webcam inicializada correctamente")

face_detected_prev = False # Evitar envíos continuos

# Bucle principal: se ejecuta mientras la webcam esté activa
while True:
    ret, frame = cap.read() # Capturar un frame desde la webcam
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Convertir frame a escala de grises

    faces = face_cascade.detectMultiScale( # Detectar rostros
        gray,
        scaleFactor=1.3,
        minNeighbors=5
    )

    face_detected = len(faces) > 0

    # Enviar un evento cuando aparezca una cara
    if face_detected and not face_detected_prev:
        aio.send(FEED_NAME, 1) # Enviar evento '1' al feed de Adafruit IO
        print("Rostro detectado -> Evento enviado a Adafruit IO")
        time.sleep(2) # Esperar 2 segundos para evitar envíos continuos

    face_detected_prev = face_detected # Guardar estado actual para comparar en la siguiente iteración del bucle

# Liberar la webcam
cap.release()
