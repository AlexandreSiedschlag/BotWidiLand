from doInventory import DoInventarioInfo
from doMission import doMission
import cv2
inventario = DoInventarioInfo()
while True:
    inventario.getTrigo() 
    
    key = cv2.waitKey(1)
    if key == ord('q'):
        cv2.destroyAllWindows()

    