#mission1.py
def make_comma(n):
    n = str(n)
    put_comma = len(n) // 3
    if put_comma % 3 == 0:        #자릿수를 계산하여 놓아야 하는 ,의 개수를 정한다.
        put_comma = put_comma - 1 #3으로 나눠 떨어질 경우 맨앞엔 ,를 두지 않기에 콤마의 수를 하나 줄인다.
    cnt_comma = 0                 #놓은 ,의 수를 카운트 하는 변수
    while cnt_comma != put_comma:
        if cnt_comma == 0:        #인덱스[-3:]과 [-3:0]은 다른 값이기 때문에 따로 해결
            new_n = ',' + n[-3:]
            cnt_comma = 1
            continue
        new_n = ',' + n[-3*(cnt_comma+1):-3*cnt_comma] + new_n  #뒤에서 부터 3숫자씩 ,를 삽입하고 이어 붙이는 코드
        cnt_comma += 1
    new_n = n[-3*(cnt_comma+1):-3*cnt_comma] + new_n            #뒤에서 부터 ,를 넣고 나면 앞의 집합이 하나 남는데 그것을 붙여주는 코드
    return new_n
print(make_comma(1000000))
        
