import os

def getcode():
    '''The function downloads a shape file into the PUIDATA directory from the NYC Open data
    Author: Achilles Edwin Alfred Saxby
    Code:
    https://github.com/fedhere/PUI2016_fb55/blob/master/HW3_fb55/citibikes_gender.ipynb
    '''
    # First I will check that required folder is already in PUIdata or not
    if not os.path.isdir(os.getenv("PUIDATA") + "/" + "nycb2010_16d"):
        
        # if in the current dir just move it to PUIData
        if os.path.isdir("nycb2010_16d"):
            print ('Folder in current directory, moving it to PUIdata')
            if os.system("mv " + "nycb2010_16d " + os.getenv("PUIDATA")):
                print ("Error moving file!, Please check!")
                
        #otherwise start looking for the zip file
        else:
            # Check if zip file in PUIdata
            if not os.path.isfile(os.getenv("PUIDATA") + "/" + "nycb2010_16d.zip"):
                # Check zip file in current directory
                if not os.path.isfile("nycb2010_16d.zip"):
                    # Download zip file if not in PUIdata and current directory
                    print ('Downloading')
                    os.system("curl -O https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nycb2010_16d.zip")
                
                #Move Zip file to PUIdata
                os.system("mv " + "nycb2010_16d.zip " + os.getenv("PUIDATA"))
                
            ### unzip the zip file, it gets unzipped to current directory 
            if not os.system("unzip " + os.getenv("PUIDATA") + "/" + "nycb2010_16d.zip"):
                print("Unzipped")
                # Move the unzipped folder to PUIData
                if os.system("mv " + "nycb2010_16d " + os.getenv("PUIDATA")):
                    print ("Error moving file!, Please check!")
                    
    ### One final check:
    if not os.path.isdir(os.getenv("PUIDATA") + "/" + "nycb2010_16d"):
        print ("WARNING!!! something is wrong: the file is not there!")
    else:
        print ("Folder with required files in PUIdata, you can continue")