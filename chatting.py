# 加载库
from itchat.content import *
import requests
import itchat
import json
import VendingMachine

# import RPiGPIO as GPIO

itchat.auto_login(hotReload = False)
lastmsg = 0     #初始化


def replyMessage(info):
    info = info.replace(' ','')
    info = info.replace('\n','')
    if info == '1' or '2' or '3' or '4' or '5' or '6':
        return vm.buy(int(info) - 1)
    # 选择商品的情况结束
    # 退币
    elif info == '退币':
        return vm.backMoney()
    # 显示余额
    elif info == '显示余额' or info == '显示当前余额' or info == '当前余额':
        return vm.showAvailableMoney()
    else:
        return '非法指令'
        '''
        appkey = "e5ccc9c7c8834ec3b08940e290ff1559"
        url = "http://www.tuling123.com/openapi/api?key=%s&info=%s" % (appkey, info)
        req = requests.get(url)
        content = req.text
        data = json.loads(content)
        answer = data['text']
        return answer
        '''
# 注册文本消息，绑定到text_reply处理函数
# text_reply msg_files可以处理好友之间的聊天回复
@itchat.msg_register([TEXT,MAP,CARD,NOTE])
def text_reply(msg):
    # if not msg['Text'] == []:
    itchat.send('%s' % replyMessage(msg['Text']),msg['FromUserName'])
    lastmsg = msg

@itchat.msg_register(itchat.content.SHARING, isMpChat=True)
def reply_msg(msg):
    print("收到一条公众号信息：", msg['User']['NickName'], msg['FileName'])
    message = msg['FileName']
    if msg['User']['NickName'] == '微信支付':
        incomeStart = [i for i in range(len(message)) if message[i] == '款']
        incomeEnd =[i for i in range(len(message)) if message[i] == '元']
        message = message[incomeStart[0] + 1 : incomeEnd[0]]
        vm.insertMoney(float(message))

# @itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
# def download_files(msg):
#     msg['Text'](msg['FileName'])
#     return '@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName'])

if __name__ == '__main__':
    vm = VendingMachine.VendingMachine()
    itchat.run()