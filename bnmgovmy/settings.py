BOT_NAME = 'bnmgovmy'
SPIDER_MODULES = ['bnmgovmy.spiders']
NEWSPIDER_MODULE = 'bnmgovmy.spiders'
USER_AGENT = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0',
ITEM_PIPELINES = {
    'bnmgovmy.pipelines.DatabasePipeline': 300,
}
FEED_EXPORT_ENCODING = 'utf-8'

LOG_LEVEL = 'WARNING'

# LOG_LEVEL = 'DEBUG'
