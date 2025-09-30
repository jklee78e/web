from flask import Flask, request, abort
import subprocess
import os

app = Flask(__name__)

# NOTE: GitHub에 설정한 Secret Key와 동일하게 설정해야 합니다.
# 실제 환경에서는 환경 변수를 사용하세요.
GITHUB_SECRET = "web"  # <--- 이 부분을 반드시 GitHub 웹훅 설정과 동일하게 변경하세요!
DEPLOY_SCRIPT = "/home/ubuntu/webß/deploy.sh"

@app.route('/webhook_endpoint', methods=['POST'])
def webhook():
    # 1. Secret Key 검증 (보안 강화 시)
    # 실제 GitHub에서는 요청 헤더의 X-Hub-Signature-256를 확인하는 복잡한 과정이 필요하지만,
    # 간단한 테스트를 위해 Secret Key가 일치하는지 확인하는 로직을 추가할 수 있습니다.
    # 이 코드는 보안 검증을 단순화한 버전입니다. (보안을 위해 실제 서명 검증을 권장합니다.)

    # 2. 유효한 요청 확인 (Ping 테스트 등)
    if request.json and 'zen' in request.json:
        print("Received GitHub Ping Event.")
        return 'Pong', 200

    # 3. 배포 스크립트 실행
    if request.method == 'POST':
        try:
            print(f"Deployment triggered by webhook. Running {DEPLOY_SCRIPT}...")
            
            # 스크립트에 실행 권한이 있는지 확인
            if not os.path.exists(DEPLOY_SCRIPT) or not os.access(DEPLOY_SCRIPT, os.X_OK):
                print(f"Error: {DEPLOY_SCRIPT} is not executable or does not exist.")
                return 'Deploy script not found or not executable', 500

            # deploy.sh 실행 (비동기로 실행하는 것이 좋습니다)
            subprocess.Popen([DEPLOY_SCRIPT], cwd=os.path.dirname(DEPLOY_SCRIPT))
            
            return 'Deployment script started successfully', 200
        
        except Exception as e:
            print(f"Error executing deploy script: {e}")
            return 'Internal Server Error', 500
    
    abort(400) # POST 요청이 아니면 거부

if __name__ == '__main__':
    # Flask 앱을 5000번 포트에서 실행
    app.run(host='0.0.0.0', port=5000)