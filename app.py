from flask import Flask
from flask_cors import CORS
# 데이터 조회 파일
import csv_test as df

app = Flask(__name__)
# CORS 설정을 해줘야 클라이언트에서 접속 가능, 하지만 보안 취약
cors = CORS(app, resources={r"*":{"origins":"*"}})

# csv 데이터 가져오기
themepark_recent = df.themepark_recent()
themepark_basic = df.themepark_basic()

# 기본 로컬 설정
@app.route("/")
def hello():
    return "Hello, my Flask!"

@app.route("/themepark/<date>/<place>/<kategorie>")
def get_themepark(date, place, kategorie):
    result = df.get_info(themepark_recent, themepark_basic, place, kategorie, int(date))
    return result

# python app.py 서버 열기
if __name__ == "__main__":
    # app.run(ssl_context = "adhoc")
    app.run(host="0.0.0.0", port=5555)

# pythonanywhere를 이용해서 배포해서 flutter에 연결