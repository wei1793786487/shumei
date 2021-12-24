import subprocess
import threading


class nps(threading.Thread):

    def run(self):
        cmd="/home/pi/nps/npc -server=82.157.163.140:8024 -vkey=2cemufh45hrzsxht -type=tcp"
        print(cmd)
        # 线程不阻塞
        popen = subprocess.Popen([cmd], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE,
                                 stderr=subprocess.PIPE)


