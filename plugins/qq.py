# coding:utf-8
from __future__ import unicode_literals
from __future__ import print_function
from NetCube.module.debug_log import debug_log
import re

def tcp(packet, request_info, data):
    datas = data.get('load')
    if datas:
        if datas.startswith("000003340000000c0200000004000000000e".decode("hex")):
            try:
                r = re.search("000003340000000c0200000004000000000e".decode("hex")+"(\d+)",datas)
                debug_log(packet['src'],packet['dst'],"QQ","QQ号码:%s" % r.group(1))
            except:
                pass


def udp(p1, p2, p3):
    pass


def other(p1, p2, p3):
    pass
