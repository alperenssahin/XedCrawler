from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
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
    template = loader.get_template('box/master.html')
    # ctx = subprocess.check_output(.split(" "))
    f = open('scrapy/tmpResponse.html','r')

    context = {
        'data':f.read()
    }

    f.close()
    return HttpResponse(template.render(context, request))
