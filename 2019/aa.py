# -*- coding: utf-8 -*-
# @Author: n4663
# @Date:   2017-05-19 12:59:02
# @Last Modified by:   n4663
# @Last Modified time: 2019-10-15 19:47:21

from __future__ import division, print_function
import sys
sys.path.append("./module/")
import urllib2
import urllib
import cookielib
import os,sys
import ConfigParser, json
import time
from datetime import datetime, date, timedelta
import codecs
import binascii
import my_common as my
import time
from UUtils import UUtils
import io
import re
from helper import json_serial, timedelta_total_seconds
import punish_lhc
import logging
import os
from collections import Counter
import difflib

log = logging.getLogger()
formatter = logging.Formatter('[%(asctime)s] [%(name)s] %(levelname)s: %(message)s')
stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler(os.path.join(os.getcwd(), 'test.log'))

file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)
log.addHandler(file_handler)
log.addHandler(stream_handler)
log.setLevel(logging.DEBUG)


os.environ['no_proxy'] = '163.com'
os.environ['no_proxy'] = 'netease.com'


class DCUtils(object):
    def __init__(self, path):
        self.cf = ConfigParser.RawConfigParser()
        if not os.path.isfile(path):
            raise ValueError('path is not valid config file. Please check.')
        try:
            with codecs.open(path, 'r', encoding='utf-8') as f:
                self.cf.readfp(f)
        except:
            with codecs.open(path, 'r', encoding='gbk') as f:
                self.cf.readfp(f)

        self.username = self.cf.get("baseconf", "username")
        self.password = self.cf.get("baseconf", "password")
        print (self.password)
        self.game = self.cf.get("baseconf", "game")
        self.game = 'g103'
        self.apikey = self.cf.get("baseconf", "apikey")
        self.dcurl = {
            "0": "http://g103dc.gameyw.netease.com:8088/logs/{game}/_REALTIME_".format(game=self.game),
            "1": "http://g103dc.gameyw.netease.com:8088/logs/{game}".format(game=self.game)
        }

        password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
        top_level_url = self.dcurl['1']
        password_mgr.add_password(None, top_level_url, self.username, self.password)
        basic_auth_handler = urllib2.HTTPBasicAuthHandler(password_mgr)
        proxy_support = urllib2.ProxyHandler({})
        cookie = cookielib.CookieJar()
        opener = urllib2.build_opener(proxy_support, urllib2.HTTPCookieProcessor(cookie), basic_auth_handler)
        opener.addheaders = [('User-agent', 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)')]
        urllib2.install_opener(opener)

    def realtimeLog(self, logname, day=None, seek_size=None):
        if not day:
            day = datetime.now()

        url = "{base}/{logname}/{date:%Y%m%d}.log".format(
            base=self.dcurl['0'], logname=logname, date=day)
        print (url)
        headers = {}
        seek_begin = self.getRealtimeSeek(logname, day)
        print(seek_begin)
        if seek_size:
            headers["Range"] = "bytes={0}-{1}".format(
                seek_begin, seek_begin + seek_size * 1024 * 1024)
        else:
            headers["Range"] = "bytes={0}-{1}".format(
                seek_begin, '')

        req = urllib2.Request(url, headers=headers)

        try:
            response = urllib2.urlopen(req)
            #print(response.read())
            new_size = int(response.headers['Content-Length']) + seek_begin
            self.setRealtimeSeek(logname, day, new_size)
        except urllib2.HTTPError as e:
            print(e.code)
            if e.code == 416:
                print(u'没有新的资源下载')
            elif e.code == 404:
                print(u'日志还未生成')
            return False
        except urllib2.URLError as e:
            print(e.code)
            return False

        return response


    def getRealtimeSeek(self, logname, day):
        try:
            day = day.strftime("%Y%m%d")
            j = json.load(file(logname + '.json'))
            seek_size = j.get(day, 0)

        except IOError:
            print(u'重新开始读log', logname)
            seek_size = 0

        return int(seek_size)

    def setRealtimeSeek(self, logname, day, seek_size):
        try:
            day = day.strftime("%Y%m%d")
            d = {day: seek_size}
            with open(logname + '.json', 'w') as f:
                json.dump(d, f)
        except:
            return False
        return True


def xiangsidu(chat_list):####相似度
    chat_cnt = len(chat_list)
    first_chat = chat_list[0]
    xsd = 0
    for i in range(-chat_cnt+1,0):
        xsd += difflib.SequenceMatcher(None , first_chat , chat_list[i]).ratio()
    average_xsd = xsd/(chat_cnt - 1)
    return float ('%.2f' % average_xsd)


if __name__ == '__main__':


    cb = DCUtils(os.path.join(os.environ['USERPROFILE'], 'config', 'config.ini'))
    response = cb.realtimeLog("chat", day=None, seek_size=None)
    response = False

    while 1:

        #try:
        #if  1:
            #pass
            # launcher_hack_udids = set()
            # with codecs.open(u'./launcher_hack_udids.txt', 'r', encoding='utf-8', errors='ignore') as f1:
            #     for line in f1:
            #         launcher_hack_udids.add(line.strip().split('\t')[0])
            # login_hack_udids = set()
            # with codecs.open(u'./login_hack_udids.txt', 'r', encoding='utf-8', errors='ignore') as f1:
            #     for line in f1:
            #         login_hack_udids.add(line.strip().split('\t')[0])


            log.info(u'g103刷屏(g103-chat)')
            today = datetime.now().strftime('%Y%m%d')
            # pass_create_app_channel = ["zqgame","xiaomi_app","360_assistant","oppo","nearme_vivo","wandoujia","4399com","huawei","baidu","baidu_sem_dev","flyme","yixin"]
            try:
                with codecs.open(ur'\\fs16\手游一组共享盘\g-个人文件夹\n4663\g103_apikey.txt', 'r', encoding='utf-8') as api:
                    Apikey = api.read()
            except Exception,e:
                log.info(e)
                continue
            # with codecs.open(ur'\\fs16\手游一组共享盘\g-个人文件夹\n4663\opdhyt_apikey.txt', 'r', encoding='utf-8') as api:
            #     Apikey_opdhyt = api.read()
            # #Apikey = 'CE2F4A21E3E39E8EF6BE3CF2EB3B7A82E4B69DECCA982C2B517FC2B41542711914B3A479B3816D16'
            cb = DCUtils(os.path.join(os.environ['USERPROFILE'], 'config', 'config.ini'))

            #need_day = datetime.now() + timedelta(days=-1)
            response = cb.realtimeLog("kafka_chat", day=None, seek_size=None)
  
            if response:
                filename = u'./data/{0}_g103_shuaping.txt'.format(today)
                chat_cnt = {}
                for line in response:
                    try:
                        data = json.loads(line.strip().split('[Chat],')[1])
                        #c_time = line.strip().split('[hytpe-chat],')[0].split('hyt_pe: ')[1][1:-1]

                        #timeArray = time.strptime(c_time, "%Y-%m-%d %H:%M:%S")
                        #timeStamp = int(time.mktime(timeArray))
                        server = data['server']
                        if int(server) == 10002:
                            continue
                        role_level = data['role_level']
                        if int(role_level) >= 8:
                            continue


                        content = data['content'].replace('\\n',"").replace('\\r',"").replace('\r',"")
                        if re.search(ur'^(#[BD]\d{5}){1,5}$|^(#\d{5}){1,5}$|喜[好欢]|级.*?食物|好友|BOSS|boss|副本|篝火晚会|居酒屋|固定队|邀请码|章鱼|扑克|牌|吃饭|骷髅|石距|庭院|带.*?过|爱心|肥寝|胧车|寝肥|土蜘蛛|麒麟|螃蟹|剧|鲶|求|互.*?[赞屋吃]|餐|船|饭|章|打工|简单.*?本',content):
                            continue
                        role_id = data['role_id']


                        # role_id = data['role_id']
                        # role_id = data['role_id']
                        # role_id = data['role_id']
                        # role_id = data['role_id']
                        # if u'<全体>' in content or u'<队伍>' in content:
                        #     continue
                        # game_role_name = data['game_role_name']
                        key = str(server) + '\t' + role_id
                        chat_cnt.setdefault(key,[])
                        chat_cnt[key].append(content)
                    except Exception,e:
                        log.info(e)
                        continue
                print(len(chat_cnt))
                with codecs.open(filename, 'a+', encoding='utf-8', errors='ignore') as f2:
                    # 完全相同
                    # for each in chat_cnt:
                    #     c = Counter(chat_cnt[each])
                    #     for i in c:

                    #         if c[i] >= 3 and len(i) >= 20 and re.search(r'\d+',i):
                    #             # user_data = punish_lhc.get_user_info(each,u'查询uid',Apikey_g79)
                    #             # uid = user_data['result'][0]['user_info']['uid']
                    #             # print(uid)
                    #             record = '\t'.join([each,unicode(i),str(c[i])]) + '\n'
                    #             f2.write(record)

                    #相似85%
                    for each in chat_cnt:

                        if len(chat_cnt[each]) >= 6 and min([len(i) for i in chat_cnt[each]])>6:
                            similar = xiangsidu(chat_cnt[each])
                            if similar > 0.85:
                                # print(each)
                                server = each.split('\t')[0]
                                role_id = each.split('\t')[1]
                                if not re.search(r'\d{5}',str(server)):
                                    continue
                                mgdc_reason = u'{"ischufa":"1", "account_id": "", "urs": "", "level": "C", "type":"4_G_4", "reason":"刷屏禁言：' + chat_cnt[each][0] +'"}'
                                result = punish_lhc.ban_chat(server,role_id,1440,u'违规/刷屏言论',mgdc_reason,Apikey)
                                print(result)
                                record = '\t'.join([each,json.dumps(chat_cnt[each],ensure_ascii=False),str(similar),str(result['succ']),mgdc_reason]) + '\n'
                                #record = '\t'.join([each,json.dumps(chat_cnt[each],ensure_ascii=False),str(similar)]) + '\n'
                                #record = '\t'.join([each,json.dumps(chat_cnt[each],ensure_ascii=False),str(similar),str(result)]) + '\n'
                                f2.write(record)




            time.sleep(150)
            #break
        # except Exception,e:
        #     log.info(e)



