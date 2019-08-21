import urllib.request
import time
import lxml.html
import csv
import os
import random
import sys

def readPages(url, filename):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    request = urllib.request.Request(url,headers={'User-Agent': user_agent})
    response = urllib.request.urlopen(request)
    html = response.read().decode(response.headers.get_content_charset())

    with open(filename, "w") as outfile:
        outfile.write(html)

directories = ["Singapore-pages", "Asia-pages", "World-pages", "Business-pages", "Sport-pages"]
for directory in directories:
    articleNumber = 0
    for filename in os.listdir(directory):
        cat = directory.replace("-pages", "")
        if filename.endswith(".html"): 
            print("in folder {0} reading {1} ...".format(directory, filename))
            with open(directory+"/" + filename, 'r') as infile:
                page = lxml.html.fromstring(infile.read())
            for j in range(1, 11):
                try:
                    articleNumber += 1
                    print("reading article {0} ... ".format(articleNumber))
                    teaser = page.xpath('//ol[@class="result-section__list"]/li[{0}]/div/div/div/div[1]/a/text()'.format(j))[0]
                    title = page.xpath('//ol[@class="result-section__list"]/li[{0}]/div/div/div/h3/a/text()'.format(j))[0]
                    link = page.xpath('//ol[@class="result-section__list"]/li[{0}]/div/div/div/h3/a/@href'.format(j))[0]

                    url = "https://www.channelnewsasia.com" + link
                    articleHtmlName = "{0}-articles/articles{1}.html".format(cat, articleNumber)
                    with open("{0}-articles.csv".format(cat), "a") as artiCsv:
                        writer = csv.writer(artiCsv, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
                        writer.writerow([teaser, title, url, articleHtmlName])
                
                    readPages(url, articleHtmlName)
                except:
                    print("Unexpected error:", sys.exc_info()[0])
                sleepRand = random.uniform(0.8, 2)
                print("sleeping for {0}".format(sleepRand))
                time.sleep(sleepRand)
