import scrapy

class Myspider(scrapy.Spider):
	name="price_spider"

	def start_requests(self):

		urls=[
			"http://books.toscrape.com/",
		]

		for url in urls:
			yield scrapy.Request(url=url,callback=self.parse)

	def parse(self,response):
		
		quotes=response.css("article.product_pod")

		for quote in quotes:
				title=quote.css(".product_pod h3 a::text").get()
				price=quote.css(".product_pod .product_price p::text").get()
				

				yield {
				"title":title,
				"price":price,
				
				}

				next_page_id=response.css("li.next a::attr(href)").get()

				if next_page_id is not None:
					next_page=response.urljoin(next_page_id)
					yield scrapy.Request(next_page,callback=self.parse)



