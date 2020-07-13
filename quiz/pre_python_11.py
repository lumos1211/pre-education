"""11. 최대공약수를 구하는 함수를 구현하시오

예시
<입력>
print(gcd(12,6))

<출력>
6
"""

from math import gcd
print(gcd(12,6))



def list(num):
    list = []
    for i in range(1,num+1,1):
        if num%i==0:
            list.append(i)
    # print(list)
    return list

def gcd2( num1, num2 ) :
    list1 = list(num1)
    list2 = list(num2)    
    cd= set(list1)&set(list2)
    tu = tuple(cd)
    return tu[-1]


print(gcd2(12,6))


def gcd3(num1,num2):
    while num2 :
        num1 = num2
        num2 = num1 % num2
    return num1
    
print(gcd3(12,6))









