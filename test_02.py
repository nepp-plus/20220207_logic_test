import random

# 추가 문제 => 코인을 각각 20개씩 갖고 시작.
#  홀/짝에 몇개를 베팅할지 1~5 사이로 입력 제한.
#    => 내가 가진 코인 갯수보다 많이 베팅은 불가.
#  베팅한 갯수 만큼 코인이 이동하도록.

user_coin = 3
cpu_coin = 3

while True:
    
    # 컴퓨터가 1~6개 사이의 구슬을 세팅함.
    cpu_count = random.randint(1, 6)
    
    # 홀/ 짝인지 답을 입력.
    
    user_answer = input('홀 / 짝을 맞춰주세요 : ')
    
    if user_answer not in ['홀', '짝']:
        print("잘못된 입력입니다.")
        continue  # 반복문의 이번 바퀴만 skip
        
    # 제대로 입력햇다면 마저 진행.
    
    # CPU가 몇개를 집었는지 공개
    print(f'CPU는 {cpu_count}개의 구슬을 집었습니다.')
    
    if user_answer == '홀':
        if cpu_count % 2 == 1:
            
            print('사용자 승리입니다.')
            
            # 사용자 승리. => 코인 한개 CPU로부터 받아오자.
            user_coin += 1
            cpu_coin -= 1
        else:
            print('사용자 패배입니다.')
            user_coin -= 1
            cpu_coin += 1
    else:
        # 짝을 입력한 경우.
        if cpu_count % 2 == 0:
            
            print('사용자 승리입니다.')
            # 맞춘 경우.
            user_coin += 1
            cpu_coin -= 1
        else:
            
            print('사용자 패배입니다.')
            user_coin -= 1
            cpu_coin += 1
            
    # 둘중 하나의 코인이 다 떨어졌다면?  경기 종료
    
    if user_coin == 0:
        print('사용자의 코인이 바닥났습니다.')
        print('GAME OVER')
        break
    elif cpu_coin == 0:
        print('CPU의 코인이 바닥났습니다.')
        print('You win!')
        break