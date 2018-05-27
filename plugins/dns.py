# coding:utf-8
from __future__ import unicode_literals
from __future__ import print_function
from NetCube.module.debug_log import debug_log


def tcp(packet, request_info, data):
    pass


def udp(packet, request_info, data):
    if request_info.get('dport') == 53:
        debug_log(packet['src'], packet['dst'], "DNS", "查询:%s" % data['qd'].qname)


def other(p1, p2, p3):
    pass


def icmp(packet, request_info, data):
    if data['load'].endswith(
            "08090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f202122232425262728292a2b2c2d2e2f3031323334353637".decode(
                    "hex")):
        debug_log(packet['src'], packet['dst'],"PING")
