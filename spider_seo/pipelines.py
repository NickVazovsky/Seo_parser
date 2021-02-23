# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from parser_app.models import Results, DeleteWhileSaving
from spider_seo.check_seo import Check
import datetime


class SpiderSeoPipeline:
    def process_item(self, item, spider):
        date_add = datetime.date.today()

        title = item['title']

        if item['keywords'] is not None:
            keywords = item['keywords']

        else:
            keywords = 'Ошибок нет'

        if item['description'] is not None:
            descriptions = item['description']

        else:
            descriptions = 'Ошибок нет'

        if item['h1'] is not None:
            h1 = item['h1']

        else:
            h1 = 'Ошибок нет'


        if item['h2'] is not None:
            h2 = item['h2']

        else:
            h2 = 'Ошибок нет'
        broken_link = item['broken_link']
        base_url = item['base_url']
        title_unique = item['title_unique']

        desc_unique = item['description_unique']
        if item['google'] is not None:
            google = item['google']

        else:
            google = 'Ошибок нет'
        if item['yandex'] is not None:
            yandex = item['yandex']

        else:
            yandex = 'Ошибок нет'

        vk = item['vk']
        facebook = item['facebook']
        instagram = item['instagram']
        # results = Results(base_url=base_url, title=title, url=item['link'], keywords=keywords,
        #                    description=descriptions,
        #                    h1=h1, h2=h2,google=google,yandex=yandex,date_add=date_add)
        # base_url = models.CharField(max_length=256, default=True)
        # url = models.CharField(max_length=255, default=True)
        # title = models.CharField(max_length=255, default=True)
        # description = models.CharField(max_length=255, default=True)
        # title_unique = models.CharField(max_length=255, default=True)
        # description_unique = models.CharField(max_length=255, default=True)
        # keywords = models.CharField(max_length=255, default=True)
        # h1 = models.CharField(max_length=255, blank=True, default=True)
        # h2 = models.CharField(max_length=255, blank=True, default=True)
        # broken_link = models.CharField(max_length=255, default=True)
        # date_add = models.DateTimeField(auto_now_add=True)
        results = Results(base_url=base_url, url=item['link'], title=title, description=descriptions,
                          title_unique=title_unique, description_unique=desc_unique,
                          keywords=keywords, h1=h1, h2=h2, broken_link=broken_link, google= google, yandex=yandex,
                          vk=vk, instagram=instagram, facebook=facebook)
        results.save()
        deletes = DeleteWhileSaving(title='title', keyrwords='kword', description='desc')
        deletes.save()

        return item
