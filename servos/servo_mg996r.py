import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(37, GPIO.OUT)   
GPIO.setup(35, GPIO.OUT)  
servo_t= GPIO.PWM(37, 50)  #theta servo     {3.5:0,7:90,12:180}  left center right
servo_v= GPIO.PWM(35, 50)  #vertical servo  {3.5:0,7:90,12:180}  top center bottom


def servo_T(ang):
    if ang<=180 and ang>=0:
        d=float(3.5+0.04722*ang)
        servo_t.start(d)
    else:
        print("Servo_T out of range")


def servo_V(ang):
    if ang<=180 and ang>=0:
        d=float(3.2+0.04202*ang)
        servo_v.start(d)
    else:
        print("Servo_V out of range")


def servo_init():     # initialize the servo_V/T
    servo_V(90)
    servo_T(90)
    time.sleep(1)
    servo_t.start(0)
    servo_v.start(0)
    return [90,90]

def servo_safe():
    servo_V(90)
    servo_T(10)
    time.sleep(1.3)
    servo_silent()
    
def servo_silent():   # stop arm move or shake
    servo_t.start(0)
    servo_v.start(0)

def servo_silent_V():   # stop arm move or shake
    servo_v.start(0)

def servo_silent_T():   # stop arm move or shake
    servo_t.start(0)

if __name__=='__main__':
    a=servo_init()
    print("MG996R Servo Arm going to move test!!!")
    print(a,type(a))
    time.sleep(4)
    while 1:
        ang=100
        servo_T(ang)
        time.sleep(1.5)
        ang=0
        servo_T(ang)
        time.sleep(1.5)
        ang=180
        servo_V(ang)
        time.sleep(1.5)
        ang=0
        servo_V(ang)
        time.sleep(1.5)
     



        
        
        
            
        




        
    

