#Homework 2
#William O'Brochta

from bs4 import BeautifulSoup
import urllib2
import csv 

#Do something interesting that fixed unicode problems.
if sys.version[0] == '2':
    reload(sys)
    sys.setdefaultencoding("utf-8")

#Run through all three pages of petitions and pull urls out.
web_address='https://petitions.whitehouse.gov/petitions'
web_page = urllib2.urlopen(web_address)
soup = BeautifulSoup(web_page.read())
soup.prettify()

#Landing page
petitions0=[]
for petition in range(14,54):
    site=soup.find_all('a')[petition]
    website=site['href']
    website2='https://petitions.whitehouse.gov'+website
    petitions0.append(website2)
#There are duplicates of each petition for whatever reason, so get rid of those.
new_petitions0=petitions0[::2]

#First page
#Note, I could do a loop for the landing and first pages, but I couldn't for
#second page because it has fewer urls. That's why I just repeated the url
#finding process three times.
web_address='https://petitions.whitehouse.gov/petitions?page=1'
web_page = urllib2.urlopen(web_address)
soup = BeautifulSoup(web_page.read())
soup.prettify()

petitions1=[]
for petition in range(14,54):
    site=soup.find_all('a')[petition]
    website=site['href']
    website2='https://petitions.whitehouse.gov'+website
    petitions1.append(website2)
new_petitions1=petitions1[::2]

#Second page
web_address='https://petitions.whitehouse.gov/petitions?page=2'
web_page = urllib2.urlopen(web_address)
soup = BeautifulSoup(web_page.read())
soup.prettify()
petitions2=[]
for petition in range(14,22):
    site=soup.find_all('a')[petition]
    website=site['href']
    website2='https://petitions.whitehouse.gov'+website
    petitions2.append(website2)
new_petitions2=petitions2[::2]

#Merge all petition urls
all_petitions=new_petitions0+new_petitions1+new_petitions2

#Function to get a certain petition information from url
def getPetition(link):
    web_address=link
    web_page = urllib2.urlopen(web_address)
    soup = BeautifulSoup(web_page.read())
    
    #Title
    Title=soup.find_all('h1')[0]
    Title=Title.text
    
    #Date
    #Split out author and date, re-combine date, encode in utf
    Date=soup.find_all('h4')[0]
    Date=Date.text
    Date=Date.split()[4:]
    Date=" ".join(Date)
    Date=Date.encode('utf-8')

    #Issues
    #Pull div tags only in main content so there are no duplicates in the 'other petitions' section
    Main=soup.find('div', {'id':'content-main'})
    all_Issues=[]
    #Create list with the length of all issue tags (varies from 1 to 3).
    for num in range(0,len(Main.find_all('h6'))):
        new=Main.find_all('h6')[num]
        new=new.text
        all_Issues.append(new)
    #Put the issues in one string joined with commas.
    all_Issues=", ".join(all_Issues)

    #Signatures
    Signatures=soup.find('span',{'class':'signatures-number'})
    Signatures=Signatures.text
    
    #Create info dictionary with title, date, issues, and signatures
    info={'Title':Title, "Date":Date, 'Issues':all_Issues, "Signatures":Signatures}
    return info

#Create the file to run through all the urls collected for the petitions.
with open('data_file.csv', 'ab') as f:
    my_writer=csv.DictWriter(f, fieldnames=('Title', "Date", "Issues", "Signatures"))
    my_writer.writeheader()
    for petition_link in all_petitions:
        temp1=getPetition(petition_link)
        my_writer.writerow({'Date':temp1['Date'], 'Issues':temp1["Issues"], 'Title':temp1['Title'], 'Signatures':temp1['Signatures']})

