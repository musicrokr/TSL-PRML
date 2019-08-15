import urllib.request
import time
import lxml.html
import csv
import random

def readPages(url, filename):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    request = urllib.request.Request(url,headers={'User-Agent': user_agent})
    response = urllib.request.urlopen(request)
    html = response.read().decode(response.headers.get_content_charset())

    with open(filename, "w") as outfile:
        outfile.write(html)

for i in range(0, 101):
    pageFile = "pages/page{0}.html".format(i)
    print("reading {0} ...".format(pageFile))
    with open(pageFile, 'r') as infile:
        page = lxml.html.fromstring(infile.read())
    for j in range(1, 11):
        articleNumber = i * 10 + j
        print("reading article {0} ... ".format(articleNumber))
        teaser = page.xpath('//*[@id="section-content-8396078"]/div[2]/ol/li[{0}]/div/div/div/div[1]/a/text()'.format(j))[0]
        title = page.xpath('//*[@id="section-content-8396078"]/div[2]/ol/li[{0}]/div/div/div/h3/a/text()'.format(j))[0]
        link = page.xpath('//*[@id="section-content-8396078"]/div[2]/ol/li[{0}]/div/div/div/h3/a/@href'.format(j))[0]

        url = "https://www.channelnewsasia.com" + link
        articleHtmlName = "articles/articles{0}{1}.html".format(i,j)
        with open("articles.csv", "a") as artiCsv:
            writer = csv.writer(artiCsv, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
            writer.writerow([teaser, title, url, articleHtmlName])
        try:
            readPages(url, articleHtmlName)
        except:
            print("Unexpected error:", sys.exc_info()[0])

        sleepRand = random.uniform(0.8, 2)
        print("sleeping for {0}".format(sleepRand))
        time.sleep(sleepRand)
