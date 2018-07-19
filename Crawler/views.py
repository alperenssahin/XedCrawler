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
    # call spider ...
    tmpdir = os.getcwd()
    # print(tmpdir)
    os.chdir('spider/')
    # print(os.getcwd())
    out = context['link'].split("/")[-1]
    context['output'] = 'gg_%s.txt' % out
    subprocess.call(['bash','XedzoneCrawler.sh',context['link'],context['limit']])
    subprocess.call(['mv', context['output'] , '%s/static/' % tmpdir])
    os.chdir(tmpdir)
    # subprocess.check_output(['cd','spider/'])
    # print(subprocess.call(['ls','-l']))
    return HttpResponse(template.render(context, request))

