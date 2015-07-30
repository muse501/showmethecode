# 统计代码行数，空行数，注释行数
from q0005 import find_suffix

import os

from collections import Counter


def count_lines(*data):
    cl = {}
    for fn in data:
        c = Counter()
        file_name = os.path.splitext(os.path.basename(fn))[0]
        with open(fn) as fp:
            for i in fp.readlines():
                if i.startswith('#'):
                    c['comment'] += 1
                if not i.strip():
                    c['blank'] += 1
                c['text'] += 1
        cl.update({file_name: c})
    return cl


if __name__ == '__main__':
    file_list = find_suffix('./q0007/', ['.py'])
    c = count_lines(*file_list)
