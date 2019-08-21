import lxml.html
import sys
files = ["Asia-pages/page0.html", "Business-pages/page0.html", "Singapore-pages/page0.html", "World-pages/page0.html", "Sport-pages/page0.html"]
articleNumber = 0
cat = "test"
for f in files:
    with open(f, 'r') as infile:
        page = lxml.html.fromstring(infile.read())
    for j in range(1, 11):
        articleNumber += 1
        print("reading article {0} ... ".format(articleNumber))
        teaser = page.xpath('//ol[@class="result-section__list"]/li[{0}]/div/div/div/div[1]/a/text()'.format(j))[0]
        title = page.xpath('//ol[@class="result-section__list"]/li[{0}]/div/div/div/h3/a/text()'.format(j))[0]
        link = page.xpath('//ol[@class="result-section__list"]/li[{0}]/div/div/div/h3/a/@href'.format(j))[0]

        url = "https://www.channelnewsasia.com" + link
        articleHtmlName = "{0}-articles/articles{1}.html".format(cat, articleNumber)
        print([teaser, title, url, articleHtmlName])
