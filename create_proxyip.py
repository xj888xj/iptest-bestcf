import pandas as pd
#####################################################################################
# 读取 CSV 文件
df = pd.read_csv('latest_sorted.csv')

# 提取第一列数据
first_column = df.iloc[:, 0]

# 将数据写入文本文件
first_column.to_csv('proxyip.txt', index=False, header=False)
#####################################################################################
# 读取 CSV 文件
df = pd.read_csv('latest_sorted-HK.csv')

# 提取第一列数据
first_column = df.iloc[:, 0]

# 将数据写入文本文件
first_column.to_csv('proxyip-HK.txt', index=False, header=False)
#####################################################################################
# 读取 CSV 文件
df = pd.read_csv('latest_sorted-SG.csv')

# 提取第一列数据
first_column = df.iloc[:, 0]

# 将数据写入文本文件
first_column.to_csv('proxyip-SG.txt', index=False, header=False)
#####################################################################################
# 读取 CSV 文件
df = pd.read_csv('latest_sorted-US.csv')

# 提取第一列数据
first_column = df.iloc[:, 0]

# 将数据写入文本文件
first_column.to_csv('proxyip-US.txt', index=False, header=False)
#####################################################################################
# 读取 CSV 文件
df = pd.read_csv('latest_sorted-KR.csv')

# 提取第一列数据
first_column = df.iloc[:, 0]

# 将数据写入文本文件
first_column.to_csv('proxyip-KR.txt', index=False, header=False)
#####################################################################################
