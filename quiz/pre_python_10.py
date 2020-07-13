"""10. 팩토리얼을 구하는 함수를 작성하시오.
ex ) 5! = 5x4x3x2x1
  print(factoral(5)) -> 120 출력
  
예시
<입력>
print(factorial(5))

<출력>
120
  """

def factorial(num):
      if num == 0 or num == 1 :
            return 1
      elif num <0:
            print("factorial은 음수 입력이 불가능합니다")
      else:
            return num * factorial(num-1)


print(factorial(5))