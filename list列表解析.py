print([i * 2 for i in range(10)])

el = []
ml = ["小明", "小兰", "小红", "王五", "李四", "张三", "王二"]
for name1 in ml:
    if name1.startswith("王"):
        el.append(name1)
        print(el)
for name2 in ml:
    if name2.startswith("小"):
        print(name2)
