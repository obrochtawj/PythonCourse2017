#Go to https://polisci.wustl.edu/faculty/specialization
#Go to the page for each of the professors.
#Create a .csv file with the following information for each professor:
# 	-Specialization
# 	-Name
# 	-Title
# 	-E-mail
# 	-Web page
	
from bs4 import BeautifulSoup
import urllib2
import csv 

web_address='https://polisci.wustl.edu/faculty/specialization'
web_page = urllib2.urlopen(web_address)
soup = BeautifulSoup(web_page.read())
soup.prettify()

all_names=[]
for person in range(15,57):
    site=soup.find_all('a')[person]
    person_name=site.text
    all_names.append(person_name)
    
all_links=[]
for person in range(15,57):
    site=soup.find_all('a')[person]
    website=site['href']
    website2='http://polisci.wustl.edu'+website
    all_links.append(website2)
all_links[16]='https://polisci.wustl.edu/Matthew_Gabel'
all_links[-10]='https://polisci.wustl.edu/Matthew_Gabel'

all_titles=[]
for person in range(0,42): 
    profs=soup.find('div',{'class':'view-content'})
    profs.find_all('div')
    ex=[x.text for x in profs.find_all('div')][person]
    all_titles.append(ex.split('\n')[2])

#Titles
indexes=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,33,35,37,38,39,40,41]
new_titles=[all_titles[x] for x in indexes]

#Specilization
specialization=['American']*11+['Comparative']*13+["Methods"]*2+["Theory"]*5
specialization[1]='American, Formal'
specialization[2]='American, Formal'
specialization[6]='American, Methods'
specialization[11]='Comparative, Conflict'
specialization[12]='Comparative, IPE'
specialization[14]='Comparative, Conflict'
specialization[16]='Comparative, IPE'
specialization[21]='Comparative, Formal'
specialization[22]='Comparative, Formal'

new_names=[]
for link in all_names:
    if link not in new_names:
        new_names.append(link)

new_links=[]
for link in all_links:
    if link not in new_links:
        new_links.append(link)

all_emails=[]
for link in new_links:
    web_address=link
    web_page = urllib2.urlopen(web_address)
    soup = BeautifulSoup(web_page.read())
    soup.prettify()
    email=[a["href"] for a in soup.select('a[href^=mailto:]')][0]
    all_emails.append(email)

all_personal_site=[]
for link in new_links:
    web_address=link
    web_page = urllib2.urlopen(web_address)
    soup = BeautifulSoup(web_page.read())
    temp_soup = soup.find_all("a", text=re.compile('Personal'))
    if len(temp_soup)==0:
        all_personal_site.append(" ")
    else:
        for a in soup.find_all("a", text=re.compile('Personal')):
            all_personal_site.append(a['href'])

with open('info.csv', "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for val in new_names:
        writer.writerow([val])  

with open('info2.csv', "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for val in new_titles:
        writer.writerow([val]) 
        
with open('info3.csv', "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for val in specialization:
        writer.writerow([val])
        
with open('info4.csv', "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for val in all_emails:
        writer.writerow([val]) 

with open('info5.csv', "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for val in all_personal_site:
        writer.writerow([val]) 
        

from itertools import izip
import csv
with open('info.csv','rb') as f1, open('info2.csv','rb') as f2, open('out.csv','wb') as w:
    writer = csv.writer(w)
    for r1,r2 in izip(csv.reader(f1),csv.reader(f2)):
        writer.writerow(r1+r2)

with open('out.csv','rb') as f1, open('info3.csv','rb') as f2, open('out2.csv','wb') as w:
    writer = csv.writer(w)
    for r1,r2 in izip(csv.reader(f1),csv.reader(f2)):
        writer.writerow(r1+r2)        

with open('out2.csv','rb') as f1, open('info4.csv','rb') as f2, open('out3.csv','wb') as w:
    writer = csv.writer(w)
    for r1,r2 in izip(csv.reader(f1),csv.reader(f2)):
        writer.writerow(r1+r2)  

with open('out3.csv','rb') as f1, open('info5.csv','rb') as f2, open('out4.csv','wb') as w:
    writer = csv.writer(w)
    for r1,r2 in izip(csv.reader(f1),csv.reader(f2)):
        writer.writerow(r1+r2)  

with open('out4.csv','w',newline='') as f:
    w = csv.writer(f)
    w.writerow(['Name','Title', 'Specialization', 'Email', 'Personal Site'])
    w.writerows(data)

with file('out4.csv', 'r') as original: data = original.read()
with file('out5.csv', 'w') as modified: modified.write("Name, Title, Specialization, Email, Website\n" + data)



