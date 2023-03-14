import sqlite3


CREATION_DATABASE_SCRIPT: str = """
CREATE TABLE IF NOT EXISTS `sitemap` (
    id INTEGER PRIMARY KEY,
    URL TEXT NOT NULL,
    TIME_PROCEED REAL NOT NULL,
    LINKS_FOUND INTEGER NOT NULL,
    FILE_NAME TEXT NOT NULL
);
"""

INSERTION_SCRIPT: str = """
INSERT INTO `sitemap` (URL, TIME_PROCEED, LINKS_FOUND, FILE_NAME)
VALUES (?, ?, ?, ?)
"""


def create_data_base() -> None:
    """ Function. Creates database table called sitemap. """
    with sqlite3.connect('sitemap.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute(CREATION_DATABASE_SCRIPT)


def add_new_sitemap_value(
        url: str,
        proceed_time: float,
        total_urls_found: int,
        result_filename: str
) -> None:
    """ Function to add new value into sitemap table. """
    with sqlite3.connect('sitemap.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute(
            INSERTION_SCRIPT,
            (url, proceed_time, total_urls_found, result_filename)
        )
