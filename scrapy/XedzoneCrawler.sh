#!/usr/bin/env bash
ls -l
scrapy crawl orumcuk -a link=$1 -a lmt=$2
