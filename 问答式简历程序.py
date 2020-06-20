# 输入个人信息
name = input('请输入您的姓名：')
gender = input('请输入您的性别：')
age = input('请输入您的年龄：')
school = input('请输入您的学校：')
major = input('请输入您的专业：')

# 输出简历内容
print('正在生成您的简历......\n')
print('*' * 30)
print('简历'.center(30))
print(f'''
姓名：{name}
性别：{gender}
年龄：{age}
学校:{school}
专业：{major}
''')
print('*' * 30)
