import torch

'''
初识张量
'''
# 创建并打印未初始化的5x3的矩阵
x1 = torch.empty(5, 3)
print(x1)

# 创建并打印内容是随机数的5x3的矩阵
x2 = torch.rand(5, 3)
print(x2)

# 创建并打印内容全为0的5x3的矩阵
x3 = torch.zeros(5, 3, dtype=torch.long)
print(x3)

# 创建包含确定数值的张量并打印
x4 = torch.tensor([3.5, 5.3])
print(x4)

# 在原有张量的基础之上创建新的张量
x5 = x1.new_ones(5, 3)      # 在x1的维度基础上将其改为全1张量并赋予给x5，x1不变
print(x5)

x6 = torch.randn_like(x1, dtype=torch.float)    # 在x1的维度基础上将其改为全1张量并赋予给x6，x1不变
print(x6)

# 打印张量的尺寸（元组）
print(x1.size())


'''
张量的运算
'''

# 张量的加法
print("x3的值\n", x3)
print("x5的值\n", x5)
y = x3 + x5                         # 加法方式1
print("x3和x5的和\n", y)
print(torch.add(x3, x5))            # 加法方式2
add_result = torch.empty(5, 3)      # 加法方式3，torch.add()中有out参数，作为指定赋值对象
torch.add(x3, x5, out=add_result)
print(add_result)                   # 加法方式4，x5.add_(x2):把x2加到x5上并赋给x5
x5.add_(x2)                         # 任何使张量会发生变化的操作都有一个前缀 '_'
print(x5)

# 索引操作
print(x5[:, 1])

# 改变Tensor大小 torch.view
x7 = torch.empty([3, 4])
x8 = x7.view(-1, 2)                 # '-1'所在的纬度值是计算得来
print(x7.size(), x8.size())

# 获取张量中元素确切值                 # .item()来确定张量中某一个元素的确切值
print(x5[0, 0].item())
