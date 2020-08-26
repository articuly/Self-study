# coding:utf-8
import random

# 创建单词列表
WORD = ['python', 'jumble', 'easy', 'difficult', 'answer', 'continue', 'phone', 'position', 'pose', 'game', 'machine',
        'learn', 'strength', 'length', 'width', 'height']

print(
    """
    　　欢迎参加猜单词游戏
    把字母组合成一个正确的单词
    """
)
is_continue = 'y'
while is_continue == 'y' or is_continue == 'Y':
    # 从列表中随机捐出一个单词
    word = random.choice(WORD)
    # 保存正确的单词
    correct = word
    # 保存乱序的单词
    jumble = ''
    while word:
        # 根据单词长度选择随机位置
        position = random.randrange(len(word))
        # 组合随机位置的字母
        jumble += word[position]
        # 通过切片将随机位置的字母从原单词删除
        word = word[:position] + word[(position + 1):]
    print('乱序后单词：', jumble)

    guess = input('\n请你猜：')
    while guess != correct or guess == '':
        print('对不起，没猜对')
        guess = input('请继续猜：')
        if guess == correct:
            print('真棒，你猜对了')
    is_continue = input('\n是否继续（Y/N）:')
