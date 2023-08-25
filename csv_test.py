import pandas as pd

def csv_data():
    data = pd.read_csv("230818_Themepark_df.csv")
    return data

# 일주일을 반환하는 함수
def show_week(data):
    week = str(list(set(data["날짜"].values)))
    return week

# 선택된 날짜와 장소의 공연일정을 보여줌
def themepark_info(data, date, place):
    today_show = data.loc[(data["날짜"]==date) & (data["장소"]==place)]["공연일정"]
    # Series 형식을 String 형식으로 변환
    result = ", ".join(today_show.values)
    return result


# data = csv_data()
# week = list(set(data["날짜"].values))
# print(type(week))