import pandas as pd
from sklearn.cluster import KMeans

# 读取CSV文件
type_counts_df = pd.read_csv('类型数量.csv')

# (1) 统计分析
statistics = type_counts_df[['序号', '数量']].describe()
print("统计分析:")
print(statistics)

# (2) 相关性分析
correlation_matrix = type_counts_df[['序号', '数量']].corr()
print("\n相关性分析:")
print(correlation_matrix)

# (3) 聚类分析
# 使用KMeans算法进行聚类，这里假设将数据分成3类
kmeans = KMeans(n_clusters=3, random_state=42)
type_counts_df['类型'] = kmeans.fit_predict(type_counts_df[['序号', '数量']])

# 删除原始的“序号”列
type_counts_df = type_counts_df.drop(columns=['序号'])

# 打印聚类结果
print("\n聚类分析:")
print(type_counts_df)