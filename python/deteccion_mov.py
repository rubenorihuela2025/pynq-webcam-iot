from Adafruit_IO import Client
import time

ADAFRUIT_AIO_USERNAME = "rubenorihuela"
ADAFRUIT_AIO_KEY = "insertar_clave"

aio = Client(ADAFRUIT_AIO_USERNAME, ADAFRUIT_AIO_KEY)


import cv2                  # Importar librería OpenCV
import numpy as np          # Importar NumPy para operaciones numéricas

cap = cv2.VideoCapture(0) # Inicializar captura de vídeo desde la webcam USB

ret, frame1 = cap.read() # Capturar primer frame

ret, frame2 = cap.read() # Capturar segundo frame

# Bucle principal: se ejecuta mientras la cámara esté abierta correctamente
while cap.isOpened():

    diff = cv2.absdiff(frame1, frame2) # Calcular diferencia entre los frames

    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY) # Convertir imagen de la diferencia entre frames a escala de grises

    blur = cv2.GaussianBlur(gray, (5, 5), 0) # Aplicar un desenfoque Gaussiano a la imagen en escala de grises para reducir el ruido


    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY) # Convertir píxeles >20 a blancos y <20 a negros

    dilated = cv2.dilate(thresh, None, iterations=3) # Rellenar huecos de la imagen resultante y hacer más visible la zona de movimiento

    # Detectar contornos en la imagen resultante (los contornos representan regiones donde ha habido movimiento)
    _, contours, _ = cv2.findContours(
        dilated,
        cv2.RETR_TREE,
        cv2.CHAIN_APPROX_SIMPLE
    )

    motion_detected = False # Indicar si se ha detectado movimiento

    # Recorrer todos los contornos detectados
    for contour in contours:

        # Calcular el área del contorno para descartar pequeños cambios o ruido
        if cv2.contourArea(contour) < 1500:
            continue            # Ignorar contornos pequeños

        motion_detected = True # Hallar movimiento si hay un contorno lo suficientemente grande
        break                  # Salir del bucle al detectar movimiento

    # Imprimir mensaje
    if motion_detected:
        aio.send("adafruit", 1) # Enviar alerta al feed de Adafruit IO (IoT)
        print("Movimiento detectado y enviado a Adafruit IO")
        time.sleep(2)   # Evitar enviar demasiados eventos seguidos

    frame1 = frame2 # Actualizar frames

    ret, frame2 = cap.read() # Capturar nuevo frame para seguir analizando
