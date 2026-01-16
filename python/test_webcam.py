## Código de prueba para capturar imagen mediante la biblioteca OpenCV de Python
import cv2

# Abrir webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("ERROR: Webcam no detectada")
    exit(1)

ret, frame = cap.read()

if ret:
    cv2.imwrite("captura.jpg", frame) # Guardar imagen
    print("Imagen capturada correctamente")
else:
    print("ERROR: No se ha podido capturar la imagen")

cap.release()
