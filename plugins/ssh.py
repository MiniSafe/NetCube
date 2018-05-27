# coding:utf-8
from __future__ import unicode_literals
from __future__ import print_function
from NetCube.module.debug_log import debug_log

import re


def tcp(packet, request_info, data):
    datas = data.get("load")
    if datas:
        if datas.startswith(b"SSH"):
            r = re.match(b"SSH-(\d\.\d)-OpenSSH_((?:\d\.)+\d)\r\n",datas)
            debug_log(packet['src'], packet['dst'],"SSH","协议版本:%s" % r.group(1))


def udp(p1, p2, p3):
    pass


def other(p1, p2, p3):
    pass
