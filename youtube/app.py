from flask import Flask, render_template, request, send_file
import yt_dlp
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    # 비밀번호 확인
    password = request.form.get('password')
    url = request.form.get('url')

    if password != 'ydy':
        return "비밀번호가 틀렸습니다.", 403

    if not url:
        return "URL을 입력해주세요.", 400

    # 다운로드 설정
    ydl_opts = {
        'format': 'best',
        'outtmpl': 'downloaded_video.mp4',
        'noplaylist': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        return send_file('downloaded_video.mp4', as_attachment=True)
    except Exception as e:
        return f"에러 발생: {str(e)}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))
