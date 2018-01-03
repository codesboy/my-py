#!/usr/bin/python3

# 打开文件
fo = open("1.txt", "r+",encoding= 'utf-8')
print ("文件名为: ", fo.name)

line = fo.read(10)
print ("读取的字符串: %s" % (line))

# 关闭文件
fo.close()