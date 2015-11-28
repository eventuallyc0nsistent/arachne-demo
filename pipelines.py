from models import AllData, db

class AddTablePipeline(object):

    def process_item(self, item, spider):

        # create a new SQL Alchemy object and add to the db session
        record = AllData(title=item['title'][0].decode('unicode_escape'),
                         url=item['url'][0],
                         desc=item['desc'])
        db.add(record)
        db.commit()
        return item
