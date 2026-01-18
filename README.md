# PYNQ-Webcam-IoT
Sistema de detección de intrusos IoT con PYNQ-Z2 y Adafruit IO.

En este proyecto se implementa un sistema IoT con la placa PYNQ-Z2, con el objetivo de aplicar un detector de intrusos mediante una webcam USB.
Se detectan los rostros mediante OpenCV, que se trata de una biblioteca de código abierto con herramientas de visión por computadora. El sistema publica el estado en una plataforma IoT, en este caso Adafruit IO, donde el usuario puede visualizar y recibir alertas.

## Hardware
- PYNQ-Z2
- Fuente de alimentación
- USB Webcam Logitech C505
- Cable ethernet
- Tarjeta microSD

## Software
- Sistema operativo: PYNQ Linux
- Lenguaje de programación: Python 3
- Librerías: OpenCV, Adafruit IO Python Client
- Plataforma IoT: Adafruit IO

## Arquitectura IoT
El sistema se compone de una capa de adquicisión y procesamiento de datos mediante la PYNQ, una capa de comunicación a Internet y una capa de aplicación IoT con Adafruit IO.

Este es su diagrama y flujo:
<img width="1642" height="582" alt="ArquitecturaIoT" src="https://github.com/user-attachments/assets/06e9a0c1-d8b8-449b-b95a-2d13dcae11ab" />


