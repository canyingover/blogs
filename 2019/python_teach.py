# -*- coding: UTF-8 -*-
 
'''
标准数据类型：
Numbers（数字）:int、float、long、comlpex
String（字符串）
Tuple（元组）
List（列表）
Dictionary（字典）
'''
# example_int = 100 # 赋值整型变量
# example_float = 1000.0 # 浮点型
# example_string = "n4663" # 字符串
# example_tuple = ('n4663','1234') # 元组
# example_list = ["n4663","n4664","n4665"] # 列表
# example_dict = {"gonghao":"n4664","password":"1234"} # 字典

# # print example_int
# # print example_float
# # print example_string
# # print example_tuple
# # print example_list
# # print example_dict


# # 数字与字符串
# print example_int + 100 # int + int -->  int
# print example_float + 100 # float + int -->  float
# print example_float + 100.0 # float + float -->  float
# print example_int / 100.0 # int / float -->  float
# # 类型强转
# # int 强转为 float
# print type(example_int)
# print type(float(example_int))
# # float 强转为 int
# print type(example_float)
# print type(int(example_float))
# # 数字与字符串互转
# print type(str(example_float))


# # 列表
# example_list = ["n4663","n4664","n4665"]
# # 查
# print example_list # 打印完整列表
# print example_list[0] # 打印列表索引为0的值，即第一个
# print example_list[1:3] # 打印列表索引为1到2的值，即第二和第三个

# # 增
# example_list.append("n4663") # 列表末尾追加值,可以重复
# print example_list
# example_list.insert(1,100) # 特定索引位置插入值
# print example_list

# # 删
# example_list.remove("n4663") # 移除列表中某个值的第一个匹配项
# print example_list
# del example_list[0] # 删除索引位置的值
# print example_list
# example_list.pop(-2) # 删除索引位置的值,默认-1
# print example_list

# # 改
# example_list.sort() # 排序
# print example_list
# example_list.reverse() # 反转
# print example_list


# 字典
example_dict = {"gonghao":"n4664","password":"1234"} 
#查
print example_dict
# 取值
print example_dict["gonghao"]
# 遍历
for key in example_dict:
    print key,example_dict[key]

# # 默认key
# work_days = {}
# work_list = ["n4663", "n4663", "n4664", "n4665", "n4663",]
# for each in work_list:
#     work_days.setdefault(each,0) 
#     #如果键不存在于字典中,将会添加键并将值设为默认值
#     work_days[each] += 1
# # work_days = {'n4663': 3, 'n4665': 1, 'n4664': 1}



# # 条件语句
# num = 9
# if num >= 0 and num <= 10:  # 判断值是否在0~10之间
#     print '0 - 10'
# elif  num > 10:  # 判断值是否在小于0或大于10
#     print '> 10'
# else:
#     print '< 0'

# # 循环语句
# # while 循环
# i = 1
# while i < 10:   
#     i += 1
#     if i%2 > 0:     # 非双数时跳过输出
#         continue    # 跳过后面的代码,执行下一轮循环
#     print i         # 输出双数2、4、6、8、10

# i = 1
# while 1:            # 循环条件为1必定成立
#     print i         # 输出1~10
#     i += 1
#     if i > 10:      # 当i大于10时跳出循环
#         break       # 跳出整个循环



# import json
# s1 = '{"n4663": 3, "n4665": 1, "n4664": 1}'
# print type(s1)
# data = json.loads(s1)
# print data
# print type(data)

# s2 = {"n4663": 3, "n4665": 1, "n4664": 1}
# print type(s2)
# data = json.dumps(s2)
# print data
# print type(data)










# # for 循环
# fruits = ['banana', 'apple',  'mango']
# for fruit in fruits:        
#    print u'当前水果 :', fruit


# # # 读文件
# f = open('./test_for_read.txt','r')
# #print f.read()
# for line in f:
#     print line.strip() # strip()移除字符串头尾指定的字符（默认为空格或换行符）
#     print line.strip().split('\t')[0]
# f.close()

# # 写文件
# w = open('./test_for_write.txt','w')
# record1 = 'n4663'
# record2 = '\t'.join(['n4663','n4664','n4665']) + '\n'
# record3 = '{first}_VS_{second}'.format(first='n4663',second='n4665')
# w.write(record1)
# w.write(record2)
# w.write(record3)
# w.close()
# '''
# n4663n4663  n4664   n4665
# n4663_VS_n4665
# '''

# # 推荐codecs
# import codecs
# with codecs.open('./test_for_read.txt','r',encoding='utf-8') as f:
#     print line.strip()
# with codecs.open('./test_for_read.txt','w',encoding='utf-8') as w:
#     record1 = 'n4663'
#     w.write(record1)


# # 压缩包
# import gzip
# f_in = open("./data.txt", "rb") #打开文件
# f_out = gzip.open("./data.txt.gz", "wb")#创建压缩文件对象
# f_out.writelines(f_in)
# f_out.close()
# f_in.close()

# # 解压
# f = gzip.open("./data.txt.gz", 'rb')#打开压缩文件对象
# for line in f:
#     print line.strip()


# import codecs
# s = u'中或2编码与错误处理'
# print s
# with codecs.open(u'./编码_utf-8.txt','w',encoding='utf-8') as w:
#     w.write(s)
# with codecs.open(u'./编码_gbk.txt','w',encoding='gbk') as w:
#     w.write(s)
# print s.encode('gbk')


# try:
#     with codecs.open(u'./不存在的文件.txt','r',encoding='utf-8') as f:
#         print f.read()                        #正常逻辑
# except Exception,err:
#     print u'文件不存在'#触发自定义异常    
