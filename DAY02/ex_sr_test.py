## =================================================
##          Series 인스턴스 생성 및 이해
## =================================================
import pandas as pd

## 데이터
data = [ 'Google', 1995, 'USA', True ]

## [1] 위 데이터를 Series로 저장하세요.
series_data = pd.Series(data)

## [2] 생성된 Series 객체의 기본 속성 즉, 
##     index, values, dtype, shape, ndim 값을 출력하세요.
print(f"[1]index: {series_data.index}\n")
print(f"[2]values: {series_data.values}\n")
print(f"[3]dtype: {series_data.dtype}\n")
print(f"[4]ndim: {series_data.ndim}\n")

## [3] 생성된 Series 객체의 인덱스를 사명, 창립년도, 위치, 대기업여부로
##     변경해주세요.
series_data.index = ['사명', '창립년도', '위치', '대기업여부']
print(f"[5] 인덱스명 변경하기: {series_data}\n")

## [4] 생성된 Series 객체에서 1995 데이터만 추출해서 출력하세요.
print(f"[6] 1995 데이터 뽑기: {series_data['창립년도']}\n")

## [5] 생성된 Series 객체에서 사명, 창립년도, 위치를 출력하세요.
## [5-1] 리스트 방식
print(f"[7] 리스트 방식:\n{series_data[['사명', '창립년도', '위치']]}\n")

## [5-2] 슬라이싱 방식
print(f"[8] 슬라이싱 방식:\n{series_data['사명': '위치']}\n")