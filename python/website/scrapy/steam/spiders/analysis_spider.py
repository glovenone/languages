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

        # #title, publish_time
        # detail_ori = response.xpath('//div[@class="details_block"]/text()').extract()
        # detail = []
        # for detail_item in detail_ori:
        #     has_r = detail_item.find('\r')
        #     has_n = detail_item.find('\n')
        #     has_t = detail_item.find('\t')
        #     if has_r == -1 and has_n==-1 and has_t==-1 and detail_item.strip() != "":
        #        detail.append(detail_item)
        # item['title'] = detail[0]
        # item['publish_time'] = detail[1]

        # #type, developer, publisher
        # detail2 = []
        # detail2_ori = response.xpath('//div[@class="details_block"][1]/a/text()').extract()
        # for detail_item in detail2_ori:
        #     detail2.append(detail_item)
        # item['type'] = detail2[0]
        # item['developer'] = detail2[1]
        # item['publisher'] = detail2[2]

        # item['desc_short'] = response.xpath('//div[@class="game_description_snippet"]/text()').extract()

        # about detail
        #http://www.zhihu.com/question/38080188

        item['desc_long'] = response.xpath('//div[@id="game_area_description"]').extract()
        for fu in item['desc_long']:
            print fu

        # item['link'] = sel.xpath('a/@href').extract()
        # item['desc'] = sel.xpath('text()').extract()
        print item
        # yield item
        print '====================='

# scrapy crawl dmoz -o items.json
