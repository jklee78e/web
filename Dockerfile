# Python 3.9 공식 이미지를 기반으로 사용
FROM python:3.9-slim

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 Python 패키지 설치
# requirements.txt 파일에 명시
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 앱 소스 코드 복사
COPY . .

# Streamlit 앱 실행 (컨테이너가 시작될 때 자동으로 실행)
# `--server.port=8051`으로 포트 설정
CMD ["streamlit", "run", "app.py", "--server.port=8051", "--server.enableCORS=false", "--server.enableXsrfProtection=false", "--server.runOnSave=true"]