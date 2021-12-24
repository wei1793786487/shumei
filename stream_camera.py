
# 此类属于流媒体的
import threading
import subprocess

class camera(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)


    def run(self):
        # url="rtmp://35.236.157.126:1935/stream/123"
        url="rtmp://tuiliu.etqyl.com/live/1234"
        dirvice="/dev/video0"
        cmd = "ffmpeg -r 30  -i {} -vcodec h264 -max_delay 100 -f flv -g 5 -b 700000 {}".format(dirvice,url)
        print(cmd)
        # 线程不阻塞
        popen = subprocess.Popen([cmd], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE,
                                 stderr=subprocess.PIPE)

    def stop(self):
        cmd = "pgrep ffmpeg"
        p = subprocess.call(cmd, shell=True)
        cmd2 = "sudo kill {}".format(p)
        p = subprocess.call(cmd2, shell=True)




