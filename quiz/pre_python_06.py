"""6. 아래와 같이 별이 찍히게 출력하시오.
숫자를 입력하세요 : 5
    ★
   ★★
  ★★★
 ★★★★
★★★★★
 ★★★★
  ★★★
   ★★
    ★

예시
<입력>
숫자를 입력하세요 : 5

<출력>
    ★
   ★★
  ★★★
 ★★★★
★★★★★  
 ★★★★
  ★★★
   ★★
    ★


"""

num = int(input("숫자를 입력하세요 :"))
star = "★"
blank = " "

for i in range(1,num*2):
    if i <= num :
        # print(" "*(num-i), star*i)
        # print(f'{blank*(num-i)}{star*i}')
        print("{:s}{:s}".format(blank*(num-i),star*i))
    elif i > num :
        print("{:s}{:s}".format(blank*(i-num),star*(num*2-i)))
