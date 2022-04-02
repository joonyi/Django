from app.models import *
from django.shortcuts import render,redirect
from django.http  import HttpResponse
import feedparser

# Create your views here.
def updatepython(request):
    #-------python----------------
    # url = feedparser.parse(
    #         "https://medium.com/feed/tag/python"
    #     )
    # for i in range(len(url.entries)):
    #     info = url.entries[i]
    #     content= PyContent()
    #     content.headline= info.title
    #     #-----finding image link
    #     desc = info.description
    #     start=desc.find("img src=")
    #     end=desc.find("width")

    #     print(desc[end:])
    #     desc=desc[start+9:end-2:]
    #     print("-----------------------------")
    #     print(desc)

    #     #---------------
    #     content.img = desc
    #     content.url  = info.link
    #     content.save()

    return redirect('/')


def updatecovid(request):
    #-------python----------------
    url = feedparser.parse("https://medium.com/feed/tag/covid")

    for i in range(len(url.entries)):
        info = url.entries[i]
        content= CovidContent()
        content.headline= info.title
        print("################################")
        print(content.headline)
        #-----finding image link
        desc = info.description
        start=desc.find("img src=")
        end=desc.find("width")

        print(desc[end:])
        desc=desc[start+9:end-2:]
        print("-----------------------------")
        print(desc)

        #---------------
        content.img = desc
        content.url  = info.link
        content.pubDate = info.published
        content.save()

    return redirect('/')


def updateGoogleNews(request):
    url = feedparser.parse("https://news.google.com/rss/topics/CAAqIggKIhxDQkFTRHdvSkwyMHZNREZqY0hsNUVnSmxiaWdBUAE?hl=en-MY&gl=MY&ceid=MY%3Aen")

    for i in range(len(url.entries)):
        info = url.entries[i]
        content = CovidGoogleNewsContent()
        content.headline= info.title
        print("################################")
        print(content.headline)
        content.url  = info.link
        content.pubDate = info.published
        content.save()

    return redirect('/')


def updateMalaysiakini(request):
    url = feedparser.parse("https://www.malaysiakini.com/rss/my/news.rss")

    for i in range(len(url.entries)):
        info = url.entries[i]
        if "Covid" in info.title:
            content = CovidMalaysiakiniContent()
            content.headline = info.title
            print("################################")
            print(content.headline)
            content.url  = info.link
            content.pubDate = info.published
            content.save()

    return redirect('/')


def updateprog(request):
    #-------python----------------
    # url = feedparser.parse(
    #         "https://medium.com/feed/tag/programming"
    #     )
    # for i in range(len(url.entries)):
    #     info = url.entries[i]
    #     content= ProgContent()
    #     content.headline= info.title
    #     #-----finding image link
    #     desc = info.description
    #     start=desc.find("img src=")
    #     end=desc.find("width")
    #
    #     print(desc[end:])
    #     desc=desc[start+9:end-2:]
    #     print("-----------------------------")
    #     print(desc)
    #
    #     #---------------
    #     content.img = desc
    #     content.url  = info.link
    #     content.save()

    return redirect('/')


def home(request):
    pycontent = PyContent.objects.all()
    progcontent = ProgContent.objects.all()
    covidcontent = CovidContent.objects.all()
    covidgooglenewscontent = CovidGoogleNewsContent.objects.all()
    covidmalaysiakinicontent = CovidMalaysiakiniContent.objects.all()

    context = {
        'pycontent': pycontent,
        'progcontent': progcontent,
        'covidcontent': covidcontent,
        'covidgooglenewscontent': covidgooglenewscontent,
        'covidmalaysiakinicontent': covidmalaysiakinicontent,
    }
    return render(request,'app/home.html',context)
