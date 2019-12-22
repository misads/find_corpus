import glob
import os
import sys
import time


def p(v):
    """
        Recursively print list, tuple or dict items
        :param v:
        :return:
    """
    if type(v) == list or type(v) == tuple:
        for i in v:
            print(i)
    elif type(v) == dict:
        for k in v:
            print('%s: %s' % (k, v[k]))
    else:
        print(v)

def color_print(text='', color=0, end=''):
    """
        Example:
            color_print('yellow', 3)

        :param text:
        :param color:
            0       black
            1       red
            2       green
            3       yellow
            4       blue
            5       cyan (like light red)
            6       magenta (like light blue)
            7       white

        :return:
    """
    print('\033[1;3%dm' % color, end='')
    print(text, end='')
    print('\033[0m', end=end)


def get_file_paths_by_pattern(folder, pattern='*'):
    """
        Examples: get all *.png files in folder
            get_file_paths_by_pattern(folder, '*.png')
        get all files with '_rotate' in name
            get_file_paths_by_pattern(folder, '*rotate*')

        :param folder:
        :param pattern:
        :return: a list of matching paths
    """
    paths = glob.glob(os.path.join(folder, pattern))
    return paths


def format_time(seconds):
    """
        Examples:
            format_time(10) -> 10s
            format_time(100) -> 1m
            format_time(10000) -> 2h 47m
            format_time(1000000) -> 11d 13h 47m
        :param seconds:
        :return:
    """
    eta_d = seconds // 86400
    eta_h = (seconds % 86400) // 3600
    eta_m = (seconds % 3600) // 60
    eta_s = seconds % 60
    if eta_d:
        eta = '%dd %dh %dm' % (eta_d, eta_h, eta_m)
    elif eta_h:
        eta = '%dh %dm' % (eta_h, eta_m)
    elif eta_m:
        eta = '%dm' % eta_m
    else:
        eta = '%ds' % eta_s
    return eta


try:
    _, term_width = os.popen('stty size', 'r').read().split()
    term_width = int(term_width)
except:
    term_width = 80


TOTAL_BAR_LENGTH = 30
last_time = time.time()
begin_time = last_time


def progress_bar(current, total, pre_msg=None, msg=None):
    """
        Training...  Step: [=======>... 26/100 ...........] ETA: 0s | loss:0.45

        Example:
            for i in range(100):
                progress_bar(i, 100, 'Training...', 'loss:0.45')

        :param current: from 0 to total-1
        :param total:
        :param pre_msg: msg **before** progress bar
        :param msg: msg **after** progress bar
        :return:
    """
    global last_time, begin_time
    if current == 0:
        begin_time = time.time()  # Reset for new bar.

    cur_len = int(TOTAL_BAR_LENGTH*current/total)
    rest_len = int(TOTAL_BAR_LENGTH - cur_len) - 1

    if pre_msg is None:
        pre_msg = ''
    sys.stdout.write(pre_msg + ' Step:')

    sys.stdout.write(' [')
    for i in range(cur_len):
        sys.stdout.write('=')
    sys.stdout.write('>')
    for i in range(rest_len):
        sys.stdout.write('.')
    sys.stdout.write(']')

    cur_time = time.time()
    step_time = cur_time - last_time
    last_time = cur_time
    tot_time = cur_time - begin_time
    eta_time = int((total - current) * step_time)
    eta = format_time(eta_time)

    L = []
    L.append(' ETA: %s' % eta)
    if msg:
        L.append(' | ' + msg)

    msg = ''.join(L)
    sys.stdout.write(msg)
    for i in range(3):
        sys.stdout.write(' ')
    # for i in range(term_width-int(TOTAL_BAR_LENGTH)-len(msg)-3):
    #     sys.stdout.write(' ')

    # Go back to the center of the bar.
    # for i in range(term_width-int(TOTAL_BAR_LENGTH/2)+2):
    #     sys.stdout.write('\b')
    # sys.stdout.write(' %d/%d ' % (current+1, total))
    for i in range(len(msg) + int(TOTAL_BAR_LENGTH/2)+8):
        sys.stdout.write('\b')
    sys.stdout.write(' %d/%d ' % (current+1, total))

    if current < total-1:
        sys.stdout.write('\r')
    else:
        sys.stdout.write('\n')
    sys.stdout.flush()
