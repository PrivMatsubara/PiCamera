# Raspberry Pi Web Camera App

FlaskとOpenCVを使用して、Raspberry Piに接続したカメラの映像をMotion JPEG (MJPEG) ストリームとしてWebページに表示するシンプルなアプリケーションです。

## 実行要件
- Raspberry Pi (OS: Raspberry Pi OS)
- Python 3.x
- カメラ (USB Webカメラ、または Raspberry Pi カメラモジュール)

## 準備と実行手順 (Raspberry Pi上での操作)

1. パッケージ一覧を更新し、必要なシステムライブラリ（OpenCVに必要）をインストールします:
   ```bash
   sudo apt-get update
   sudo apt-get install -y libgl1-mesa-glx libglib2.0-0
   ```

2. 仮想環境（任意ですが推奨）を作成し、アクティベートします:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. 依存ライブラリをインストールします:
   ```bash
   pip install -r requirements.txt
   ```

4. アプリケーションを起動します:
   ```bash
   python app.py
   ```

5. 同じネットワーク内にあるブラウザから、以下のURLにアクセスして映像を確認します:
   `http://<Raspberry_PiのIPアドレス>:5000`

## トラブルシューティング
- 画像が表示されない場合、OpenCVがカメラを正しく認識できていない可能性があります。`app.py` 内の `cv2.VideoCapture(0)` の数値を 1 などの他のインデックスに変更するか、Linux特有のドライバ指定（`cv2.VideoCapture(0, cv2.CAP_V4L2)`）を試してください。
- GPIOやRaspi Camera固有の設定（legacy stack等）が必要なOSバージョンの場合、 `sudo raspi-config` からカメラのインターフェースを有効化してください。
