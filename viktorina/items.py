# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class ViktorinaItem(Item):
    # define the fields for your item here like:
    question = Field()
    answer = Field()

class URLItem(Item):
    url = Field()
    data = Field()
