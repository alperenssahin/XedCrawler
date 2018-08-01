
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from pymongo import MongoClient
from bson.objectid import ObjectId

import subprocess
import os
# Create your views here.
def index(request):

    template = loader.get_template('box/index.html')
    context = {
        'question':list,
    }
    return HttpResponse(template.render(context, request))

def runCrawl(request):
    template = loader.get_template('box/index.html')
    # ctx = subprocess.check_output(.split(" "))
    context = {
        'con': 1,
        'link':request.POST['link'],
        'limit':request.POST['limit'],
        'output': 0,
    }
    # call scrapy ...
    tmpdir = os.getcwd()
    # print(tmpdir)
    os.chdir('scrapy/')
    # print(os.getcwd())
    out = context['link'].split("/")[-1]
    context['output'] = 'gg_%s.txt' % out
    subprocess.call(['bash','XedzoneCrawler.sh',context['link'],context['limit']])
    subprocess.call(['mv', context['output'] , '%s/static/' % tmpdir])
    os.chdir(tmpdir)
    # subprocess.check_output(['cd','scrapy/'])
    # print(subprocess.call(['ls','-l']))
    return HttpResponse(template.render(context, request))


def master(request):
    template = loader.get_template('box/tmpResponse.html')
    # ctx = subprocess.check_output(.split(" "))


    context = {
    }

    return HttpResponse(template.render(context, request))

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from bson.json_util import dumps
@csrf_exempt
def xedExtension(request):
    #Setup
    client = MongoClient()
    db = client.reference
    col = db.tmp
    items = col.find({},{"category.title":1})
    items = dumps(items)
    return  JsonResponse(items,safe=False)