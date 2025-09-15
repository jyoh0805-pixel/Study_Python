# 반환타입:O 매개변수:O 자판기
# 반환타입:O 매개변수:X 폴라로이드
# 반환타입:X 매개변수:O 모금함
# 반환타입:X 매개변수:X 리모컨

#자판기
def vending(drink):
    print(f'{drink}를 준비중입니다.')
    return f'주문한{drink}가 나왔다.'
hand = vending('콜라')
print(hand)

#폴라로이드
def film():
    print('출력중')
    return '사진이 나왔습니다.'
photo = film()
print(photo)

#모금함
def box(money):
    print(f'{money}원 넣으셨습니다.')
box('70,000')

# 리모컨
def remote():
    print('TV가 켜진다.')
remote()