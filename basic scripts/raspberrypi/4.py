from gpiozero import MotionSensor
#from picamera import PiCamera
import time
import datetime
#libraries for importing to excel
import xlwt 
from xlwt import Workbook 
 
# Create object for PIR Sensor
# PIR Sensor is on GPIO-4 (Pin 7)
pir = MotionSensor(4)

# Workbook is created 
wb = Workbook()

# add_sheet is used to create sheet. 
sheet1 = wb.add_sheet('Sheet 1') 
#use only if required if excel file isnt present

#define variables here
x=0

# Create Object for Camera
#camera = PiCamera()
 
# Function to create new Filename from date and time
def getFileName():
	return datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S.jpg")

def makeentry():
    dtdt = datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S")
 
while True:
    # Get a Filename
    ##filename = getFileName()
    # Wait for a motion to be detected
    pir.wait_for_motion()#Do not forget the brackets else it runs constantly
    # Print text to Shell
    print("Motion Detected!!")
    x = x+1
    sheet1.write(x, 0, datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S")) #.strftime("%Y-%m-%d_%H.%M.%S")) 
    wb.save('pir_data.xls') 
    # Preview camera on screen until picture is taken
    ##camera.start_preview()
    # Take a picture of intruder
    ##camera.capture(filename)
    ##camera.stop_preview()
    # Wait t seconds before repeating
    time.sleep(5)