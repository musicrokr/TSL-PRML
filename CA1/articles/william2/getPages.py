import urllib.request
import time
import random

def readPages(cat, uf, n):
    url = uf.format(n)
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    request = urllib.request.Request(url,headers={'User-Agent': user_agent})
    response = urllib.request.urlopen(request)
    html = response.read().decode(response.headers.get_content_charset())

    with open("{0}-pages/page{1}.html".format(cat, n), "w") as outfile:
        outfile.write(html)
urls = {
    "Singapore": "https://www.channelnewsasia.com/archives/8396078/singapore?pageNum={0}&channelId=7469254",
    "Asia": "https://www.channelnewsasia.com/archives/8395764/asia?pageNum={0}&channelId=7469252",
    "World": "https://www.channelnewsasia.com/archives/8395892/world?pageNum={0}&channelId=7469478",
    "Business": "https://www.channelnewsasia.com/archives/8395946/business?pageNum={0}&channelId=7469482",
    "Sport": "https://www.channelnewsasia.com/archives/8395834/sport?pageNum={0}&channelId=7469512"
}

for cat in urls:
    url = urls[cat]
    for i in range(0, 101):
        print("processing: {0} {1}".format(cat, i))
        readPages(cat, url, i)
        sleepRand = random.uniform(0.8, 2)
        time.sleep(sleepRand)

