#!/usr/bin/env python
# coding: utf-8

# # 미션3
# ## SyntaxError

# In[1]:


num=20
while num>5;
    print(num)
    num=num-1


#  SyntaxError는 문법에 틀리게 작성했을때 발생하는 에러입니다. 이 코드에선 :(콜론)자리에 ;(세미콜론)을 잘못 작성하였습니다.
#  아래 코드는 위의 코드를 디버깅한 코드입니다. 정상 동작 하는 것을 확인할 수 있습니다.

# In[2]:


num=20
while num>5:
    print(num)
    num=num-1


# In[3]:


print('What's your name?')


# print함수는 str타입을 출력하기 위해서 ''을 사용합니다. 여기선 '이 중간에 하나 삽입되어 에러가 발생하였습니다.
# 아래 코드는 이를 디버깅한 코드입니다.
# 

# In[4]:


print('''What's your name?''')


# '''입력값''' 을 사용하여 안에 어떤 입력이 들어와도 무조건 출력하게 할 수 있습니다.

# ## ValueError
#  파이썬의 ValueError는 사용자가 함수에 잘못된 값을 제공하지만 유효한 인수일 때 발생합니다. 그것은 보통 값이 올바른 인수일 때에도 특정 종류의 값이 필요한 수학적 연산에서 발생한다. 파이썬에게 음수 정수의 제곱근을 취하라고 말하는 것을 상상해 보세요._https://www.educative.io/answers/what-is-valueerror-in-python

# In[1]:


name='컨택트'
int(name)


# int함수는 str타입의 숫자 데이터를 받아 int형으로 변환해주는 함수로 str형의 데이터가 인자로 들어오는 것은 옳다.  
# 그러나 str형의 숫자가 아닌 문자형 값이 저장되어 있기에 int함수가 올바른 값이 아니라며 ValueError가 발생하는 것이다.

# In[4]:


age=input('몇살이세요?')
print(type(age))
age=int(age)
print(type(age))


# 처음 입력받은 데이터가 str형으로 저장되는 것이 input함수의 특징이다. 이를 수학적 연산을 하기위해선 int, float함수로 변환을 해주어야 한다. 위의 코드를 확인하면 int함수를 통해 데이터 타입이 정상적으로 변환된것을 확인 할 수 있다.

# In[15]:


list1=['a','1','3']
print(list1.index('b'))


# list를 만들고 list.index('찾고자 하는 인자')메소드를 통해서 찾고자하는 인자의 index값을 알려고 할때 리스트에 존재하지 않는 'b'에 대해서 접근하려고 할 때 발생함     
# 아래 코드에선 정상적으로 작동헤 'b'의 index값이 3을 출력했다

# In[16]:


list1=['a','1','3','b']
print(list1.index('b'))


# ## TypeError
# 데이터의 Type이 잘못되어 생기는 에러이다.

# In[5]:


n1='hello'
n2='world'
print(n1*n2)


# TypeError: can't multiply sequence by non-int of type 'str'     
# 위의 에러메시지를 살펴보면 'str'타입의 데이터는 곱 연산을 할 수 없다고 한다. 이를 디버깅하면 +을 하거나 둘중 하나의 데이터는 int타입이어야 한다

# In[17]:


n1='hello'
n2='world'
print(n1*5,n2*5)


# In[19]:


n1='hello'
n2=5
print(n1+n2)


# str형 데이터와 int형 데이터는 서로 더할 수 없다     
# 아래와 같이 숫자 5를 str형으로 저장 하면 덧셈이 가능하다

# In[20]:


n1='hello'
n2='5'
print(n1+n2)


# ## 그외의 에러
# ### NameError
# 참조 변수가 없을 때 발생 즉 변수 지정을 해주지 않았을 때

# In[21]:


print(a)


# In[22]:


a='a'
print(a)


# ### ZeroDivsionError
# 0으로 나눴을 때 발생하는 에러

# In[23]:


1231/0


# In[24]:


1231/1


# ### IndexError
# 인덱스 범위를 초과했을 때 발생함.   
# 인덱스가 0,1,2,3 일때 4를 호출하면 발생함

# In[25]:


a=[1,2,3,4]
print(a[4])


# In[26]:


a=[1,2,3,4,5]#5를 추가해 index=4인 데이터를 추가함
print(a[4])

