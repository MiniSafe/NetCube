# coding:utf-8
from __future__ import unicode_literals
from __future__ import print_function


def debug_log(src, dst, type, *text):
    print("请求流量 : %s > %s 类型:%s\t%s" % (
        src + (15 - len(src)) * " ", dst + (15 - len(dst)) * " ",type + (6 - len(type)) * " ", " ".join(text)))
