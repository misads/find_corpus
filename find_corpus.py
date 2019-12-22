#####################################
# 把root_dir 设置到文本目录下(txt格式)
# Usage:
#     >>> as ? in fig           # 任意1个单词
#     >>> code * publicly       # 任意数量个单词(0-n)
#     >>> (show|demonstrate|achieve) ? results   # 多个单词选择
#     >>> show[ns]? ? results   # 不确定的时态(第一个?表示不确定有或没有 第二个?表示任意一个单词)
#     >>> ### ? feature fusion  # 显示上下文
#####################################

import os
import os.path as osp
import pdb
import re

from utils import get_file_paths_by_pattern, p
from utils import color_print
from utils import progress_bar
root_dir = '.'
min_times = 1
max_length = 50
max_display = 30


all_files = []
all_files.extend(get_file_paths_by_pattern(root_dir, '*.txt'))
all_files.extend(get_file_paths_by_pattern(root_dir, '*/*.txt'))

print('\033[1;37m', end='')
pattern = input('pattern:\n  ')
print('\033[0m', end='')
pattern = pattern.replace(' ? ', ' \w+ ').replace('*', '(.*)')

show_context = False
if pattern.startswith('### '):
    pattern = pattern[4:]
    show_context = True
    max_display = min(20, max_display)

if pattern.startswith('?'):
    pattern = '\w+' + pattern[1:]
if pattern.endswith('?'):
    pattern = pattern[:-1] + '\w+'



context = {}
results = {}
num_results = 0
for i, file in enumerate(all_files):
    progress_bar(i, len(all_files), pre_msg='Processing...', msg='%d results' % num_results)
    with open(file, 'r') as f:
        text = f.read()
        f = re.finditer(pattern, text, flags=re.IGNORECASE)
        for i in f:
            result = i.group().lower()
            if len(result) > max_length:
                continue
            if result not in results:
                results[result] = 1
                if show_context:
                    m1, m2 = i.span()[0], i.span()[1]
                    context[result] = [text[m1-70: m2+70] + '... ('+text[:50]]
                num_results += 1
            else:
                results[result] += 1
                if show_context:
                    m1, m2 = i.span()[0], i.span()[1]
                    context[result].append(text[m1-70: m2+70] + '... ('+ text[:50])
            # print(i.span())


def print_with_color(sentence: str):
    print('  ', end='')
    s = sentence.split()
    for i in s:
        if i in pattern:
            print('\033[1;32m', end='')
            print(i, end='')
            print('\033[0m', end='')
        else:
            print('\033[4;33m', end='')
            print('\033[1;33m', end='')

            print(i, end='')
            print('\033[0m', end='')
        print(' ', end='')


color_print('Find %d Matching Results in %d Files:' % (len(results.keys()), len(all_files)), 7, end='\n')
results = sorted(results.items(), key=lambda kv:(kv[1], kv[0]), reverse=True)

a = 0
with open('result.txt', 'w') as f:
    for i in results:
        if i[1] >= min_times and a < max_display:
            print_with_color(i[0])
            print('(%d times)' % i[1])
            a += 1
            if show_context:
                for j in context[i[0]]:
                    print('    ...', end='')
                    print(j.replace('\n', '+').replace(i[0], '\033[4;33m%s\033[0m' % i[0])+'...')
        else:
            line = '%s (%d times)' % (i[0], i[1])
            f.writelines(line+'\n')


