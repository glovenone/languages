#-*- coding: UTF-8 -*-

import scrapy

from steam.items import SteamItem


class AnalysisSpider(scrapy.Spider):
    name = "analysis"
    allowed_domains = ["analysis.org"]
    start_urls = [
        "file:///Users/glove/workspace/git/languages/python/website/scrapy/481870.html",
    ]

    def parse(self, response):
        print '---------------------'
        item = SteamItem()


        #--------- title -------------
        # item['title'] = response.xpath('//div[@class="apphub_AppName"]//text()').extract()


        #--------- 类型、开发商、发行商、发行日期 ------------
        # detail = response.xpath('//div[@class="details_block"][1]//text()').extract()
        # item['detail'] = detail

        #--------- desc -------------
        # item['desc_short'] = response.xpath('//div[@class="game_description_snippet"]/text()').extract()
        # item['desc_long'] = response.xpath('//div[@class="game_area_description"]//text()').extract()

        # about detail
        #http://www.zhihu.com/question/38080188


        # item['link'] = sel.xpath('a/@href').extract()
        # item['desc'] = sel.xpath('text()').extract()

        for i in item:
            print i
            print item[i]
        print item

        # yield item
        print '====================='

# scrapy crawl dmoz -o items.json
