from flask import Flask
from flask_restx import Api

# 데이터 조회 파일
import csv_test as df

app = Flask(__name__)
api = Api(app)

# csv 데이터 가져오기
data = df.csv_data()

# 기본 로컬 설정
@app.route("/")
def hello():
    return "Hello, my Flask!"

# 일주일 날짜를 넘겨주는 api
@app.route("/week")
def week():
    result = df.show_week(data)
    return result

"""
/themepark/<date>/<place>의 <date> 에
int 형이면 공연일정, str 형이면 기타정보
"""
# 테마파크 정보를 가져오는 api
@app.route("/themepark/<date>/<place>")
# 날짜와 원하는 놀이공원 이름을 받음
def get(date, place):
    # 해당 일자와 놀이공원의 공연 보여줌 - 날짜 int, 장소 str
    result = df.themepark_info(data , int(date), place)
    return result

# python app.py 서버 열기
if __name__ == "__main__":
    # app.run(ssl_context = "adhoc")
    app.run(host="0.0.0.0", port=5555)

# pythonanywhere를 이용해서 배포해서 flutter에 연결