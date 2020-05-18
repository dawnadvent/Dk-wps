#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@time      :2020/05/09 13:44:54
@author    :4rat
'''

import urllib3
import requests
import time
import json
import os
urllib3.disable_warnings()


def wps_invite(sid):
    '''
    签到
    sid可以登录http://zt.wps.cn，查看cookie里的sid进行获取
    '''
    if sid != '':
        url = "https://zt.wps.cn/2018/clock_in/api/clock_in?member=wps"
        headers = {
            'Host': 'zt.wps.cn',
            'content-type': 'application/json',
            'sid': sid,
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
        }
        r = requests.get(url, headers=headers, verify=False)
        try:
            html = json.loads(r.text)
        except Exception:
            msglog = '[*]    请正确填写SID !'
            return msglog
        if html['result'] == 'ok':
            msglog = '[-]   签到状态 ' + html['result']+" wps签到打卡成功！" + \
                time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            return msglog
        else:
            msglog = '[*]    签到状态 ' + html['result']+' : '+html['msg'] + \
                "  " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            return msglog
    else:
        msglog = '[*]    请正确填写SID !'
        return msglog


def wps_sign_in(userid):
    path = os.getcwd()
    print(path)
    '''
    邀请
    '''
    msgtextlog = []
    if userid != '':
        url = "https://zt.wps.cn/2018/clock_in/api/invite"
        if os.path.exists('sids.txt'):
            sids = open('sids.txt', 'r')
            i = 1
            for sid in sids:
                if i <= 10:
                    headers = {
                        'Host': 'zt.wps.cn',
                        'content-type': 'application/json',
                        'sid': sid.rstrip("\n"),
                        'Accept-Encoding': 'gzip, deflate',
                        'Connection': 'close',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
                    }
                    r = requests.post(
                        url, headers=headers, data='{"invite_userid":"'+userid+'"}', verify=False)
                    if r.status_code == 200:
                        msglog = "[-]    邀请{}位好友, 成功, 状态码: {}, sid: {}".format(
                            i, r.status_code, sid).strip()
                        r.close()
                        i += 1
                        msgtextlog.append(msglog)
                    else:
                        msglog = "[*]    邀请好友失败, 状态码: {}, sid: {}".format(
                            r.status_code, sid).strip()
                        r.close()
                        msgtextlog.append(msglog)
                        continue
                else:
                    break
            return msgtextlog
        else:
            open("sids.txt", mode='w', encoding='utf-8')
            msgtextlog.append('[*]    未发现sids配置文件, 文件初始化成功, 请填写目录下sids配置 !')
            return msgtextlog
    else:
        msgtextlog.append('[*]    请正确填写UserID !')
        return msgtextlog
