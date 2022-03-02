from windowcapture import WindowCapture
from vision import Vision

class visionInstances:
    wincap = WindowCapture()
    
    #First Config----------------------------------------------------------------
    Folder = 'Standards'
    Separator = '\\'
    
    #Second Config----------------------------------------------------------------
    #Colher
    PathColher = f'{Folder}{Separator}2-Colher{Separator}1-Common{Separator}'
    #Plantar
    PathPlantar = f'{Folder}{Separator}1-Plantar{Separator}1-Common{Separator}'
    #Missions
    PathMissionCommon = f'{Folder}{Separator}3-Missions{Separator}1-Common{Separator}'
    PathMissionProducts = f'{Folder}{Separator}3-Missions{Separator}2-Products{Separator}'
    #Geral
    PathGeral = f'{Folder}{Separator}4-Geral{Separator}1-Common{Separator}'
    #Achievements
    PathAchievements = f'{Folder}{Separator}5-Achievements{Separator}1-Common{Separator}'
    #Levelup
    PathLevelup = f'{Folder}{Separator}6-Levelup{Separator}1-Common{Separator}'
    #Disconnected
    PathDisconnected = f'{Folder}{Separator}7-Disconnected{Separator}1-Common{Separator}'
    #Login
    PathLogin = f'{Folder}{Separator}8-Login{Separator}1-Common{Separator}'
    #logout
    PathLogout = f'{Folder}{Separator}9-Logout{Separator}1-Common{Separator}'
    
    
    #Third Config-------------------------------------------------
    #Colher
    # visionColherTrigo = Vision(f'{PathMissionProducts}TrigoColher.jpg')
    
    #Plantar
    # visionPlantarTrigo = Vision(f'{PathMissionProducts}TrigoPlantar.jpg')
    
    #Missoes
    #Missoes-Common
    visionMissaoEntrar = Vision(f'{PathMissionCommon}Prancheta.jpg')
    visionMissaoDeliverGreen = Vision(f'{PathMissionCommon}MissionDeliverButtonGreen.jpg')
    visionMissaoDeliverGray = Vision(f'{PathMissionCommon}MissionDeliverButtonGray.jpg')
    visionMissaoLixo = Vision(f'{PathMissionCommon}Lixo.jpg')
    #Missoes-Produtos(single)
    visionTrigo = Vision(f'{PathMissionProducts}Trigo.jpg') #Used
    visionMilho = Vision(f'{PathMissionProducts}Milho.jpg')
    visionCana = Vision(f'{PathMissionProducts}Cana.jpg')
    visionPao = Vision(f'{PathMissionProducts}Pao.jpg')
    visionLeite = Vision(f'{PathMissionProducts}Leite.jpg')
    #Missoes-Produtos(double)
    visionTrigoMilho = Vision(f'{PathMissionProducts}TrigoMilho.jpg')
    visionTrigoCana = Vision(f'{PathMissionProducts}TrigoCana.jpg')
    visionMilhoCana = Vision(f'{PathMissionProducts}MilhoCana.jpg')
    visionLeitePao = Vision(f'{PathMissionProducts}LeitePao.jpg')
    #Missoes-Produtos(triple)
    #Missoes-Produtos(quadruple)
    
    #Geral
    visionSetinhaAzul= Vision(f'{PathGeral}SetinhaAzul.jpg')
        