# Detector de intrusos (IoT en PYNQ)
Sistema de detección de intrusos IoT con PYNQ-Z2 y Adafruit IO.

En este proyecto se implementa un sistema IoT con la placa PYNQ-Z2, con el objetivo de aplicar un detector de intrusos mediante una webcam USB.
Se detectan los rostros mediante OpenCV, que se trata de una biblioteca de código abierto con herramientas de visión por computadora. El sistema publica el estado en una plataforma IoT, en este caso Adafruit IO, donde el usuario puede visualizar y recibir alertas.

## Objetivos
- Implementar un sistema IoT en PYNQ.
- Realizar detección facial en tiempo real con la librería OpenCV.
- Aplicar procesamiento en el dispositivo (Edge Computing).
- Enviar eventos a una plataforma IoT.

## Hardware
- PYNQ-Z2.
- Fuente de alimentación.
- USB Webcam Logitech C505.
- Cable ethernet.
- Tarjeta microSD.

## Software
- Sistema operativo: PYNQ Linux.
- Lenguaje de programación: Python 3.
- Librerías: OpenCV, Adafruit IO Python Client.
- Plataforma IoT: Adafruit IO.

## Arquitectura IoT
El sistema se compone de una capa de adquicisión y procesamiento de datos mediante la PYNQ, una capa de comunicación a Internet y una capa de aplicación IoT con Adafruit IO.

Este es su diagrama y flujo:

<img width="1642" height="582" alt="ArquitecturaIoT" src="https://github.com/user-attachments/assets/06e9a0c1-d8b8-449b-b95a-2d13dcae11ab" />

## Guía de instalación y configuración
### Configuración de la PYNQ-Z2
1. Alimentación de la placa desde fuente de alimentación externa (jumper REG).
2. Se arranca desde la tarjeta microSD (jumper SD) con la imagen del sistema operativo de la PYNQ descargada en la url https://drive.ugr.es/index.php/s/0c6nhf0vVRTGcTA (contraseña: sei2020).
3. Insertar microSD, conectar Webcam vía USB y conectar la placa al PC (SO Windows 11) mediante cable Ethernet.
4. Encender la placa.

### Acceso a Jupyter Notebook y conectividad a Internet
1. Existe un acceso por defecto a Jupyter Notebook mediante la IP 192.168.2.99 por la pasarela con IP 192.168.2.1, pero se cambia esta subred desde la terminal de Jupyter por la 192.168.137.0/24 con la IP 192.168.137.10 para acceder a Jupyter Notebook y la pasarela con IP 192.168.137.1. Se configura y se reinicia la PYNQ.
2. Se le da acceso a Internet a la PYNQ mediante Internet Connection Sharing (ICS) en Windows 11 desde el PC, que proporciona salida a Internet vía WiFi. Se configura el DNS para que pueda resolver los nombres de dominio al descargar paquetes y comunicarse con el exterior.
3. Se instala el cliente IoT de Adafruit IO mediante el comando `pip install adafruit-io` en la terminal de Jupyter.

### Configuración de Adafruit IO
1. Se crea una cuenta en https://io.adafruit.com
2. Se crea un feed donde se mostrarán los eventos.
3. Se obtienen tanto el `ADAFRUIT_AIO_USERNAME` como el `ADAFRUIT_AIO_KEY` correspondientes.

## Uso del código
Se describe como ejecutar el sistema de detección facial y como interactúa con la plataforma IoT.

1. Se accede a la PYNQ mediante Jupyter Notebook (IP 192.168.137.10 en el navegador web).
2. Se abre una terminal.
3. Se verifica la conexión a Internet mediante los comandos `ping 8.8.8.8` y `ping google.com`.
4. Se navega al directorio con el comando `cd /home/xilinx/jupyter_notebooks/python`
5. Se ejecuta el script Python mediante el comando `python3 deteccion_cara.py`([deteccion_cara.py](python/deteccion_cara.py)).

Al ejecutar el programa se muestra un mensaje en la terminal de que la webcam está iniciada y cuando se detecta un rostro se muestra también un mensaje. A su vez, se genera un evento IoT que se envía con valor 1 al feed de Adafruit IO.
Para detener el bucle de captura infinito desde la webcam se pulsa Ctrl + Z para pausarlo y se introduce el comando `kill %1` para detenerlo.

## Resultados obtenidos
- Detección facial en tiempo real.
- Envío de eventos a Adafruit IO.
- Visualización de eventos en el feed de Adafruit IO.

## Autor
- Nombre completo: Rubén Orihuela Romero
- Asignatura: Sistemas Electrónicos Integrados

