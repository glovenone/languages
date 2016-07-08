import scrapy

from steam.items import AlluserItem
import json

class AlluserSpider(scrapy.Spider):
    name = "alluser"
    allowed_domains = ["alluser.org"]
    f = file("part_user.json")
    s = json.load(f)
    user_ids = s.keys()

    base_url = 'http://store.steampowered.com/app/'

    start_urls = []
    for i in user_ids:
        start_urls.append(base_url + str(i) + '/')

    f.close
    print start_urls
    start_urls = [
        # "http://steamspy.com/api.php?request=top100in2weeks"
        #"http://steamspy.com/api.php?request=all"
        'http://store.steampowered.com/app/431470/',
        'http://store.steampowered.com/app/242320/'
    ]



    def parse(self, response):
        print '---------------------'
        print response.xpath('//a')
        for sel in response.xpath('//ul/li'):
            item = AlluserItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['desc'] = sel.xpath('text()').extract()
            yield item
        print '====================='


# scrapy crawl alluser -o items.json
