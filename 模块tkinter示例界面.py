# coding:utf-8
import tkinter

# 初始化对象
root = tkinter.Tk()
# Label组件
label = tkinter.Label(root, text='hello, python')
label.pack()
# Button组件
button1 = tkinter.Button(root, text='button1')
button1.pack(side=tkinter.LEFT)

button2 = tkinter.Button(root, text='button2')
button2.pack(side=tkinter.RIGHT)

root.mainloop()
