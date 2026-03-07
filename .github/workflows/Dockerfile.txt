# ラズパイ(ARM)でも動作する軽量なPythonベースイメージ
FROM python:3.9-slim

WORKDIR /app

# 依存モジュールのインストール
COPY src/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ソースコードのコピー
COPY src/ .

# ポートの公開
EXPOSE 80

# アプリケーションの起動
CMD ["python", "app.py"]
