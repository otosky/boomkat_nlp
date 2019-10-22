# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class pitchfork(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    artist = scrapy.Field()
    title = scrapy.Field()
    label = scrapy.Field()
    release_year = scrapy.Field()
    rating = scrapy.Field()
    author = scrapy.Field()
    author_title = scrapy.Field()
    genre_style = scrapy.Field()
    publish_date = scrapy.Field()
    body = scrapy.Field()

class boomkat(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    url = scrapy.Field()
    artist = scrapy.Field()
    title = scrapy.Field()
    label = scrapy.Field()
    release_date = scrapy.Field()
    cat_no = scrapy.Field()
    genre_style = scrapy.Field()
    body = scrapy.Field()
    img_link = scrapy.Field()
