from visionInstances import visionInstances
from functions import clicar
from time import sleep
import pyautogui
import cv2
from time import time
loop_time = time()
xabuska = visionInstances() #Classe


def catch_screenshot(wincap):
    return wincap.get_screenshot()  

def doMission():
    print('Fazendo Missoes')
    contadorMission = 0        
    def doProdutos():
        def entregarTudo():
            print('Entregando As Missoes Ja Prontas(Botao Deliver Verde)')
            contador =0
            while contador<2:
                points = xabuska.visionMissaoDeliverGreen.find(catch_screenshot(xabuska.wincap), 0.95, 'points')
                print(points)
                if len(points)>0: 
                    print(f'Detectado {len(points)} card de trigo, Clicando em {points}')
                    offset_x = 0
                    offset_y = 0
                    mouse_x_Position = points[0][0] + xabuska.wincap.cropped_x + offset_x
                    mouse_y_Position = points[0][1] + xabuska.wincap.cropped_y + offset_y
                    pyautogui.moveTo(int(mouse_x_Position), int(mouse_y_Position))
                    clicar(int(mouse_x_Position), int(mouse_y_Position))
                    sleep(1)
                contador+=1
        
        def doProdutosTrigo(): #Detectando o card só com trigo
            print('Procurando Trigo')
            contador=0
            while contador<2:
                points = xabuska.visionTrigo.find(catch_screenshot(xabuska.wincap), 0.95, 'points')
                if len(points)>0: 
                    print(f'Detectado {len(points)} card de trigo, Clicando em {points}')
                    offset_x = 0
                    offset_y = 80
                    mouse_x_Position = points[0][0] + xabuska.wincap.cropped_x + offset_x
                    mouse_y_Position = points[0][1] + xabuska.wincap.cropped_y + offset_y
                    pyautogui.moveTo(int(mouse_x_Position), int(mouse_y_Position))
                    clicar(int(mouse_x_Position), int(mouse_y_Position))
                    sleep(1)
                elif points==None:
                    print('Nao encontrei trigo')
                contador+=1
        # entregarTudo()
        # doProdutosTrigo()
        
    doProdutos()
    def doRoletar():
        points = xabuska.vision_missao_card_deliver_cinza.find(catch_screenshot(xabuska.wincap), 0.9, 'points')
        lixo = xabuska.vision_missao_lixo.find(catch_screenshot(xabuska.wincap), 0.7,'points')
        qt = len(points)
        if qt>0: #Detectando o card só com milho
            print(f'Detectado Deliver Cinza {qt}, Clicando em {points}')
            print(points)
            for item in points: 
                offset_x = 0
                offset_y = -50
                offset_lixo_x = 0
                offset_lixo_y = 0
                mouse_x_Position = item[0] + xabuska.wincap.cropped_x + offset_x
                mouse_y_Position = item[1] + xabuska.wincap.cropped_y + offset_y
                
                lixo_x_Position = lixo[0][0] + xabuska.wincap.cropped_x + offset_lixo_x
                lixo_y_Position = lixo[0][1] + xabuska.wincap.cropped_y + offset_lixo_y
                
                pyautogui.moveTo(int(mouse_x_Position), int(mouse_y_Position))  #Seleciona o card
                clicar(int(mouse_x_Position), int(mouse_y_Position))        #Clica no card
                sleep(0.5)
                pyautogui.moveTo(int(lixo_x_Position), int(lixo_y_Position))  #Seleciona o lixo
                # clicar(int(lixo_x_Position), int(lixo_y_Position))        #Clica no lixo
                sleep(0.5)         
    
    key = cv2.waitKey(1)
    if key == ord('q'):
        cv2.destroyAllWindows()
    elif key == ord('f'):
        cv2.imwrite('positive/{}.jpg'.format(loop_time), catch_screenshot(xabuska.wincap))
    elif key == ord('d'):
        cv2.imwrite('negative/{}.jpg'.format(loop_time), catch_screenshot(xabuska.wincap)) 
    
    contadorMission+=1
    print(f'contadorMission depois: {contadorMission}')
    sleep(2)




# while count<3:
    #     points = xabuska.vision_missao_card.find(catch_screenshot(xabuska.wincap), 0.9, 'points')
    #     points2 = xabuska.vision_missao_deliver.find(catch_screenshot(xabuska.wincap), 0.9, 'points')
    #     qt = len(points)
    #     qt2 = len(points2)
    #     if qt>0: #Detectando o card só com milho
    #         print(f'Detectado card de trigo {qt}, Clicando em {points}')
    #         offset_x = 0
    #         offset_y = 80
    #         mouse_x_Position = points[0][0] + xabuska.wincap.cropped_x + offset_x
    #         mouse_y_Position = points[0][1] + xabuska.wincap.cropped_y + offset_y
    #         # pyautogui.moveTo(int(mouse_x_Position), int(mouse_y_Position))
    #         clicar(int(mouse_x_Position), int(mouse_y_Position))
    #         sleep(1)
    #     elif qt2>0: #Detectando "Deliver Verde"
    #         print(f'Detectado Deliver Verde {qt2}, Clicando em {points2}')
    #         for item in points2:
    #             offset_x = 0
    #             offset_y = 0
    #             mouse_x_Position = item[0] + xabuska.wincap.cropped_x + offset_x
    #             mouse_y_Position = item[1] + xabuska.wincap.cropped_y + offset_y
    #             # pyautogui.moveTo(int(mouse_x_Position), int(mouse_y_Position))
    #             clicar(float(mouse_x_Position), float(mouse_y_Position))
    #             sleep(1)
    #     else: #Detectando "Deliver Cinza"
    #         points3 = xabuska.vision_missao_card_deliver_cinza.find(catch_screenshot(xabuska.wincap), 0.9, 'points')
    #         lixo = xabuska.vision_missao_lixo.find(catch_screenshot(xabuska.wincap), 0.7,'points')
    #         print(f'lixo: {lixo}')
    #         qt3 = len(points3)
    #         if qt3>0: #Detectando o card só com milho
    #             print(f'Detectado Deliver Cinza {qt}, Clicando em {points}')
    #             print(points3)
    #             for item in points3: 
    #                 offset_x = 0
    #                 offset_y = -50
    #                 offset_lixo_x = 0
    #                 offset_lixo_y = 0
    #                 mouse_x_Position = item[0] + xabuska.wincap.cropped_x + offset_x
    #                 mouse_y_Position = item[1] + xabuska.wincap.cropped_y + offset_y
                    
    #                 lixo_x_Position = lixo[0][0] + xabuska.wincap.cropped_x + offset_lixo_x
    #                 lixo_y_Position = lixo[0][1] + xabuska.wincap.cropped_y + offset_lixo_y
                    
    #                 pyautogui.moveTo(int(mouse_x_Position), int(mouse_y_Position))  #Seleciona o card
    #                 clicar(int(mouse_x_Position), int(mouse_y_Position))        #Clica no card
    #                 sleep(0.5)
    #                 pyautogui.moveTo(int(lixo_x_Position), int(lixo_y_Position))  #Seleciona o lixo
    #                 # clicar(int(lixo_x_Position), int(lixo_y_Position))        #Clica no lixo
    #                 sleep(0.5)
        