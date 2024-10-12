import os
import cv2
import numpy as np
import time
def showimg(img):
    cv2.imshow("asd", img)
    cv2.waitKey()
    cv2.destroyAllWindows()


top_notes = ["C","D","E","F","G","A","B","C","D","E","F","G"]
bot_notes = ["F","G","A","B","C","D","E","F","G","A","B","C"]

def split():

    notes = os.path.join(os.getcwd(), "notes")


    img_path = os.path.join(os.getcwd(), "notes.png")


    img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
    # 1400x600
    timg = img[50:300,:]
    bimg = img[350:600,:]

    #showimg(timg)
    #showimg(bimg)
    
    LEFT = 150
    top_mark = img[50:300,40:LEFT]
    #showimg(top_mark)
    bot_mark = img[350:600,40:LEFT]
    #showimg(bot_mark)

    last = LEFT + 17
    DELTA = 52
    idx = 0
    while True:
        cropt = timg[::, last:last+DELTA]
        cropb = bimg[::, last:last+DELTA]
        last += DELTA
        if idx >= len(top_notes):
            break

        combt = np.hstack((top_mark, cropt))
        combb = np.hstack((bot_mark, cropb))


        cv2.imwrite(notes + "/top_" + top_notes[idx] + "_" + str(idx) +"_.png", combt)
        cv2.imwrite(notes + "/bot_" + bot_notes[idx] + "_" + str(idx) +"_.png", combb)
        idx+=1

    time.sleep(1)
        

    return

    TOP = 35
    NOTE = img[35:,:44]

    LEFT = 48
    DELTA = 33
    
    last = LEFT
    idx = 0
    while True:
        crop = img[TOP:,last:last+DELTA]
        if last+DELTA>img.shape[1]:
            break
        last += DELTA
        idx +=1
        
        comb = np.hstack((NOTE, crop))
        cv2.imwrite(notes + "/" + str(idx) + ".png", comb)


if __name__ == "__main__":
    split()