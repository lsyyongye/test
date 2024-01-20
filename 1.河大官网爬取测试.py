import requests
base_url = 'http://www.henu.edu.cn'
res = requests.get(base_url) #  发送GET请求
# 获取响应状态码
print("响应状态码：{}".format(res.status_code))
# 获取响应内容的编码方式
print("编码方式：{}".format(res.encoding))
# 更新响应内容的编码方式为utf-8
res.encoding = 'utf-8'
# 获取响应内容
print("网页源代码：\n{}".format(res.text))
