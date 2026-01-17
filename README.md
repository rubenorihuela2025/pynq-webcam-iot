# PYNQ-Webcam-IoT
Sistema de detección de movimiento IoT con PYNQ-Z2 y Adafruit IO.

En este proyecto se implementa un sistema IoT con la placa PYNQ-Z2, con el objetivo de aplicar un detector de movimiento mediante una webcam USB.
Se detecta movimiento mediante OpenCV, que se trata de una biblioteca de código abierto con herramientas de visión por computadora. El sistema publica el estado del movimiento en una plataforma IoT, en este caso Adafruit IO, donde el usuario puede visualizar y recibir alertas.

## Tecnologías empleadas
- PYNQ-Z2
- FPGA (Verilog)
- Python
- OpenCV
- IoT (MQTT/Adafruit IO)
