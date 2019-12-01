# -*- coding: UTF-8 -*-
# 
# # 函数
# 定义函数
def count_fruits(fruits):
    data = {}
    for fruit in fruits:
        data.setdefault(fruit,0)
        data[fruit] += 1
    return data


if __name__ == '__main__':

	today_fruits = ['banana', 'apple',  
                'apple', 'mango']         
	# 调用函数
	result = count_fruits(today_fruits)
	print result
	# {'mango': 1, 'banana': 1, 'apple': 2}

