import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen

def url_scrap(url):
    
    info = {}
    
    html = urlopen(url)
    bsObj = BeautifulSoup(html.read())
    
    
    for link in bsObj.find_all('meta'):
        
        if link.get('name')=='description':
            
            info['description'] = link.get('content')
            
        if link.get('name')=='keywords':
            
            info['keywords'] = link.get('content')
            
    titles = bsObj.find_all(['h1', 'h2','h3','h4'])
 
    for i in range(len(titles)):

        info['heading'+str(i)] = titles[i].text.split('¶')[0]

    return info

def scrap(input_url):
    html = urlopen(input_url) # Insert your URL to extract

    bsObj = BeautifulSoup(html.read());
    link_ =[]
    Entire_data = pd.DataFrame(columns=['urls','link_info','scrapped_data'])
    urls = []
    link_info = []
    scrapped_data = []

    for link in bsObj.find_all('a'):
        
        a = str(link)
        
        try:
            if link.get('href').split(':')[0]=='https':
                
                scrapped_data.append(url_scrap(link.get('href')))
                urls.append(link.get('href'))
                link_info.append(a)
                 

            else:
                if link.get('href')[0]=='/':
                    
                    url = input_url.split('com')[0]+'com'+link.get('href')
                    
                else:
                    
                    url = input_url+link.get('href')
                    
                scrapped_data.append(url_scrap(url))   

                urls.append(url)

                link_info.append(a)
                 
        except Exception as e:
            print(e)

    Entire_data['urls'] = urls
    Entire_data['link_info'] = link_info
    Entire_data['scrapped_data'] = scrapped_data

    Entire_data.to_csv('scrapped_data.csv')

    
url = 'https://rasa.com/docs/getting-started/'
scrap(url)
