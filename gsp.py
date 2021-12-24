import json

import serial

import threading
import time

ser = serial.Serial("/dev/ttyUSB0",38400)#打开串口，存放到ser中，/dev/ttyUSB0是端口名，9600是波特率

class myThread(threading.Thread):  # 继承父类threading.Thread
    def __init__(self, socket):
        threading.Thread.__init__(self)
        self.socket = socket


    def run(self):
        while True:
            readline = str(str(ser.readline())[2:])
            if("$CFANT" in str(readline)):
                # print("开始")
                info = []
                for i in  range(6):
                    info.append(str(str(ser.readline())[2:]))
                self.analysis(info)

    def analysis(self,info):
        gps_info = self.getGpsInfo(info[0])
        if(int(gps_info[4])==0):
            # print("未定位不触发")
            return
        speed = self.getSpeed(info[4])
        time = self.getTime(info[-1])
        self.sendMessage([time, speed, gps_info])

    def getGpsInfo(self,infos):
        info = infos.split(",")
        latitude = info[2]
        Latitudinal_hemisphere = info[3]
        longitude = info[4]
        longitude_hemisphere = info[5]
        gps_status = info[6]
        satellite_number = info[7]
        accuracy = info[8]
        Altitude = info[9]
        return [latitude, Latitudinal_hemisphere, longitude, longitude_hemisphere, gps_status, satellite_number,
                accuracy, Altitude]

    def getSpeed(self,speeds):
        print(speeds)
        # 正北方向与速度
        speed = speeds.split(",")
        direction = speed[1]
        speed = speed[7]
        return [direction, speed]

    def getTime(self,time):
        times = time.split(",")
        hour = times[1][0:2]
        minute = times[1][2:4]
        second = times[1][4:6]
        millisecond = times[1][7::]
        return "{}-{}-{} {}:{}:{} {}".format(times[4], times[3], times[2], hour, minute, second, millisecond)

    def sendMessage(self,message):
        # 10是主动推送数据
        # print(message)
        message = {
            "instructions": 10,
            "message": message,
            "to": "1"
        }
        dumps = json.dumps(message)
        self.socket.send(dumps)
        time.sleep(1)