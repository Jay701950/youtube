import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    data = request.json
    if data.get('password') != 'ydy':
        return jsonify({'success': False, 'message': '비밀번호 틀림!'})
    
    # Render 서버의 용량 제한 때문에 실제 다운로드 로직은 
    # 테스트 후 클라우드 저장소(S3 등)나 바로 전송 방식으로 고도화가 필요합니다.
    # 일단은 기본 로직을 유지합니다.
    return jsonify({'success': True, 'message': '서버 연결 성공!'})

if __name__ == '__main__':
    # Render에서 지정하는 포트를 사용하도록 설정
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)