import requests
from bs4 import BeautifulSoup

print("free proxy lists : ")
request = requests.get("https://free-proxy-list.net/")
soup = BeautifulSoup(request.content, 'html.parser')
give_info = soup.find('table')

#row print
for row in give_info.find_all('tr'):
    #columns
    columns = row.find_all('td')
    #try : and except : statment..
    try:#% for printing  all headings... and \t for spece
        print("%s:%-20s %-20s%-20s" % (columns[0].get_text(),columns[1].get_text(),columns[3].get_text(),columns[4].get_text()))
    except:
        pass