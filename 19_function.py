# 함수선언(define)
# 반환타입 : O 매개변수 : O
def toaster(bread): # 선언 : 만들어만놨지 누가 사용한건 아님
   print(f'{bread} 이 구워지고 있다.') # 실질적 동작이 아님, 사람눈에만 보이는거
   return f'구워진 {bread}' # 실제로 밖으로 나오는 값

# 함수 사용
# dish = toaster('식빵') # return으로 나온 값을 dish에 담는다.
# print(dish) # dish 안의 값을 출력
print(toaster('식빵')) # 토스트기에서 나온 값을 바로 출력