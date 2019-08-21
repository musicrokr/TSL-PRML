import csv
import lxml.html
import unicodedata
import sys

csvFiles = ["Asia-articles.csv", "Business-articles.csv", "Singapore-articles.csv", "Sport-articles.csv", "World-articles.csv"]

def processFile(fileName):
    with open(fileName, 'r') as file:
        page = lxml.html.fromstring(file.read())
        dt = page.xpath("//time[@class='article__details-item']/text()")
        tags = page.xpath("//footer[@class='article__footer']/div/ul/li/a/text()")
        headline = page.xpath("//h1[@class='article__title']/text()")
        article = page.xpath("//div[@class='c-rte--article']/p/text()")

    return (dt[0], tags, headline[0], "\n".join([unicodedata.normalize('NFKD', a) for a in article]))

for csvFile in csvFiles:
    finalCSV = csvFile.replace("-articles", "-final")
    errorCount = 0
    with open(csvFile, 'r') as artiCsv:
        f = csv.reader(artiCsv, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
        for r in f:
            try:
                teaser, title, url, htmlFile = r
                print("processing {0} ...".format(htmlFile))
                datetime, tags, headline, body = processFile(htmlFile)
                articleTxtFile = htmlFile.replace(".html", "txt").replace("articles/", "articles-txt/")
                with open(articleTxtFile, 'w') as writeFile:
                    writeFile.write(body)

                with open(finalCSV, 'a') as outFile:
                    writer = csv.writer(outFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
                    writer.writerow([headline,articleTxtFile, datetime, ",".join(tags + [teaser])])
            except:
                errorCount += 1
                print("-------------------Unexpected error:", sys.exc_info()[0])
   
print("total errors: {0}".format(errorCount))
