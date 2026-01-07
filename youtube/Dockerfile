FROM python:3.11-slim

# 필요한 패키지 설치
RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .

# 라이브러리 설치
RUN pip install --no-cache-dir -r requirements.txt

# Render 포트 설정
ENV PORT=10000
EXPOSE 10000

# 서버 실행
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:10000"]
