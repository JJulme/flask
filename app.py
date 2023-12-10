
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, make_response
from flask_cors import CORS
import json
# 데이터 조회 파일
import csv_test as df

app = Flask(__name__)
# CORS 설정을 해줘야 클라이언트에서 접속 가능, 하지만 보안 취약
cors = CORS(app, resources={r"*":{"origin":"*"}})

# 놀이공원 데이터 가져오기 8_9
themepark_recent = []
themepark_basic = df.read_basic("Themepark_230926")
themepark_place = ["롯데월드", "서울랜드", "에버랜드", "이월드", "경주월드", "광주패밀리랜드", "롯데월드 부산", "신화테마파크"]
themepark_kategorie = ["운영시간", "이용요금", "요금우대", "편의시설", "장애인 편의시설", "가족 편의시설", "음식점", "대중교통 이용방법", "주변 가볼만한 곳"]

# 동물원 데이터 가져오기 10_9
zoo_recent = []
zoo_basic = df.read_basic("Zoo_230926")
zoo_place = ["서울대공원", "어린이대공원", "에버랜드 주토피아", "대전오월드 쥬랜드", "전주동물원", "우치동물원", "쥬쥬랜드 동물원", "청주랜드 동물원", "진양호동물원", "인천대공원 어린이동물원"]
zoo_kategorie = ["이용시간", "입장요금", "우대할인", "인기동물", "특이시설", "편의시설", "음식점", "주변 가볼만한 곳", "대중교통 이용방법"]

# 아쿠아리움 데이터 가져오기 16_9
aquarium_recent=[]
aquarium_basic = df.read_basic("Aquarium_230926")
aquarium_place = ["코엑스 아쿠아리움", "아쿠아플라넷 63", "롯데월드 아쿠아리움", "아쿠아플라넷 일산", "아쿠아플라넷 광교", "플레이아쿠아리움 부천", "경포아쿠아리움", "대전아쿠아리움", "대전엑스포아쿠아리움", "다누리아쿠아리움", "SEA LIFE 부산아쿠아리움", "아라마루 아쿠아리움", "대구아쿠아리움", "울진아쿠아리움", "아쿠아플라넷 여수", "아쿠아플라넷 제주"]
aquarium_kategorie = ["이용시간", "입장요금", "우대할인", "특이시설", "편의시설", "음식점", "주변 가볼만한 곳", "대중교통 이용방법"]

# 스키장 데이터 가져오기 12_11
ski_recent=[]
ski_basic = df.read_basic("Ski_231209")
ski_place = ["곤지암리조트", "지산리조트","엘리시안 강촌", "비발디파크", "알펜시아", "오크벨리", "오투리조트", "용평리조트", "하이원리조트", "휘닉스파크", "덕유산 리조트", "에덴벨리 리조트"]
ski_kategorie = ["이용시간", "입장요금", "장비렌탈", "의류렌탈", "눈썰매장", "우대할인", "특이시설", "음식점", "편의시설", "셔틀버스", "대중교통 이용방법"]

# 기본 로컬 설정
@app.route('/')
def hello_world():
    return 'Hello from JJulme`s Flask!'

# 크롤링 데이터와 기본 정보 조회해서 결과 보여줌
@app.route("/themepark/<date>/<code>")
def get_themepark(date, code):
    # 장소, 정보, 코드로 선택한 버튼 추출
    check_list = df.get_code(themepark_place, themepark_kategorie, code)
    # 선택된 정보로 데이터 반환
    result = df.get_data(themepark_recent, themepark_basic, int(date), check_list)
    # 한글 깨짐 현상 해결
    result = json.dumps(result, ensure_ascii=False)
    res = make_response(result)
    return res

# 동물원 정보 조회해서 결과 보여줌
@app.route("/zoo/<date>/<code>")
def get_zoo(date, code):
    # 장소, 정보, 코드로 선택한 버튼 추출
    check_list = df.get_code(zoo_place, zoo_kategorie, code)
    # 선택된 정보로 데이터 반환
    result = df.get_data(zoo_recent, zoo_basic, int(date), check_list)
    # 한글 깨짐 현상 해결
    result = json.dumps(result, ensure_ascii=False)
    res = make_response(result)
    return res

# 아쿠아리움 정보 조회해서 결과 보여줌
@app.route("/aquarium/<date>/<code>")
def get_aquarium(date, code):
    # 장소, 정보, 코드로 선택한 버튼 추출
    check_list = df.get_code(aquarium_place, aquarium_kategorie, code)
    # 선택된 정보로 데이터 반환
    result = df.get_data(aquarium_recent, aquarium_basic, int(date), check_list)
    # 한글 깨짐 현상 해결
    result = json.dumps(result, ensure_ascii=False)
    res = make_response(result)
    return res

# 스키장 정보 조회해서 결과 보여줌
@app.route("/ski/<date>/<code>")
def get_ski(date, code):
    # 장소, 정보, 코드로 선택한 버튼 추출
    check_list = df.get_code(ski_place, ski_kategorie, code)
    # 선택된 정보로 데이터 반환
    result = df.get_data(ski_recent, ski_basic, int(date), check_list)
    # 한글 깨짐 현상 해결
    result = json.dumps(result, ensure_ascii=False)
    res = make_response(result)
    return res

# python app.py 서버 열기
if __name__ == "__main__":
    # app.run(ssl_context = "adhoc")
    app.run(host="0.0.0.0", port=5555)

# pythonanywhere를 이용해서 배포해서 flutter에 연결