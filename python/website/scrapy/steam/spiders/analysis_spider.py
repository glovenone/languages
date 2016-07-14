# -*- coding: UTF-8 -*-

import scrapy
import json

from steam.items import SteamItem

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# import MySQLdb

class AnalysisSpider(scrapy.Spider):
    name = "analysis"
    allowed_domains = ["analysis.org"]

    # f = file("part_user.json")
    f = file("all_user.json")
    s = json.load(f)
    user_ids = s.keys()
    base_url = 'file:///Users/glove/Documents/steam_data_cn3/'

    start_urls = []
    for i in user_ids:
        start_url = base_url + str(i) + '.html'
        start_urls.append(start_url)

    # start_urls = [
    #     "file:///Users/glove/workspace/git/languages/python/website/scrapy/481870.html",
    # ]

    def parse(self, response):
        print '---------------------'
        item = SteamItem()

        appid = response.xpath('//@data-appid').extract_first()


        # --------- desc -------------
        desc_short_arr =  response.xpath('//div[@class="game_description_snippet"]/text()').extract()
        item['desc_short'] = ''
        for i in desc_short_arr:
            item['desc_short'] = item['desc_short'] + '-----'+ i

        desc_long_arr = response.xpath('//div[@class="game_area_description"]//text()').extract()
        item['desc_long'] = ''
        for i in desc_long_arr:
            item['desc_long'] = item['desc_long'] + i


    # --------- 类型、开发商、发行商、发行日期 ------------
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
        detail_decode_list = {type_decode: type_key, title_decode: title_key, developer_decode: developer_key,
                              publisher_decode: publisher_key, publish_date_decode: publish_date_key}

        detail_key = ''
        for detail_val in detail_ori:
            if (detail_val in detail_decode_list):
                detail_key = detail_decode_list[detail_val]
                item[detail_key] = ''
            elif (detail_key != ''):
                item[detail_key] = item[detail_key] + detail_val
                # if(is_mul == 1) :
                #     item[detail_key] = item[detail_key] + detail_val
                # else:
                #     item[detail_key] = detail_val

        pics = response.xpath('//div[@class="highlight_strip_item highlight_strip_screenshot"]/img/@src').extract()
        item['pic'] = ''
        for i in pics:
            item['pic'] = item['pic'] + i.replace('.116x65', '') + ','

        # --------- title -------------
        # item['title'] = response.xpath('//div[@class="apphub_AppName"]//text()').extract()

        # about detail
        # http://www.zhihu.com/question/38080188

        dict = 'analysis'
        file_name = dict + '/' + appid
        handle = open(file_name, 'a')

        print item
        for i in item:
            # item[i] = item[i].replace('\t', '')
            item[i] = item[i].replace('\r', '')
            item[i] = item[i].replace('\n', '')
            handle.write(i)
            handle.write('\t')
            handle.write(item[i])
            handle.write("\n")
        handle.close()


        # print item

        # yield item
        print '====================='

# scrapy crawlanalysis  -o items.json
