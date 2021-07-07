import numpy as np
import os
import pathlib

def clean(amount="", directory=""):
    '''
    amount: integer or "all"-for all
    directory: string containing path
    return: string containing details of removal
    '''
    
    message = ""
    
    try:
        current_dir = os.getcwd()
        os.chdir(directory)
    except OSError:
        print(f"{directory} does not exist or is faulty")
        return message=None
    
    if amount == "all":
        # delete all files in the folder
        try:
            for i in os.listdir(directory):
                os.remove(os.path.join(directory, i))
        except OSError:
            print(f"Error deleting \"all\" files in {directory}")
    else:
        try:
            amount = int(amount)
        except TypeError:
            print(f"{amount} is an invalid value for the clean method")
            
    os.chdir(current_dir)
            
    return message
        
        