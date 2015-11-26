SPIDER_SETTINGS = [
    {
        'endpoint': 'cg-spider',
        'location': 'spiders.CraigslistSpider',
        'spider': 'CraigslistSpider',
        'scrapy_settings': {
            'TELNETCONSOLE_PORT': 44500
        }
    },
    {
        'endpoint': 'dmoz',
        'location': 'spiders.DmozSpider',
        'spider': 'DmozSpider'    
    }
]

LOGS = True

EXPORT_JSON = True
EXPORT_CSV = True

SCRAPY_SETTINGS = {
    'TELNETCONSOLE_PORT': 12345
}
