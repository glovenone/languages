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




        #--------- 类型、开发商、发行商、发行日期 ------------
        # detail = response.xpath('//div[@class="details_block"][1]//text()').extract()
        detail_ori = response.xpath('//div[@class="details_block"][1]//text()').extract()
        detail = []
        type_decode = '类型:'.decode('utf-8')
        type_key = 'type'
        title_decode = '名称:'.decode('utf-8')
        title_key = 'title'
        developer_decode = '开发商:'.decode('utf-8')
        developer_key = 'developer'
        publisher_decode = '发行商:'.decode('utf-8')
        publisher_key = 'publisher'
        publish_date_decode = '发行日期:'.decode('utf-8')
        publish_date_key = 'publish_time'
        detail_decode_list = {type_decode:type_key, title_decode:title_key, developer_decode:developer_key, publisher_decode:publisher_key, publish_date_decode:publish_date_key}

        detail_key = ''
        for detail_val in detail_ori:
            if(detail_val in detail_decode_list) :
                detail_key = detail_decode_list[detail_val]
                item[detail_key] = ''
            elif(detail_key != ''):
                item[detail_key] = item[detail_key] + detail_val
                # if(is_mul == 1) :
                #     item[detail_key] = item[detail_key] + detail_val
                # else:
                #     item[detail_key] = detail_val


        #--------- title -------------
        # item['title'] = response.xpath('//div[@class="apphub_AppName"]//text()').extract()


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
        # print item

        # yield item
        print '====================='

# scrapy crawl dmoz -o items.json
