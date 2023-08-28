# 简介 / 簡介 / Introduction
一个简单的 nyahentai 免登录爬虫。  
A Simple nyahentai Non-Login Crawler.
<br>
<br>
## 需求 / 前置 / Requirement
1. Python 3.x
2. scrapy (使用 pip install scrapy 进行安装)

## 使用说明 / 使用說明 / Guide
<font color="red">不要</font>修改文件名称或变更文件结构。（最外层文件夹名除外）  
Please <font color="red">DO NOT</font> modify file names or alter file structure.  

尽管运行时只能对单个页面的数据进行抓取，但你可以同时开启多个实例并输入不同的 URL  
While it can only scrape data for a single page at runtime, you can simultaneously launch multiple instances and input different URLs.
1. 运行 <code>user-run.bat</code>  
   Run <code>user-run.bat</code>
2. 复制要爬取的漫画详情页面 <code>URL</code>，按下回车  
   Copy the <code>URL</code> of the comic details page you want to crawl, then press Enter

   示例（Example）: https://nyahentai.red/g/XXXXXX  
3. 出现 “进程退出” 标记时，可安全关闭命令窗口，在 .\download\漫画标题\
   应当会出现已经获取到的所有源图文件  
   When the 'Press any button to continue...' indicator appears, you can safely close the command window  
   In the './download/comic_title' directory, you should find all the source image files that have been successfully crawled  
<br>
<br>

# 维护及更新 / 維護及更新 / Maintenance & Updates  
由于该项目只做公开存档，所以一般情况下不会进行功能更新。若目标网站更新导致程序运行失败，也许会进行常规维护  
由于目标网站的特殊性质，且没什么（正经）人会浏览，加之上述功能完全可以通过网站登录后内置的打包功能实现（宁愿写代码也不愿意注册这回事）  
所以该项目允许二次修改发布，允许在注明的前提下重用所有已有代码，也允许提出功能建议（但也许不会有时间做代码实现）  

Since this project is intended solely for personal archiving purposes, functional updates are generally not pursued   
In case updates on the target website lead to program failures, routine maintenance might be carried out  
Due to the specific nature of the website's content, if you know what I mean...  
Furthermore, the aforementioned functionalities can be entirely achieved through the built-in packaging feature after logging into the website  
（Even if I'm ready to hustle like a dog, I'd rather not fetch that website login）  
So, this project allows for secondary modifications and releases. It permits the reuse of all existing code with proper attribution  
And also welcomes feature suggestions (though there might not be time for code implementation)

