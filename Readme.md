    install python
    install scrapy
    install mongodb
    install django
    install pymongo**
    install selenium


## scrapy
### ***don't use scrapy for dynamicWebpages***
*   **scrapy selector type example**
   
   
    //h4[contains(@class,"product-title")]/span/text()     

## Selenium
read this installation 
http://selenium-python.readthedocs.io/installation.html#introduction
* **get driver from** 
https://github.com/mozilla/geckodriver/releases/tag/v0.21.0


    java -jar selenium-server-standalone-3.x.x.jar


## mongodb
    mongod --dbpath data/db 
    #start mongodb on your local directory
    mongo --host 127.0.0.1:27017

## django
    #run server
    python manage.py runserver 0.0.0.0:80

## pymongo
    
    import pymongo
    from pymongo import MongoClient
    #...
    #database connetion...  
    
