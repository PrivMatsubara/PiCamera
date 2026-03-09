import cv2
from flask import Flask, render_template, Response
from picamera2 import Picamera2
import numpy as np

app = Flask(__name__)

# Picamera2で初期化
picam2 = Picamera2()
config = picam2.create_video_configuration(main={"size": (640, 480), "format": "RGB888"})
picam2.configure(config)
picam2.start()

def generate_frames():
    while True:
        # フレーム取得（numpy配列で返ってくる）
        frame = picam2.capture_array()
        
        # RGB → BGR に変換（OpenCVはBGR）
        frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        
        # JPEGエンコード
        ret, buffer = cv2.imencode('.jpg', frame_bgr)
        if not ret:
            continue
        
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
