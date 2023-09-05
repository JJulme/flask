import pandas as pd

def themepark_recent():
    data = pd.read_csv("230818_Themepark_df.csv")
    return data

def themepark_basic():
    data = pd.read_csv("Themepark_df.csv")
    return data

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
        # Series 형식을 String 형식으로 변환
        result = ", ".join(data.values)
        return result
    
def get_code(place:list, kategorie:list, code:str):
    code_list = code.split("_")
    place_code = list(code_list[0])
    kategorie_code = list(code_list[1])
    check_place = []
    check_kategorie=[]
    for i in range(len(place_code)):
        if place_code[i]=="0":
            pass
        else:
            check_place.append(place[i])
    for i in range(len(kategorie_code)):
        if kategorie_code[i]=="0":
            pass
        else:
            check_kategorie.append(kategorie[i])

    result = [check_place, check_kategorie]
    return result

def get_data(recent, basic, day, check_list):
    check_place = check_list[0]
    check_kategorie = check_list[1]
    list_large = []
    for kategorie in check_kategorie:
        list_small = []
        for place in check_place:
            try:
                data = recent.loc[(recent["날짜"]==day) & (recent["장소"]==place)][kategorie]
            except:
                data = basic.loc[(basic["장소"]==place)][kategorie]
            finally:
                # Series 형식을 String 형식으로 변환
                result = ", ".join(data.values)
                list_small.append(result)
        list_large.append(list_small)
    return list_large