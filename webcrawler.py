from bs4 import BeautifulSoup
import urllib.request
import operator

seed_url = "http://www8.gsb.columbia.edu"

urls = [seed_url]    #queue of urls to crawl
seen = [seed_url] # stack of urls seen so far
opened = []
newdic = {}


maxNumUrl = 10; #set the maximum number of urls to visit
print("Starting with url="+str(urls))
while len(urls) > 0 and len(opened) < maxNumUrl:
    # DEQUEUE A URL FROM urls AND TRY TO OPEN AND READ IT
    try:
        curr_url=urls.pop(0)
        print("num. of URLs in stack: %d " % len(urls))
        webpage=urllib.request.urlopen(curr_url)
        opened.append(curr_url)

    except Exception as ex:
        print(ex)
        continue    #skip code below
    soup = BeautifulSoup(webpage)   #creates object soup     
    htmltext = soup.find_all('p')
    str(htmltext)
    html = ','.join([str(elm) for elm in htmltext])
    html1 = html.replace("<p>", "",1000)
    w = html1.count('business')
    x = html1.count('finance')
    y = html1.count('engineering')
    z = html1.count('research')
    count = w + x + y + z + 1
    newdic[str(curr_url)] = count
    d={}
    sorted_d = sorted(newdic.items(), key=operator.itemgetter(1), reverse=True)    
    # IF URL OPENS, CHECK WHICH URLS THE PAGE CONTAINS
    # ADD THE URLS FOUND TO THE QUEUE url AND seen

    # Put child URLs into the stack
    for tag in soup.find_all('a', href = True): #find tags with links
        childUrl = tag['href']          #extract just the link
        o_childurl = childUrl
        childUrl = urllib.parse.urljoin(seed_url, childUrl)
        print("url=" + seed_url)
        print("original childurl=" + o_childurl)
        print("childurl=" + childUrl)
        print("url in childUrl=" + str(seed_url in childUrl))
        print("childUrl not in seen=" + str(childUrl not in seen))
        if seed_url in childUrl and childUrl not in seen:
            print("***urls.append and seen.append***")
            urls.append(childUrl)
            seen.append(childUrl)
        else:
            print("######")

print("num. of URLs seen = %d, and scanned = %d" % (len(seen), len(opened)))

print("List of seen URLs:")
for seen_url in seen:
    print(seen_url)