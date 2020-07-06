""""2.if문을 이용해 첫번째와 두번 수, 연산기호를 입력하게 하여 계산값이 나오는 계산기를 만드시오


예시
<입력>
첫 번째 수를 입력하세요 : 10
두 번째 수를 입력하세요 : 15
어떤 연산을 하실 건가요? : *

<출력>
150
"""


num = [int(input("첫 번째 수를 입력하세요 : ")), int(input("두 번째 수를 입력하세요 : ")), input("어떤 연산을 하실 건가요? : ")]
cal = ['+','-','*','/','%','//']

if num[2] in cal :
    if num[2] == cal[0] :
        print("%d + %d = %d" %(num[0],num[1],num[0]+num[1]))
    elif num[2] == cal[1] :
        print("%d - %d = %d" %(num[0],num[1],num[0]-num[1]))
    elif num[2] == cal[2] :
        print("%d * %d = %d" %(num[0],num[1],num[0]*num[1]))
    elif num[2] == cal[3] :
        print("%d / %d = %.4f" %(num[0],num[1],num[0]/num[1]))
    elif num[2] == cal[4] :
        print("%d % %d = %d" %(num[0],num[1],num[0]%num[1]))
    elif num[2] == cal[5] :
        print("%d // %d = %d" %(num[0],num[1],num[0]//num[1]))
else :
    print("error")


