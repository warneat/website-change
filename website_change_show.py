#!/usr/bin/env python3

import time
import website_change
from bs4 import BeautifulSoup

website_content = website_change.get_website_text(website_change.URL,
                                                  website_change.USER,
                                                  website_change.PWRD
                                                  )
soup = BeautifulSoup(website_content, 'html.parser')
text_human_readable = soup.get_text()
print('Status at {0}: {1} '.format(time.strftime('%d %b %Y %H:%M'), text_human_readable))
exit()
