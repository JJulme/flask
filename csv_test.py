import pandas as pd

def themepark_recent():
    data = pd.read_csv("230818_Themepark_df.csv")
    return data

def themepark_basic():
    data = pd.read_csv("Themepark_df.csv")
    return data

# 코드를 가져와 해석해서 선택된 목록을 확인    
def get_code(place:list, kategorie:list, code:str):
    # 언더바를 기준으로 장소와 정보 코드 분리
    code_list = code.split("_")
    # 장소선택한 코드 저장
    place_code = list(code_list[0])
    # 정보선택한 코드 저장
    kategorie_code = list(code_list[1])
    # 선택한 목록 저장할 빈 리스트 생성
    check_place = []
    check_kategorie=[]
    # 선택한 장소 알아내기
    for i in range(len(place_code)):
        if place_code[i]=="0":
            pass
        else:
            check_place.append(place[i])
    # 선택한 정보 알아내기
    for i in range(len(kategorie_code)):
        if kategorie_code[i]=="0":
            pass
        else:
            check_kategorie.append(kategorie[i])
    # 장소리스트와 정보리스트를 하나의 리스트에 넣어 반환
    result = [check_place, check_kategorie]
    return result

# 크롤링 데이터, 기본 정보 데이터, 날짜, 선택한 리스트를 넣고 그에 해당하는 정보 반환
def get_data(recent, basic, day, check_list):
    # 선택한 장소 리스트
    check_place = check_list[0]
    # 선택한 정보 리스트
    check_kategorie = check_list[1]
    # 전체를 저장할 빈리스트 생성
    list_large = []
    # 정보 반복
    for kategorie in check_kategorie:
        # 각 정보를 저장할 빈리스트 생성
        list_small = []
        # 장소반복
        for place in check_place:
            # 크롤링 데이터 조회
            try:
                data = recent.loc[(recent["날짜"]==day) & (recent["장소"]==place)][kategorie]
            # 기본 정보 조회
            except:
                data = basic.loc[(basic["장소"]==place)][kategorie]
            # 나온 결과를 리스트에 저장
            finally:
                # Series 형식을 String 형식으로 변환
                result = ", ".join(data.values)
                # 정보에 맞게 리스트에 추가
                list_small.append(result)
        # 정리된 각 정보리스트를 하나의 리스트에 추가
        list_large.append(list_small)
    return list_large