from bs4 import BeautifulSoup
import requests


def get_favicon(domain) -> str:
    # if 'http' not in domain:
    #     domain = 'http://' + domain
    try:
        page = requests.get(domain)
        soup = BeautifulSoup(page.text, features="lxml")

        icon_link = soup.find("link", rel="shortcut icon")
        if icon_link is None:
            icon_link = soup.find("link", rel="icon")
        if icon_link is None:
            return domain + '/favicon.ico'

        return icon_link["href"]
    except Exception as e:
        return  ""
