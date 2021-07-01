while True:
    #src: https://www.geeksforgeeks.org/text-detection-and-extraction-using-opencv-and-ocr/
    # Import required packages
    import cv2
    import mariadb
    import sys
    import pytesseract
    # Connect to MariaDB Platform
    try:
        conn = mariadb.connect(
            user="root",
            password="",
            host="127.0.0.1",
            port=3307,
            database="test"

        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

    # Get Cursor
    cur = conn.cursor()
    
    def compare_imgText_database():
        cur.execute("SELECT * FROM license_plate") 
        # get all records
        records = cur.fetchall()
        trueFalseRecord=[]
        for search in records:
            try:
                if(text.index(search[1])!=-1 and text.index(search[2])!=-1):
                    trueFalseRecord.append(True)
            except ValueError:
                trueFalseRecord.append(False)
        
        try:
            if(trueFalseRecord.index(True)!=-1):
                print("Matched in Database")
        except ValueError:
            print("Not Matched in Database")
        #print what was read from the image    
        print(text)
    # Mention the installed location of Tesseract-OCR in your system
    pytesseract.pytesseract.tesseract_cmd = 'D:/Program Files/Tesseract-OCR/tesseract.exe'
    
    # Read image from which text needs to be extracted
    val = input("Enter image name with extension: ")
    img = cv2.imread("F:/PythonApp/firstgui/img/"+val)
    
    # Convert the image to gray scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Performing OTSU threshold
    ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (50, 50))
    dilation = cv2.dilate(thresh1, kernel, iterations = 1)
    contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, 
                                                    cv2.CHAIN_APPROX_NONE)
    im2 = img.copy()   
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cropped = im2[y:y + h, x:x + w]
        text = pytesseract.image_to_string(cropped)
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
    
    compare_imgText_database()        
    while True:
        answer = str(input('Run again? (y/n): '))
        if answer in ('y', 'n'):
            break
        print("Invalid Entry. Try Again.")
    if answer == 'y':
        continue
    else:
        print("Take Care")
        break
    