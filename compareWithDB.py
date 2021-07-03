#src: https://www.geeksforgeeks.org/text-detection-and-extraction-using-opencv-and-ocr/
# Import required packages
import cv2
import mariadb
import sys
import pytesseract
# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="admin",
        password="admin123",
        host="127.0.0.1",
        port=3306,
        database="license_plate"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()

def compare_imgText_database(text):
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
    


