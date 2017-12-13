from bs4 import BeautifulSoup
import requests, json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import mmcode as green

#plant_data = json.load()

#f = open("plant_data.json", "r")
#with open("plant_data.json", "r", encoding='utf-8') as f:
plant_data = json.loads(green.plant_data)
tropData = []
plantlistData = []
gobotantData = []

for plant_name in plant_data:
	 #print(plant_name)
	 #print(plant_data[plant_name]["Tropicos"])
	# print(plant_data[plant_name]["wikidata"])
	plantlistData.append(plant_data[plant_name]["Plantlist"])
	tropData.append(plant_data[plant_name]["Tropicos"])
	gobotantData.append(plant_data[plant_name]["GoBotany"])

Tropicos_Accepted_Names = []

for trop in tropData:
	print("Worning on a Trop")

	url = "http://www.tropicos.org/Name/" + trop

	author = requests.get(url, verify = False)
	if author.status_code != 200:
	    print('error', url)

	page_html = author.text
	soup = BeautifulSoup(page_html, "html.parser")

	list_style = soup.find('td', attrs = {'class': "ItemHeader"}).get_text()

	list_style = list_style.replace('\t', '')
	list_style = list_style.replace('\n', '')

	Tropicos_Accepted_Names.append(list_style)

Plantlist_Accepted_Names = []
Synonyms = []

for plist in plantlistData:
	print("Worning on a Plantlist")

	url = "http://www.theplantlist.org/tpl1.1/record/" + plist

	author = requests.get(url, verify = False)
	if author.status_code != 200:
	    print('error', url)

	page_html = author.text
	soup = BeautifulSoup(page_html, "html.parser")

	try:

		list_style = soup.find('span', attrs = {'class': "name"}).get_text()
		syn = soup.find_all('td', attrs = {'class' : "Synonym"})

	except:

		list_style = "none"

	list_style = list_style.replace('\t', '')
	list_style = list_style.replace('\n', '')

	Plantlist_Accepted_Names.append(list_style)
	Synonyms.append(syn)

GoBotany_Common_Names = []
GoBotany_Images = []
GoBotany_Facts = []
GoBotany_Status = []
GoBotany_Conserve = []


for go in gobotantData:
	print("Working on a GoBotany")

	if go != "":
		url = go

		author = requests.get(url, verify = False)

		if author.status_code != 200:
			print('error', url)

		page_html = author.text
		soup = BeautifulSoup(page_html, "html.parser")

		try:

			list_style = soup.find('p', attrs = {'class': "common"}).get_text()
			GoBotanyImage = soup.find('a', attrs = {'id': "startimage"})
			factsab = soup.find("div", attrs = {'id': "facts"}).get_text()
			status = soup.find("div", attrs = {'id': "wetland"}).get_text()
			conserve = soup.find('div', attrs = {'id': 'status'}).get_text()



		except:

			list_style = "none"
			GoBotanyImage = "none"
			factsab = "none"
			status = "none"
			conserve = "none"


		list_style = list_style.replace('\t', '')
		list_style = list_style.replace('\n', '')

		GoBotany_Common_Names.append(list_style)

		GoBotany_Images.append(str(GoBotanyImage))
		GoBotany_Facts.append(str(factsab))
		GoBotany_Status.append(str(status))
		GoBotany_Conserve.append(str(conserve))

	else:
		GoBotany_Common_Names.append("none")
		GoBotany_Images.append("none")
		GoBotany_Facts.append("none")
		GoBotany_Status.append('none')
		GoBotany_Conserve.append('none')

# for i in Tropicos_Accepted_Names:
# 	print("Tropicos Accepted Name: " + i)

# for i in Plantlist_Accepted_Names:
# 	print("Plantlist Accepted Name: " + i)

# for i in GoBotany_Common_Names:
# 	print("GoBotany Common Name: " + i)


for i in range(0, len(Tropicos_Accepted_Names)):
	print("Tropicos Accepted Name: " + Tropicos_Accepted_Names[i] + "  Plantlist Accepted Name: " + Plantlist_Accepted_Names[i] + "  GoBotany Common Name: " + GoBotany_Common_Names[i])
	print("List of Synonyms from Plantlist: ")
	for x in Synonyms[i]:
		print(x.get_text())

	print("GoBotany Image: " + GoBotany_Images[i])
	print(GoBotany_Facts[i])
	print(GoBotany_Status[i])
	print(GoBotany_Conserve[i])





# for syn in Synonyms:
# 	for s in syn:
# 		print(s.get_text())
