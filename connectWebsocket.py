import json

import websocket

from engineAction import engineAction
from gsp import myThread
from runCar import runCar

id = "744e3e90-4f20-46b4-9b5d-677663375945"

url = "ws://82.157.163.140:10086/api/websocket/0/{}".format(id)
# url = "ws://192.168.1.102:10086/api/websocket/0/{}".format(id)
engin=engineAction()


alive=False

car = runCar()
def on_open(ws):
  myThread(ws).start()
  print("连接成功")

def on_message(ws, message):
    print(message)
    message = json.loads(message)
    distribution = instruction_distribution(message)
    print(message['instructions'])
    if(distribution):
        ws.send(distribution)

def on_error(ws, error):
    print(error)


def on_close(ws):
    print(ws)


# 分发来自手机的小车的命令
def instruction_distribution(message):
    global alive
    print(message)
    instructions = message["instructions"]
    # 处理小车移动
    if instructions == "0":

        car.distribute(message["message"])
    elif instructions=="1":
        # 处理舵机的移动
        engin.distribute(message["message"])



def webSocket():
    # websocket.enableTrace(True)
    # 这里应该生成一个token来加密解密用户的id,不应该直接明文id
    ws = websocket.WebSocketApp(url,
                                on_message=on_message,
                                on_open=on_open,
                                on_error=on_error,
                                on_close=on_close)
    ws.run_forever()
