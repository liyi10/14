import random
times=0
computer = random.randint(1, 100)
while times<3:
    admin = int(input('猜年龄:'))
    if admin==computer:
        print('恭喜您猜对了')
        break
    elif admin>computer:
        print('您猜测的年龄大了')
    else:
        print('您猜测的年龄小了')
    times = times + 1
    if times==3:
        print('三次机会用完了，您是否继续?\n[N or n:否,Y or y:是]')
        again = input()
        if again == 'N' or again == 'n':
            times=4
            print('游戏结束')
        elif again == 'Y' or again == 'y':
            times=0
        else:
            print('不要乱输入')