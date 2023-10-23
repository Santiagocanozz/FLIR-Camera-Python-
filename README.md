# FLIR-Camera-Python-
In this repository you will find the connection to the FLIR BFS-U3-19S4C-C 2.0MP Color camera via Python. 


Para la conexión es necesario tener instalado el SDK de flir segun el tipo de cámara. 
A través del siguiente link se obtiene: 

https://www.flir.com.mx/products/spinnaker-sdk/?vertical=machine+vision&segment=iis

Para la lectura de la cámara es necesario la instalación de la libreria: EasyPySpin: 
Adjunto repositorio: 
https://github.com/elerac/EasyPySpin

Para instalar a través de comandos PIP: 
pip install EasyPySpin

Para conexión con el dispositivo: 

import cv2
import EasyPySpin

cap = EasyPySpin.VideoCapture(0)

ret, frame = cap.read()

cv2.imwrite("frame.png", frame)
    
cap.release()

