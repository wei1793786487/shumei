# import time
#
# import serial
#
# # ser = serial.Serial("/dev/ttyUSB1", 9600)    # 第一个参数就是上面那个黄色字体  第二个参数填波特率
# # ser.flushInput()    # 清除缓存
#
#
# def car_up():
#     print("上")
#     d = bytes.fromhex("55")
#     print(d)
#     ser.write(d)
#     time.sleep(1)
#     ser.write(bytes.fromhex("ff"))
#
#
# def car_down():
#     print("上")
#     d = bytes.fromhex("55")
#     print(d)
#     ser.write(d)
#     time.sleep(1)
#     ser.write(bytes.fromhex("ff"))
#
#
# def car_right():
#     print("左")
#     d = bytes.fromhex("77")
#     print(d)
#     ser.write(d)
#     time.sleep(1)
#     ser.write(bytes.fromhex("ff"))
#
#
# def car_left():
#     print("右")
#     d = bytes.fromhex("15")
#     print(d)
#     ser.write(d)
#     time.sleep(1)
#     ser.write(bytes.fromhex("ff"))
#
#
#
#
#
#
