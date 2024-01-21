import requests # send get requests
from bs4 import BeautifulSoup # parser by page
from fake_user_agent import user_agent # user-agent generator

# header for referring to the site
headers = {
    'Host': 'hh.ru',
    'User-agent': f'{user_agent("chrome")}',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    }

# get request
hh_request = requests.get("https://hh.ru/search/vacancy?text=seo&salary=&ored_clusters=true&items_on_page=100&area=113&hhtmFrom=vacancy_search_list&hhtmFromLabel=vacancy_search_line", headers=headers)

# object library bs4
soup = BeautifulSoup(hh_request.text, "html.parser")

# get page title
pages = soup.find('div', {'class':'bloko-button bloko-button_pressed'})

print(pages)