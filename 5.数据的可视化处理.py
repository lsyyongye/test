import pandas as pd
import pymysql
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']

# 数据库连接信息
host = 'localhost'
user = 'root'
password = '1234'
database = 'henu'
table = 'leixing_count'

# 创建数据库连接
connection = pymysql.connect(host=host, user=user, password=password, database=database)

# 从数据库中读取数据
query = f"SELECT * FROM {table};"
df_mysql = pd.read_sql_query(query, connection)

# 关闭数据库连接
connection.close()

# 可视化数据

# 点线图
plt.figure(figsize=(10, 6))
plt.plot(df_mysql['序号'], df_mysql['数量'], marker='o', linestyle='-', color='b')
plt.title('折线图 - 类型数量')
plt.xlabel('序号')
plt.ylabel('数量')
plt.grid(True)
plt.show()

# 柱状图
plt.figure(figsize=(10, 6))
plt.bar(df_mysql['类型'], df_mysql['数量'], color='c')
plt.title('柱状图 - 类型数量')
plt.xlabel('类型名称')
plt.ylabel('数量')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# 雷达图
plt.figure(figsize=(10, 6))
plt.polar(df_mysql['序号'] * 2 * 3.14159 / max(df_mysql['序号']), df_mysql['数量'], marker='o', linestyle='-', color='r')
plt.title('雷达图 - 类型数量')
plt.show()
