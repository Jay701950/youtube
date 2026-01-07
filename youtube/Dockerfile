FROM python:3.11-slim

# 시스템 패키지 업데이트 및 FFmpeg 설치
RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*

# 작업 디렉토리 설정
WORKDIR /app

# 현재 폴더의 모든 파일을 서버로 복사
COPY . .

# 파이썬 라이브러리 설치
RUN pip install --no-cache-dir -r requirements.txt

# 서버 실행 (포트는 Render 환경변수 사용)
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:10000"]
