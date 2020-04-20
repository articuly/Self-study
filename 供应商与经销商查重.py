# coding:utf-8
import time
import tkinter as tk
from tkinter import filedialog


def getrate(str1, str2):
    str1 = list(set(str1))
    str2 = list(set(str2))
    intersection = [value for value in str1 if value in str2]
    total_len = len(str1) + len(str2)
    rate = len(intersection) * 2 / total_len
    return rate


if __name__ == '__main__':
    start = time.time()
    # 读取经销商列表
    agency_name = 'agencytest.txt'
    root = tk.Tk()
    root.withdraw()  # 避免TK打开出现问题
    agency_name = filedialog.askopenfilename(title='请选择经销商列表')
    agency = open(agency_name, 'r', encoding='utf-8')
    agency_list = []
    for name in agency.readlines():
        agency_list.append(name.strip())

    # 读取供应商列表
    vendor_name = 'vendortest.txt'
    vendor_name = filedialog.askopenfilename(title='请选择供应商列表')
    vendor = open(vendor_name, 'r', encoding='utf-8')
    vendor_list = []
    for name in vendor.readlines():
        vendor_list.append(name.strip())

    # 输出表头
    output = open('testing_result.txt', 'w', encoding='utf-8')
    line = ['供应商', '经销商', '相似度']
    output.write('\t'.join(line))
    output.write('\n')

    # 循环计算两者相似度
    count = 1
    for i in agency_list:
        for j in vendor_list:
            count += 1
            if count % 1000 == 0:  # 每1000次打印一次
                print(count)
            rate = 0.00
            rate = getrate(i, j)
            # import Levenshtein
            # rate=Levenshtein.ratio(i, j)
            if rate > 0.8:
                line = [i, j, str(rate)]
                output.write('\t'.join(line))
                output.write('\n')
    output.close()
    agency.close()
    vendor.close()

    end = time.time()
    print('finished in %.3f s' % (end - start))
    print('\n★★★ Mapping Completed ★★★\n')
    print('Enter to exit 按任意键退出')
    input()
