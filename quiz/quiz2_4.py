'''
4.
다중상속을 이용하여 카드사의 클래스를 만들고
영화카드는 20% 할인
마트카드는 10% 할인
교통은 10%할인을 받는 카드 class를 구현하시오


테스트코드
<입력>
multi_card=Multi_card()
multi_card.charge(20000)
multi_card.consume(5000,'마트')
multi_card.consume(10000,'영화관')
multi_card.consume(2000,'교통')
multi_card.print()

<출력>
카드가 발급 되었습니다.
20000이 충전되었습니다.
마트에서 4500.0원을 사용했습니다.
영화관에서 8000.0원을 사용했습니다.
교통에서 1800.0원을 사용했습니다.
잔액이 5700.0원 입니다
'''


class Card :
    tot = 0
    print(f'카드가 발급되었습니다.')

    def charge(self, money):
        self.tot += money
        print(f'{money}원이 충전되었습니다.')

    def print(self):
        print(f'잔액이 {self.tot}원 입니다.')


class Multi_card(Card) :

     def consume(self, money, place):
        
        self.place = place

        if self.place == '마트':
            self.money = money*0.9
        elif self.place == '영화관':
            self.money = money*0.8
        elif self.place == '교통':
            self.money = money*0.9
        else :
            self.money = money

        self.tot -= self.money
        print(f'{self.place}에서 {self.money}원을 사용했습니다.')
   

multi_card=Multi_card()
multi_card.charge(20000)
multi_card.consume(5000,'마트')
multi_card.consume(10000,'영화관')
multi_card.consume(2000,'교통')
multi_card.print()