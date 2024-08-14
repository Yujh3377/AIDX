# 주어진 데이터프레임을 Value 열을 기준으로 내림차순으로 정렬하시오.

# pandas 불러옴 줄여서 pd
import pandas as pd

# 아무거나 데이터프레임 생성
data = {
    'Name': ['AAA', 'BCA', 'CBA', 'DABC','ADBC','ABDC','ABCD'],
    'Value': [10, 30, 20, 40, 76, 35, 67]
}
# df는 data 리스트의 판다스 데이터구조
# (1차원)은 Series로 (2차원)은 Data Frame이 사용
df = pd.DataFrame(data)

# Value 열을 기준으로 내림차순 정렬 
# ascending 매개변수를 False로 설정하면 내림차순
# sort_values함수(['기준열1','기준열2']ascending =True,False)
df_sorted = df.sort_values(['Value'], ascending=False)

# 결과 출력
print(df_sorted)