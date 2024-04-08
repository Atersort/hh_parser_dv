from bs4 import BeautifulSoup  # parser by page
import requests  # send get requests

ITEMS = 100
URL = f"https://hh.ru/search/vacancy?text=seo&area=113&items_on_page={ITEMS}"
# header for referring to the site
headers = {
    'Host': 'hh.ru',
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
}
# creating a session to send a get request
sessions = requests.Session()


def extract_num_last_page():
    # get request
    hh_request = sessions.get(URL, headers=headers)

    # object library bs4
    soup = BeautifulSoup(hh_request.text, "html.parser")

    # parsing span containing number of page
    paginator = soup.find_all('span', {'class': 'pager-item-not-in-short-range'})

    num_pages = []

    # loop that append text in <a> to the list
    for page in paginator:
        num_pages.append(int(page.find('a').text))

    return num_pages[-1]


def extract_job(html):
    title = html.find('a').text
    link = html.find('a')['href']
    name_company = (html.find('div', {'class': 'vacancy-serp-item__meta-info-company'}).text).strip()
    location = html.find('div', {'data-qa':'vacancy-serp__vacancy-address'}).text
    experience = html.find('div', {'class': 'bloko-h-spacing-container bloko-h-spacing-container_base-0'}).text
    return {'title': title, 'link': link, 'name_company': name_company, 'location': location, 'experience': experience}


def extract_all_page(num_last_page):
    jobs = []
    # loop accessing pages
    for page in range(0, num_last_page):
        print(f'Парсинг страницы {page}')
        result = sessions.get(f"{URL}&page={page}", headers=headers)
        soup = BeautifulSoup(result.text, 'html.parser')
        # receive blocks with vacancies
        vacancy_title = soup.find_all('div', {'class': 'serp-item vacancy-serp-item_clickme'})
        # in loop get information about vacancies
        for vacancy in vacancy_title:
            job = extract_job(vacancy)
            jobs.append(job)
    return jobs

def get_jobs():
    last_page = extract_num_last_page()
    jobs = extract_all_page(5)
    return jobs