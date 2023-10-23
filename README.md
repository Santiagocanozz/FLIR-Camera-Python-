# FLIR-Camera-Python-
In this repository you will find the connection to the FLIR BFS-U3-19S4C-C 2.0MP Color camera via Python.

For the connection it is necessary to have the flir SDK installed according to the type of camera. You can get it through the following link:

https://www.flir.com.mx/products/spinnaker-sdk/?vertical=machine+vision&segment=iis

To read the camera it is necessary to install the library: EasyPySpin: Repository attached: https://github.com/elerac/EasyPySpin

To install through PIP commands: pip install EasyPySpin

Example:

import cv2 import EasyPySpin

cap = EasyPySpin.VideoCapture(0)

ret, frame = cap.read()

cv2.imwrite("frame.png", frame)

cap.release()
