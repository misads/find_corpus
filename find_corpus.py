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
import sys
import readline

from utils import get_file_paths_by_pattern, p, get_file_name
from utils import color_print
from utils import progress_bar
root_dir = 'txt'
min_times = 1
max_length = 50
max_display = 30


description="""
Usage:
  >>> as ? in fig             ? 匹配任意一个单词
  >>> code * publicly         * 匹配 1~n 个单词
  >>> (show|provide) results  (A|B|C) 匹配多个单词中的一个
  >>> show[ns]? ? results     正则表达式匹配
  >>> comparison is ?ed       匹配以ed结尾的单词
  >>> ### ? feature fusion    在开头加上 ### 可以显示上下文的语境
  >>> show all                显示上一次搜索所有的结果
  >>> exit                    退出
    """
print(description)

if len(sys.argv) > 1 and (sys.argv[1] == '--help' or sys.argv[1] == '-h'):
    exit()


all_files = []
all_files.extend(get_file_paths_by_pattern(root_dir, '*.txt'))
all_files.extend(get_file_paths_by_pattern(root_dir, '*/*.txt'))


print('\033[1;37mpattern:\033[0m')

while True:
        
    try:
        print('\033[1;37m', end='')
        pattern = input('  >>> ')
        print('\033[0m', end='')
        pattern = pattern.replace(']?', ']$').replace('*', '(.*)').replace('?', '\w+').replace(']$', ']?')

    except KeyboardInterrupt:
        print()
        continue

    show_context = False
    ends_string = ['exit', 'end', 'quit', 'q']
    help_string = ['help', 'h', '\w+']

    if pattern in ends_string:
        exit()

    if pattern in help_string:
        print(description)
        continue

    if pattern == 'show all':
        with open('result.txt', 'r') as f:
            lines = f.readlines()

        print('\033[1;33m', end='')
        for line in lines:
            line = line.rstrip('\n')
            print('  ' + line)

        print('\033[0m', end='')
        continue
    
    if pattern.startswith('### '):
        pattern = pattern[4:]
        show_context = True
        max_display = min(20, max_display)

    context = {}
    results = {}
    num_results = 0
    for i, file in enumerate(all_files):
        try:
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
                            context[result] = [text[m1-70: m2+70] + '... (' + get_file_name(file) + ')']
                        num_results += 1
                    else:
                        results[result] += 1
                        if show_context:
                            m1, m2 = i.span()[0], i.span()[1]
                            context[result].append(text[m1-70: m2+70] + '... (' + get_file_name(file) + ')')
                    # print(i.span())
        except KeyboardInterrupt:
            break
        


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
                        j = j.replace('\n', '+')
                        j = re.sub('(?i)' + i[0], '\033[4;33m%s\033[0m' % i[0], j)
                        print(j)
            else:
                line = '%s (%d times)' % (i[0], i[1])
                f.writelines(line+'\n')

    print()
    print('\033[1;37mpattern:\033[0m')

