# The purpose of this program is to teach the foundation of web scraping
import requests
from bs4 import BeautifulSoup

scrape_site_link = ""
tag_to_scrape = ""

custom_headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"}

response_object = requests.get(scrape_site_link, headers=custom_headers)
soup_object = BeautifulSoup(response_object.text, "html.parser")

scraped_tags_list = soup_object.find_all(tag_to_scrape)

for scraped_tag in scraped_tags_list:
    scraped_text = scraped_tag.text.strip()

    print(scraped_text)


# < ------------ NOTES ------------ >
# A custom header with the key of "user-agent" helps to mimic a real browser and can prevent the server from blocking your requests as coming from a bot

# soup_object = BeautifulSoup(<html content>, "<parser to use>")
# Common parsers that are used
#   - html.parser
#   - lxml
#   - html5lib

# .find_all("<specified tag without <> >") -> used to extract (returns a list) all instances of the specified tag from the HTML content
# .find("<specified tag without <> >") -> used to extract the first occurance of the specified tag from the HTML content

# .find() and .find_all() can be used to scrape specific class names by examples:
#   - .find(class_="<class name to scrape>")
#   - .find_all(class_="<class name to scrape>")

# .text -> is used to extract the text enclosed by the tag
# .strip() -> it is used in addition to .text to remove whitespaces and other characters (very usual because there are allot of whitespaces)