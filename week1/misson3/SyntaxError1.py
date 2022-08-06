age=int(input('나이가 어떻게 되십니까?'))
birth=int(input('생일이 지났습니까? 맞으면 0 아니면 -1:'))
if birth==0:
    age=age-1
if birth==-1:
    age=age-2
print('당신의 미국 나이는:%d 입니다.'%age)