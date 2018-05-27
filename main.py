#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function
import os
print("[***] 正在导入依赖库")
from scapy.all import *

print("[***] 导入完成")
from module.load import load_module, work

modules = load_module()
pkts = []
count = 0
pcapnum = 0
filename = ''


def test_dump_file(dump_file):
    if os.path.exists(dump_file):
        print("[+++] 写入到文件:", dump_file)
        # pkts = sniff(offline=dump_file)
        # count = 0
        # while (count <= 2):
        #     print("[***] 数据包信息:", dump_file)
        #     print(hexdump(pkts[count], True))
        #     count += 1
        #     print("[---] 数据包结束")
    else:
        print("[!!!] 数据包写入失败:", dump_file)


def pack(site, pack_num):
    def write_cap(x):
        global pkts
        global count
        global pcapnum
        global filename
        pkts.append(x)
        # print("[***] 流量走向 ：%s (%s)\t>\t%s (%s)\t包长度 :%s" % (
        #     x.payload.fields.get("src", "无线包"), x.src, x.payload.fields.get("dst", "Broadcast"), x.dst,
        #     x.payload.fields.get("len", "0")))
        types = {"TCP": "tcp", "UDP": "udp", "ICMP": "icmp"}
        try:
            work(modules, types.get(x.payload.payload.__class__.__name__, "other"),
                 (x.payload.fields, x.payload.payload.fields, x.payload.payload.payload.fields))
        except:
            pass

        count += 1
        if count == pack_num:  # 每3个TCP操作封为一个包（为了检测正确性，使用时尽量增多）
            pcapnum += 1
            pname = "pcap%d.pcap" % pcapnum
            filename = os.path.join(site, pname)
            wrpcap(filename, pkts)  # 写入到文件中
            # test_dump_file(filename)
            pkts = []
            count = 0

    return write_cap


def sniffer(log_site, filter="", pack_num=3):
    print("[!!!] 正在清空历史包数据")
    count = 0
    for name in os.listdir(log_site):
        os.remove(os.path.join(log_site, name))
        count += 1
    print("[***] 已清空 %s 个日志包" % count)
    print("[+++] 开始对流量包进行捕获")
    print("[***] 正在分析流量中")
    print("[***] 包日志目录:%s 当前设置每 %s 个请求存储为一个包" % (log_site, pack_num))
    sniff(filter=filter, prn=pack(log_site, pack_num))  # BPF过滤规则


if __name__ == '__main__':
    sniffer("./packs", "", pack_num=300)
