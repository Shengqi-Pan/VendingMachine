# 此文件用于测试
remains = '1 2 3 4 2 3'
remainArray = []
for char in remains:
    if not char == ' ':
        remainArray.append(int(char))
print(remainArray)
remainArray[0] -= 1
remains = []
for num in remainArray:
    remains.append(str(remainArray[num]) + ' ')
remains = ''.join(remains)
print(remains)
remains = remains.strip()
print(remains)