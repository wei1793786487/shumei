# 舵机移动
from time import sleep
import RPi.GPIO as GPIO

vertica=0
lever=90
gpio_io1 = 18
gpio_io2 = 23

class engineAction(object):
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        GPIO.setup(gpio_io1, GPIO.OUT)
        GPIO.setup(gpio_io2, GPIO.OUT)

        self.setServoAngle(gpio_io1, vertica)
        self.setServoAngle(gpio_io2, lever)

    def setServoAngle(self,servo, angle):
        print(angle)
        assert angle >= 0 and angle <= 180
        pwm = GPIO.PWM(servo, 50)
        pwm.start(8)
        dutyCycle = 1.8 + angle / 360 * 20
        pwm.ChangeDutyCycle(dutyCycle)
        sleep(0.3)
        pwm.stop()

    def distribute(self,type):
        if (type == "0"):
            self.t_stop()
        elif (type == "1"):
            self.t_up()
        elif (type == "2"):
            self.t_down()
        elif (type == "3"):
            self.t_left()
        elif (type == "4"):

            self.t_right()

        else:
            print("未知命令")

    def t_up(self):
        global vertica
        print("上")
        if(vertica<100):
            vertica =vertica + 10
        self.setServoAngle(gpio_io1, vertica)

    def t_left(self):
        print("左")
        global lever
        if (lever > 0):
            lever = lever - 10
        self.setServoAngle(gpio_io2, lever)

    def t_right(self):
        print("右")
        global lever
        if (lever < 180):
         lever = lever + 10
        self.setServoAngle(gpio_io2, lever)


    def t_down(self):
        global vertica
        print("下")
        if (vertica >0):
            vertica = vertica - 10
        self.setServoAngle(gpio_io1, vertica)



    def t_stop(self):
        print("归为")


