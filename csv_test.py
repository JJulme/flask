import pandas as pd

def themepark_recent():
    data = pd.read_csv("230818_Themepark_df.csv")
    return data

def themepark_basic():
    data = pd.read_csv("Themepark_df.csv")
    return data

# 안쓰게 됨
# 일주일을 반환하는 함수
def show_week(data):
    week = str(list(set(data["날짜"].values)))
    return week

# 선택된 날짜와 장소의 공연일정을 보여줌
def themepark_recent_info(data, date, place, kategorie):
    data = data.loc[(data["날짜"]==date) & (data["장소"]==place)][kategorie]
    # Series 형식을 String 형식으로 변환
    result = ", ".join(data.values)
    return result

# 선택된 장소, 카테고리 보여줌
def themepark_basic_info(data, place, kategorie):
    data = data.loc[(data["장소"]==place)][kategorie]
    result = ", ".join(data.values)
    return result

# 크롤링 데이터와 기본 정보 조회해서 결과 보여줌
def get_info(recent, basic, place:str, kategorie:str, date=2023):
    # 크롤링 데이터 조회
    try:
        data = recent.loc[(recent["날짜"]==date) & (recent["장소"]==place)][kategorie]
    # 기본 정보 조회
    except:
        data = basic.loc[(basic["장소"]==place)][kategorie]
    # 결과
    finally:
        result = ", ".join(data.values)
        return result
