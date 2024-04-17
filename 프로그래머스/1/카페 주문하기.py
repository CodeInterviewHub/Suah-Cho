# 음료 메뉴를 화면에 출력
print("---별다방 메뉴---")
print("1. 아메리카노 : 5500원")
print("2. 카페라떼 : 6000원")
print("3. 카푸치노 : 6500원")
print("0. 종료")

cost = 0

# 음료 메뉴를 입력받음
while True:
    name = input("당신의 이름:")
    while True:
        menu = int(input("메뉴 선택:"))
        if menu == 0:
            break
        count = int(input("수량 선택:"))

        # 메뉴 선택에 따라 가격을 계산
        if menu == 1:
            cost += 5500 * count
        elif menu == 2:
            cost += 6000 * count
        elif menu == 3:
            cost += 6500 * count
        else:
            print("잘못된 입력입니다.")
            continue

    print(f"{name}님의 결제 금액은 {cost}원입니다.")
    print(name + "님의 총 요금은 " + cost + "원 입니다.")

    next = input("다음 손님 있습니까? (y/n)")

    if next == 'n' or next == 'N':
        break
    elif next == 'y' or next == 'Y':
        continue
    else:
        print("잘못된 입력입니다.")
