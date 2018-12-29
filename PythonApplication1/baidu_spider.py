#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import urlparse
import urllib
import threading
import threadpool
from threading import Thread
from HTMLParser import HTMLParser
from  multiprocessing import Process

g_baidu_urls = ["https://www.baidu.com/s?wd=%E8%A7%86%E9%A2%91&rsv_spt=1&rsv_iqid=0x90f8a2b40005b3b6"
               "&issp=1&f=8&rsv_bp=0&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_sug3=10&rsv_sug1=5&rsv_sug7=100&rsv_sug2=0&inputT=4499&rsv_sug4=5998",
                "https://www.baidu.com/s?wd=TV&pn=20&oq=TV&ie=utf-8&rsv_idx=1&rsv_pq=80b232ed000368e7&rsv_t=9d11mI%2FyssS4dmSwUysoaKxcutTewUKJw0Vi3iSDTwZ4y%2BJNcAKGOMlPg%2FA&rsv_page=1",
                "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd=%E7%9B%B4%E6%92%AD&rsv_pq=85992a8a00032f1f"
                "&rsv_t=d9f9LaXuZO6VUD7%2BsqKjFd36CqQWsllorY635vo5jwwc8YIiTlR8JusYQAg&rqlang=cn&rsv_enter=1&rsv_sug3=9&rsv_sug1=13&rsv_sug7=100",
                "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E4%B8%BB%E6%92%AD&oq=%25E7%259B%25B4%25E6%2592%25AD"
                "&rsv_pq=84d103b90003584b&rsv_t=1f16gvCAYzh5%2F8XBulwdNWOVGxN%2FQWZJVR8Vj%2BU7aa9pSO%2BRtvMAOQw%2BgAY&rqlang=cn&rsv_enter=1&inputT=3509&rsv_sug3=19&rsv_sug1=24&rsv_sug7=100&rsv_sug2=0&rsv_sug4=3509",
                "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E5%9C%A8%E7%BA%BF%E6%95%99%E8%82%B2&oq=%25E5%259C%25A8%25E7%25BA%25BF%25E6%2595%2599%25E8%2582%25B2"
                "&rsv_pq=8c8b658600073ffd&rsv_t=f73ek0Dn3f2w9Neg9v1aRtvptKQww9AatER4cphq5XkjW15DYesmyxfG4mA&rqlang=cn&rsv_enter=0&rsv_sug=1",
                "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=25017023_10_pg&wd=%E5%85%8D%E8%B4%B9%E8%A7%82%E7%9C%8B&oq=%25E5%259C%25A8%25E7%25BA%25BF%25E8%25A7%2582%25E7%259C%258B&"
                "rsv_pq=b15879db0000751e&rsv_t=8900uUEDrd1dbJWk1Xx8G2suxLDyZfefq%2BCQFYtpmiE7xvFufl1foln11D9RJnpg%2FDHHBv0&rqlang=cn&rsv_enter=1&inputT=3355&rsv_sug3=26&rsv_sug1=17&rsv_sug7=100&rsv_sug2=0&rsv_sug4=3355",
                "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=25017023_10_pg&wd=%E5%9C%A8%E7%BA%BF%E8%A7%82%E7%9C%8B&oq=%25E5%25BD%25B1%25E8%25A7%2586&rsv_pq=99acd34a00002c2b&"
                "rsv_t=6a4c34RDzPXCeF3yIHKUrKbtx4FNN0drqja0lC8JYQ%2FmpZ4GnQ9dUECNxsGp%2FHkxxvrzSYI&rqlang=cn&rsv_enter=1&rsv_sug3=13&rsv_sug1=8&rsv_sug7=100&bs=%E5%BD%B1%E8%A7%86",
                "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=21076068_cpr&wd=%E7%94%B5%E5%BD%B1%E7%BD%91&"
                "fenlei=mv6qUZNxTZn0IZRqIHnYPWnLrHc0T1dWmvnLnyFbPHn3uyfzPhFB0ZwV5HD1PWmkrH00mvmqnfKzmWYk0AkdpvbqnfKWUMw85HcknjTvnjm3gvPsT6K1TL0qnfK1TL0z5HD0IZws5HD0UZN15HPhryPhrHndPhmvn17BrHn0UZN1IjYdm1cYPHf3P6K_IyPY5HNWnWfdPyn40Akdgv-bm1dCX6KbIZ0qnfKGIAYqn0K9uAP_mgP15HD10ZIG5Hf0&oq=c%2523%2520using&rsv_pq=d94d11a80003341d&rsv_t=97cbjeYsNZhnSl8EbVkPYGpKbOsWP0U8eCEeKSIPs3sABXseGR7hyF0KXbZ8sQWyQamZ&rqlang=cn&rsv_enter=1&inputT=7641&rsv_sug3=34&rsv_sug1=35&rsv_sug7=101&rsv_sug2=0&rsv_sug4=7641",
                "https://www.baidu.com/s?ie=utf-8&f=3&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E5%B9%BF%E5%9C%BA%E8%88%9E%E8%A7%86%E9%A2%91&oq=%25E5%25B9%25BF%25E5%259C%25BA%25E8%2588%259E%25E8%25A7%2586%25E9%25A2%2591&rsv_pq=b57f8a080003fa9c&rsv_t=a809hqMvey5vvw2uM9P7H7dzEOTPql4rhnzVJo2XLxxwp39dk6ze5ni%2F9x4&rqlang=cn&rsv_enter=0&prefixsug=%25E5%25B9%25BF%25E5%259C%25BA%25E8%2588%259E%25E8%25A7%2586%25E9%25A2%2591&rsp=0&rsv_sug=1",
                "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E7%BE%8E%E5%A5%B3%E7%9B%B4%E6%92%AD&oq=%25E7%25BE%258E%25E5%25A5%25B3%25E7%259B%25B4%25E6%2592%25AD&rsv_pq=e30d249f0002a3db&rsv_t=63aa4TrQGuKEMdFN%2F8XlY%2Bbhj2aNRw0VFYcEiq2XEY97%2F0hws%2FNYCVdLeDo&rqlang=cn&rsv_enter=0"
                ]

