# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline

class JiandanPipeline(object):
    def process_item(self, item, spider):
        return item

class JiandanImagePathPipeline(ImagesPipeline):
    def item_completed(self, results, item, info):
        if "img_url" in item:
            for ok, value in results:
                image_file_path = value['path']
                item['image_path'] = image_file_path
            return item