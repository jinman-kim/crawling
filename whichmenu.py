def which_menu_gogo():
    import random
    nation = ['한식','일식','중식','양식']
    food_dict = {'한식':['뚝배기','더진국',
                      '미미 식당(오삼불고기)','작은집',
                      '할매 순대국','한라산 감자탕(뼈해장국)',
                      '왕 순대국','학교 종이 땡땡땡(순두부)',
                      '월계 숯불 갈비(갈비백반)','마포연탄불고기(연탄불백)',
                      '김가네','김밥천국',
                      '마루','경대컵밥','밥은','한솥',
                      '한끼 철판','수육 국밥','명태 이야기'],
                 '일식':['푸른 스시','지지고?',
                       '윤스쿡(카츠)','33카츠(3300원 아님)'],
                 '중식':['미식성','친친(역앞)','더원(베라옆, 맛닭꼬2층)'],
                 '양식':['오네스토 테이블(노맛)','브릿지오(누리관 가는길,존맛)',
                       '맘스터치 치킨피자','서브웨이',
                       '파파존스','맛닭꼬',
                       '썬더치킨']}

    nation_rand = random.choice(nation)
    fixed_menu = random.choice(food_dict[nation_rand])
    import time
    start = time.time()
    while True:
        print('     두구')
        print('  두구     ')
        print('두구')
        print('  두구     ')
        print('     두구')
        if time.time()-start > 3:
            break
    return '오늘 랜덤식사는 {} :{} 입니다~!'.format(nation_rand,fixed_menu)


print(which_menu_gogo())
