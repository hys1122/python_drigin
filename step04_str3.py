# yaml 형식의 문자열 다루기

#yaml 문자열을 다룰때는 외부 모듈을 pip 로 설치를 해서 import 를 해야한다.
import yaml

info = '''
name: 한윤성
addr: 수원
foods:
  - 피자
  - 초밥
isMan: true
body:
  weight: 70
  height: 180
'''

#오늘 과제 (검색 혹은 ai 의 도움을 받아서 info 에 들어있는 문자열을 dict type 으로 바꾸세요)
#(그다음 dict 에 들어 있는 내용을 확인 후 다시 dict 에 있는 내용을 이용해서 yaml 문자열 형식으로 변환해보세요)


#info 문자열을 dict로 변환
dict_obj = yaml.safe_load(info)


print(dict_obj)

print(type(dict_obj))

#dict에서 yaml로 변경
yaml_str = yaml.dump(dict_obj, allow_unicode=True)

print("\nYAML info:")

print(yaml_str)

print(type(yaml_str))