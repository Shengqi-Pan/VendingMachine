# 定义自动贩卖机类
class VendingMachine:
    count = 0
    availableMoney = 0
    PRICE = [4, 5, 3.5, 3, 4.5, 2]     # PRICE[n]表示商品n的价格
    def __init__(self):
        f = open('record.txt', 'r')  # 打开文件
        i = 0
        data = []
        for line in f:  # 读取文件内容
            data.append(line.strip('\n'))
            i += 1
        self.profit = float(data[0])          # 总盈利，需要把profit加到VendingMachine的属性
        self.availableMoney = float(data[1])  # 当前余额
        self.remains = data[2]              # 当前商品
        self.remainArray = []
        for char in self.remains:
            if not char == ' ':
                self.remainArray.append(float(char))
        f.close()                   # 关闭文件
        print(self.profit, self.availableMoney)
    # 投入硬币，任何状态都可能投币
    def insertMoney(self,money):
        self.profit += money
        self.availableMoney += money
        self.saveText()
        print('投币成功'+ str(money) + '元，请选择商品')
        return '投币成功'+ str(money) + '元，请选择商品'
	# 退币，任何状态都可能退币
    def backMoney(self):
        self.profit -= self.availableMoney
        self.availableMoney = 0
        print('退币成功')
        return '退币成功'
	# 发放商品
    def dispense(self,n):
        # 这里加上与arduino通讯的代码
        #
        #
        #
        #
        print('请取货')
    def showAvailableMoney(self):
        print('当前余额' + str(self.availableMoney) + '元')
        return '当前余额' + str(self.availableMoney) + '元'
    def showProfit(self):
        print('总收入' + str(self.profit) + '元')
        return '总收入' + str(self.profit) + '元'
    def saveText(self):
        f = open('record.txt', 'w')     # 打开文件
        f.write(str(self.profit) + '\n')
        f.write(str(self.availableMoney) + '\n')
        f.write(str(self.remains))
        f.close()# 关闭文件
    def buy(self, n):
        if not self.remains[n] == '0':
            self.availableMoney -= self.PRICE[n]
            self.remainArray[n] -= 1
            self.remains = []
            for num in self.remainArray:
                self.remains.append(str(num) + ' ')
            self.remains = ''.join(self.remains)
            self.remains = self.remains.strip()
            self.saveText()
            print('购买成功')
            return '购买成功'


if __name__ == '__main__':
    vm = VendingMachine()
    vm.insertMoney(10)  # 支付
    vm.showProfit()     # 显示总收入
    #vm.backMoney()      # 退币
    vm.dispense()       # 出货
    vm.showAvailableMoney()   # 显示可用余额
    vm.showProfit()         #显示总收入
    vm.buy(0)
    vm.showAvailableMoney()