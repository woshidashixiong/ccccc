一个简单的例子，你可以做个参考

from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get('http://example.com')

# 定位下拉框元素
select_element = driver.find_element_by_xpath('xpath_of_select_element') # 这里可以换成其他你比较方便的方法

# 创建Select对象
select = Select(select_element)

# 选择下拉框中的第二个元素
select.select_by_index(1)

你是要解析源代码吗
可以试试BeautifulSoup
from bs4 import BeautifulSoup
html = "html代码"
soup = BeautifulSoup(html, 'html.parser')
