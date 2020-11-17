import torch

# 创建并打印未初始化的5x3的矩阵
x1 = torch.empty(5, 3)
print(x1)

# 创建并打印内容是随机数的5x3的矩阵
x2 = torch.rand(5, 3)
print(x2)

# 创建并打印内容全为0的5x3的矩阵
x3 = torch.zeros(5, 3, dtype=torch.long)
print(x3)

x4 =
