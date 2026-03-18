#step03_Example.py

'''
    회원 한명의 정보는 번호, 이름 ,주소 로 이루어 있다.
    그리고 그러한 회원이 여러명이다.
    여러명의 회원 목록을 하나의 묶음으로(하나의 data) 로 순서대로 관리하고 싶다면...
'''

#3명의 회원정보를 각각 dict 에 담은 다음 그 dict 를 list 에 담는 코드를 작성해보세요

num1 = {"tel":"010-0000-0000", "name":"한윤성", "addr":"수원"}
num2 = {"tel":"010-0000-0000", "name":"김수겸", "addr":"수원"}
num3 = {"tel":"010-0000-0000", "name":"정성준", "addr":"수원"}

#dict 3 개를 list 에 담기
members = [num1, num2, num3]

#list type
a = members
#dict type
b = members[0]
#int type
c = members[0]["tel"]
d = members[0]["name"]


print("마무리~")
