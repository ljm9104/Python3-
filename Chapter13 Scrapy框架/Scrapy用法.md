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
