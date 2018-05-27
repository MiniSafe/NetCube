# coding:utf-8
from __future__ import unicode_literals
from __future__ import print_function
from NetCube.module.debug_log import debug_log
from NetCube.module.encode import decoder



def tcp(packet, request_info, data):
    datas = data.get('load')
    if datas:
        if datas.startswith(b"GET "):
            try:
                r_line, tmp = datas.split(b"\r\n", 1)
                r_header = dict(map(lambda x: x.split(b": ", 1), tmp.split(b"\r\n\r\n")[0].split(b"\r\n")))
                debug_log(packet['src'], packet['dst'], "HTTP", "协议版本:%s" % decoder(r_line.split(b" ")[-1].split(b"/", 1)[1]),
                          "请求网站:GET http://%s:%s/%s" % (
                              r_header.get("Host"), request_info['dport'], decoder(r_line.split(b" ")[1].lstrip(b"/"))))
            except Exception, e:
                pass
        if datas.startswith(b"POST "):
            try:
                r_line, tmp = datas.split(b"\r\n", 1)
                try:
                    r_header = dict(map(lambda x: x.split(b": ", 1), tmp.split(b"\r\n\r\n")[0].split(b"\r\n")))
                except:
                    r_header = dict(map(lambda x: x.split(b": ", 1), tmp.split(b"\r\n")))
                debug_log(packet['src'], packet['dst'], "HTTP", "协议版本:%s" % decoder(r_line.split(b" ")[-1].split(b"/", 1)[1]),
                          "请求网站:POST http://%s:%s/%s  数据：%s" % (
                              decoder(r_header.get("Host")), request_info['dport'], decoder(r_line.split(b" ")[1].lstrip(b"/")),
                              decoder(repr(tmp.split(b"\r\n\r\n")[1]))))
            except Exception,e:
                pass


def udp(p1, p2, p3):
    pass


def other(p1, p2, p3):
    pass
