import random   # import가 뭔지 ?


number = random.randint(1, 31)
print(f'내 마음속 숫자: {number}')


running = True # while을 쓰기위해 running을 True 선언.


while running: # while = True 일때만 가능. while= ~하는동안 위에 running은 True를 이미 선언했기때문에 while running: < 사용
    guess = int(input('1~31 중 내가 생각한 숫자는?')) # 입력받은 값을 정수(int)로 변환하여 guess에 대입
    print(f'입력받은숫자:{guess}')
    if number > guess:
        print('내가 생각한 숫자보다 작습니다.')
    elif number < guess:
        print('내가 생각한 숫자보다 큽니다.')
    else:
        print('정답입니다.')
        running = False # while은 True일때 계~속 돌기때문에, 선언했던 running을 False로 재선언해서 종료함.
    

