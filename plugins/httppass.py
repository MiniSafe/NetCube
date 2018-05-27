# coding:utf-8
from __future__ import unicode_literals
from __future__ import print_function
from NetCube.module.debug_log import debug_log
from NetCube.module.encode import decoder
import re


def tcp(packet, request_info, data):
    datas = data.get('load')
    if datas:
        lists = [('u=', '&p='),
                 ('txtUserId=', '&txtPassword='),
                 ('username=', '&password='),
                 ('F_LOGINNAME=', '&F_PASSWORD='),
                 ('account=', '&password='),
                 ('username=', '&pwd='),
                 ('userId=', '&password='),
                 ('UserName=', '&PASSWORD='),
                 ('txtName=', '&txtPwd='),
                 ('UserTxt=', '&PsdTxt='),
                 ('account=', '&password='),
                 ('dd=', '&mm='),
                 ('UserName=', '&Password='),
                 ('userCode=', '&password='),
                 ('j_username=', '&j_password='),
                 ('login_name=', '&login_password='),
                 ('NAME=', '&PAS='),
                 ('txtUsername=', '&txtPassword='),
                 ('UserNameTemp=', '&PassWordTemp='),
                 ('UserName=', '&PassWord='),
                 ('tbxUserName=', '&tbxPassword='),
                 ('userName=', '&password='),
                 ('id=', '&password='),
                 ('uid=', '&pwd='),
                 ('txtLoginName=', '&txtPwd='),
                 ('userName=', '&pwd='),
                 ('uname=', '&pwd='),
                 ('txtUserCode=', '&txtPassword='),
                 ('"userAccounts":', ',"password":'),
                 ('UserNameTextBox=', '&PasswordTextBox='),
                 ('txtAdminName=', '&txtPassword='),
                 ('uName=', '&uPwd='),
                 ('UserName=', '&pwd='),
                 ('email=', '&password='),
                 ]
        if datas.startswith(b"POST "):
            try:
                r_line, tmp = datas.split(b"\r\n", 1)
                post = tmp.split(b"\r\n\r\n",1)[1]
                for key, value in lists:
                    info = re.search(b'%s(.*?)%s(.*?)($|&)' % (key, value),post)
                    if info:
                        debug_log(packet['src'], packet['dst'], "HTTP",
                                  "协议版本:%s" % decoder(r_line.split(b" ")[-1].split(b"/", 1)[1]),
                                  "用户信息 <%s:%s> %s" % (info.group(1), info.group(2), r_line))
            except Exception, e:
                pass


def udp(p1, p2, p3):
    pass


def other(p1, p2, p3):
    pass
