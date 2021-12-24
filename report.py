import json
import time



# 读取经纬度
# 读取电量
def report(ws):
    while True:
        message = {
            "instructions": "0",
            "message": "上传数据开始",
            "to": "system"
        }
        dumps = json.dumps(message)
        ws.send(dumps)
        time.sleep(1)