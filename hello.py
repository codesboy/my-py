# a=[1,3,5]
# # b=[3,5,1]
# b=[1,3,5]

a={1,3,5}
# b={5,1,3}
b={1,3,5}
print(id(a))
print(id(b))

print(a == b)
print(type(a))
print(isinstance(a,set))


''' 
# 对象的三种特征：
id(身份、内存地址 用is比较) 
value(值 用==比较)
type(数据类型用isinstance判断) 

'''
