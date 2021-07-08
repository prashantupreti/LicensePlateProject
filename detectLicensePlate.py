#src: https://medium.com/programming-fever/license-plate-recognition-using-opencv-python-7611f85cdd6c
import cv2
import imutils
import numpy as np
import pytesseract
import compareWithDB as compare

def returnStateName(text):#still working on it.
    states=["Alabama", "Alaska", "American Samoa", "Arizona", "Arkansas", "California",
        "Colorado", "Connecticut", "Delaware", "Washington, DC",
        "Federated States Of Micronesia", "Florida", "Georgia", "Guam", "Hawaii",
        "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana",
        "Maine", "Marshall Islands", "Maryland", "Massachusetts", "Michigan",
        "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada",
        "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina",
        "North Dakota", "Northern Mariana Islands", "Ohio", "Oklahoma", "Oregon",
        "Palau", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina",
        "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virgin Islands",
        "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
    index=states.index(text)
    return upper(states[index])

def refineTxt(text):
    text = text.replace('*', ' ')
    text = text.replace('+', ' ')
    text = text.replace('-', ' ')
    text = text.replace('', '')
    text = text.replace('3°', '')
    text = text.replace('°', '')
    text = text.replace('=', '')
    text = text.replace('sk.', '')
    text = text.replace('«C', '')
    text = text.replace('he Lone Star State itu', '')
    text = text.replace('|', '')
    text = text.replace('"ies', '')
    text = text.replace('»', ' ')
    text = text.replace('©','')
    text = text.replace('\n',' ')
    text = text.lstrip()
    text = text.replace('THE LONE STAR STATE', '')
    text = text.replace('YOURS TO DISCOVER','')
    text = text.replace('&','')
    text = text.replace('/','7')
    text = text.replace('ENDIANA','INDIANA')
    text = text.replace('       ',' ') 
    text = text.replace('app® ','') 
    text = text.replace('@PwrR','')  
    text = text.replace('TheCross','')  
    text = text.replace('~',' ')
    text = text.replace('‘','')
    text = text.replace('EVERGREEN STATE','')
    text = text.replace('e','')
    text = text.replace('s','')
    text = text.replace('«OC','')
    

def getLicensePlateNumber(val):
    #this is where we include the src image
    img = cv2.imread('/home/pi/LicensePlateProject/img/temp/'+val,cv2.IMREAD_COLOR)
    try:
        img = cv2.resize(img, (600,400) )
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #cv2.imshow('Grayscale',gray)
        gray = cv2.bilateralFilter(gray, 13, 15, 15) 
        cv2.imshow('Grayscale',gray)
        edged = cv2.Canny(gray, 30, 200) 
        contours = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours = imutils.grab_contours(contours)
        contours = sorted(contours, key = cv2.contourArea, reverse = True)[:10]
        screenCnt = None

        for c in contours:
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.018 * peri, True)
         
            if len(approx) == 4:
                screenCnt = approx
                break

        if screenCnt is None:
            detected = 0
            print ("No contour detected")
        else:
             detected = 1

        if detected == 1:
            cv2.drawContours(img, [screenCnt], -1, (0, 0, 255), 3)
        else:
            cv2.drawContours(img, contours, -1, (0, 0, 255), 3)
        mask = np.zeros(gray.shape,np.uint8)
        if detected == 1:
            new_image = cv2.drawContours(mask,[screenCnt],0,255,-1,)

        new_image = cv2.bitwise_and(img,img,mask=mask)

        (x, y) = np.where(mask == 255)
        try:
            (topx, topy) = (np.min(x), np.min(y))
            (bottomx, bottomy) = (np.max(x), np.max(y))
            Cropped = gray[topx:bottomx+1, topy:bottomy+1]

            text = pytesseract.image_to_string(Cropped, config='--psm 11')
            refineTxt(text)
            print("Detected license plate Number is:",text)
            #print("State:",returnStateName(text))
            matched=compare.compare_imgText_database(text)
            
            Cropped = cv2.resize(Cropped,(400,200))
        except ValueError:
            pass
        
        
    #    if(matched):
     #       added_image = cv2.addWeighted(img,0.4,cv2.imread('check.png'),0.1,0)
      #  else:
       #     added_image = cv2.addWeighted(img,0.4,cv2.imread('times.png'),0.1,0)
            
        img = cv2.resize(img,(500,300))
        cv2.imshow('License Plate Detected Region',img)
        #cv2.imshow('Cropped Region',Cropped)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

    except Exception as e:
        print(str(e))