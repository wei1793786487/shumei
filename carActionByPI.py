import RPi.GPIO as GPIO
import time

# BOARD编号方式，基于插座引脚编号
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


left_front_1=19
left_front_2=26
right_front_1=6
right_front_2=13

left_after_1=21
left_after_2=20
right_after_1=16
right_after_2=12

GPIO.setup(left_after_1, GPIO.OUT)
GPIO.setup(left_after_2, GPIO.OUT)
GPIO.setup(right_after_1, GPIO.OUT)
GPIO.setup(right_after_2, GPIO.OUT)


GPIO.setup(left_front_1, GPIO.OUT)
GPIO.setup(left_front_2, GPIO.OUT)
GPIO.setup(right_front_1, GPIO.OUT)
GPIO.setup(right_front_2, GPIO.OUT)

def left_after_wheel(reverse):
    if(reverse==1):
        GPIO.output(left_after_1, GPIO.LOW)
        GPIO.output(left_after_2, GPIO.HIGH)
    elif(reverse==2):
        GPIO.output(left_after_1, GPIO.HIGH)
        GPIO.output(left_after_2, GPIO.LOW)
    else:
        GPIO.output(left_after_1, GPIO.LOW)
        GPIO.output(left_after_2, GPIO.LOW)


def right_after_wheel(reverse):
    if (reverse == 1):
        GPIO.output(right_after_1, GPIO.LOW)
        GPIO.output(right_after_2, GPIO.HIGH)
    elif (reverse == 2):
        GPIO.output(right_after_1, GPIO.HIGH)
        GPIO.output(right_after_2, GPIO.LOW)
    else:
        GPIO.output(right_after_1, GPIO.LOW)
        GPIO.output(right_after_2, GPIO.LOW)



def left_front_wheel(reverse):
    if(reverse==1):
        GPIO.output(left_front_1, GPIO.LOW)
        GPIO.output(left_front_2, GPIO.HIGH)
    elif(reverse==2):
        GPIO.output(left_front_1, GPIO.HIGH)
        GPIO.output(left_front_2, GPIO.LOW)
    else:
        GPIO.output(left_front_1, GPIO.LOW)
        GPIO.output(left_front_2, GPIO.LOW)


def right_front_wheel(reverse):
    if (reverse == 1):
        GPIO.output(right_front_1, GPIO.LOW)
        GPIO.output(right_front_2, GPIO.HIGH)
    elif (reverse == 2):
        GPIO.output(right_front_1, GPIO.HIGH)
        GPIO.output(right_front_2, GPIO.LOW)
    else:
        GPIO.output(right_front_1, GPIO.LOW)
        GPIO.output(right_front_2, GPIO.LOW)

def car_front():
    left_front_wheel(1)
    right_front_wheel(1)
    left_after_wheel(1)
    right_after_wheel(1)

def car_stop():
    left_front_wheel(0)
    right_front_wheel(0)
    left_after_wheel(0)
    right_after_wheel(0)


def car_after():
    left_front_wheel(2)
    right_front_wheel(2)
    left_after_wheel(2)
    right_after_wheel(2)


def car_front_turn_left():
    left_front_wheel(0)
    right_front_wheel(1)
    left_after_wheel(1)
    right_after_wheel(1)

def car_front_turn_rigth():
    left_front_wheel(1)
    right_front_wheel(0)
    left_after_wheel(1)
    right_after_wheel(1)


def car_after_turn_rigth():
    left_front_wheel(1)
    right_front_wheel(1)
    left_after_wheel(0)
    right_after_wheel(1)

def car_after_turn_left():
    left_front_wheel(1)
    right_front_wheel(1)
    left_after_wheel(1)
    right_after_wheel(0)

if __name__ == '__main__':
    car_stop()