import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

# 初始URL
base_url = "http://news.henu.edu.cn/xxxw/{}.htm"

# 初始页面的URL
initial_url = "http://news.henu.edu.cn//xxxw.htm"

# 发送HTTP请求获取初始页面内容
initial_response = requests.get(initial_url)
initial_response.encoding = initial_response.apparent_encoding

# 使用BeautifulSoup解析HTML
initial_soup = BeautifulSoup(initial_response.text, 'html.parser')

# 找到class为mytzlist的ul标签
initial_ul_tag = initial_soup.find("ul", class_="mytzlist")

# 找到ul标签下的所有li标签
initial_li_tags = initial_ul_tag.find_all("li")

# 提取初始页面的标题信息
initial_titles = []
for initial_li_tag in initial_li_tags:
    a_tag = initial_li_tag.find("a")
    title = a_tag.get("title")
    initial_titles.append({"Title": title})

# 打开CSV文件，如果不存在则创建新文件
with open("河大新闻.csv", mode="a", encoding="utf-8", newline="") as csvfile:
    # 定义CSV文件的列名
    fieldnames = ["Title"]

    # 创建CSV写入对象
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # 如果文件为空，写入列名
    if csvfile.tell() == 0:
        writer.writeheader()

    # 将初始页面的标题信息写入CSV文件
    writer.writerows(initial_titles)

    # 遍历URL列表
    for url_index in range(2109, 2095, -1):
        url = base_url.format(url_index)

        # 发送HTTP请求获取页面内容
        response = requests.get(url)
        response.encoding = response.apparent_encoding

        # 使用BeautifulSoup解析HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # 找到class为mytzlist的ul标签
        ul_tag = soup.find("ul", class_="mytzlist")

        # 找到ul标签下的所有li标签
        li_tags = ul_tag.find_all("li")

        # 遍历li标签，获取a标签的title值，并写入CSV文件
        for li_tag in li_tags:
            a_tag = li_tag.find("a")
            title = a_tag.get("title")
            writer.writerow({"Title": title})

print("爬取完成并已写入CSV文件。")

# 数据清洗
# 读取CSV文件到DataFrame
df = pd.read_csv("河大新闻.csv", encoding="utf-8")

# 1. 去除重复数据
df.drop_duplicates(inplace=True)

# 2. 处理缺失值，这里使用空字符串填充缺失值，你也可以根据实际情况选择其他方式
df.fillna("", inplace=True)

# 3. 处理异常值（这里仅打印统计信息，你可以根据需要添加处理逻辑）
print("数据统计信息:")
print(df.describe())

# 将清洗后的数据写回CSV文件
df.to_csv("cleaned_河大新闻.csv", encoding="utf-8", index=False)

print("数据清洗完成，并已写入cleaned_河大新闻.csv文件。")
