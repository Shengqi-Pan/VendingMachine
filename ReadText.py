# 该文件为测试用
try:
    f = open('record.txt', 'r')    # 打开文件
    i = 0
    data = [0, 0]
    for line in f:                 # 读取文件内容
        data[i] = line.strip('\n')
        i += 1
    profit = int(data[0])          # 总盈利，需要把profit加到VendingMachine的属性
    availableMoney = int(data[1])  # 当前余额
    print(profit, availableMoney)

except:
    print('fail')
finally:
    if f:
        f.close()                  # 确保文件被关闭
