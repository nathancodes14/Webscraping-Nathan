


import requests
import re
from bs4 import BeautifulSoup


namesin = []
namesout = []
valuein = []
valueout = []
totalisin = []
totalisout = []
page = requests.get("https://www.fotmob.com/teams/8455/transfers/chelsea") 
soup = BeautifulSoup(page.content, 'html.parser')
code = list(soup.find_all(class_= "css-vrtjgu-TransferSectionWrapper earw3rv0"))
transferin = list(code[0].find_all(class_= "css-4j1x7b-CardCSS eenhk2w0"))
transferout = list(code[1].find_all(class_= "css-4j1x7b-CardCSS eenhk2w0"))
for i in transferin: 
    name = (i.find(class_="css-e07y08-PlayerName e1w8dl0x2")).get_text()
    
    namesin.append(name)
    gothru = (i.find_all(class_="css-x6llg4-detailWrapper"))
    for j in range (1,len(gothru)):
        value = (gothru[j].get_text())
        if len(re.findall(r"value", value )) > 0:
            break
        else:
            value = "Market value€0M"
    valuein.append(value)
    

for i in transferout: 
    name = i.find (class_="css-e07y08-PlayerName e1w8dl0x2").get_text()
   
    
    namesout.append(name)
    gothru = (i.find_all(class_="css-x6llg4-detailWrapper"))
    for j in range (1,len(gothru)):
        value = (gothru[j].get_text())
        if len(re.findall(r"value", value )) > 0:
            break
    else:
            value = "Market value€0M"
    
        
    
    valueout.append(value)


Transfersintotal = list(zip(namesin, valuein))
Transfersouttotal = list(zip(namesout, valueout)) 


for l in valuein:
    thevalueis = l.split('€')
    if len(re.findall(r"M", thevalueis[1] )) > 0:
        tosplit = (thevalueis[1].split('M'))
        nathanseligmemorialvariable = float(tosplit[0]) *1000000
    elif len(re.findall(r"K", thevalueis[1] )) > 0:
        tosplit = (thevalueis[1].split('K'))
        nathanseligmemorialvariable = float(tosplit[0]) *1000
    totalisin.append(nathanseligmemorialvariable)
    
for l in valueout:
    thevalueis = l.split('€')
    if len(re.findall(r"M", thevalueis[1] )) > 0:
        tosplit = (thevalueis[1].split('M'))
        nathanseligmemorialvariable = float(tosplit[0]) *1000000
    elif len(re.findall(r"K", thevalueis[1] )) > 0:
        tosplit = (thevalueis[1].split('K'))
        nathanseligmemorialvariable = float(tosplit[0]) *1000
    totalisout.append(nathanseligmemorialvariable)
    #just make it not double
    

finalin = sum(totalisin)/1000000
finalout = sum(totalisout)/1000000

print("____________________________")
print("Transfers in:")
for i in Transfersintotal:
    print(i)
print("____________________________")
print("Transfers out")
for i in Transfersouttotal:
    print(i)
print("____________________________")
print(f"In: {finalin} million, out {finalout} million. Total profit: {(finalout - finalin)} million")