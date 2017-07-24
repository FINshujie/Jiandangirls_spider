# -*- coding: utf-8 -*-
import scrapy
import urllib.parse
from scrapy.http import Request
from Jiandan.items import JiandanPhotoItem,JiandanItem


class JiandanSpiderSpider(scrapy.Spider):
    name = 'Jiandan_spider'
    allowed_domains = ['jandan.net']
    start_urls = ['http://jandan.net/ooxx/']

    def parse(self, response):
        Image_Item = JiandanPhotoItem()
        img_urls = response.xpath('//p/a[@class ="view_img_link"]')
        for img_url in img_urls:
            img_url_mid= img_url.xpath("@href").extract_first("")
            img_url_join =urllib.parse.urljoin(response.url, img_url_mid)
            Image_Item['img_url'] = [img_url_join]
            yield Image_Item



        next_url =  response.xpath('//a[@title="Older Comments"]/@href').extract_first('')

        if next_url:
            yield Request(url=next_url,callback=self.parse)



    def parse_detail(self,response):
        pass
