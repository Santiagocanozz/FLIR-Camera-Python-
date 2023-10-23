import cv2
import cv2 as cv
import numpy as np
#from pyspin import PySpin
import EasyPySpin

global dimension_tabla 
cap = EasyPySpin.VideoCapture(0)

while True:
    try:
    # capturar frame a frame
        ret, frame = cap.read()
        frame = frame[0:1240,200:1616]
        cap.set(cv2.CAP_PROP_EXPOSURE,8500)
        cap.set(cv2.CAP_PROP_FPS,100)
        cap.set(cv2.CAP_PROP_GAIN,20)	
        cap.set(cv2.CAP_PROP_GAMMA,0.9)
        cap.set(cv2.CAP_PROP_BRIGHTNESS,20)	 
        #gpu_mat = cv2.cuda_GpuMat(416, cv2.CV_32FC1)
        img_show = cv2.resize(frame, None, fx=0.3, fy=0.3)
        cv2.imshow('ss',img_show)
        img_show1 = img_show
        img_show1=cv2.cvtColor(img_show1, cv2.COLOR_GRAY2BGR)
        

        img_show = cv2.cvtColor(img_show, cv2.COLOR_BayerBG2BGR)
        img_show= cv2.medianBlur(img_show,15)
        img_show=cv2.GaussianBlur(img_show,(7,7),cv2.BORDER_DEFAULT)
        #MORFOLOGIA
        #Erosion
        
        #cv2.imshow('recorte',recorte)
        #img_show = recorte
        height, width = img_show.shape[:2]  # Tomamos las dimensiones de la imagen cargada
        lower_red = np.array([110, 110, 110])  # Creamos un vector con los valores minimos del limite
        upper_red = np.array([255, 255, 255])  # Creamos un vector con los valores maximos del limite
        mask = cv2.inRange(img_show, lower_red, upper_red)  # Creamos una mascara con los rangos a segmentar
        segImg1 = cv2.bitwise_and(img_show, img_show, mask=mask)  # Realimos una operacion bit a bit para aplicar la mascara a la imagen
        segImg2 = cv2.inRange(img_show, lower_red, upper_red)  # Segemetacion usando el comando inrange
        ret,segImg2 = cv2.threshold(segImg2,0,255,cv2.THRESH_BINARY +cv2.THRESH_OTSU)
        element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(40,40))
        erode = cv2.erode(segImg2,element)
        erode= cv2.morphologyEx(segImg2,cv2.MORPH_OPEN,(80,80))
        #cv2.imshow('erosion',erode)
        erode=segImg2
        _,contornos,_ = cv2.findContours(segImg2,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
        
        for contour in contornos:
            cv2.drawContours(img_show1,contour,-1,(0,255,255),3)
            ### CALCULO DE AREA ####
            area = cv2.contourArea(contour)
            a=1

            #### RELLENAR CONTORNO ###
            list = []
            for i in range(len(contornos)):
                cimg = np.zeros_like(img_show1)
                #print(cimg.shape)
                
                cv2.drawContours(cimg,contornos,i,color=255,thickness=-1)
            cv2.imshow('cimg',cimg)
            canny=cv2.Canny(cimg,0,255,)
            cv2.imshow('cannyy',canny)
        ## Coordenadas imagen
            #canny = cv2.resize(canny, None, fx=3.333, fy=3.333)
            tabla = cv2.findNonZero(canny)
            #coordenadas
            a = tabla[:,0,0].min()
            b = tabla[:,0,0].max()
            c = tabla[:,0,1].min()
            d = tabla[:,0,1].max()
            
            dimension_tabla = [a,b,c,d]
            #print(dimension_tabla)
            #print(a,b,c,d)

        ## RECORTE IMAGEN ##
        recorte_contorno = img_show1[200:700,100:900]     
        cv2.imshow('recorte_contorno',recorte_contorno)      
        
        ### IMAGEN ESCALADA PARA OBTENER DIMENSIONES REALES
        imagen_escala_real = cv2.resize(img_show1, None, fx=3.333, fy=3.333)
        #print(imagen_escala_real.shape)

        ## ESCALA DE DIMENSIONES DE TABLA
        ancho_tabla = abs(dimension_tabla[1]-dimension_tabla[0])
        #Factor de escala:
        factor_escala = 3.3
        ancho_real_px = factor_escala * ancho_tabla
        ancho_real_px = int(ancho_real_px)
        print(ancho_real_px)

        cv2.waitKey(1)
        
        
    except KeyboardInterrupt:
    
        #cv2.destroyAllWindows()
        print('keyboard')
        break

cv2.destroyAllWindows()
print("stop video")