from random import randint


def main():
    while True:
        num = randint(1, 1000)
        count = 0
        while True:
            try:
                guess = input("请输入你猜的数字（1-1000）：")
                guess = int(guess)
                count += 1
                if guess < num:
                    print(f"{guess}小了")
                elif guess > num:
                    print(f"{guess}大了")
                else:
                    print(f"{guess}:恭喜你，猜对了！共{count}次!")
                    if input('------\n新的游戏?(y/n)') == 'y':
                        break
                    else:
                        exit()
            except ValueError:
                print(f"{guess}:请输入一个有效的数字！")


if __name__ == '__main__':
    main()
