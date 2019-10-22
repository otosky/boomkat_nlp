# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from music_review_scraper.items import boomkat
from pymongo import MongoClient
import pickle

client = MongoClient('mongodb://localhost:27017')
db = client['musicReviews']


class BoomkatbotSpider(scrapy.Spider):
    name = 'boomkatbot'
    allowed_domains = ['boomkat.com']
    
    # number of pages as of 10/20/19 in the techno/house section (100 releases per page)
    page_list = [i for i in range(1,867)]
    start_urls = [f'https://boomkat.com/t/genre/techno-slash-house?page={i}&per_page=100' for i in page_list]

    collection_name = 'boomkat'

    def parse(self, response):
        # parse the page of releases to get individual release URLs
        releases = response.xpath('//li[@class="product_item"]')
        for release in releases:
            relative_url = release.xpath('.//a/@href').extract_first()
            absolute_url = ''.join(['https://boomkat.com', relative_url])
            yield Request(absolute_url, callback=self.parse_release, meta={'URL': absolute_url})

    def parse_release(self, response):
        # parse individual release page and extract details
        item = boomkat()

        item['url'] = response.meta.get('URL')
        item['artist'] = response.xpath('//h1[@class="detail--artists"]/a//text()').extract()
        item['title'] = response.xpath('//h2[@class="detail_album"]//text()').extract_first()
        try:
            item['cat_no'] = response.xpath('//span[contains(., "Cat No: ")]/text()').extract_first().replace('Cat No: ','')
        except:
            item['cat_no'] = None
        item['img_link'] = response.xpath('//div[@class="variant-image-wrapper hidden"]//img/@src').extract()[0]

        item['release_date'] = response.xpath('//@data-release-date').extract_first()
        item['label'] = response.xpath('//span[contains(., "Label")]//text()').extract()[1]
        item['genre_style'] = response.xpath('//span[text()= "Genre: "]/a//text()').extract_first()
        # 'body' is akin to a product description - they have humorously vivid ones at boomkat
        body = response.xpath('//div[@class="product-review"]//p//text()').extract()
        # note there are actually multiple instances of 'product-review' for a release(mp3, flac, wav, etc.)
        # will have to figure out how to fix this
        # could maybe do a loop through each extract until it hits a repeat...
        item['body'] = ''.join(body)

        yield item
