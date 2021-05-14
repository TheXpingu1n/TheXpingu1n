#just a test of web scrapping skill :@
import requests
import csv
from bs4 import BeautifulSoup
from itertools import zip_longest
import lxml
a1 = []
a2 = []
a3 = []
a4 = []
a5 = []
a6 = []
links = []
sal = []
respo = []
page = 0
while True: 
        result = requests.get(f'https://wuzzuf.net/search/jobs/?a=hpb&q=python%20developer&start={page}')
        src = result.content
        #print(src)
        soup = BeautifulSoup(src , 'lxml')
        page_limit = int(soup.find('strong').text)
        if(page > page_limit // 15):
                print('pages ended, terminate')
                break
        #print(soup)
        job_title = soup.find_all('h2' , {'class' : "css-m604qf"})
        company_names = soup.find_all('h2' , {'class' : "css-1s8r46l"})
        loc = soup.find_all('span', {'class' : 'css-5wys0k'})
        zeit = soup.find_all('div', {'class' : 'css-do6t5g'})
        tyype = soup.find_all('span', {'class' : 'css-1ve4b75 ex6kyvk0'})
        job_skills = soup.find_all('div', {'class' : 'css-y4udm8'})
        link = soup.find_all('h2', {'class' : 'css-m604qf'})
        #print(job_skills)
        #print(loc)
        #print(job_title)
        for i in range(len(job_title)):
                a1.append(job_title[i].text)
                

        for ii in range(len(company_names)):
                a2.append(company_names[ii].text)

        for iii in range(len(loc)):
                a3.append(loc[iii].text)

        for iv in range(len(zeit)):
                a4.append(zeit[iv].text)

        for v in range(len(tyype)):
                a5.append(tyype[v].text)

        for vi in range(len(job_skills)):
                a6.append(job_skills[vi].text)

        for vii in range(len(link)):
                links.append(link[vii].find('a').attrs['href'].replace(" ", "+")) 
        page += 1
        print('page switched') 

        for liink in links:
                resuult = requests.get(liink)
                srrc = resuult.content
                soup = BeautifulSoup(srrc , 'lxml')
                salaries = soup.find('div' , {'class' : 'css-rcl8e5'} , {'class' : 'css-47jx3m'} , {'class' : 'css-8il94u'} )
                sal.append(str(salaries))
                req = soup.find('div' , {'class' : 'css-1t5f0fr'}).find('ul')
                respon_text = ''
                #for li in req.find_all('li') :
               #         respon_text += li.text + '|'
                #respon_text = respon_text[: -2]
               # respo.append(respon_text)


       
        



file_list = [a1 , a2 , a3 , a4 , a5 , a6 , links , sal , respo]
exported = zip_longest(*file_list)

with open('/Users\Azad\Desktop\iii.csv' , 'w') as myfile :
        wr = csv.writer(myfile)
        wr.writerow(['Job Title' , 'Company Names' , 'Location' , 'Time' , 'Type of Job' , 'Job Skills' , 'Links' , 'Salary' , 'Responsibilites'])
        wr.writerows(exported)

#print(a1 , a2 , a3 , a4 , a5 , a6)

