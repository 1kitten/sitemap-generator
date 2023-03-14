from typing import Tuple

from database import create_data_base
from thread_worker import UrlSearcher

URLS_TO_SITEMAP: Tuple[str, ...] = (
    'http://crawler-test.com/',
    'http://google.com/',
    'https://vk.com/',
    'https://yandex.ru/',
    'https://stackoverflow.com/'
)


if __name__ == '__main__':
    create_data_base()

    threads: list = []

    for i_url in URLS_TO_SITEMAP:
        thread = UrlSearcher(url=i_url)
        thread.start()
        threads.append(thread)

    for i_thread in threads:
        i_thread.join()
