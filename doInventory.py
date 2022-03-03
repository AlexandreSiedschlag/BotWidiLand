from ast import Yield
from visionInstances import visionInstances
from functions import clicar
from time import sleep
import pyautogui
import cv2
from time import time
import pytesseract as tess
from PIL import Image, ImageGrab

loop_time = time()
xabuska = visionInstances() #Classe

def catch_screenshot(wincap):
    return wincap.get_screenshot()  

def doInventarioInfo():
    
    def test(lele):
        x = getattr(xabuska, lele)
        print(x)
        print(str(x,'utf8'))
        print(bytes(x))
        # y = f'xabuska.{list(x)}.find(catch_screenshot(xabuska.wincap), 0.7, "points")'
        # print(y)
        # return y
    test('visionCapacity')
        
    
    def get_points():
        print('Procurando Trigo')
        contador=0
        while contador<2:
            points = xabuska.visionCapacity.find(catch_screenshot(xabuska.wincap), 0.7, 'points')
            if len(points)>0: 
                print(f'Detectado {len(points)} imagem inventario, Clicando em {points}')
                return points
    def saveimg(points):
        offset_x = -100
        offset_y = -50
        mouse_x_Position = points[0][0] + xabuska.wincap.cropped_x + offset_x
        mouse_y_Position = points[0][1] + xabuska.wincap.cropped_y + offset_y
        w = 200
        h = 100
        bottom_right = (mouse_x_Position + w, mouse_y_Position + h)
        image = ImageGrab.grab(bbox=(mouse_x_Position,mouse_y_Position,bottom_right[0],bottom_right[1]))
        image.save('sc2.png')
        return 'sc2.png'
        
    def imageToText(img):
        tess.pytesseract.tesseract_cmd = r'C:\Tesseract\tesseract.exe'
        img =Image.open(f'{img}')
        text = tess.image_to_string(img)
        return text
    return imageToText(saveimg(get_points()))

def decodeInventarioInfo(indexPosition, x,y):
    te = doInventarioInfo()
    te = te.split()
    te = te[indexPosition][x:y]
    return te

# print(decodeInventarioInfo(1,0,2))
