Spider类
    定义爬取网站的动作
    分析抓取的网页
    
    爬取循环的过程
        1.已初始的url初始化Request，并设置回调函数，当Request返回后，Response生成并作为参数传到回调函数
        2.回调函数解析网页
            a.解析得到item
            b.解析下一页（个）链接，Request
        3.返回item继续处理保存
          返回Request
          
    Spider类分析
        name
        allow_domains
        start_urls
        custom_settings
        crawler
        settings
        start_requests()
        parse()
        close()
        open()
    
    Downloader Middleware
        可以设置修改UA，重定向，代理，失败重试，cookies
    
        设置UA
            1.setting里
            2.Downloader Middleware里
                在settings.py(配置文件)中禁用默认的useragent并启用重新实现的User Agent，
                'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware' : None,
                在middlewares设置类RandomUserAgentMiddleware，并在setting里启用
    
    Spider Middleware
        三个作用
        1.可以在 Downloader 生成 Response 发给 Spider 之前对Spider处理
        2.可以在 Spider 生成 Request 发给 Schedule 之前对 Request 处理
        3.可以在 Spider 生成 Item 发给 Item Pipline 之前对 Item 处理
        
        在SPIDER_MIDDLEWARES_BASE 变量中定义好了默认
        
        核心算法, 只需实现以下四个之一就可定义一个Middleware
            process_spider_input(response, spider)
                应该返回None或者跑出异常
            process_spider_output(response, result, spider)
                返回Request或者Item对象
            process_spider_exception(response, exception, spider)
                返回Request, Response, 或者Item对象
            process_start_requests(start_requests, spider)
                返回Request对象
                
    Item Pipline
        1.清理HTML数据
        2.验证爬虫数据
        3.查重并丢弃数据
        4.将结果保存
        
        核心方法
            process_item(item, spider) 必须实现
            返回Item或者DropItem异常
        
        其他常用方法
            open_spider(spider)
            close_spider(spider)
            from_crawler(cls, crawler)  依赖注入     

