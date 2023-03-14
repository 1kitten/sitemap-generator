import asyncio
import re
import time
from re import Match
from threading import Thread
from typing import Optional
from pysitemap import crawler
import logging

from database import add_new_sitemap_value


def get_domain_name(url: str) -> Optional[str]:
    """
    Function. Getting domain name from pasted URL.
    :param url: (str). Pasted url to get domain from.
    :return: (str). Domain of pasted URL.
    """
    domain: Match = re.match(r'https*://(\w+)', url)
    if domain:
        return domain.groups()[0]
    return


def get_amount_of_urls_from_sitemap_file(filename: str) -> int:
    """
    Function. Returns amount of found urls from XML file.
    :param filename: (str). Path to XML file with sitemap.
    :return: (int). Amount of urls found.
    """
    with open(filename, 'r') as sitemap_file:
        total_lines: list[str] = sitemap_file.readlines()
        return len(total_lines[2:-1])


class UrlSearcher(Thread):
    """ Thread class to get all the URLS from website. """

    def __init__(self, url: str):
        """
        Initial dander method for UrlSearcher class.
        Getting url as an input parameter.
        """
        super().__init__()
        self.url = url

    def run(self) -> None:
        """
        Method. Starts after '*.start()' method raised.
        Creating new event loop for asyncio.
        Getting domain name from pasted url, if there is any,
        starts generating sitemap for pasted url.
        Result will be writen to filename format: '<pasted_url>.xml'.
        Also information will be writen into sqlite3 database.
        """
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        domain_name: str = get_domain_name(url=self.url)

        if domain_name:
            output_filename: str = f'search_results/{domain_name}.xml'
            started_at = time.time()

            print(f'Searching urls at {self.url} website.')
            crawler(root_url=self.url, out_file=output_filename)
            print(f'Stops getting urls from {self.url}')

            amount_of_urls = get_amount_of_urls_from_sitemap_file(output_filename)
            ended_at = round(time.time() - started_at, 2)

            add_new_sitemap_value(
                url=self.url,
                proceed_time=ended_at,
                total_urls_found=amount_of_urls,
                result_filename=output_filename
            )
        else:
            print('Error: bad url pasted.')
