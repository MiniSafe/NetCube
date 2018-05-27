# coding:utf-8
from __future__ import unicode_literals
from __future__ import print_function
from chardet import detect


def decoder(s):
    if (not isinstance(s, str)) and (not isinstance(s, unicode)):
        s = str(s)
    if isinstance(s, str):
        code = detect(s)['encoding']
        if code:
            s = s.decode(code)
        else:
            s = s.decode("utf-8", "ignore")
    if isinstance(s, unicode):
        return s
