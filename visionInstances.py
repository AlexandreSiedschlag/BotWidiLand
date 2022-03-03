from windowcapture import WindowCapture
from vision import Vision

class visionInstances:
    wincap = WindowCapture()
    def __init__(self):
            
        #First Config----------------------------------------------------------------
        self.Folder = 'Standards'
        self.Separator = '\\'
        
        #Second Config----------------------------------------------------------------
        #Colher
        self.PathColher = f'{self.Folder}{self.Separator}2-Colher{self.Separator}1-Common{self.Separator}'
        #Plantar
        self.PathPlantar = f'{self.Folder}{self.Separator}1-Plantar{self.Separator}1-Common{self.Separator}'
        #Missions
        self.PathMissionCommon = f'{self.Folder}{self.Separator}3-Missions{self.Separator}1-Common{self.Separator}'
        self.PathMissionProducts = f'{self.Folder}{self.Separator}3-Missions{self.Separator}2-Products{self.Separator}'
        #Geral
        self.PathGeral = f'{self.Folder}{self.Separator}4-Geral{self.Separator}1-Common{self.Separator}'
        #Achievements
        self.PathAchievements = f'{self.Folder}{self.Separator}5-Achievements{self.Separator}1-Common{self.Separator}'
        #Levelup
        self.PathLevelup = f'{self.Folder}{self.Separator}6-Levelup{self.Separator}1-Common{self.Separator}'
        #Disconnected
        self.PathDisconnected = f'{self.Folder}{self.Separator}7-Disconnected{self.Separator}1-Common{self.Separator}'
        #Login
        self.PathLogin = f'{self.Folder}{self.Separator}8-Login{self.Separator}1-Common{self.Separator}'
        #logout
        self.PathLogout = f'{self.Folder}{self.Separator}9-Logout{self.Separator}1-Common{self.Separator}'
        
        self.PathInventory = f'{self.Folder}{self.Separator}10-Inventory{self.Separator}1-Common{self.Separator}'
        
        
        #Third Config-------------------------------------------------
        #Colher
        # visionColherTrigo = Vision(f'{PathMissionProducts}TrigoColher.jpg')
        
        #Plantar
        # visionPlantarTrigo = Vision(f'{PathMissionProducts}TrigoPlantar.jpg')
        
        #Missoes
        #Missoes-Common
        self.visionMissaoEntrar = Vision(f'{self.PathMissionCommon}Prancheta.jpg')
        self.visionMissaoDeliverGreen = Vision(f'{self.PathMissionCommon}MissionDeliverButtonGreen.jpg')
        self.visionMissaoDeliverGray = Vision(f'{self.PathMissionCommon}MissionDeliverButtonGray.jpg')
        self.visionMissaoLixo = Vision(f'{self.PathMissionCommon}Lixo.jpg')
        #Missoes-Produtos(single)
        self.visionTrigo = Vision(f'{self.PathMissionProducts}1-Positive{self.Separator}Trigo.jpg') #Used
        self.visionMilho = Vision(f'{self.PathMissionProducts}1-Positive{self.Separator}Milho.jpg')
        self.visionCana = Vision(f'{self.PathMissionProducts}1-Positive{self.Separator}Cana.jpg')
        self.visionPao = Vision(f'{self.PathMissionProducts}1-Positive{self.Separator}Pao.jpg')
        self.visionLeite = Vision(f'{self.PathMissionProducts}1-Positive{self.Separator}Leite.jpg')
        #Missoes-Produtos(double)
        self.visionTrigoMilho = Vision(f'{self.PathMissionProducts}1-Positive{self.Separator}TrigoMilho.jpg')
        self.visionTrigoCana = Vision(f'{self.PathMissionProducts}1-Positive{self.Separator}TrigoCana.jpg')
        self.visionMilhoCana = Vision(f'{self.PathMissionProducts}1-Positive{self.Separator}MilhoCana.jpg')
        self.visionLeitePao = Vision(f'{self.PathMissionProducts}1-Positive{self.Separator}LeitePao.jpg')
        #Missoes-Produtos(triple)
        #Missoes-Produtos(quadruple)
        
        #Geral
        self.visionSetinhaAzul= Vision(f'{self.PathGeral}SetinhaAzul.jpg')
        
        self.visionCapacity = Vision(f'{self.PathInventory}{self.Separator}capacity.jpg') #Used
    
        