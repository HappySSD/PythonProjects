import json


class MoviePipeline(object):
    def __init__(self):
        self.filename = open("movie.json", "wb")

    def process_item(self, item, spider):
        jsontext = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        self.filename.write(jsontext.encode("utf-8"))
        return item

    def close_spider(self, spider):
        self.filename.close()
