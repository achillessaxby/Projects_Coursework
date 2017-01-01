import os

command = "curl -O https://data.cityofnewyork.us/api/file_data/\
YObIR0MbpUVA0EpQzZSq5x55FzKGM2ejSeahdvjqR20?filename=ZIP_CODE_040114.zip"
name = "YObIR0MbpUVA0EpQzZSq5x55FzKGM2ejSeahdvjqR20?filename=ZIP_CODE_040114.zip"

def getzips():
    '''The function downloads a zipcode shape file 
    into the PUIDATA directory from the NYC Open data
    Author: aes807 referring code from vys217 and from:
    https://github.com/fedhere/PUI2016_fb55/blob/master/HW3_fb55/citibikes_gender.ipynb
    '''
    if not os.path.isfile(os.getenv("PUIDATA") + "/" + "ZIP_CODE_040114.shp"):
        
        # if in the current file just move it to PUIData
        if os.path.isfile("ZIP_CODE_040114.shp"):
            print ('files in current directory, moving it to PUIdata')
       
            if os.system("mv " + "ZIP_CODE* " + os.getenv("PUIDATA")):
                print ("Error moving files!, Please check!")
                
        #otherwise start looking for the zip file
        else:
            # Check if zip file in PUIdata
            
            if not os.path.isfile(os.getenv("PUIDATA") + "/" + name):
                # Check zip file in current directory
                if not os.path.isfile(name):
                    # Download zip file if not in PUIdata and current directory
                    print ('Downloading')
                    
                    os.system(command)
                    
                #Move Zip file to PUIdata
                
                os.system("mv " + name + ' ' + os.getenv("PUIDATA"))
                
            ### unzip the zip file, it gets unzipped to current directory
            
            if not os.system("unzip " + os.getenv("PUIDATA") + "/" + name):
                print("Unzipped")
                # Move the unzipped folder to PUIData
                
                if os.system("mv " + "ZIP_CODE*" + ' ' + os.getenv("PUIDATA")):
                    print ("Error moving files!, Please check!")
                    
    ### One final check:
    if not os.path.isfile(os.getenv("PUIDATA") + "/" + "ZIP_CODE_040114.shp"):
        print ("WARNING!!! something is wrong: the file is not there!")
    else:
        print ("Folder with required files in PUIdata, you can continue")                
               