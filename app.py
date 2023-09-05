from flask import Flask
from flask_cors import CORS
# 데이터 조회 파일
import csv_test as df

app = Flask(__name__)
# 한글 깨짐 현상 해결
app.config["JSON_AS_ASCII"]=False
# CORS 설정을 해줘야 클라이언트에서 접속 가능, 하지만 보안 취약
cors = CORS(app, resources={r"*":{"origins":"*"}})

# csv 데이터 가져오기
themepark_recent = df.themepark_recent()
themepark_basic = df.themepark_basic()
themepark_place = ["에버랜드", "롯데월드", "서울랜드"]
themepark_kategorie = ["운영시간", "공연일정", "편의시설", "장애인 편의시설", "가족 편의시설", "요금우대", "음식점", "대중교통 이용방법"]

# 기본 로컬 설정
@app.route("/")
def hello():
    return "Hello, my Flask!"

# 크롤링 데이터와 기본 정보 조회해서 결과 보여줌
@app.route("/themepark/<date>/<code>")
def get_themepark(date, code):
    check_list = df.get_code(themepark_place, themepark_kategorie, code)
    result = df.get_data(themepark_recent, themepark_basic, int(date), check_list)
    return result
    

# python app.py 서버 열기
if __name__ == "__main__":
    # app.run(ssl_context = "adhoc")
    app.run(host="0.0.0.0", port=5555)

# pythonanywhere를 이용해서 배포해서 flutter에 연결