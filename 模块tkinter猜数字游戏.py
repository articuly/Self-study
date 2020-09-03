# coding:utf-8
import tkinter as tk
import random

number = random.randint(0, 1024)
running = True
num = 0
nmaxn = 1024
nminn = 0


def eBtnClose(event):
    root.destroy()


def eBtnGuess(event):
    global nmaxn
    global nminn
    global num
    global running
    if running:
        val_a = int(entry_a.get())
        if val_a == number:
            labelqval('恭喜你答对了！')
        elif val_a < number:
            if val_a > nminn:
                nminn = val_a
                num += 1
                print(num)
                labelqval('小了哦，请输入{}到{}之间做任意整数'.format(nminn, nmaxn))
        else:
            if val_a < nmaxn:
                nmaxn = val_a
                num += 1
                print(num)
                labelqval('大了哦，请输入{}到{}之间任意整数'.format(nminn, nmaxn))
    else:
        labelqval('你已经答对啦！')


def numGuess():
    if num == 1:
        labelqval('一次答对！！！')
    elif num < 10:
        labelqval('十次内答对，真棒。尝试次数{}'.format(num))
    else:
        labelqval('好吧，你都试了超过10次了。尝试次数{}'.format(num))


def labelqval(vText):
    label_q_val.config(label_q_val, text=vText)


root = tk.Tk(className='猜数字游戏')
root.geometry('400x90+200+200')

label_q_val = tk.Label(root, width='80')
label_q_val.pack(side='top')
labelqval('请输入0到1024之间任意整数：')

entry_a = tk.Entry(root, width='40')
entry_a.pack(side='left')
entry_a.bind('<Return>', eBtnGuess)

btnGuess = tk.Button(root, text='猜测')
btnGuess.pack(side='left')
btnGuess.bind('<Button-1>', eBtnGuess)

btnClose = tk.Button(root, text='关闭')
btnClose.pack(side='left')
btnClose.bind('<Button-1>', eBtnClose)

entry_a.focus_set()
print(number)
root.mainloop()
