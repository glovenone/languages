import scrapy

from steam.items import AlluserItem

class AlluserSpider(scrapy.Spider):
    name = "alluser"
    allowed_domains = ["alluser.org"]
    start_urls = [
        "http://store.steampowered.com/app/338390/"
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
