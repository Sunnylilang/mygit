from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from showApp.models import Positions


def showMain(request):
    return render(request,'main.html')


def showIntroduce(request):
    return render(request,'introduce.html')


def showData(request):
    city = request.GET.get("city")
    position = request.GET.get("position")
    num = request.GET.get("num")
    positions = Positions.objects.filter(area__contains=city,position__contains=position)
    count = len(positions)
    if num:
        num = num
    else:
        num = 1
    pagtor = Paginator(positions,per_page=30)
    # 获取页面总数
    num_pages = pagtor.num_pages
    # 获取某一页的对象
    page = pagtor.page(num)
    return render(request,'menu.html',{
        "positions":positions,
        "num_pages":num_pages,
        "num":num,
        "page":page,
        "count":count,
        "city":city,
        "position":position
    })


def keywordQuery(request):
    position = request.POST.get('position')
    positions = Positions.objects.filter(position__contains=position)
    return render(request,"menu.html",{
        "positions": positions
    })


def brokenLine(request):
    web = Positions.objects.filter(area__contains="北京",position__contains="Python")
    crawl = Positions.objects.filter(area__contains="北京", position__contains="爬虫")
    hadoop = Positions.objects.filter(area__contains="北京", position__contains="大数据")
    ai = Positions.objects.filter(area__contains="北京", position__contains="AI")
    data=[len(web),len(crawl),len(hadoop),len(ai)]
    return JsonResponse(data,safe=False)


def showBrokenline(request):
    return render(request,"brokenLine.html")