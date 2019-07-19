import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(15, GPIO.OUT)   
GPIO.setup(11, GPIO.OUT)   
GPIO.setup(13, GPIO.OUT)   
GPIO.setup(16, GPIO.OUT)
GPIO.setup(40, GPIO.OUT,initial=False)

p1= GPIO.PWM(11, 50)      #right back    定义你前进方向右边的轮子向后转，
p2= GPIO.PWM(13, 50)      #right front 
p3= GPIO.PWM(15, 50)      #left front
p4= GPIO.PWM(16, 50)      #left back

def front(d):
    #d=d*0.7
    p1.start(00)
    p2.start(d)
    p3.start(d)
    p4.start(00)   

def back(d):
    #d=d*0.7
    p1.start(d)
    p2.start(00)
    p3.start(00)
    p4.start(d)
        
def right(d):
    #d=d*0.7
    p1.start(00)
    p2.start(d)
    p3.start(00)
    p4.start(d)
    
def left(d):
    #d=d*0.7
    p1.start(d)
    p2.start(00)
    p3.start(d)
    p4.start(00)
    
def stop():
    p1.start(0)
    p2.start(0)
    p3.start(0)
    p4.start(0)



   

        
    


        
        
        
            
        




        
    

