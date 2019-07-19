import joystick,time,threading
import RPi.GPIO as GPIO
import run_pwm
from servos import servo_mg996r as mg996r
from servos import servo_sg90 as sg90

mg996r.servo_init()    			#Initial servo to middle position

def go1():
    time.sleep(3)
    ang_V=90
    ang_T=90
    while 1:
        d=joystick.joy_axi1		#Get joystick key values
        d0=d[0]
        d1=d[1]
        d2=d[2]
        d3=d[5]
        d4=d[4]
        if abs(d1)>=abs(d0):		#Define the car motor moving direction
            if d1>0 and abs(d1)>=0.1:
                run_pwm.front(abs(d1*100))
                time.sleep(0.05)
            elif d1<0 and abs(d1)>=0.1:
                run_pwm.back(abs(d1*100))
                time.sleep(0.05)
        elif abs(d1)<abs(d0):
            if d0>0 and abs(d0)>=0.1:
                run_pwm.right(abs(d0*100))
                time.sleep(0.05)
            elif d0<0 and abs(d0)>=0.1:
                run_pwm.left(abs(d0*100))
                time.sleep(0.05)
        if abs(d1)<0.1 and abs(d0)<0.1:
            run_pwm.stop()
            time.sleep(0.01)
       
        if abs(d2)>0:
            ang_V+=d2*12
            if ang_V>180:
                ang_V=180
            elif ang_V<0:
                ang_V=0
            mg996r.servo_V(ang_V)
            time.sleep(abs(d2)*0.001)
        else:
            mg996r.servo_silent_V()
        if abs(d3)>0:
            ang_T+=d3*12
            if ang_T>180:
                ang_T=180
            elif ang_T<0:
                ang_T=0
            mg996r.servo_T(ang_T)
            time.sleep(abs(d3)*0.001)
        else:
            mg996r.servo_silent_T()
       
def main_axi():
   while 1:
       if joystick.joy_left1[0] == 1:
           print("buton 0 being pressed")
           time.sleep(0.1)

thread1 = threading.Thread(target=go1, args=())				#car main flow
thread2 = threading.Thread(target=joystick.ps4_detect, args=())		#PS4 detect

thread1.start()
thread2.start()
