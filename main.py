from doMission import doMission
import cv2

while True:

    doMission()
    
    key = cv2.waitKey(1)
    if key == ord('q'):
        cv2.destroyAllWindows()

    