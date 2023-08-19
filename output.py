"""Generate output from Google Contact birthday data."""

from calendar import month_name
from datetime import date
from jinja2 import Environment, FileSystemLoader
from os import makedirs
from weasyprint import HTML
from output_config import BIRTHDAY_ALERT_FILE, BIRTHDAYS_HTML_FILE, BIRTHDAYS_PDF_FILE, BIRTHDAYS_FILE_FOLDER, BIRTHDAYS_HTML_URL, BIRTHDAYS_PDF_URL


def generate_output(data):
    """Create PDF and HTML reports.

    Parameters:
    data (list): List of dicts containing contact people.

    """
    today = date.today()

    # Generate Birthday Alert html file (e.g. to use as email alert body)
    # Alert contains data on the remainder of the current month, and the whole of the following month.

    this_month = today.month
    next_month = this_month+1
    if next_month == 13:
        next_month = 1

    birthday_alert_list = list(
        filter(lambda r: r['month'] == this_month and r['day'] >= today.day, data))
    birthday_alert_list += list(
        filter(lambda r: r['month'] == next_month, data))

    environment = Environment(loader=FileSystemLoader(
        "templates/"), trim_blocks=True, autoescape=True)

    template = environment.get_template("birthdays_alert.html")
    birthday_alert_report = template.render(
        birth=birthday_alert_list, months=month_name, date=date.strftime(today, "%d/%m/%y"), today=today, link=BIRTHDAYS_HTML_URL, linktext="link to birthdays web page")

    with open(BIRTHDAY_ALERT_FILE, 'w') as output:
        output.write(birthday_alert_report)

    # Create HTML birthdays document from template
    template = environment.get_template("contact_birthdays.html")
    birthday_report = template.render(
        birth=data, months=month_name, date=date.strftime(today, "%d/%m/%y"), link=BIRTHDAYS_PDF_URL, linktext="link to birthdays PDF")

    # Create folder
    makedirs(BIRTHDAYS_FILE_FOLDER, exist_ok=True)

    with open(BIRTHDAYS_HTML_FILE, 'w') as output:
        output.write(birthday_report)

    # Regenerate report with HTML link instead of PDF
    birthday_report = template.render(
        birth=data, months=month_name, date=date.strftime(today, "%d/%m/%y"), link=BIRTHDAYS_HTML_URL, linktext="link to birthdays web page")

    # Create PDF of the bithdays document
    html = HTML(string=birthday_report)
    html.write_pdf(BIRTHDAYS_PDF_FILE)
