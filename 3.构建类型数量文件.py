import pandas as pd
from sklearn.preprocessing import LabelEncoder

# 读取CSV文件
df = pd.read_csv('河大新闻分类.csv')

# 使用LabelEncoder将类别标签转换为数值型
label_encoder = LabelEncoder()
df['类型'] = label_encoder.fit_transform(df['类型'])

# 打印各类别数量
category_counts = df['类型'].value_counts()

# 按数量大小从大到小输出对应的名称和数量
sorted_categories = label_encoder.inverse_transform(category_counts.index)

# 创建一个新的DataFrame保存标签名、数量和序号
type_counts_df = pd.DataFrame({'类型名称': sorted_categories, '数量': category_counts.values})

# 添加“序号”列
type_counts_df['序号'] = range(1, len(type_counts_df) + 1)

# 调整列的顺序，将“序号”列放在第一列
type_counts_df = type_counts_df[['序号', '类型名称', '数量']]

# 保存到CSV文件
type_counts_df.to_csv('类型数量.csv', index=False)
print("\n已保存类型数量到 '类型数量.csv'")
