# Module Imports
import tkinter as tk
import mariadb
import sys
from tkinter import ttk  
from ttkthemes import ThemedTk
# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="admin",
        password="admin123",
        host="127.0.0.1",
        port=3306,
        database="test"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()
def insert_entry_fields():
    cur.execute("INSERT INTO license_plate (state_name, license_plate_num) VALUES (%s, %s)", (state_name.get(), license_plate_num.get(), )) 
    ttk.Label(window, text="Successfully Inserted!",justify='center').grid(row=3,column=1,padx=20,pady=20)
    state_name.delete(0,'end')
    license_plate_num.delete(0,'end')
    conn.commit()

# def show_data():
#     cur.execute("SELECT * FROM license_plate")
window = ThemedTk(theme="arc")
window.title("License Plate GUI")
window.geometry("350x160")
ttk.Label(window, text="State Name",justify='center').grid(row=0,padx = 20, pady = 10)
state_name = ttk.Entry(window)
state_name.grid(row=0, column=1,padx = 20, pady = 10)

ttk.Label(window, text="License Plate",justify='center').grid(row=1,padx = 20, pady = 10)
license_plate_num = ttk.Entry(window)
license_plate_num.grid(row=1, column=1,padx = 20, pady = 10)

ttk.Button(window,
          text='Quit', 
          command=window.quit).grid(row=2, 
                                    column=0, 
                                    sticky=tk.W, 
                                    padx = 20)
ttk.Button(window, 
          text='Insert', command=insert_entry_fields).grid(row=2, 
                                                       column=1, 
                                                       sticky=tk.W, 
                                                       padx = 20)
window.mainloop()