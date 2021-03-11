import sqlite3
import json
import codecs


class JsonPipeline(object):
    def open_spider(self, spider):
        self.file = codecs.open('scraped_items.json', 'w', encoding='utf-8')
        self.file.write("[")

    def close_spider(self, spider):
        self.file.write("]")
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(
            dict(item),
            indent=4,
            sort_keys=True,
            ensure_ascii=False,
            separators=(',', ': ')
        ) + ",\n"
        self.file.write(line)
        return item

class SqlitePipeline(object):
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect("mydata.db")
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS politic_tb""")
        self.curr.execute("""create table politic_tb(
                Name text,
                Date_of_Birth text,
                Place_of_Birth text,
                Job text,
                Language text,
                Politic text,
                Email text,
                Picture_URL text
                )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute("""insert into politic_tb values(?,?,?,?,?,?,?,?)""", (
        item['Name'],
        item['Date_of_Birth'],
        item['Place_of_Birth'],
        item['Job'],
        item['Language'],
        item['Politic'],
        item['Email'],
        item['Picture_URL']
        ))
        self.conn.commit()
