FROM python:3.11-slim

# FFmpeg 및 필수 패키지 설치
RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# 현재 폴더의 모든 파일을 복사
COPY . .

# 라이브러리 설치
RUN pip install --no-cache-dir -r requirements.txt

# 서버 실행 (포트는 Render가 환경변수로 주입)
CMD gunicorn app:app --bind 0.0.0.0:$PORT
