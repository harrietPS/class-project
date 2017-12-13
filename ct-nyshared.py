#making list of ct and ny threatened
from bs4 import BeautifulSoup
import requests, re, json
import urllib3
def common_elements(list1, list2):
    result = []
    for element in list1:
        if element in list2:
            result.append(element)
    return result

ctplant =[]
nyplant =[]
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
url ="https://plants.usda.gov/java/threat?stateSelect=US09&statelist=states"
threat = requests.get(url, verify = False)
if threat.status_code != 200:
    print('error', url)
page_html = threat.text
soup = BeautifulSoup(page_html, "html.parser")

td_articles = soup.find_all("tr", attrs ={"class": "rowon"})
#the below code gives me just the latin name, within ghe first <td> tag, but does not move on the
#more td listings, I want to pull out the td with the L48 tag

for an_article in td_articles:
    state = an_article.find_all('td')
    #state_text = state.text




    #print(state)# if I blank out the above lines and just do
    #print(state)# then I get a list
    if "E" in state[2].text:
        ctplant.append(state[0].text)
#print(ctplant)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
url ="https://plants.usda.gov/java/threat?stateSelect=US36&statelist=states"
threat = requests.get(url, verify = False)
if threat.status_code != 200:
    print('error', url)
page_html = threat.text
soup = BeautifulSoup(page_html, "html.parser")

td_articles = soup.find_all("tr", attrs ={"class": "rowon"})
#the below code gives me just the latin name, within ghe first <td> tag, but does not move on the
#more td listings, I want to pull out the td with the L48 tag
for an_article in td_articles:
    state = an_article.find_all('td')
    #state_text = state.text




    #print(state)# if I blank out the above lines and just do
    #print(state)# then I get a list
    if "E" in state[2].text:
        nyplant.append(state[0].text)



plantctny = common_elements(ctplant, nyplant)
for x in plantctny:
    print(x)
