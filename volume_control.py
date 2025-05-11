import cv2
import time
import numpy as np
import mediapipe as mp
import htmmod
import math

from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


###############################################
wCam, hCam = 1280, 720
###############################################


cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0

detector = htmmod.handDetector(detectCon=0.7)

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)

volRange = volume.GetVolumeRange() # -65.0(min) - 0(max)
# volume.SetMasterVolumeLevel(0, None)
minVol = volRange[0]
maxVol = volRange[1]

while True:
    success, img = cap.read()

    if not success:
        break

    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

    
    if len(lmList) != 0:

        x1, y1 = lmList[4][1], lmList[4][2] 
        x2, y2 = lmList[8][1], lmList[8][2] 

        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2


        cv2.circle(img, (x1, y1), 7, (255,0,255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 7, (255,0,255), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255,0,255), 3)

        cv2.circle(img, (cx, cy), 7, (255,0,255), cv2.FILLED)

        length = math.hypot(x2-x1, y2-y1)

        vol = np.interp(length, [17, 215], [minVol, maxVol])
        volume.SetMasterVolumeLevel(vol, None)

            
        if length<17:
            cv2.circle(img, (cx, cy), 7, (0,255,0), cv2.FILLED)


    cv2.imshow("Img", img)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()