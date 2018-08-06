    install python
    install scrapy
    install mongodb
    install django
    install pymongo**
    install stunnel //not working
    install selenium


##scrapy
###***don't use scrapy for dynamicWebpages***
*   **scrapy selector type example**
   
   
    //h4[contains(@class,"product-title")]/span/text()     

##Selenium
read this installation 
http://selenium-python.readthedocs.io/installation.html#introduction
* **get driver from** 
https://github.com/mozilla/geckodriver/releases/tag/v0.21.0


    java -jar selenium-server-standalone-3.x.x.jar


##mongodb
    mongod --dbpath data/db 
    #start mongodb on your local directory
    mongo --host 127.0.0.1:27017

##django
    #run server
    python manage.py runserver 0.0.0.0:80

##pymongo
    
    import pymongo
    from pymongo import MongoClient
    #...
    #database connetion...  
    
##stunnel-not working
    conda install -c bkreider stunnel
    
in your Django directory:
    
    mkdir stunnel
    cd stunnel
    
create key

    openssl genrsa 1024 > stunnel.key
    
Create the certificate that uses this key

    openssl req -new -x509 -nodes -sha1 -days 365 -key stunnel.key > stunnel.cert   
    
Now combine these into a single file that stunnel will use for its SSL communication:

    cat stunnel.key stunnel.cert > stunnel.pem
    
Create config file

    pid=

    cert = stunnel/stunnel.pem
    sslVersion = SSLv3
    foreground = yes
    output = stunnel.log
    
    [https]
    accept=8443
    connect=8001
    TIMEOUTclose=1
    
in django directory

    stunnel stunnel/dev_https &
    python manage.py runserver&
    HTTPS=1 python manage.py runserver 8001
    