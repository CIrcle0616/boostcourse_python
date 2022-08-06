while True:
    a, b = input('주민등록번호를 입력해주세요: ').split('-')
    def check_id(a1, b1):
        birth, iden = a1, b1
        print(birth,iden)
        month = list(range(1,13))
        print(month)
        day = list(range(1,32))
        id_ok = list(map(str,range(1,5)))
        if int(birth[2:4]) not in month:
            print('잘못된 입력입니다. 월을 확인해주세요')
            return 
        if int(birth[4:]) not in day:
            print('잘못된 입력입니다. 일을 확인해주세요')
            return
        if iden[0] not in id_ok:
            print('잘못된 입력입니다 성별을 확인해주세요')
            return
        if (int(birth[:2]) < 23) and (iden[0] == '3' or iden[0] == '4'):
            after_2000 = int(input('2000년대 이후 출생이신가요? 맞으면 1 아니면 0을 입력해주세요'))
            if after_2000 and iden == '3':
                vla_id = '20'+birth[:2] + ' ' + birth[2:4] + '월' + birth[4:] + '일' + ' 남자입니다'
            if after_2000 and iden == '4':
                vla_id = '20'+birth[:2] + ' ' + birth[2:4] + '월' + birth[4:] + '일' + ' 여자입니다'
            return vla_id
        if iden[0] == '1':
            vla_id = '19'+birth[:2] + ' ' + birth[2:4] + '월' + birth[4:] + '일' + ' 남자입니다'
        if iden[0] == '2':
            vla_id = '19'+birth[:2] + ' ' + birth[2:4] + '월' + birth[4:] + '일' + ' 여자입니다'
        return vla_id
    print(check_id(a, b))
