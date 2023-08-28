import scrapy, os
from scrapy.pipelines.files import FilesPipeline


class NyaspiderPipeline(FilesPipeline):
    folder_name = ""
    pages = 0
    times = 0
    count = 0


    def get_media_requests(self, item, info):
        if item['title'] is not None and item['title'] != '':
            self.handle_folder(item['title'])
            # self.handle_folder("<>*/\\|:?")
        else:
            exit("")            

        try:
            if item['pages'] is not None and item['pages'] != '':
                self.pages = int(item['pages'])
        except:
            exit("")

        for url in item['file_urls']:
            yield scrapy.Request(url)
    

    def handle_folder(self, title) -> None:
        self.folder_name = title
        illegal_dict = {'/':'', '\\':'', ':':'：', '*':'⭕', '\"':'', '<':'[', '>':']', '|':'', '?':'？'}
        
        for k in illegal_dict:
            if k in self.folder_name:
                self.folder_name = self.folder_name.replace(k, illegal_dict[k])


    def file_path(self, request, response=None, info=None, *, item=None):
        self.times = self.times + 1
        file_name = os.path.basename(request.url)
        path = self.folder_name + '\\' + file_name
        
        if response and (self.times % 2) != 0:
            self.count = self.count + 1
            print("Downloading:", file_name, end="\t")
            print(f"({self.count}/{self.pages})")

        return path


    def item_completed(self, results, item, info):
        return item


    def close_spider(self, spider):
        file_list = os.listdir(os.getcwd() + "\\download\\" + self.folder_name)
        
        if len(file_list) < self.pages:
            for check_file in range(1, self.pages + 1):
                if str(check_file) + ".jpg" not in file_list and \
                   str(check_file) + ".png" not in file_list:
        
        