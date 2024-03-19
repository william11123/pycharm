#!/usr/bin/env python
# coding: utf-8

# In[11]:


import requests
from bs4 import BeautifulSoup

url = "https://www.ithome.com.tw/news/152373"
response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, "lxml")

title = soup.title.string.strip()

# 尋找所有帶有 "content" 或 "content-summary" 類別的 <div> 元素
content_elements = soup.find_all("div", class_=["content", "content-summary"])

useless = ["field field-name-field-photo-source field-type-text field-label-inline clearfix", "title", "created"]

# 移除要排除的類別的元素
for element in content_elements:
    for cls in useless:
        labels = element.find_all(class_=cls)
        for label in labels:
            label.decompose()

# 創建一個空列表來存儲每個段落的文本內容
paragraphs = []

# 遍歷 content_elements 中的每個元素，並尋找所有段落 <p>
for element in content_elements:
    paragraphs.extend([p.text.strip() for p in element.find_all('p')])

# 將段落內容合併成字符串，每個段落之間插入兩個換行字符，方便閱讀
content = "\n\n".join(paragraphs)

with open("ithome_news.txt", "w", encoding="utf-8") as file:
    file.write(title + "\n\n")
    file.write(content)

print("内容已保存到 ithome_news.txt 文件中。")

