import re

a = "111.1米大萨你好123x"


def place(zi, mu):
    """查询子字符串在大字符串中的所有位置"""
    len1 = len(zi)
    pl = []
    for each in range(len(mu) - len1):
        if mu[each:each + len1] == zi:  # 找出与子字符串首字符相同的字符位置
            pl.append(each)
    return pl


def is_en(a):
    for f in ["*", "x"]:
        index = place(f, a)
        for x in index:
            if x >= len(a):
                return False
            if a[x + 1].isdigit():
                return True
    return False


print(is_en(a))

