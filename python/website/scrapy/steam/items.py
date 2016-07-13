# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SteamItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    detail = scrapy.Field()
    # publish_time = scrapy.Field()
    # type = scrapy.Field()
    # developer = scrapy.Field()
    # publisher = scrapy.Field()
    desc_short = scrapy.Field()
    desc_long = scrapy.Field()
    pass


class DmozItem(scrapy.Item):
    title = scrapy.Field()
    desc = scrapy.Field()
    link = scrapy.Field()


class AlluserItem(scrapy.Item):
    title = scrapy.Field()
    desc = scrapy.Field()
    link = scrapy.Field()
