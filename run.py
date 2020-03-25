# coding=utf-8
# python3
#@Author : Dev-Leo
#@Email : dengziqi52@gmail.com

import requests
import json
import time


def request():
    post_url = "https://app.xiaoyuan.ccb.com/channelManage/outbreak/addOutbreak"
    headers = {'Content-Type': 'application/json;charset=UTF-8'}
    cs = {'Cookie': 'Your Cookie'}
    datas = {
    "stuClass":"",
    "schoolId":"",
    "schoolName":"",
    "stId":"",
    "userId":"",
    "stName":"",
    "locationAddr":"",
    "id":"",
    "departments":"",
    "isContact":"N",
    "isFever":"0",
    "isWuhan":"N",
    "nowArea":"",
    "familyaddress":"",
    "familyStatus":"0",
    "diagnosisTreatment":"",
    "nowStatus":"0",
    "isLevel":"N",
    "isbackLive":"N",
    "trafficTool":"",
    "backTrafficTool":"",
    "levelDate":"",
    "backtime":"",
    "arriveAddr":"",
    "trafficNo":"",
    "backTrafficNo":"",
    "professional":"",
    "personType":"",
    "temperature":36.8,
    "remarks":"",
    "timeToLeaveHuBei":"",
    "dateOfDisengagement":"",
    "otherSymptoms":"",
    "nowStatusStartTime":"",
    "familyStatusStartTime":"",
    "feverStartTime":"",
    "coughStartTime":"",
    "fatigueStartTime":"",
    "diarrheaStartTime":"",
    "coldStartTime":"",
    "headacheStartTime":"",
    "isAppearDiagnosis":"N",
    "isContactWithDiagnosis":"N",
    "isInSchool":"",
    "stMobile":""
    }
    r = requests.post(post_url,cookies=cs,data=json.dumps(datas),headers=headers)
    r = r.text
    return r

def return1():
    post_url = "You DingTalk Api"
    headers = {'Content-Type': 'application/json'}
    data =  {
    "msgtype": "text",
     "text": {
         "content":"此处填写你的API关键词"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+msg
    }
    }
    requests.post(post_url, data=json.dumps(data), headers=headers)
    print(r)

if __name__ == '__main__':
    r = request()
    message = "成功"
    if message in r :
        msg = "打卡成功"
        return1()
    else:
        msg = "打卡失败"
        return1()
