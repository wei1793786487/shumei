# 驱动小车移动
from  carActionByPI import *


class runCar(object):

    def distribute(self,type):
        type=int(type)
        if (type == 0):
            print("stop")
        elif (type == 2):
            self.t_up()
        elif (type == 3):
            self.t_left()
        elif (type == 4):
            self.t_right()
        elif (type == 1):
            self.t_down()
        else:
            print("未知命令")

    def t_up(self):
        car_front()
        time.sleep(0.3)
        car_stop()

    def t_left(self):
        car_front_turn_left()
        time.sleep(1)
        car_stop()


    def t_right(self):
        car_front_turn_rigth()
        time.sleep(1)
        car_stop()
    def t_down(self):
        car_after()
        time.sleep(0.3)
        car_stop()

