import cv2
from flask import Flask, render_template, Response

app = Flask(__name__)

# カメラの初期化 (0はデフォルトカメラ。USBカメラやPiカメラモジュールのデバイス番号に依存します)
# Raspberry Pi OSのバージョンや環境によっては cv2.VideoCapture(0, cv2.CAP_V4L2) が必要な場合があります。
camera = cv2.VideoCapture(0)

def generate_frames():
    while True:
        # カメラからフレームを読み込む
        success, frame = camera.read()
        if not success:
            break
        else:
            # フレームをJPEG形式にエンコード
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            # マルチパートレスポンスとしてフレームを返す（MJPEGストリーム）
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    # host='0.0.0.0' を指定することで、ローカルネットワーク内の他の端末からもアクセス可能になります
    app.run(host='0.0.0.0', port=5000, debug=True)