v_domains = ["v.baidu.com"]
v_domains_lock = threading.RLock()


def not_in_array(urls, url):
    if len(urls) <= 0:
        return True
    for item in urls:
        if item == url:
            return False
    else:
        return True


class AHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.links = []
        self.url_next = u""

    def handle_starttag(self, tag, attrs):
        # print "Encountered the beginning of a %s tag" % tag
        if tag != "a":
            pass
        if len(attrs) <= 0:
            pass

        for (variable, value) in attrs:
            if value is None or variable is None:
                continue
            if variable == 'href':
                str_val = value
                if str_val is None or len(str_val) <= 0:
                    continue
                if False == not_in_array(urls=self.links, url=str_val):
                    continue

                # 百度存储跳转页面
                if "link?" in str_val:
                        self.links.append(str_val)
                else:  # 存储'next' 链接
                    if "rsv_page=1" in str_val:
                        self.url_next = u"https://www.baidu.com" + str_val


"""
else:  # 存储非百度域名链接
    if "http" not in str_val:
        continue
    if ".baidu" not in str_val or "v." in str_val:
        self.links.append(str_val)
"""


def parse_page_urls(htmldata):
    hp = AHTMLParser()
    hp.feed(htmldata)
    hp.close()
    return hp.url_next, hp.links


def search_by_baidu(root_url):
    # "open baidu url search for'视频'"
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, compress',
        'Accept-Language': 'en-us;q=0.5,en;q=0.3',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'
    }

    if root_url is None:
        assert False
        return "", []

    session = requests.session()
    session.headers = headers

    try:
        scon = session.get(root_url)
        htmldata = scon.text
    except IOError:
        print "Error opening "
        return "", []
    else:
        if htmldata is not None:
            return parse_page_urls(htmldata)

    return "", []


def redirect_url(url):
    try:
        urlcon = urllib.urlopen(url)
    except:
        return ""
    else:
        if "baidu" not in urlcon.url:
            return urlcon.url

    return ""


def write_config_file(domains):
    conf_hearder = "<?xml version=\"1.0\" encoding=\"utf-8\" ?>\n"\
                  "<configuration>\n<dnsList>\n"
    conf_tail = "</dnsList>\n</configuration>"

    with open("d://Dns.config", "w+") as f:
        f.writelines(conf_hearder)
        for domain in domains:
            f.write("<add domain=\"%s\" ip=\"127.0.0.1\"/>\n" % domain)
        f.writelines(conf_tail)


def do_jump_jugment(url):
    if "link?" in url:
        url = redirect_url(url)
    else:
        return

    if url is None or url == "":
        return
        # 分析域名,写入数组
    url_component = urlparse.urlsplit(url)
    if url_component is None:
        return
    v_domains_lock.acquire()
    try:
        if not_in_array(v_domains, url_component.hostname):
            v_domains.append(url_component.hostname)
    except:
            pass
    v_domains_lock.release()


def start_spider(begin_url,deep):
    """begin to start spider,using multi-thread tech"""

    global v_domains
    for i in range(deep):
        if begin_url is None or begin_url == "":
            break
        begin_url, urls = search_by_baidu(begin_url)

       # threads = []
        # 转换跳转链接
        if urls is not None:
            for url in urls:
                print("process:"+ url)
                do_jump_jugment(url)
                print("ok..")
                #sp = Thread(target=do_jump_jugment, args=[url, ])
                #threads.append(sp)
                #sp.start()
           #else:
                #for ps in threads:
                    #ps.join()


# 由一个url开始进行搜索,深度20
if __name__ == "__main__":
    """
    for root_url in g_baidu_urls:
        start_spider(root_url, 50)

    if len(v_domains) > 0:
        write_config_file(v_domains)
        print("ok,domain count:%d" % len(v_domains))
    else:
        print("Error, None domain!")

    
    processes = []
    for root_url in g_baidu_urls:
        sp = Process(target=start_spider, args=[root_url, 30])
        processes.append(sp)
        sp.start()

    for sp in processes:
        sp.join()

    if len(v_domains) > 0:
        write_config_file(v_domains)
        print("ok,domain count:%d" % len(v_domains))
    else:
        print("Error, None domain!")
        """
    processes = []
    for root_url in g_baidu_urls:
        sp = Thread(target=start_spider, args=[root_url, 50])
        processes.append(sp)
        sp.start()

    for sp in processes:
        sp.join()

    if len(v_domains) > 0:
        write_config_file(v_domains)
        print("ok,domain count:%d" % len(v_domains))
    else:
        print("Error, None domain!")