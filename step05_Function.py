#Step05_Functhion.py

'''
    functhion type

    -특정시점에 여러줄의 code 를 일괄 실행하고자 할때 사용한다,
    -함수도 data 이다. (변수에 담을 수 있다.)
    -함수 안에 저장 된 code 를 일괄 실행하는 것을 함수를 call 한다라고 이야기한다.
    -함수는 저장된 code 를 다 실행하고 나면 원래 call 했던 위치로 실행의 흐름이 넘어온다.
    -call 했던 위치로 돌아오면서 어떤 data 를 반드시 가져온다.
'''

def test1():
    print("test1() 호출됨")

test1()
result1 = test1()

#매개변수가 선언되어 있는 함수
#매개변수에 대입 할 값을 전달해야지 호출할수가 있다.
#매개변수의 이름은 마음대로 지을 수 있다.
def test2(arg):
    print("전달 받은 내용", arg)
    print(f"전달받은 내용: {arg} ")

test2(None)
test2(10)
test2("han")

#값(숫자)을 2개 전달 받은 두 수의 합을 출력하는 함수
def print_sum(num1: int, num2: int):
    sum = num1+num2
    print(f" {num1} + {num2} = {sum}")

print_sum(10,20)
print_sum(30,40)

def print_info(name: str, addr: str):
    print(f" 이름은 {name} 이고 주소는 {addr}")

print_info("한윤성", "수원")
#keyword 를 이용해서 인자(argument) 를 전달할수도 있다.
print_info(addr="우만동", name="윤성이")

def get_sum(num1: int, num2: int):
    sum=num1+num2
    return sum

result2 = get_sum(10,20)


print("마무리")