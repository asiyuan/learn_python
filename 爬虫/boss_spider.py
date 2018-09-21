import requests
from lxml import etree


# 定义职位数据的模型
class Job(object):

    def __init__(self):
        self.company = ''
        self.degree = ''


# 定义爬虫的类
class Spider(object):
    url = 'https://www.zhipin.com/c101010100/h_101010100/?query=web&page='
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36',
    }

    def get_list_page(self):
        urls = []
        for i in range(11):
            url = self.url + str(i)
            urls.append(url)
        return urls

    def parse_url(self):
        urls = self.get_list_page()
        for url in urls:
            response = requests.get(url, headers=self.headers)
            html = etree.HTML(response.text)
            lis = html.xpath('//div[@class="job-list"]//ul/li')
            for li in lis:
                company = li.xpath('//h3[@class="name"]/a/text()')
                company = ''.join(company)
                print(company)

            break


if __name__ == '__main__':
    s = Spider()
    s.parse_url()
