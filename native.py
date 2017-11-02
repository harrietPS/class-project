from bs4 import BeautifulSoup
import requests, re, json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
url ="https://plants.usda.gov/java/noxious?rptType=State&statefips=09"
noxious = requests.get(url, verify = False)
if noxious.status_code != 200:
    print('error', url)

page_html = noxious.text
soup = BeautifulSoup(page_html, "html.parser")

td_articles = soup.find_all("tr", attrs ={"class": "rowon"})
#the below code gives me just the latin name, within ghe first <td> tag, but does not move on the
#more td listings, I want to pull out the td with the L48 tag
data = []
for an_article in td_articles:
    state = an_article.find_all('td')
    #state_text = state.text

    #print("---------")


    #print(state.text)# if I blank out the above lines and just do
    #print(state)# then I get a list
    if "L48 (I)" in state[3]:
        print(state[0])
        print(state[3])

        #for name in state:
            #print(state[0])
