from __future__ import annotations
from bs4 import BeautifulSoup
from PIL import Image
import requests

_DEFAULT_TIMEOUT = 30


def parse_html_to_scratch_favicon(domain: str) -> str | None:
    try:
        page = requests.get(domain, timeout=_DEFAULT_TIMEOUT)
        if page.status_code == 200:
            soup = BeautifulSoup(page.text, features="lxml")

            icon_link = soup.find("link", rel="shortcut icon")
            if icon_link is None:
                icon_link = soup.find("link", rel="icon")
            if icon_link is None:
                return None

            icon_link = icon_link["href"]
            if 'http' not in icon_link:
                if icon_link[0] == '/':
                    return domain + icon_link[1:]
                else:
                    return domain + icon_link
            return icon_link
    except Exception as e:
        print(e)
        return None


def save_favicon_as_png(domain: str, courier_name: str) -> bool:
    try:
        format = domain[-3:]
        filename = f"resources/icons/{courier_name}.{format}"
        with open(filename, 'wb') as handle:
            response = requests.get(
                domain, stream=True,
                timeout=_DEFAULT_TIMEOUT
            )

            if not response.ok:
                print(response)

            for block in response.iter_content(1024):
                if not block:
                    break

                handle.write(block)

        if format == 'ico':
            img = Image.open(filename)
            img.save(f'resources/icons/{courier_name}.png')

        return True
    except Exception as e:
        print(e)
        return False
