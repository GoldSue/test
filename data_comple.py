import requests
from bs4 import BeautifulSoup

# 百度新闻的URL
url = "https://news.baidu.com/"

# 发送HTTP GET请求
response = requests.get(url)

# 检查请求是否成功
if response.status_code == 200:
    # 解析HTML内容
    soup = BeautifulSoup(response.text, 'html.parser')

    # 查找所有新闻标题和链接
    news_items = soup.find_all('a', class_='title-content-title')

    # 打印新闻标题和链接
    for item in news_items:
        title = item.get_text(strip=True)
        link = item['href']
        print(f"标题: {title}")
        print(f"链接: {link}")
        print("-" * 50)
else:
    print(f"请求失败，状态码: {response.status_code}")
