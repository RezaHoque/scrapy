from django.shortcuts import render
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

#pages=set()
# Create your views here.
def index(request):
    return render(request,'index.html')

def scrap(request):
    linkData = []
    output=[]

    pattern = re.compile("^(/)")
    url=urlopen(request.GET['url'])
    text=request.GET['t']

    content=url.read().decode("utf-8")
    soup = BeautifulSoup(content,"html.parser")
    #links = s.find_all("a",href=pattern)
    
    for link in soup.find_all("a", href=pattern):
        if "href" in link.attrs:
            if link.attrs["href"] not in linkData:
                new_page = link.attrs["href"]
                linkData.append(str(new_page))
    
    for lnk in linkData:
        fullUrl=request.GET['url']+lnk
        
        try:
            subPageUrl=urlopen(fullUrl)
        except:
            pass
       
        subLinkContent=subPageUrl.read().decode("utf-8")
        sSoup=BeautifulSoup(subLinkContent,"html.parser")
        #pageText=sSoup.get_text()
        pageText=sSoup(text=lambda t: text in t)
        #sSoup.body.findAll(text=re.compile('^'+text+'$'))

        #if(pageText.find(text)!=-1):
        if pageText:   
            #found the string
            obj={'PageLink':fullUrl,'Text':pageText}
            output.append(obj)
          
    return render(request,'scrap.html',{'data':output})

        


