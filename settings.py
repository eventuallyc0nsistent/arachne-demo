SPIDER_SETTINGS = [
    {
        'endpoint': 'cg-spider',
        'location': 'spiders.CraigslistSpider',
        'spider': 'CraigslistSpider',
    },
    {
        'endpoint': 'dmoz',
        'location': 'spiders.DmozSpider',
        'spider': 'DmozSpider',
        'scrapy_settings':  {
            'ITEM_PIPELINES': {
                'pipelines.AddTablePipeline': 500
            }
        }       
    }
]

LOGS = True

EXPORT_JSON = True
EXPORT_CSV = True
