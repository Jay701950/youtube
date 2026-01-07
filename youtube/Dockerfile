# 1. 파이썬 환경 설정
FROM python:3.11-slim

# 2. FFmpeg 설치 (Docker 환경에서는 apt-get 권한이 있습니다!)
RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*

# 3. 작업 디렉토리 설정 및 파일 복사
WORKDIR /app
COPY . .

# 4. 필수 라이브러리 설치
RUN pip install --no-cache-dir -r requirements.txt

# 5. 실행 (포트는 Render가 자동으로 지정해줍니다)
CMD gunicorn app:app --bind 0.0.0.0:$PORT