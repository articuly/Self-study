import os
import time

start = time.time()
with open('2020_plan.txt', 'r', encoding='utf-8') as read_f, open('2020_plan.txt.swap', 'w',
                                                                  encoding='utf-8') as write_f:
    for line in read_f:
        line = line.replace('2020', 'XXXX')
        write_f.write(line)
os.remove('2020_plan.txt')
os.rename('2020_plan.txt.swap', '2020_plan.txt')
print(f'cost time {(time.time() - start):2f} s')

start2 = time.time()
with open('2020_plan.txt', 'r', encoding='utf-8') as read_f, open('2020_plan.txt.swap', 'w',
                                                                  encoding='utf-8') as write_f:
    data = read_f.read()
    data = data.replace('XXXX', '2020')
    write_f.write(data)
os.remove('2020_plan.txt')
os.rename('2020_plan.txt.swap', '2020_plan.txt')
print(f'cost time {(time.time() - start2):2f} s')
