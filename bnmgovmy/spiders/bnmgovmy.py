import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst
from datetime import datetime
from bnmgovmy.items import Article


class bnmgovmySpider(scrapy.Spider):
    name = 'bnmgovmy'
    start_urls = ['https://www.bnm.gov.my/press-release-1996']
    page = 1996

    def parse(self, response):
        links = response.xpath('//td/p/a/@href').getall()
        if links:
            yield from response.follow_all(links, self.parse_article)

            self.page += 1

            next_page = f'https://www.bnm.gov.my/press-release-{self.page}'
            yield response.follow(next_page, self.parse)

    def parse_article(self, response):
        if 'pdf' in response.url.lower():
            return

        item = ItemLoader(Article())
        item.default_output_processor = TakeFirst()

        title = response.xpath('//div[@class="article-header"]/h1/text()').get()
        if title:
            title = title.strip()

        date = response.xpath('//div[@class="article-header"]//span[@class="text-small text-muted"]/text()').get()
        if date:
            date = " ".join(date.split())

        content = response.xpath('//div[@class="article-content-cs"][2]//text()').getall()
        content = [text.strip() for text in content if text.strip() and '{' not in text]
        content = " ".join(content).strip()

        item.add_value('title', title)
        item.add_value('date', date)
        item.add_value('link', response.url)
        item.add_value('content', content)

        return item.load_item()
