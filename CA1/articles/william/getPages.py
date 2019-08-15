import urllib.request
import time

def readPages(n):
    url = "https://www.channelnewsasia.com/archives/8396078/news?pageNum={0}&channelId=7469254".format(n)
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    request = urllib.request.Request(url,headers={'User-Agent': user_agent})
    response = urllib.request.urlopen(request)
    html = response.read().decode(response.headers.get_content_charset())

    with open("pages/page{0}.html".format(n), "w") as outfile:
        outfile.write(html)

for i in range(0, 101):
    print("reading page {0} ... ".format(i))
    readPages(i)
    time.sleep(2)
