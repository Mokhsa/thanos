import os 
import random
import time


def get_files(p):
    return(os.listdir(p))

def destroy(path): 
    '''
    parameters
    path: path to the directory you want to destroy
    delete half of the files in the directory
    
    '''
    Folderlength=len(get_files(path))//2
    for i in range(Folderlength):
        file_name=random.choice(get_files(path))
        os.remove(f"{path}/{file_name}")
        time.sleep(1)
        print(f"{file_name} destroyed")
        
        #comment
destroy('universe')