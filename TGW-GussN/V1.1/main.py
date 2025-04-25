from random import randint
from tkinter import *


try:
    root = Tk()
    count = 0
    num = randint(1, 1000)
    # print(num)
    def game(guess, num):
        try:
            global count
            guess = int(guess)
            count += 1
            if guess < num:
                return [f"{guess}小了", 0]
            elif guess > num:
                return [f"{guess}大了", 0]
            else:
                return [f"{guess}:恭喜你，猜对了！共{count}次!", 1]
        except ValueError:
            return [f"{guess}:请输入一个有效的数字！", -1]

    def main():
        global root, num, count
        Label(root, text="请输入你猜的数字（1-1000）：").pack(fill=X)
        equ = StringVar()
        ent = Entry(root, textvariable=equ)
        ent.pack(fill=X)
        Button(root, text="提交", command=lambda: lb.insert(END, game(ent.get(), num)[0])).pack(fill=X)
        result = game(ent.get(), num)
        sc = Scrollbar(root)
        sc.pack(sid=RIGHT, fill=Y)
        lb = Listbox(root, yscrollcommand=sc.set)
        lb.pack(fill=BOTH, expand=True)
        sc.config(command=lb.yview)
        root.mainloop()
        if result[1] == 1:
            main()
        elif result[1] == -1:
            main()
        else:
            count += 1
            main()
        
        


    if __name__ == '__main__':
        main()

except:
    pass
