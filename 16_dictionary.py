# 사전은 키:값 형태로 되어있다.
# 비슷한 자료구조로는 자바스크립트에는 오브젝트, 자바의 맵이 있다.
dic1 = {'name':'Oh,jun-young',
        'phone':'010-1234-1234',
        'age' :55
}

dic2 = {
    'name':'Oh,jun-young',
    'phone':'010-1234-1234',
    'friends':['Alice','John','Smith']
}

# 사전에 데이터 넣기 1
a = {'first':'a'}
print(a)

# 사전에 데이터 넣기 2
a ['second'] = 'b'
print(a)

# 사전에서 특정 요소 삭제
del a['second']
print(a)

# 사전의 특정 요소를 꺼내보자(사용법은 List와 비슷하다.)
print(dic2['name'])
print(dic2['friends'])