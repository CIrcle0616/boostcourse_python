guest_book = """김갑,123456789
이을,010-1234-5678
박병,010-5678-111
최정,111-1111-1111
정무,010-3333-3333"""

def find_wrong(a):
    f = open("/Users/owl/Desktop/week4/전화번호.txt", "w")
    for line in a:
        f.write(line)
    f.close()
    f = open("/Users/owl/Desktop/week4/전화번호.txt", "r")
    for line in f:
        line = line.rstrip()              #\n공백문자 제거 공백문자도 글자수로 카운트되기에 제거해야함
        name = line[:line.find(',')]      #이름부분 추출 ,를 기준으로 왼쪽은 이름
        phone = line[line.find(',')+1:]   #번호부분 추출 ,를 기준으로 오른쪽은 번호
        a = phone.startswith('010')       #조건식 구분하여 기술
        b = len(phone)!=13
        c = phone.count('-') != 2
        
        if not a or b or c:
            print('잘못 쓴 사람: ', name)
            print('잘못 쓴 번호: ', phone)
        
find_wrong(guest_book)