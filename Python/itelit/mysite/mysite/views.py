from django.http import HttpResponse, Http404
import datetime


def hello(request):
    return HttpResponse("Hello world")


def time(request):
    now = datetime.datetime.now()
    html = "<html><body><h1>Зараз: %s.<h1></body></html>" % now
    return HttpResponse(html)


def time_plus(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()

    dt = datetime.datetime.now()+datetime.timedelta(hours=offset)
    html = "<html><body><h1>Через: %s год. буде %s.<h1></body></html>" % (offset, dt)
    return HttpResponse(html)


