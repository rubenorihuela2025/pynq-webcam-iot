# PYNQ-Webcam-IoT
Sistema de detección de intrusos IoT con PYNQ-Z2 y Adafruit IO.

En este proyecto se implementa un sistema IoT con la placa PYNQ-Z2, con el objetivo de aplicar un detector de intrusos mediante una webcam USB.
Se detectan los rostros mediante OpenCV, que se trata de una biblioteca de código abierto con herramientas de visión por computadora. El sistema publica el estado en una plataforma IoT, en este caso Adafruit IO, donde el usuario puede visualizar y recibir alertas.

## Hardware
- PYNQ-Z2
- Fuente de alimentación
- USB Webcam Logitech C505
- Cable ethernet

## Software
- Sistema operativo: PYNQ Linux
- Lenguajes de programación: Python 3
- Librerías: OpenCV, NumPy, Adafruit IO Python Client
- Plataforma IoT: Adafruit IO

## Arquitectura
