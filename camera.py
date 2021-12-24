import time

from flask import Flask, Response
import cv2
app = Flask(__name__)
video = cv2.VideoCapture(0)



def gen(video):
    while True:

        success, image = video.read()

        ret, jpeg = cv2.imencode('.jpg', image)
        frame = jpeg.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    global video
    return Response(gen(video),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

def start():
    app.run(host='0.0.0.0', port=2204, threaded=True)
