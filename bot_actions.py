from visionInstances import visionInstances
from functions import clicar
from time import sleep
import pyautogui
import cv2

xabuska = visionInstances()

def catch_screenshot(wincap):
    return wincap.get_screenshot()

def clicarColher(wincap, vision_colher):
    print('Colhendo')
    count=0
    while count<10:
        points = xabuska.vision_colher.find(catch_screenshot(wincap), 0.7, 'points')
        if len(points)>0:
            clicar(points)
            count=0
        else:
            count=count+1
        if cv2.waitKey(1) == ord('q'):
            cv2.destroyAllWindows()
            break
    print('Fim Colhendo')

def clicarPlantar(wincap, vision_plantar):
    print('Colhendo')
    count=0
    while count<20:
        points = xabuska.vision_plantar.find(catch_screenshot(xabuska.wincap), 0.7, 'points')
        if len(points)>0:
            clicar(points)
        if cv2.waitKey(1) == ord('q'):
            cv2.destroyAllWindows()
            break
        count=count+1
    print("Fim Colhendo")
    
def clicarVoltar():
    print('Encontrando Setinha Azul')
    while True:
        points = xabuska.vision_setinha_azul.find(catch_screenshot(xabuska.wincap), 0.7, 'points')
        if len(points)>0:
            clicar(points[0])
            break
    print("Fim da Setinha Azul")
    
def clicarMissao():
    print('Clicando na missao')
    count=0
    while count<2:
        points = xabuska.vision_missao.find(catch_screenshot(xabuska.wincap), 0.7, 'points')
        if len(points)>0:
            clicar(points[0])
        if cv2.waitKey(1) == ord('q'):
            cv2.destroyAllWindows()
            break
        count=count+1
    print("Fim da Missao")


        