# 使用lambda表达式创建匿名平方函数
squared_numbers = map(lambda x: x ** 2, [1, 2, 3, 4, 5])
print(squared_numbers)

print(list(squared_numbers))  # 输出：[1, 4, 9, 16, 25]


