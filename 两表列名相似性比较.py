# coding:utf-8
import Levenshtein

# read file
local = '博客文章箱.txt'
remote = '博客网站.txt'
with open(local, 'r', encoding='utf-8') as lc:
    local_list = lc.readlines()
with open(remote, 'r', encoding='utf-8') as rm:
    remote_list = rm.readlines()
local_list = [i.lower().strip() for i in local_list]
remote_list = [i.lower().strip() for i in remote_list]

sim_dict = {}
print('cols in local list')
for l in local_list:
    for r in remote_list:
        sim = Levenshtein.ratio(l, r)
        sim_dict[r] = sim
    max_sim = max(sim_dict.values())
    max_col = [key for key, value in sim_dict.items() if value == max_sim]
    with open('local2rm_result.txt', 'a', encoding='utf-8') as f:
        f.write(l + '\t' + max_col[0] + '\t' + str(max_sim) + '\n')
    # print(l, max_col[0], max_sim)

sim_dict = {}
print('cols in remote list')
for r in remote_list:
    for l in local_list:
        sim = Levenshtein.ratio(l, r)
        sim_dict[l] = sim
    max_sim = max(sim_dict.values())
    max_col = [key for key, value in sim_dict.items() if value == max_sim]
    with open('remote2lc_result.txt', 'a', encoding='utf-8') as f:
        f.write(r + '\t' + max_col[0] + '\t' + str(max_sim) + '\n')
    # print(r, max_col[0], max_sim)
