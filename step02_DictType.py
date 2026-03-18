# dict type 에 대해서 알아보자



#회원 1명의 데이터
mem1 = {"num":1, "name":"hanyunsung", "isman":True}
#회원 1명의 데이터 (사용이 불편한다.)
#info1 =[1, "hanyunsung", True]
print(mem1["num"])
print(mem1["name"])
print(mem1["isman"])

#dict 안에 내용을 참조해서 변수에 담기
a = mem1["num"]
b = mem1["name"]
c = mem1["isman"]

#dict 안의 내용을 수정하기
mem1["num"]=2
mem1["name"]="한윤성"
mem1["isman"]=False

#특정 key 값으로 저장된 내용 삭제
del mem1["isman"]

#모든 값 삭제
mem1.clear()


print("종료됩니다")