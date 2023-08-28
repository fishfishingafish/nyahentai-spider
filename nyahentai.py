import scrapy, re
from ..items import NyaspiderItem

class NyahentaiSpider(scrapy.Spider):
    name = "nyahentai"
    allowed_domains = ["nyahentai.red"]
    
    
    def get_input():
        start = input("URL : ")
        return start


    start_urls = [get_input()]
    # start_urls = ["https://nyahentai.red/g/335142"]

    
    def parse(self, response):        
        item = NyaspiderItem()
        item['pages'] = response.xpath("//div[contains(text(), 'Pages')]//span[@class='name']/text()") \
        .extract()[0]
        item['title'] = response.xpath("//h2[@class='title']/span/text()").extract()[0]
        item['file_urls'] = [] 

        gen_urls = response.xpath("//noscript/img/@src").extract()[1:]
        for url in gen_urls:
            item['file_urls'].append(self.fix_url(url))
        
        # print(item['file_urls'])
        yield item
    

    def fix_url(self, url) -> str:
        parts_url = url.split("/")
        true_url = ""
        true_name = re.sub("[a-zA-z]", "", parts_url[-1].split(".")[0])
        
        for part in parts_url[:-1]:
            true_url = true_url + part + "/"
        
        true_url = true_url + true_name + "." + str(parts_url[-1].split(".")[-1])

        return true_url

    
    