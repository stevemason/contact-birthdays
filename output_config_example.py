"""Module provides values for global constants."""

from os.path import join

# The UUID is for adding to a URL when hosting the files on a web server.
# It adds some basic security as the URL would be difficult for an attacker to guess.
# It's not bulletproof, and may be insufficient to address relevant threats/risks in many cases.

UUID = "cb344f0f-5a99-4c29-8dcd-4fa962b6c2f3"

BIRTHDAY_ALERT_FILE = "birthday_alert.html"

OUTPUT_PATH = "."

FILENAME = "birthdays"

URL_PREFIX = "https://test.org"

BIRTHDAYS_HTML = join(UUID, FILENAME + ".html")
BIRTHDAYS_PDF = join(UUID, FILENAME + ".pdf")

BIRTHDAYS_FILE_FOLDER = join(OUTPUT_PATH, UUID)
BIRTHDAYS_HTML_FILE = join(OUTPUT_PATH, BIRTHDAYS_HTML)
BIRTHDAYS_PDF_FILE = join(OUTPUT_PATH, BIRTHDAYS_PDF)

BIRTHDAYS_HTML_URL = join(URL_PREFIX, BIRTHDAYS_HTML)
BIRTHDAYS_PDF_URL = join(URL_PREFIX, BIRTHDAYS_PDF)
