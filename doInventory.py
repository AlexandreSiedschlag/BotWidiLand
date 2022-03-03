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

# def test(lele):
#         x = getattr(xabuska, lele)
#         y = f'xabuska.{x}.find(catch_screenshot(xabuska.wincap), 0.7, "points")'
#         print(y)
#         return y
# test('visionInventoryCapacity')
        
class DoInventarioInfo:
    
    def __init__(self):
        self.pathCapacity = 'Standards\\10-Inventory\\1-Common\\'
        self.pathProducts = 'Standards\\10-Inventory\\2-Products\\'
        self.pathActual = 'Standards\\10-Inventory\\3-Actual\\'
    
    def getCapacity(self):
        print('Getting Storage Capacity')
        contador=0
        while contador<2:
            points = xabuska.visionInventoryCapacity.find(catch_screenshot(xabuska.wincap), 0.7, 'points')
            if len(points)>0: 
                print(f'Detectado {len(points)} imagem inventario, em {points}')
                offset_x = -100
                offset_y = -50
                mouse_x_Position = points[0][0] + xabuska.wincap.cropped_x + offset_x
                mouse_y_Position = points[0][1] + xabuska.wincap.cropped_y + offset_y
                w = 200
                h = 100
                bottom_right = (mouse_x_Position + w, mouse_y_Position + h)
                image = ImageGrab.grab(bbox=(mouse_x_Position,mouse_y_Position,bottom_right[0],bottom_right[1]))
                image.save(f'{self.pathActual}Capacity.jpg')
                tess.pytesseract.tesseract_cmd = r'C:\Tesseract\tesseract.exe'
                img =Image.open(f'{self.pathActual}Capacity.jpg')
                text = tess.image_to_string(img)
                text = text.split()
                text = text[1][0:2]
                print(text)
                return text
            
    def getTrigo(self):
        print('Getting Trigo Capacity')
        contador=0
        while contador<2:
            points = xabuska.visionInventoryTrigo.find(catch_screenshot(xabuska.wincap), 0.7, 'points')
            if len(points)>0: 
                print(f'Detectado {len(points)} imagem inventario, em {points}')
                offset_x = -25
                offset_y = 20
                mouse_x_Position = points[0][0] + xabuska.wincap.cropped_x + offset_x
                mouse_y_Position = points[0][1] + xabuska.wincap.cropped_y + offset_y
                w = 70
                h = 70
                bottom_right = (mouse_x_Position + w, mouse_y_Position + h)
                image = ImageGrab.grab(bbox=(mouse_x_Position,mouse_y_Position,bottom_right[0],bottom_right[1]))
                image.save(f'{self.pathActual}Trigo.jpg')
                tess.pytesseract.tesseract_cmd = r'C:\Tesseract\tesseract.exe'
                img = Image.open(f'{self.pathActual}Trigo.jpg')
                text = tess.image_to_string(img)
                print(text)
                text = text
                print(text)
                return text

# print(decodeInventarioInfo(1,0,2))
