# 重量单位转换器
print("请选择你需要转换的重量单位：\n1.千克转换成磅\n2.磅转换成千克")
c = input("你的选择：")
print(c)
if c == "1":
    def converter1():
        wt = float(input("请输入千克重量数值："))
        ponds = wt/0.45359237
        print(ponds)
    converter1()
elif c == "2":
    def converter2():
        wt = float(input("请输入磅重量数值："))
        kg = wt*0.45359237
        print(kg)
    converter2()
