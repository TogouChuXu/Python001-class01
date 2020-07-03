学习笔记

1.在作业完成过程中,重点需要解决在使用Scrapy框架下的反爬虫问题,主要是IP地址被封。
学习完第二周中间件内容,通过使用Scrapy框架自带Http代理中间件,基本可解决问题。
2.使用管道写入爬取内容到本地文件中,需要在settings中做相关配置：ITEM_PIPELINES = {
   'homework2.pipelines.Homework2Pipeline': 300,
}。