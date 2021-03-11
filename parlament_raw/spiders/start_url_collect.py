import scrapy
from ..items import MyItem

class UrlCollect(scrapy.Spider):
    name = 'collect'
    start_urls = ['https://www.parliament.bg/bg/MP']
    base_url = 'https://www.parliament.bg'


    def parse(self, response):
        for people in response.css('div.MPinfo'):
            url_parse = people.css('a').attrib['href']
            url = f"{self.base_url}{url_parse}"
            yield scrapy.Request(url, callback=self.parse_attr)

    def parse_attr(self, response):
        item = MyItem()

        date_birth = ''
        place_birth = ''
        job = ''
        language = ''
        politic = ''
        email = ''

        product_data = response.css('div.MPinfo li')
        for data in product_data:
            if "Дата на раждане" in data.css('li::text').get():
                split_str = data.css('li::text').get().split(' ')
                date_birth = split_str[4]
                place_birth = ' '.join(str(e) for e in split_str[5:])
                if place_birth == ', ':
                    place_birth = ''

            elif "Професия" in data.css('li::text').get():
                split_str = data.css('li::text').get().split(' ')
                job = ' '.join(str(e) for e in split_str[1:]).rstrip(';').replace(';', ',')

            elif "Езици" in data.css('li::text').get():
                split_str = data.css('li::text').get().split(' ')
                language = ''.join(str(e) for e in split_str[1:]).rstrip(';').replace(';', ',')

            elif "Избран(а) с политическа сила" in data.css('li::text').get():
                split_str = data.css('li::text').get().split(' ')
                politic = ' '.join(str(e) for e in split_str[4:-1])

            elif "E-mail" in data.css('li::text').get():
                email = data.css('li').css('a::text').get()

        pic = response.css('div.MPBlock_columns2').css('img').attrib['src']

        item['Name'] = response.css('div.MPBlock_columns2').css('img').attrib['alt']
        item['Date_of_Birth'] = date_birth
        item['Place_of_Birth'] = place_birth
        item['Job'] = job
        item['Language'] = language
        item['Politic'] = politic
        item['Email'] = email
        item['Picture_URL'] = f"{self.base_url}{pic}"

        yield item










