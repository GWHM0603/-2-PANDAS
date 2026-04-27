# Series / DataFrame에서 자주 사용되는 함수 만들기

# 함수 이름: print_info()
# 매개변수: obj - Series/DataFrmae 인스턴스
#           obj_name - 인스턴스 이름
# 결과 처리: 반환 안함
# 함수 기능: Series/DataFrame 인스턴스 속성 출력 기능


def print_info(obj, obj_name):
    # Series 인스턴스 정보 확인 -> data, index, dtype 지정한 것
    # Series 인스턴스/객체 변수명.속셩명
    print(f"\nSeries 속성들")
    print(f"index -> {obj.index}") # 원소 식별 번호
    print(f"values ->{obj.values}") # 원소에 저장된 데이터들
    print(f"shape -> {obj.shape}") # 1줄 시리즈의 형태. 튜프로 보기
    print(f"nidm -> {obj.ndim}") # 차원(1, 2, 3, ..., n) 정보
    print(f"dtype => {obj.dtype}") # 원소의 데이터 타입 정보
    print(f"name => {obj.name}") # 메타 정보/부가 정보로 이름 


    # Series 형태 출력
    print(f"\nSeries 형태 출력")
    print(obj,'\n')