import threading

from camera import start
from connectWebsocket import webSocket
from  nps import  nps
from connectWifi import startLogin

# startLogin("215071204203", "143731")
t1 = threading.Thread(target=start)
t1.start()

nps().start()

webSocket()


