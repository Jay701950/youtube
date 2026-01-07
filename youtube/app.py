from flask import Flask, render_template, request, send_file
import yt_dlp
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    password = request.form.get('password')
    url = request.form.get('url')

    if password != 'ydy':
        return "비밀번호가 잘못되었습니다.", 403

    # 파일 저장 경로 설정
    output_filename = 'video.mp4'
    
    ydl_opts = {
        'format': 'best',
        'outtmpl': output_filename,
        'noplaylist': True,
    }

    try:
        # 기존 파일이 있으면 삭제
        if os.path.exists(output_filename):
            os.remove(output_filename)

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        return send_file(output_filename, as_attachment=True)
    except Exception as e:
        return f"오류 발생: {str(e)}", 500

if __name__ == '__main__':
    # Render 환경에 맞는 포트 설정
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
