from django.shortcuts import render
from .models import Results, DeleteWhileSaving
from .forms import SaveUrlForm
from django.http import HttpResponseRedirect
from spider_seo.spiders.starting_crawler import crawl, transfer_url, Urls
from _datetime import datetime, timedelta
import csv


# Create your views here.

def result_view(request):
    title = Results.objects.values_list('url', 'title')
    keywords = Results.objects.values_list('url', 'keywords')
    description = Results.objects.values_list('url', 'description')
    h1 = Results.objects.values_list('url', 'h1')
    h2 = Results.objects.values_list('url', 'h2')
    broken_links = Results.objects.values_list('url', 'broken_link')
    link = Results.objects.values_list('url')
    context = {
        'title': title,
        'keywords': keywords,
        'description': description,
        'broken_links': broken_links,
        'link': link,
        'h1': h1,
        'h2': h2,

    }
    return render(request, 'parser_app/results.html', context)


def send_form(request):
    if request.method == "POST":
        url = request.POST['url']
        date_today = datetime.today()

        date_adds = date_today - timedelta(days=1)
        short_url = str(url).replace("http://", "").replace("https://", "").replace("/", "")
        short = short_url.split("/")
        dates = [date_today, date_adds]
        Results.objects.exclude(date_add__in=dates).delete()
        Results.objects.filter(base_url=short[0]).delete()
        crawl(url, short_url)

        transfer_url(url, short_url)
        return HttpResponseRedirect('/result/')

    else:
        form = SaveUrlForm()
        return render(request, 'parser_app/index.html', {
            'form': form
        })
