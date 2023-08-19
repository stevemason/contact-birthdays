Contact Birthdays
=================

This project retrieves birthdays from Google Contacts, and creates documents summarising this information.

It produces all three of the following outputs at once:

- an HTML file listing birthdays for the rest of the current month and the following month (e.g. to use as the body of a scheduled email alert)
- an HTML file summarising all contact birthdays for the whole calendar year
- a PDF version of the above document

The information is retrieved using Google's People API. Before this can be used, the application needs to be registered. See the following link for details: <https://developers.google.com/people/v1/getting-started>

An 'output_config.py' file is required, providing specific details about output file names and locations. An example file has been provided, but this file should be renamed and amended as required.

Sample output files may be found in the 'sample output' project folder.

Usage:

- install requirements with pip
- python birthdays.py
