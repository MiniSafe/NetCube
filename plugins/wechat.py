# coding:utf-8
from __future__ import unicode_literals
from __future__ import print_function
from NetCube.module.debug_log import debug_log
from NetCube.module.encode import decoder


def tcp(packet, request_info, data):
    datas = data.get('load')
    if datas:
        if datas.startswith(b"POST "):
            try:
                r_line, tmp = datas.split(b"\r\n", 1)
                r_header = dict(map(lambda x: x.split(b": ", 1), tmp.split(b"\r\n\r\n")[0].split(b"\r\n")))
                if r_header.get("Host") == "short.weixin.qq.com" and r_header.get("User-Agent") == "MicroMessenger Client":
                    debug_log(packet['src'], packet['dst'], "WeChat")
            except Exception,e:

                pass


def udp(p1, p2, p3):
    pass


def other(p1, p2, p3):
    pass
