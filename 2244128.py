coin = 0

while True:
    if coin == 0 or input("돈을 추가하시겠습니까? (y/n): ") == 'y':
        coin += int(input("돈을 넣으세요. -> "))

    while True:
        print(f'현재 금액 : {coin}')
        sell = int(input("1.오렌지주스 : 1500원\n2.아메리카노 : 1500원\n3.우유 : 1800원\n4.카페모카 : 2500원\n5.아이스티 : 2000원\n==> "))
        if sell < 1 or sell > 5:
            print("없는 메뉴")
            continue

        if sell == 1:
            price = 1500
        elif sell == 2:
            price = 1500
        elif sell == 3:
            price = 1800
        elif sell == 4:
            price = 2500
        elif sell == 5:
            price = 2000

        if coin < price:
            print("잔액부족")
            break
        else:
            coin -= price
            print(f"잔액 -> {coin}원")
            break


    print(f"현재 잔액: {coin}원")
    c = input("종료하려면 'q'를 입력하세요. 추가 구매나 금액 보충 하시려면 'c' 입력: ")
    if c == 'q':
        print(f"{coin}원이 반환되었습니다")
        break
    elif c == 'c':
        continue
