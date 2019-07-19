import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(33, GPIO.OUT)   
GPIO.setup(36, GPIO.OUT)  
servo_S= GPIO.PWM(33, 50)  #theta servo     {3.5:0,7:90,12:180}  left center right
servo_T= GPIO.PWM(36, 50)  #vertical servo  {3.5:0,7:90,12:180}  top center bottom


def servo_spin(ang):
    if ang<=180 and ang>=0:
        d=float(3+0.05*ang)
        servo_S.start(d)
    else:
        print("servo_spin out of range")


def servo_tilt(ang):
    if ang<=180 and ang>=0:
        d=float(3+0.05*ang)
        servo_T.start(d)
    else:
        print("servo_tilt out of range")


def servo_init():     # initialize the servo_tilt/T
    servo_tilt(90)
    servo_spin(90)
    time.sleep(1)
    servo_S.start(0)
    servo_T.start(0)
    return [90,90]

def servo_safe():
    servo_tilt(5)
    servo_spin(3)
    time.sleep(1.3)
    servo_silent()

def servo_silent():   # stop arm move or shake
    servo_S.start(0)
    servo_T.start(0)

def servo_silent_tilt():   # stop arm move or shake
    servo_T.start(0)

def servo_silent_spin():   # stop arm move or shake
    servo_S.start(0)

if __name__=='__main__':
    a=servo_safe()
    print("SG90 Servo Arm going to move test!!!")
    print(a,type(a))
    time.sleep(4)
    while 1:
        for i in [0,90,175]:
            servo_spin(i)
            time.sleep(1)
            for j in [10,90,180,70]:
                servo_tilt(j)
                time.sleep(1)
       
     



        
        
        
            
        




        
    

