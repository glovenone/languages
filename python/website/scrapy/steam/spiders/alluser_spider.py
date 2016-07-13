# import scrapy
#
# from steam.items import AlluserItem
# import os
# import json
#
# class AlluserSpider(scrapy.Spider):
#     name = "alluser"
#     allowed_domains = ["alluser.org"]
#     f = file("all_user.json")
#     s = json.load(f)
#     user_ids = s.keys()
#
#     base_url = 'http://store.steampowered.com/app/'
#
#     start_urls = []
#     for i in user_ids:
#         start_url = base_url + str(i) + '/'
#         start_urls.append(start_url)
#         command = 'wget --header="Accept-Language:zh-CN,zh;q=0.8" -O /Users/glove/baidu_sync/work/cowlevel/steam/steam_data_cn2/'+str(i)+'.html '+start_url
#         os.system(command)
#     f.close
#
#     start_urls = [
#         # "http://steamspy.com/api.php?request=top100in2weeks"
#         #"http://steamspy.com/api.php?request=all"
#         'http://store.steampowered.com/app/431470/',
#         # 'http://store.steampowered.com/app/242320/'
#     ]
#     os.system('')
#     exit()
#
#
#
#     def parse(self, response):
#         print '---------------------'
#         test = response.xpath('//a[@class="highlight_screenshot_link"]/img').extract()
#         print test
#         # for sel in response.xpath('//ul/li'):
#         #     item = AlluserItem()
#         #     item['title'] = sel.xpath('a/text()').extract()
#         #     item['link'] = sel.xpath('a/@href').extract()
#         #     item['desc'] = sel.xpath('text()').extract()
#         #     yield item
#         print '====================='
#
#
# # scrapy crawl alluser -o items.json
